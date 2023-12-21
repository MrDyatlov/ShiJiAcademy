#!/usr/bin/python3
# Client
import socket

class SafeChild:


    def __init__(self, ip, port):
        self.safechild_connection = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.safechild_connection.connect((ip, port))

save_your_child = SafeChild("10.0.2.5", 1234)