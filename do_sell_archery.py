#!/usr/bin/env python3

import argparse
import json
import pyautogui
from icecream import ic
import time
import cv2
import numpy as np
from tqdm import tqdm
from utils import right_click, click, get_rgb, hold_and_press, press, MENU_ITEM_SIZE, TICK_TIME
from number_detector import detect_numbers


SELL_QUANTITY = {
        'mithril_arrow': 1000,
        'adamant_arrow': 800,
        'oak_longbow': 4,
        'willow_shortbow': 3,
        'willow_longbow': 3,
        'maple_shortbow': 2,
        'maple_longbow': 2,
}

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
    time.sleep(2)

def interpret_inventory(top_row, row_2):
    return {
        'steel_arrow': int(top_row[0]),
        'mithril_arrow': int(top_row[1]),
        'adamant_arrow': int(top_row[2]),
        'oak_shortbow': int(top_row[3]),
        'oak_longbow': int(top_row[4]),
        'willow_shortbow': int(top_row[5]),
        'willow_longbow': int(top_row[6]),
        'maple_shortbow': int(top_row[7]),
        'maple_longbow': int(row_2[0]),
    }

def read_inventory(store_left):
    row_width = 360
    row_height = 45
    tr_region = store_left + [row_width, row_height]
    top_row = pyautogui.screenshot(region=tr_region)
    top_row = cv2.cvtColor(np.array(top_row), cv2.COLOR_RGB2BGR)
    r2_region = tr_region.copy()
    r2_region[1] += row_height
    row_2 = pyautogui.screenshot(region=r2_region)
    row_2 = cv2.cvtColor(np.array(row_2), cv2.COLOR_RGB2BGR)

    tr_numbers = detect_numbers(top_row)
    r2_numbers = detect_numbers(row_2)

    inventory = interpret_inventory(tr_numbers, r2_numbers)
    ic(inventory)
    return inventory


    
args = parse_args()

coords = None
with open(args['input']) as f:
    coords = json.load(f)

assert coords
ic(coords)

for i in tqdm(range(args['iterations'])):
    ic(i)
    trade_bryan(coords['region'])
    inventory = read_inventory(coords['store_left'])
    if not inventory:
        ic('Unable to read invetory trying again')
        time.sleep(1)
        continue
    for item in coords.keys():
        if item == 'region' or item == 'store_left':
            #Don't need to click on the region
            continue
        sell_q = SELL_QUANTITY[item]
        inv_q = inventory[item]
        if inv_q > sell_q:
            ic(item, inv_q, '>', sell_q, 'Skipping!')
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
            

