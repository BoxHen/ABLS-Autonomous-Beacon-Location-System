#!/usr/bin/env python2
import time
import math
import rospy
import board
import busio
import Adafruit_LSM303

from std_msgs.msg import Int16MultiArray 
from std_msgs.msg import Int16

class heading:
	def __init__(self):
		self.heading = 0 #compass heading in degrees
		self.heading_pub = rospy.Publisher('compass_heading', Int16, queue_size=1)
		rospy.init_node('compass_heading', anonymous = True)

		self.lsm303 = Adafruit_LSM303.LSM303() # Create a LSM303 instance
		print('Printing accelerometer & magnetometer X, Y, Z axis values, press Ctrl-C to quit...')
		
	def get_heading(self):
		while True:
			accel, mag = self.lsm303.read()     # Read the X, Y, Z axis acceleration values and print them.
	
			# Grab the X, Y, Z components from the reading and print them out.
			accel_x, accel_y, accel_z = accel
			mag_x, mag_y, mag_z = mag
			print('Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5}'.format(accel_x, accel_y, accel_z, mag_x, mag_y, mag_z))
   
			self.heading = (math.atan2(mag_y, mag_x) * 180) / math.pi;
			if (self.heading < 0): #Normalize to 0-360
				self.heading = 360 + self.heading;

			print("Compass Heading: ", self.heading) 
			self.heading_pub.publish(heading)

			# Wait half a second and repeat.
			time.sleep(0.5)

if __name__ == '__main__':
 	try:
		heading = heading()
		heading.get_heading()
	except rospy.ROSInterruptException:  
		pass
