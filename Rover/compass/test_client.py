#!/usr/bin/python2           # This is client.py file

import struct
import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
var = (struct.unpack('i', s.recv(1024)))
print(var[0])
if(var[0] < 91):
	print("YES!")
else:
	print(":(")
s.close()                     # Close the socket when done
