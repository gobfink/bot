#!/usr/bin/env python3

import argparse
import json
import pyautogui
from icecream import ic
import time
import random
from tqdm import tqdm
from utils import click



def parse_args():
    parser = argparse.ArgumentParser(description='Reads the json file and clicks on the coordinates to perform bones to bananas')
    parser.add_argument('--input', type=str, default='./string_amulets.json', help='File with pixel coordinates')
    parser.add_argument('--iterations', type=int, default=1, help='Number of iterations to complete')
    return vars(parser.parse_args())

args = parse_args()

coords = None
with open(args['input']) as f:
    coords = json.load(f)

assert coords

for i in tqdm(range(args['iterations'])):
    ic(i)
    ic('Selecting amulet')
    click(coords['amulet'],1)
    ic('Selecting wool')
    click(coords['wool'],1)
    ic('Confirming')
    click(coords['confirm'],20)
    ic('Opening bank')
    click(coords['bank'], 3)
    ic('Withdrawing wool')
    click(coords['withdraw_wool'], 1)
    ic('Depositing amulets')
    click(coords['deposit_amulets'],1)
    ic('Withdrawing unstrung amulets')
    click(coords['withdraw_amulets'],1)
    ic('Closing bank')
    click(coords['close'],1)

