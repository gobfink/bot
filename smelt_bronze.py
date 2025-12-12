#!/usr/bin/env python3

from icecream import ic
import pyautogui
import argparse
import time

from utils import write_json, get_one_left_click, click

def parse_args():
    parser = argparse.ArgumentParser(description='Writes the json file to load into the doer')
    parser.add_argument('--output', type=str, default='./bronze.json', help='File to save the coordinates to')
    return vars(parser.parse_args())


args = parse_args()
ic('This script expects you to be loaded with 14 copper and 14 tin')

ic('Click to get to the smelter')
# Don't store this one (not sure if we'll get back here)
smelter = get_one_left_click()

ic('Click on furnace')
walk_to_furnace = get_one_left_click()
ic(walk_to_furnace)

ic('Click to smelt all')
smelt = get_one_left_click()
ic(smelt)

ic('Click back to the same bank spot')
back_to_bank = get_one_left_click()
ic(back_to_bank)

ic('Click to open bank')
open_bank = get_one_left_click()
ic(open_bank)

ic('Click to withdraw copper')
w_copper = get_one_left_click()
ic(w_copper)

ic('Click to deposit bars')
d_bars = get_one_left_click()
ic(d_bars)

ic('Click to withdraw tin')
w_tin = get_one_left_click()
ic(w_tin)

# ic('Click to get back to the smelter')
# smelter = get_one_left_click()
# ic(smelter)

coordinates = {
    'walk_to_furnace': walk_to_furnace,
    'smelt': smelt,
    'back_to_bank': back_to_bank,
    'open_bank': open_bank,
    'withdraw_copper': w_copper,
    'deposit_bars': d_bars,
    'withdraw_tin': w_tin,
    'smelter': smelter,
}

ic(coordinates)

write_json(coordinates, args['output'])


