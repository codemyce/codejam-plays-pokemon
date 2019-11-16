import keyboard
from pywinauto import Application
import time
import string
from threading import *

# open up the emulator and load up the rom

emulator = Application().start("bsnes-hd_beta9.exe")
keyboard.press_and_release('alt, enter, down, enter, enter')
time.sleep(5)

# listening for keyboard activities
keys = list(string.ascii_lowercase)

def listen(key):
    while True:
        keyboard.wait(key)
        print("[+] Pressed", key)


threads = [Thread(target=listen, kwargs={"key": key}) for key in keys]
for thread in threads:
    thread.start()

"""
    player 1 controls:  up = up
                        down = down
                        left = left
                        right = right
                        
                        A = y
                        B = u
                        X = h 
                        Y = j
                        
                        
    Will have to load the config to bsnes first !
"""
