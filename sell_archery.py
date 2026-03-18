#!/usr/bin/env python3

from icecream import ic
import pyautogui
import argparse
import time
import numpy as np

from utils import write_json, get_one_left_click, click, open_magic

def parse_args():
    parser = argparse.ArgumentParser(description='Writes the json file to load into the doer')
    parser.add_argument('--output', type=str, default='./archery.json', help='File to save the coordinates to')
    return vars(parser.parse_args())


args = parse_args()

ic('Click top left of screen')
top_left = get_one_left_click()

ic('Click bottom right of screen')
bottom_right = get_one_left_click()

ic('Click the top left of the first store row')
store_left = get_one_left_click()

ic('Click mithril arrow')
m_arrow = get_one_left_click()

ic('Click adamant arrow')
ad_arrow = get_one_left_click()

ic('Click Oak longbow')
o_longbow = get_one_left_click()

ic('Click Willow shortbow')
w_shortbow = get_one_left_click()

ic('Click Willow longbow')
w_longbow = get_one_left_click()

ic('Click Maple shortbow')
m_shortbow = get_one_left_click()

ic('Click Maple longbow')
m_longbow = get_one_left_click()
width = (np.array(bottom_right) - np.array(top_left)).tolist()
region = list(top_left) + width
coordinates = {
    'region': region,
    'store_left': store_left,
    'mithril_arrow': m_arrow,
    'adamant_arrow': ad_arrow,
    'oak_longbow': o_longbow,
    'willow_shortbow': w_shortbow,
    'willow_longbow': w_longbow,
    'maple_shortbow': m_shortbow,
    'maple_longbow': m_longbow,
}

ic(coordinates)
write_json(coordinates, args['output'])


