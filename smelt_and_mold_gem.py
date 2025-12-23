#!/usr/bin/env python3

from icecream import ic
import pyautogui
import argparse
import time

from utils import write_json, get_one_left_click, click, confirm

def parse_args():
    parser = argparse.ArgumentParser(description='Writes the json file to load into the doer')
    parser.add_argument('--output', type=str, default='./gem.json', help='File to save the coordinates to')
    return vars(parser.parse_args())


args = parse_args()
ic('Start with 13 gems and 13 gold 1 mold and 1 other')
ic('Click to furnace')
walk_to_furnace = get_one_left_click()
ic('Click to smelt gold')
smelt = get_one_left_click()
ic('Click confirm')
_ = get_one_left_click()
ic('Click to mold necklaces')
_ = get_one_left_click()
ic('Click to confirm')
_ = get_one_left_click()
ic('Click back to bank')
back_to_bank = get_one_left_click()
ic('Click to open bank')
open_bank = get_one_left_click()
ic('Click to withdraw gold')
gold = get_one_left_click()
ic('Click to deposit jewlery')
d_jewlery = get_one_left_click()
ic('Click to withdraw gems')
gems = get_one_left_click()
ic('Click to the wrong furnace spot')
alternate_furnace = get_one_left_click()
ic('Click to smelt from wrong spot')
alternate_smelt = get_one_left_click()

coordinates = {
    'walk_to_furnace': walk_to_furnace,
    'smelt': smelt,
    'back_to_bank': back_to_bank,
    'open_bank': open_bank,
    'gold': gold,
    'deposit_jewlery': d_jewlery,
    'gems': gems,
    'alernate_furnace': alternate_furnace,
    'alternate_smelt': alternate_smelt,
}

ic(coordinates)

write_json(coordinates, args['output'])


