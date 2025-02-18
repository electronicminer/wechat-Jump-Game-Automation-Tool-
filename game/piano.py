import pyautogui
import cv2
import numpy as np
import time
import keyboard
from ctypes import * 

def get_color(x, y):
    gdi32 = windll.gdi32
    user32 = windll.user32
    hdc = user32.GetDC(None)  
    pixel = gdi32.GetPixel(hdc, x, y)  
    r = pixel & 0x0000ff
    g = (pixel & 0x00ff00) >> 8
    b = pixel >> 16
    return [r, g, b]

while (1):
    if keyboard.is_pressed('1'):
        x1, y1 = pyautogui.position() 
        print('1 ready')

    if keyboard.is_pressed('2'):
        x2, y2 = pyautogui.position() 
        print('2 ready') 

    if keyboard.is_pressed('3'):
        x3, y3 = pyautogui.position()  
        print('3 ready')

    if keyboard.is_pressed('4'):
        x4, y4 = pyautogui.position() 
        print('4 ready') 

    if keyboard.is_pressed('q'):
        break

while (1):
    if get_color(x1, y1)[0] < 50:
        pyautogui.click(x1, y1-100)
    if get_color(x2, y2)[0] < 50:
        pyautogui.click(x2, y2-100)
    if get_color(x3, y3)[0] < 50:
        pyautogui.click(x3, y3-100)
    if get_color(x4, y4)[0] < 50:
        pyautogui.click(x4, y4-100)
    if get_color(x1, y1)[0] < 50:
        pyautogui.click(x1, y1-100)
    if get_color(x2, y2)[0] < 50:
        pyautogui.click(x2, y2-100)
    if get_color(x3, y3)[0] < 50:
        pyautogui.click(x3, y3-100)
    if get_color(x4, y4)[0] < 50:
        pyautogui.click(x4, y4-100)
    if keyboard.is_pressed('a'):
        break