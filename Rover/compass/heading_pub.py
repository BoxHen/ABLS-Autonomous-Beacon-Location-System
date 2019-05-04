#!/usr/bin/env python2
import time
import math
import rospy
import board
import busio
import adafruit_lsm303

from std_msgs.msg import Int16MultiArray 
from std_msgs.msg import Int16

class heading:
	def __init__(self):
		self.i2c = busio.I2C(board.SCL, board.SDA)
		self.sensor = adafruit_lsm303.LSM303(self.i2c)
		self.heading = 0 #compass heading in degrees
		self.heading_pub = rospy.Publisher('compass_heading', Int16, queue_size=1)
		rospy.init_node('compass_heading', anonymous = True)
		
	def get_heading(self):
		while True:
			acc_x, acc_y, acc_z = self.sensor.acceleration
			mag_x, mag_y, mag_z = self.sensor.magnetic
			print('Acceleration (m/s^2): ({0:10.3f}, {1:10.3f}, {2:10.3f})'.format(acc_x, acc_y, acc_z))
			print('Magnetometer (gauss): ({0:10.3f}, {1:10.3f}, {2:10.3f})'.format(mag_x, mag_y, mag_z))
			
			self.heading = (math.atan2(mag_y, mag_x) * 180) / Pi;
			if (self.heading < 0): #Normalize to 0-360
				self.heading = 360 + self.heading;

			print("Compass Heading: ", self.heading) 
			self.heading_pub.publish(heading)
			time.sleep(1.0)
