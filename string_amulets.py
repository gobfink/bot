#!/usr/bin/env python3

from icecream import ic
import pyautogui
import argparse
import time

from utils import write_json, get_one_left_click, click

def parse_args():
    parser = argparse.ArgumentParser(description='Writes the json file to load into the doer')
    parser.add_argument('--output', type=str, default='./string_amulets.json', help='File to save the coordinates to')
    return vars(parser.parse_args())


args = parse_args()
ic('Requires to start with 14 wool and 14 amulets')

ic('Click on unstrung amulet')
amulet = get_one_left_click()
ic('Click on wool')
wool = get_one_left_click()
ic('Click to confirm')
confirm = get_one_left_click()
ic('Click bank')
bank = get_one_left_click()
ic('Click to withdraw wool')
w_wool = get_one_left_click()
ic('Click to deposit strung amulets')
d_amulets = get_one_left_click()
ic('Click to withdraw unstrung amulets')
w_amulets = get_one_left_click()
ic('Click to close bank')
close = get_one_left_click()


coordinates = {
    'amulet': amulet,
    'wool': wool,
    'confirm': confirm,
    'bank': bank,
    'withdraw_wool': w_wool,
    'deposit_amulets': d_amulets,
    'withdraw_amulets': w_amulets,
    'close': close
}

ic(coordinates)

write_json(coordinates, args['output'])


