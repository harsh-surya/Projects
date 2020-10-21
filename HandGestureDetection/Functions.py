import pyautogui
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

def movemouse(x,y,w,h):
    mx, my = pyautogui.position()
    delta_x = x - (w/2)
    delta_y = y - (h/2)
    pyautogui.moveTo(mx + delta_x, my + delta_y)

def movemouseslow(x,y,w,h):
    mx, my = pyautogui.position()
    delta_x = x - (w/2)
    delta_y = y - (h/2)
    pyautogui.moveTo(mx + (delta_x/5), my + (delta_y/5))
    
def lclick():
    pyautogui.click(button="left")
    
def double_lclick():
    pyautogui.click(button="left", clicks = 2)
    
def rclick():
    pyautogui.click(button="right")

def change_window():
    pyautogui.hotkey("alt", "tab")

#Function to assign action to different gestures
def action(text, x, y, w, h):
    if text == "Fist" or text == "Palm":
        movemouse(x, y, w, h)
    elif text == "Swing":
        movemouseslow(x, y, w, h)
    elif text == "OneFinger":
        lclick()
    elif text == "TwoFinger":
        double_lclick()
    elif text == "ThreeFinger":
        rclick()
    elif text == "Previous" or text =="Next":
        change_window()
    else:
        return

