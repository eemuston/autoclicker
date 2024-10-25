import keyboard
from pynput.mouse import Button, Controller as MouseController
from pynput.mouse import Listener as MouseListener
import time

mouse = MouseController()

spam_active = False
stop_spam = False

def on_click(x, y, button, pressed):
    global spam_active
    if button.name == 'left' and pressed:
        spam_active = True  

def start_spamming():
    global spam_active, stop_spam
    while not stop_spam:
        if spam_active: 
            mouse.click(Button.left, 1) 
            time.sleep(0.000000000000000000000000000000000000000000000000000000000000000000000000000000001)
            
        if keyboard.is_pressed('q'):
            stop_spam = True
            break

def check_for_stop():
    global stop_spam
    while not stop_spam:
        if keyboard.is_pressed('q'):
            stop_spam = True
            break

mouse_listener = MouseListener(on_click=on_click)
mouse_listener.start()

start_spamming()

mouse_listener.stop()
