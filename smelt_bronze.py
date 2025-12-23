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
t = time.perf_counter()

ic('Click on furnace')
walk_to_furnace = get_one_left_click()
duration = time.perf_counter() - t
ic(walk_to_furnace, duration)
t = time.perf_counter()

ic('Click to smelt all')
smelt = get_one_left_click()
duration = time.perf_counter() - t
ic(smelt, duration)
t = time.perf_counter()

ic('Click back to the same bank spot')
back_to_bank = get_one_left_click()
duration = time.perf_counter() - t
ic(back_to_bank)
t = time.perf_counter()

ic('Click to open bank')
open_bank = get_one_left_click()
duration = time.perf_counter() - t
ic(open_bank, duration)
t = time.perf_counter()

ic('Click to withdraw copper')
w_copper = get_one_left_click()
duration = time.perf_counter() - t
ic(w_copper, duration)
t = time.perf_counter()

ic('Click to deposit bars')
d_bars = get_one_left_click()
duration = time.perf_counter() - t
ic(d_bars, duration)
t = time.perf_counter()

ic('Click to withdraw tin')
w_tin = get_one_left_click()
duration = time.perf_counter() - t
ic(w_tin, duration)

ic('Click to the alternate furnace spot')
alternate_furnace = get_one_left_click()
ic(alternate_furnace)

ic('Click to recover and smelt')
alternate_smelt = get_one_left_click()
ic(alternate_smelt)

coordinates = {
    'walk_to_furnace': walk_to_furnace,
    'smelt': smelt,
    'back_to_bank': back_to_bank,
    'open_bank': open_bank,
    'withdraw_copper': w_copper,
    'deposit_bars': d_bars,
    'withdraw_tin': w_tin,
    'smelter': smelter,
    'alternate_furnace': alternate_furnace,
    'alternate_smelt': alternate_smelt,
}

ic(coordinates)

write_json(coordinates, args['output'])


