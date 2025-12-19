#! /usr/bin/env python3
import pyautogui
import numpy as np
import random
import time
import argparse
from icecream import ic

CHICKEN_RGB = (255, 0, 255)  # R, G, B
LEVEL_1_RGB = (0, 255, 0)
ITEM_RGB = (170,0,255)
TOLERANCE = 1  # set to e.g. 5–10 if you want "close enough" colors

top_left = (1100, 450)
screen_size = (75, 250)

region = top_left + screen_size

def parse_args():
    parser = argparse.ArgumentParser(description='Collecter and attacker')
    parser.add_argument('--min_delay', help='Minimum delay between actions', type=float, default=5)
    parser.add_argument('--max_delay', help='Max delay between actions', type=float, default=15)
    args = parser.parse_args()
    return vars(args)

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
    if not chicken_tiles:
        print('Unable to find chicken')
        return False
    m = random.choice(chicken_tiles)
    ic(m)
    x, y = m
    pyautogui.moveTo(x=x, y=y)
    pyautogui.click()
    # Wait for combat to finish
    delay = random.uniform(3,8)
    time.sleep(delay)
    return True

def collect():
    tiles = get_matching_pixels_numpy(ITEM_RGB, tolerance=TOLERANCE)
    if not tiles:
        print('Unable to find anything')
        return False
    m = random.choice(tiles)
    x, y = m
    pyautogui.moveTo(x=x, y=y)
    pyautogui.click()
    return True

def delay(d_min, d_max):
    _delay = random.uniform(d_min, d_max)
    ic(_delay)
    time.sleep(_delay)

args = parse_args()
while True:
    found = True
    #while found:
    #    found = collect()
    #    delay(args['min_delay'], args['max_delay'])
    attack_chicken()
    delay(args['min_delay'], args['max_delay'])
