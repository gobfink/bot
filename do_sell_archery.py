#!/usr/bin/env python3

import argparse
import json
import pyautogui
from icecream import ic
import time
import random
from tqdm import tqdm
from utils import right_click, click, get_rgb, MENU_ITEM_SIZE



def parse_args():
    parser = argparse.ArgumentParser(description='Reads the json file and clicks on the coordinates to perform bones to bananas')
    parser.add_argument('--input', type=str, default='./alch.json', help='File with pixel coordinates')
    parser.add_argument('--iterations', type=int, default=1, help='Number of iterations to complete')
    return vars(parser.parse_args())

args = parse_args()

coords = None
with open(args['input']) as f:
    coords = json.load(f)

assert coords
ic(coords)

ic('Trading with Brian')
cyans = get_rgb((0,255,255), coords['region'], offset=(20,20))
bryan = list(cyans[0])
trade_bryan = bryan.copy()
trade_bryan[1] += MENU_ITEM_SIZE * 3 - 5
# Right click bryan
right_click(bryan)
# Click to trade him
click(trade_bryan)



for i in tqdm(range(args['iterations'])):
    for item in coords.keys():
        coord = coords[item]
        sell_5 = coord.copy()
        sell_5[1] += MENU_ITEM_SIZE * 3 - 5
        ic(item, coord, sell_5)
        right_click(coordinates=coord,pixels_to_fuzz=5)
        click(sell_5)
        

        # Right click each item 
        # Wait a tick
        # Scroll to sell 5


