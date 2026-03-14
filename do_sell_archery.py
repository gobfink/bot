#!/usr/bin/env python3

import argparse
import json
import pyautogui
from icecream import ic
import time
import random
from tqdm import tqdm
from utils import right_click



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

for i in tqdm(range(args['iterations'])):
    for item in coords.keys():
        coord = coords[item]
        ic(item, coord)
        right_click(coordinates=coord)
        

        # Right click each item 
        # Wait a tick
        # Scroll to sell 5


