#!/usr/bin/env python3

import argparse
import json
import pyautogui
from icecream import ic
import time
import random
import tqdm
from utils import click, random_true


def parse_args():
    parser = argparse.ArgumentParser(description='Reads the json file and clicks on the coordinates to perform bones to bananas')
    parser.add_argument('--input', type=str, default='./bronze.json', help='File with pixel coordinates')
    parser.add_argument('--iterations', type=int, default=1, help='Number of iterations to complete')
    parser.add_arugment('--probablity', type=float, default=0.5, help='Probablity of using alternate smelt')
    return vars(parser.parse_args())

args = parse_args()

coords = None
with open(args['input']) as f:
    coords = json.load(f)

assert coords

ic('Expecting to start with 14 coppers and 14 tins')
for i in tqdm(range(args['iterations'])):
    ic(i)
    if random_true(args['probablity']):
        ic('Walking to alternate spot')
        click(coords['alternate_furnace'], 6)
        ic('Smelting from alternate spot')
        click(coords['alternate_smelt'], 1.5, 5)
    else:
        ic('Walking to smelter')
        click(coords['smelter'], 6)

        ic('Walking to furnance to smelt')
        click(coords['walk_to_furnace'], 1.5, 5)

    ic('Smelting all')
    click(coords['smelt'], 45, 5)
    ic('back to bank')
    click(coords['back_to_bank'], 6)
    ic('Open bank')
    click(coords['open_bank'], 1, 4)
    ic('Withdraw copper')
    click(coords['withdraw_copper'], 1, 5)
    ic('deposit bars')
    click(coords['deposit_bars'], 1, 5)
    ic('withdraw tin')
    click(coords['withdraw_tin'], 1, 5)

