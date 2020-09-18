#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()  #netstat -an  ===> TCP    127.0.0.1:65432        0.0.0.0:0              LISTENING
    print('listening on', (HOST, PORT))
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024) #The bufsize argument of 1024 used above is the maximum amount of data to be received at once
            print("Receive data:", data)  #Receive data: b'Hello, world'
            if not data: #if not b''
                break
            conn.sendall(data)

print("Server is closed")