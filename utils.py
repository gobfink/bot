import json
import pyautogui
from pynput import mouse
import time
import random
from icecream import ic
import numpy as np

TICK_TIME=0.6
MENU_ITEM_SIZE=20

def write_json(j_data, file):
    with open(file,'w') as f:
        json.dump(j_data,f,indent=4)

def get_one_left_click():
    l = {'pos': None}

    def on_click(x, y, button, pressed):
        if pressed and button == mouse.Button.left:
            l['pos'] = (x,y)
            return False

    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
    return l['pos']

def get_rgb(rgb: tuple[int,int,int], region: tuple[int,int,int,int], offset: tuple[int,int]):
    r, g, b = rgb
    screenshot = pyautogui.screenshot(region=region)
    img = np.array(screenshot)
    mask = (
        (img[:,:,0] == r) &
        (img[:,:,1] == g) &
        (img[:,:,2] == b) 
    )
    ys, xs = np.where(mask)
    if len(xs) == 0:
        return []
    
    xs += region[0] + offset[0]
    ys += region[1] + offset[1]

    coords = list(zip(xs,ys))
    return coords

def click(coordinates, sleep=0, pixels_to_fuzz=0):
    x = pixel_fuzz(coordinates[0], pixels_to_fuzz)
    y = pixel_fuzz(coordinates[1], pixels_to_fuzz)
    pyautogui.moveTo(x=x, y=y)
    pyautogui.click()
    sleep_f = fuzz(sleep)
    time.sleep(sleep_f)
    ic('click',x,y,sleep_f)

def right_click(coordinates, sleep=TICK_TIME, pixels_to_fuzz=0):
    x = pixel_fuzz(coordinates[0], pixels_to_fuzz)
    y = pixel_fuzz(coordinates[1], pixels_to_fuzz)
    pyautogui.rightClick(x=x, y=y)
    sleep_f = fuzz(sleep)
    time.sleep(sleep_f)
    ic('right click', x,y,sleep_f)
    
def open_inv(sleep):
    press('esc',sleep)

def esc(sleep):
    press('esc', sleep)

def open_magic(sleep):
    press('f6', sleep)

def confirm(sleep):
    press('space', sleep)

def press(key, sleep):
    pyautogui.press(key)
    sleep_f = fuzz(sleep)
    ic('press', key, sleep_f)
    time.sleep(sleep_f)

def hold_and_press(hold_keys: list, press, sleep):
    for key in hold_keys:
        pyautogui.keyDown(key)
    
    pyautogui.press(press)
    for key in hold_keys:
        pyautogui.keyUp(key)
    
    sleep_f = fuzz(sleep)
    time.sleep(sleep_f)

def fuzz(value, amount=0.05):
    return value * (1 + random.uniform(-amount,amount))

def pixel_fuzz(value, number_of_pixels):
    offset = random.randint(-number_of_pixels, number_of_pixels)
    return value + offset

def random_true(probability):
    return random.random() < probability
