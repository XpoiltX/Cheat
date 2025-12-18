import pyautogui
import random
import time

def tesks_akar():
    while True:
        # Menulis teks secara acak
        pyautogui.typewrite(''.join(random.choice(string.ascii_letters) for _ in range(10)))
        pyautogui.press('enter')
        time.sleep(0.1)