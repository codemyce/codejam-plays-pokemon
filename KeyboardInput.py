import keyboard
from pywinauto import Application
import time
import string
import threading
# open up the emulator and load up the rom

# INPUT ACTION INTO KEYBOARD SIGNAL

# Either 1 or 0, 1 indicates change needed
p1 = {
    'a': 0,
    'b': 0,
    'left': 0,
    'right': 0,
    'up': 0,
    'down': 0,
    'lTrigger': 0,
    'rTrigger': 0,
    'x': 0,
    'y': 0,
    'select': 0,
    'start': 0
}
p2 = {
    'a': 0,
    'b': 0,
    'left': 0,
    'right': 0,
    'up': 0,
    'down': 0,
    'lTrigger': 0,
    'rTrigger': 0,
    'x': 0,
    'y': 0,
    'select': 0,
    'start': 0
}
updateKeys = False
kill = False

# Update item
def updateItem(index, player):
    global p1, p2, updateKeys
    players = [p1,p2]

    try:
        players[player][index] = 1
        updateKeys = True
    except:
        pass

def readItem():
    global p1, p2, updateKeys
    for key in p1.keys():
        if p1[key] == 1:
            p1[key] = 0
            # Trigger action based on which key
            if key == 'a':

    # Same thing but for player 2
    for key in p1.keys():
        if p1[key] == 1:
            p1[key] = 0
            # Trigger action based on which key




# 0 is not pressed, 1 is currently presed, 2 is need to press, 3 is need to release
# Space and q are special, if pressed gets set to 1, this is the change state button/exits
# keys = {
#     'a': 0,
#     'b': 0,
#     'left': 0,
#     'right': 0,
#     'up': 0,
#     'down': 0,
#     'lTrigger': 0,
#     'rTrigger': 0,
#     'x': 0,
#     'y': 0,
#     'select': 0,
#     'start': 0,
#     'space': 0,
#     'q': 0
# }

STATES = {
    'main_menu' : 0,
    'driving_single' : 1,
    'driving_multi' : 2
}
ALL_STATE_EXCEPTIONS = {
    STATES['main_menu']: {},
    STATES['driving_single']: {},
    STATES['driving_multi']: {}
}
curState = STATES['main_menu']

'''
async
Runs a key sequence to start the game
'''
def setup_keyboard(startpath="bsnes-hd_beta9.exe"):
    emulator = Application().start(startpath)
    print('hello')
    keyboard.press_and_release('alt, enter, down, enter, enter')

'''
async
Sets a certain key to be pressed
'''
def press_key(key):
    global updateKeys, keys
    keys[key] = 2
    updateKeys = True

'''
async
indicates that a key is no longer being pressed
'''
def release_key(key):
    keys[key] = 3
    global updateKeys 
    updateKeys = True

def check_flag():
    global updateKeys 
    return updateKeys

def unset_flag():
    global updateKeys 
    updateKeys = False

'''
run as a thread, periodically checks if a key has been set/unset
'''
def keyboard_listener():
    # Set initial flag value to false
    # updateKeys = False
    global ALL_STATE_EXCEPTIONS
    global curState

    # Start listener
    while True:
        time.sleep(0.08)
        if (kill):
            # Exit condition for thread
            return

        # check flag. If set, run code
        if (not check_flag()):
            continue
        # Unset flag immediately
        unset_flag()

        # Make sure the correct state is set
        stateExceptions = ALL_STATE_EXCEPTIONS[curState]

        readItem()

        # # Iterate through keys
        # for key in keys.keys():
        #     if key == 'q' and keys[key] != 0:
        #         # Exit condition
        #         exit()

        #     if key == 'space' and keys[key] == 1:
        #         curState = STATES['driving_single']

        #     # Lets try this non-hardcoded thing first
        #     if keys[key] == 2:
        #         # Press requested
        #         # Check if exception
        #         if (key in stateExceptions):
        #             pass
        #         else:      
        #             # Send press key
        #             keyboard.send(key, do_release=False)
        #             keys[key] == 1

        #     elif keys[key] == 3:
        #         # Release requested
        #         # Check if exception
        #         if (key in stateExceptions):
        #             pass
        #         else:
        #             # Send release signal key
        #             keyboard.send(key, do_release=True)
        #             keys[key] == 0


if __name__ == '__main__':
    # Set up keyboard inputs
    setup_keyboard('bsnes-hd_beta9_windows\\bsnes-hd_beta9.exe')

    # Start thread for listening to other input
    task = keyboard_listener
    t = threading.Thread(target=task)
    t.start()

    while(True):
        key = input('=>')
        press_key(key)

        if (key == 'q'):
            t.join()
            exit()