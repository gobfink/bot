#!/usr/bin/env python3

import argparse
import json
import pyautogui
from icecream import ic
import time
import random
from tqdm import tqdm
from utils import click, confirm, random_true



def parse_args():
    parser = argparse.ArgumentParser(description='Reads the json file and clicks on the coordinates to perform bones to bananas')
    parser.add_argument('--input', type=str, default='./silver.json', help='File with pixel coordinates')
    parser.add_argument('--iterations', type=int, default=1, help='Number of iterations to complete')
    parser.add_argument('--probability', type=float, default=0.5, help='probability of using alternate smelt')
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
    ic('Withdrawing silver')
    click(coords['silver'], 1)
    
    if random_true(args['probability']):
        ic('Walking to alternate spot')
        click(coords['alternate_furnace'], 6)
        ic('Smelting from alternate spot')
        click(coords['alternate_smelt'], 1.5, 5)
    else:
        ic('Walking to furnace')
        click(coords['walk_to_furnace'], 6)
        ic('Walking to furnance to smelt')
        click(coords['smelt'], 1.5, 5)
    
    ic('Smelting all')
    confirm(88)
    ic('back to bank')
    click(coords['back_to_bank'], 6)
    ic('Open bank')
    click(coords['open_bank'], 1, 5)
    ic('deposit bars')
    click(coords['deposit_bars'], 1, 5)

