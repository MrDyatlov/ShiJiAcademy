#!/usr/bin/python3
# Server
import socket

ip = "192.168.25.205"
port = 8080

safety_connection = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
safety_connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
safety_connection.bind(("10.0.2.5", 8080))
print("binding to" + ip)
safety_connection.listen(1)
print("bind listening...")

safechild_connection, adress = safety_connection.accept()
print("connection succesfully to" + str(adress))

