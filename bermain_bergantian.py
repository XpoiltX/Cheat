import pyautogui
import time

def bermain_bergantian():
    while True:
        # Bermain game secara bergantian
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.1)