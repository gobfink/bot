#!/usr/bin/env python3

from pynput import mouse
from icecream import ic
import pyautogui
import argparse
import time
import json

def parse_args():
    parser = argparse.ArgumentParser(description='Writes the json file to load into the doer')
    parser.add_argument('--output', type=str, default='./bones2bananas.json', help='File to save the coordinates to')
    return vars(parser.parse_args())

def get_one_left_click():
    l = {'pos': None}

    def on_click(x, y, button, pressed):
        if pressed and button == mouse.Button.left:
            l['pos'] = (x,y)
            return False

    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
    return l['pos']

def open_bank(x, y, delay=0.2):
    pyautogui.moveTo(x=x, y=y)
    pyautogui.click()
    pyautogui.moveRel(xOffset=1, yOffset=1, duration=delay)
    pyautogui.click()
    pass

def open_magic():
    pyautogui.press('f6')

def open_inv():
    pyautogui.press('esc')

def write_json(j_data, file):
    with open(file,'w') as f:
        json.dump(j_data,f,indent=4)


args = parse_args()

ic('Click on bank')
bank = get_one_left_click()

ic(bank)
open_bank(bank[0], bank[1])

ic('Click on banked bones')
bbones = get_one_left_click()
ic(bbones)

ic('Close the bank')
close_bank = get_one_left_click()
ic(close_bank)

ic('Click on bones to bananas')
open_inv()
time.sleep(0.1)
open_magic()
bones2bananas = get_one_left_click()
ic(bones2bananas)
time.sleep(3.5)

# input('Move mouse away and press a key')
ic('Opening bank')
open_bank(bank[0], bank[1])
time.sleep(1.7)
ic('Click on banana in inventory')
banana = get_one_left_click()
ic(banana)
time.sleep(0.2)

coordinates = {
    'bank': bank,
    'banked_bones': bbones,
    'close_bank': close_bank,
    'bones2bananas': bones2bananas,
    'banana': banana
}

write_json(coordinates, args['output'])


