#!/usr/bin/env python3

import argparse
import json
import pyautogui
from icecream import ic
import time
import random
from tqdm import tqdm
from utils import click, open_magic



def parse_args():
    parser = argparse.ArgumentParser(description='Reads the json file and clicks on the coordinates')
    parser.add_argument('--input', type=str, default='./tele.json', help='File with pixel coordinates')
    parser.add_argument('--iterations', type=int, default=1, help='Number of iterations to complete')
    return vars(parser.parse_args())

args = parse_args()

coords = None
with open(args['input']) as f:
    coords = json.load(f)

assert coords

for i in tqdm(range(args['iterations'])):
    ic(i)
    ic('Selecting tele')
    click(coords['tele'], 3, 4)

