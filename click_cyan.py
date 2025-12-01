#! /usr/bin/env python3
import pyautogui
import numpy as np
import random
import time

CHICKEN_RGB = (0, 255, 241)  # R, G, B
LEVEL_1_RGB = (0, 255, 0)
FEATHER_RGB = (170,0,255)
TOLERANCE = 1  # set to e.g. 5–10 if you want "close enough" colors

top_left = (1100, 450)
screen_size = (75, 250)

region = top_left + screen_size
def get_matching_pixels_numpy(target_rgb, region=None, tolerance=0):
    # Take screenshot and convert to NumPy array
    if region:
        screenshot = pyautogui.screenshot(region=region)
    else:
        screenshot = pyautogui.screenshot()
    img = np.array(screenshot)  # shape (H, W, 3), RGB

    r, g, b = target_rgb

    if tolerance == 0:
        # Exact match
        mask = (
            (img[:, :, 0] == r) &
            (img[:, :, 1] == g) &
            (img[:, :, 2] == b)
        )
    else:
        # Allow some variation
        mask = (
            (np.abs(img[:, :, 0] - r) <= tolerance) &
            (np.abs(img[:, :, 1] - g) <= tolerance) &
            (np.abs(img[:, :, 2] - b) <= tolerance)
        )

    # np.where returns (y_indices, x_indices)
    ys, xs = np.where(mask)
    if region and len(xs) != 0:
        xs += region[0]
        ys += region[1]

    if len(xs) == 0:
        return []

    # Combine into list of (x, y) tuples
    coords = list(zip(xs, ys))
    return coords

def attack_chicken():
    chicken_tiles = get_matching_pixels_numpy(CHICKEN_RGB, tolerance=TOLERANCE)
    m = random.choice(chicken_tiles)
    if not m:
        print('Unable to find chicken')
        return
    x, y = m
    pyautogui.moveTo(x=x, y=y)
    pyautogui.click()
    # Wait for combat to finish
    delay = random.uniform(3,6)
    time.sleep(delay)

def collect_feathers():
    feather_tiles = get_matching_pixels_numpy(FEATHER_RGB, tolerance=TOLERANCE)
    m = random.choice(feather_tiles)
    if not m:
        print('Unable to find feathers')
        return False
    x, y = m
    pyautogui.moveTo(x=x, y=y)
    pyautogui.click()
    #Give them some time to pick up the
    delay = random.uniform(2,4)
    time.sleep(delay)
    return True


while True:
    attack_chicken()
    collect_feathers()
