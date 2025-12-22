#!/usr/bin/env python3

import argparse
import json
import pyautogui
from icecream import ic
import time
import random
from tqdm import tqdm
from utils import click, get_one_left_click



def parse_args():
    parser = argparse.ArgumentParser(description='Click a spot, then sleep and loop for iterations')
    parser.add_argument('--iterations', type=int, default=1, help='Number of iterations to complete')
    parser.add_argument('--sleep', type=float, help='Sleep time', default=10)
    return vars(parser.parse_args())

args = parse_args()

ic('click somewhere to loop')
spot = get_one_left_click()
ic(spot)


for i in tqdm(range(args['iterations'])):
    ic(i, spot, args['sleep'])
    click(coordinates=spot, sleep=args['sleep'], pixels_to_fuzz=3)

