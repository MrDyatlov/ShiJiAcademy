#!/usr/bin/python3
# Server
import socket

class SafeYourChild:

    def __init__(self, ip, port):
        self.safety_connection = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.safety_connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.safety_connection.bind((ip, port))
        print("binding to" + ip)
        self.safety_connection.listen(0)
        print("bind listening...")
        (self.safechild_connection, adress) = self.safety_connection.accept()
        print("connection succesfully to" + str(adress))

save_your_child = SafeYourChild("10.0.2.5", 1234)