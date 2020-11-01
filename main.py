# this will spam the hell out of some discord
import pyautogui

print(pyautogui.size())
count = 0
while count == 0:
    pyautogui.moveTo(900, 1000, duration=1)
    pyautogui.click()
    pyautogui.press('Enter')
    pyautogui.typewrite('@staff')
    pyautogui.press('Enter')
    pyautogui.press('Enter')

"""You can replace the @staff with whatever/whoever, and it
typically works just fine. I originally made this to spam the hell
out of my fiance. She was spamming me at the time, so ya know :O"""

"""I am not responsible if you get banned - this is for learning"""
