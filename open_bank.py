#!/usr/bin/env python3

from pynput import mouse
from icecream import ic
import pyautogui
import argparse
import time
bank = None

def parse_args():
    parser = argparse.ArgumentParser()
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
    pyautogui.move(x=x, y=y)
    pyautogui.click()
    # pyautogui.moveRel(xOffset=0, yOffset=40, duration=delay)
    # pyautogui.click()
    pass
def open_magic():
    pyautogui.press('f6')

def close_bank():
    pass
args = parse_args()
bank = args['bank']
if bank == None:
    ic('Click on bank')
    bank = get_one_left_click()
else:
    bank = args['bank']

ic(bank)
open_bank(bank[0], bank[1])

ic('Click on banked bones')
bbones = get_one_left_click()
ic(bbones)

ic('Close the bank')
close_bank = get_one_left_click()
ic(close_bank)

ic('Click on bones to bananas')
open_magic()
bones2bananas = get_one_left_click()
ic(bones2bananas)

time.sleep(0.5)
ic('Opening bank')
open_bank(bank[0], bank[1])
ic('Click on banana in inventory')
banana = get_one_left_click()
ic(banana)
