from pynput.keyboard import Controller,Key
import keyboard
import time

# AUTO_KEYBOARD TYPING MAX --> 856 WPM
keyC = Controller()
time.sleep(4)
message = ''''''
for i in message:
    keyC.type(i)
    time.sleep(0.0000001)
print("Work done")

# SPRINTER GAME IS FROM HERE game -->https://www.numuki.com/game/sprinter/
while not keyboard.is_pressed("q"):
    keyC.press(Key.left)
    keyC.release(Key.left)
    time.sleep(0.000000001)

    keyC.press(Key.right)
    keyC.release(Key.right)
    time.sleep(0.000000001)
