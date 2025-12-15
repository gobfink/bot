#!/usr/bin/env python3

import argparse
import json
import pyautogui
from icecream import ic
import time
import random
from tqdm import tqdm
from utils import click, confirm



def parse_args():
    parser = argparse.ArgumentParser(description='Reads the json file and clicks on the coordinates to perform bones to bananas')
    parser.add_argument('--input', type=str, default='./gold.json', help='File with pixel coordinates')
    parser.add_argument('--iterations', type=int, default=1, help='Number of iterations to complete')
    return vars(parser.parse_args())

args = parse_args()

coords = None
with open(args['input']) as f:
    coords = json.load(f)

assert coords

ic('Opening bank')
click(coords['open_bank'],3)
for i in tqdm(range(args['iterations'])):
    ic(i)
    ic('Withdrawing gold')
    click(coords['gold'], 1)
    ic('Walking to furnace')
    click(coords['walk_to_furnace'], 6)

    ic('Clicking on furnace to smelt')
    click(coords['smelt'], 1.5)
    ic('Smelting all')
    confirm(85)
    ic('Molding all')
    click(coords['smelt'], 1.5)
    confirm(60)
    ic('back to bank')
    click(coords['back_to_bank'], 6)
    ic('Open bank')
    click(coords['open_bank'], 1)
    ic('deposit jewlery')
    click(coords['deposit_jelwery'], 1)

