import cv2
import numpy as np
from pathlib import Path

LOWER_YELLOW = np.array([24, 200, 200], dtype=np.uint8)
UPPER_YELLOW = np.array([30, 255, 255], dtype=np.uint8)

NORM_W = 12
NORM_H = 16

MIN_AREA = 6
MIN_W, MIN_H = 2, 6
MAX_W, MAX_H = 30, 30

DIGIT_JOIN_GAP = 2      # blobs this close are part of the same digit
NUMBER_SPLIT_GAP = 6    # bigger gap means a new number


def yellow_mask(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, LOWER_YELLOW, UPPER_YELLOW)
    return mask


def normalize_binary(binary, out_w=NORM_W, out_h=NORM_H):
    ys, xs = np.where(binary > 0)
    if len(xs) == 0:
        return np.zeros((out_h, out_w), dtype=np.uint8)

    x1, x2 = xs.min(), xs.max() + 1
    y1, y2 = ys.min(), ys.max() + 1
    crop = binary[y1:y2, x1:x2]

    h, w = crop.shape
    scale = min(out_w / w, out_h / h)
    new_w = max(1, int(round(w * scale)))
    new_h = max(1, int(round(h * scale)))

    resized = cv2.resize(crop, (new_w, new_h), interpolation=cv2.INTER_NEAREST)

    canvas = np.zeros((out_h, out_w), dtype=np.uint8)
    xoff = (out_w - new_w) // 2
    yoff = (out_h - new_h) // 2
    canvas[yoff:yoff + new_h, xoff:xoff + new_w] = (resized > 0).astype(np.uint8) * 255
    return canvas


def bitmap_key(binary):
    norm = normalize_binary(binary)
    return tuple((norm > 0).astype(np.uint8).flatten().tolist())


def load_digit_lookup(template_dir="templates"):
    lookup = {}
    for d in "0123456789":
        path = Path(template_dir) / f"{d}.png"
        img = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)
        if img is None:
            raise FileNotFoundError(path)

        key = bitmap_key(img)
        lookup[key] = d
    return lookup


def connected_boxes(mask):
    n, labels, stats, _ = cv2.connectedComponentsWithStats(mask, connectivity=8)
    boxes = []
    for i in range(1, n):
        x, y, w, h, area = stats[i]
        if area < MIN_AREA:
            continue
        if w < MIN_W or h < MIN_H:
            continue
        if w > MAX_W or h > MAX_H:
            continue
        boxes.append((x, y, w, h))
    boxes.sort(key=lambda b: (b[1], b[0]))
    return boxes


def merge_boxes_into_clusters(boxes, y_tol=3, gap=NUMBER_SPLIT_GAP):
    if not boxes:
        return []

    boxes = sorted(boxes, key=lambda b: b[0])

    clusters = []
    cur = [boxes[0]]

    for b in boxes[1:]:
        px, py, pw, ph = cur[-1]
        x, y, w, h = b

        prev_right = px + pw
        same_row = abs(y - py) <= y_tol
        close = (x - prev_right) <= gap

        if same_row and close:
            cur.append(b)
        else:
            clusters.append(cur)
            cur = [b]

    clusters.append(cur)
    return clusters


def crop_cluster(mask, cluster):
    x1 = min(x for x, y, w, h in cluster)
    y1 = min(y for x, y, w, h in cluster)
    x2 = max(x + w for x, y, w, h in cluster)
    y2 = max(y + h for x, y, w, h in cluster)
    return mask[y1:y2, x1:x2], (x1, y1, x2 - x1, y2 - y1)


def split_digits_by_projection(cluster_img):
    # vertical projection
    col_sum = np.sum(cluster_img > 0, axis=0)

    spans = []
    in_run = False
    start = 0

    for i, v in enumerate(col_sum):
        if v > 0 and not in_run:
            start = i
            in_run = True
        elif v == 0 and in_run:
            spans.append((start, i))
            in_run = False

    if in_run:
        spans.append((start, len(col_sum)))

    digits = []
    for x1, x2 in spans:
        digit = cluster_img[:, x1:x2]
        digits.append((x1, digit))

    return digits


def classify_digit(binary_digit, lookup):
    key = bitmap_key(binary_digit)
    if key in lookup:
        return lookup[key]

    # fallback: nearest bitmap by Hamming distance
    best_digit = None
    best_dist = 10**9

    vec = np.array(key, dtype=np.uint8)
    for tmpl_key, digit in lookup.items():
        tmpl_vec = np.array(tmpl_key, dtype=np.uint8)
        dist = np.count_nonzero(vec != tmpl_vec)
        if dist < best_dist:
            best_dist = dist
            best_digit = digit

    return best_digit


def detect_numbers(img, template_dir="templates", debug=False):
    
    # optional: only scan the top band if your counts are always there
    # img = img[:35, :]

    mask = yellow_mask(img)
    boxes = connected_boxes(mask)
    clusters = merge_boxes_into_clusters(boxes)
    lookup = load_digit_lookup(template_dir)

    found = []
    dbg = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    for cluster in clusters:
        cluster_img, (x, y, w, h) = crop_cluster(mask, cluster)
        pieces = split_digits_by_projection(cluster_img)

        text = ""
        for rel_x, digit_img in pieces:
            ch = classify_digit(digit_img, lookup)
            text += ch

            if debug:
                cv2.rectangle(dbg, (x + rel_x, y), (x + rel_x + digit_img.shape[1], y + digit_img.shape[0]), (0, 255, 0), 1)

        if text:
            found.append((x, text))

        if debug:
            cv2.rectangle(dbg, (x, y), (x + w, y + h), (255, 0, 0), 1)
            cv2.putText(dbg, text, (x, max(10, y - 2)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)

    found.sort(key=lambda t: t[0])

    if debug:
        cv2.imwrite("debug_mask.png", mask)
        cv2.imwrite("debug_detect.png", dbg)

    return [text for _, text in found]


if __name__ == "__main__":
    img_path = "brians.png"
    img = cv2.imread(img_path)
    if img is None:
        raise FileNotFoundError(img_path)

    numbers = detect_numbers(img, template_dir="templates", debug=True)
    print(numbers)