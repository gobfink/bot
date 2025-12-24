#!/usr/bin/env python3

from icecream import ic
import argparse

from utils import write_json, get_one_left_click, click, open_magic

def parse_args():
    parser = argparse.ArgumentParser(description='Writes the json file to load into the doer')
    parser.add_argument('--output', type=str, default='./tele.json', help='File to save the coordinates to')
    return vars(parser.parse_args())


args = parse_args()

ic('Opening magic')
open_magic(1)

ic('Click teleport')
tele = get_one_left_click()

coordinates = {
    'tele': tele,
}
ic(coordinates)
write_json(coordinates, args['output'])


