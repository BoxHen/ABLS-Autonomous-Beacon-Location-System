#!/usr/bin/python2           

import rospy
import time
import struct
import socket       
from std_msgs.msg import Float64

class heading_py_2():
	def __init__(self):
		self.heading_pub = rospy.Publisher('rover_heading', Float64, queue_size=1)
		rospy.init_node('ultrasonic_sensor', anonymous = True)

	def send_heading(self):
		s = socket.socket()       			  # Create a socket object
		host = socket.gethostname()	  # Get local machine name
		port = 12345                				  # Reserve a port for your service.
		s.connect((host, port))
		recieved_from_socket = (struct.unpack('f', s.recv(1024)))
		heading = recieved_from_socket[0]
		self.heading_pub.publish(heading)
		s.close()                     # Close the socket when done

if __name__ == '__main__':
	try:
		heading = heading_py_2()
		while True:
			heading.send_heading()
	except KeyboardInterrupt:  
		pass