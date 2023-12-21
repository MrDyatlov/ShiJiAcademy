#!/usr/bin/python3
# Client
import socket

ip = "192.168.25.242"
port = 8080

safechild_connection = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
safechild_connection.connect(("10.0.2.15", 8080))
