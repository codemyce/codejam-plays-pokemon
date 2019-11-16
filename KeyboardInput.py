import keyboard
from pywinauto import Application
import time
import string
# open up the emulator and load up the rom

emulator = Application().start("bsnes-hd_beta9.exe")
print('hello')
keyboard.press_and_release('alt, enter, down, enter, enter')

while True:
    time.sleep(0.08)
    # try:
    #     if keyboard.is_pressed('left'):
    #         keyboard.send('left',)
    #     elif keyboard.is_pressed('right'):
    #         print('right key is pressed')
    #         keyboard.send('right')
    #     else:
    #         pass
    #     if keyboard.is_pressed('u'):
    #         print('B button is pressed')
    #         keyboard.release('y')
    #         keyboard.send('u')
    #     elif keyboard.is_pressed('y'):
    #         print('A button is pressed')
    #         keyboard.send('y',do_release=False)
    #     else:
    #         pass        
    # except:
    #     pass
    try:
        if keyboard.is_pressed('x'):
            keyboard.send('u',do_release=False)
    except:
        pass

"""
threads = [Thread(target=listen, kwargs={"key": key}) for key in keys]
for thread in threads:
    thread.start()


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
