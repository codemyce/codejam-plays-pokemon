import keyboard
from pywinauto import Application

# open up the emulator and load up the rom
emulator = Application().start("bsnes-hd_beta9.exe")
keyboard.press_and_release('alt, enter, down, enter, enter')
