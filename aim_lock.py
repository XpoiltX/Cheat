import pyautogui
import time

def aim_lock():
    while True:
        # Cek lokasi musuh
        lokasi_musuh = pyautogui.position()
        if abs(lokasi_musuh[0] - 500) < 50 and abs(lokasi_musuh[1] - 300) < 50:
            # Aim lock
            pyautogui.moveTo(500, 300)
            time.sleep(0.1)