import pyautogui
import time

def tesks_bergantian():
    while True:
        # Menulis teks secara bergantian
        pyautogui.typewrite('Hello')
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite('World')
        pyautogui.press('enter')
        time.sleep(0.1)