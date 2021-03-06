#!/usr/bin/env python3
import time
import math
import board
import busio
import struct
import socket
import Adafruit_LSM303

class heading_py_3:
	def __init__(self):
		self.heading = 0 #compass heading in degrees
		self.s = socket.socket() # Create a socket object
		self.host = socket.gethostname() # Get local machine name
		self.port = 12345                # Reserve a port for your service.

		self.lsm303 = Adafruit_LSM303.LSM303() # Create a LSM303 instance
		print('Printing accelerometer & magnetometer X, Y, Z axis values, press Ctrl-C to quit...')
		
	def get_heading(self):
		accel, mag = self.lsm303.read()     # Read the X, Y, Z axis acceleration values and print them.
	
		# Grab the X, Y, Z components from the reading and print them out.
		accel_x, accel_y, accel_z = accel
		mag_x, mag_y, mag_z = mag
		print('Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5}'.format(accel_x, accel_y, accel_z, mag_x, mag_y, mag_z))
   
		self.heading = (math.atan2(mag_y, mag_x) * 180) / math.pi;
		if (self.heading < 0): #Normalize to 0-360
			self.heading = 360 + self.heading;

		print("Compass Heading: ", self.heading) 
			
		# Wait half a second and repeat.
		time.sleep(0.5)

	def socket(self):
		self.s.bind((self.host, self.port))        # Bind to the port

		self.s.listen(5)                 # Now wait for client connection.
		while True:
			self.get_heading()
			c, addr = self.s.accept()     # Establish connection with client.
			print ('Got connection from', addr)
			#c.send('Thank you for connecting'.encode())
			heading = struct.pack('f', self.heading)
			c.sendall(heading)
			c.close()                # Close the connection


if __name__ == '__main__':
	try:
		heading = heading_py_3()
		heading.socket()
	except KeyboardInterrupt:  
		pass

