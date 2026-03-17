#!/usr/bin/env python3

import argparse
import json
import pyautogui
from icecream import ic
import time
import random
from tqdm import tqdm
from utils import right_click, click, get_rgb, hold_and_press, press, MENU_ITEM_SIZE, TICK_TIME
from number_detector import detect_numbers


def parse_args():
    parser = argparse.ArgumentParser(description='Reads the json file and clicks on the coordinates to perform bones to bananas')
    parser.add_argument('--input', type=str, default='./alch.json', help='File with pixel coordinates')
    parser.add_argument('--iterations', type=int, default=1, help='Number of iterations to complete')
    return vars(parser.parse_args())

def trade_bryan(region):
    ic('Trading with Brian')
    cyans = get_rgb((0,255,255), region, offset=(0,0))
    bryan = list(cyans[0])
    trade_bryan = bryan.copy()
    trade_bryan[1] += MENU_ITEM_SIZE * 2 - 5
    pyautogui.moveTo(bryan)
    time.sleep(0.005)
    # Right click bryan
    right_click(bryan)
    # Click to trade him
    click(trade_bryan)
    time.sleep(TICK_TIME)

def read_inventory(store_left):
    row_width = 360
    row_height = 45
    tr_region = store_left + [row_width, row_height]
    top_row = pyautogui.screenshot(region=tr_region)
    r2_region = tr_region.copy()
    r2_region[1] += row_height
    row_2 = pyautogui.screenshot(region=r2_region)

    tr_numbers = detect_numbers(top_row)
    r2_numbers = detect_numbers(row_2)
    breakpoint()
    
args = parse_args()

coords = None
with open(args['input']) as f:
    coords = json.load(f)

assert coords
ic(coords)

for i in tqdm(range(args['iterations'])):
    ic(i)
    trade_bryan()
    inventory = read_inventory()
    breakpoint()
    for item in coords.keys():
        if item == 'region' or item == 'store_left':
            #Don't need to click on the region
            continue
        coord = coords[item]
        sell_5 = coord.copy()
        sell_5[1] += MENU_ITEM_SIZE * 3 - 5
        ic(item, coord, sell_5)
        right_click(coordinates=coord,pixels_to_fuzz=5)
        click(sell_5)
    
    # Keys to switch worlds
    press('esc', 1)
    hold_and_press(['ctrlleft','shiftleft'], 'right', 2)
    press('space', 6)
            

