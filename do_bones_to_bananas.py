#!/usr/bin/env python3

import argparse
import json
import pyautogui
from icecream import ic
import time
import random
from tqdm import tqdm

def parse_args():
    parser = argparse.ArgumentParser(description='Reads the json file and clicks on the coordinates to perform bones to bananas')
    parser.add_argument('--input', type=str, default='./bones2bananas.json', help='File with pixel coordinates')
    parser.add_argument('--iterations', type=int, default=1, help='Number of iterations to complete')
    return vars(parser.parse_args())

def click(coordinates, sleep=0):
    pyautogui.moveTo(x=coordinates[0], y=coordinates[1])
    pyautogui.click()
    sleep_f = fuzz(sleep)
    time.sleep(sleep_f)
    
def open_inv(sleep):
    press('esc',sleep)

def open_magic(sleep):
    press('f6', sleep)

def press(key, sleep):
    pyautogui.press(key)
    time.sleep(sleep)

def fuzz(value, amount=0.05):
    return value * (1 + random.uniform(-amount,amount))

args = parse_args()

coords = None
with open(args['input']) as f:
    coords = json.load(f)

assert coords

ic('Opening bank')
click(coords['bank'],sleep=1)
for i in tqdm(range(args['iterations'])):
    ic(i)
    ic('Withdrawing bones')
    click(coords['banked_bones'], 1)

    ic('Closing bank')
    click(coords['close_bank'], 1)

    ic('Casting bones to bananas')
    open_inv(0.1)
    open_magic(0.1)
    click(coords['bones2bananas'], 3.5)

    ic('Opening bank')
    click(coords['bank'], sleep=1)

    ic('Depositing bananas')
    click(coords['banana'], sleep=1)

ic('Closing bank')
click(coords['close_bank'], 1)
