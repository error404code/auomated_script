from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Title  1 Position: X: 358 Y: 400
#Title  2 Position  X: 463 Y: 400
#Title  3 Position: X: 559 Y: 400
#Title  4 Position  X: 661 Y: 400

def click(x, y):
    win32api.SetCursorPos(x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01) #pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(358, 400)[0] == 0:
        click(358, 400)
    if pyautogui.pixel(463, 400)[0] == 0:
        click(463, 400)
    if pyautogui.pixel(559, 400)[0] == 0:
        click(559, 400)
    if pyautogui.pixel(661, 400)[0] == 0:
        click(661, 400)
        
        
