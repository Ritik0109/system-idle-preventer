#!python3
#!mouse jiggler :)

import pyautogui
import time
import datetime

try:
    timer = int(input('Enter how long to spend (in minutes): '))
    print('Press Ctrl + C to exit')
    print('Timer is set for', timer, 'minutes')

    start = datetime.datetime.now()
    end = start + datetime.timedelta(minutes=timer)

    print(f'Start time: {start},End time: {end}')

    while start < end:
        time.sleep(10)
        pyautogui.press('volumedown')
        time.sleep(10)
        pyautogui.press('volumeup')
        start = datetime.datetime.now()


except ValueError:
    print("Invalid input. Please enter a number.")


print('Session over')
