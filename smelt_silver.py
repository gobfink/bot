#!/usr/bin/env python3

from icecream import ic
import pyautogui
import argparse
import time

from utils import write_json, get_one_left_click, click

def parse_args():
    parser = argparse.ArgumentParser(description='Writes the json file to load into the doer')
    parser.add_argument('--output', type=str, default='./silver.json', help='File to save the coordinates to')
    return vars(parser.parse_args())


args = parse_args()

ic('Click to open bank')
open_bank = get_one_left_click()

ic('Click to withdraw silver')
silver = get_one_left_click()

ic('Click to get to the smelter')
# Don't store this one (not sure if we'll get back here)
walk_to_furnace = get_one_left_click()
ic('Click to smelt')
smelt = get_one_left_click()

ic('Click to smelt all')
_ = get_one_left_click()

ic('Click back to the same bank spot')
back_to_bank = get_one_left_click()
ic(back_to_bank)

ic('Open bank')
_ = get_one_left_click()

ic('Click to deposit bars')
d_bars = get_one_left_click()

coordinates = {
    'open_bank': open_bank,
    'silver': silver,
    'walk_to_furnace': walk_to_furnace,
    'smelt': smelt,
    'back_to_bank': back_to_bank,
    'deposit_bars': d_bars,
}

ic(coordinates)

write_json(coordinates, args['output'])


