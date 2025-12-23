#!/usr/bin/env python3

from icecream import ic
import pyautogui
import argparse
import time

from utils import write_json, get_one_left_click, esc

def parse_args():
    parser = argparse.ArgumentParser(description='Writes the json file to load into the doer')
    parser.add_argument('--output', type=str, default='./gold.json', help='File to save the coordinates to')
    return vars(parser.parse_args())


args = parse_args()

ic('Click to open bank')
open_bank = get_one_left_click()

ic('Click to withdraw gold')
gold = get_one_left_click()

ic('Click to get to the smelter')
walk_to_furnace = get_one_left_click()

ic('Click to smelt')
smelt = get_one_left_click()

ic('Click to confirm smelt')
_ = get_one_left_click()

ic('Click to mold')
_ = get_one_left_click()

ic('Click to confirm')
_ = get_one_left_click()

ic('Click back to the same bank spot')
back_to_bank = get_one_left_click()
ic(back_to_bank)


ic('Click to open bank')
_ = get_one_left_click()

ic('Click to deposit jewlery')
d_jewlery = get_one_left_click()

time.sleep(0.7)
ic('Closing bank')
esc(0)


coordinates = {
    'open_bank': open_bank,
    'gold': gold,
    'walk_to_furnace': walk_to_furnace,
    'smelt': smelt,
    'back_to_bank': back_to_bank,
    'deposit_jelwery': d_jewlery,
}

ic(coordinates)

write_json(coordinates, args['output'])


