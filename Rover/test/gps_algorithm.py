#!/usr/bin/env python2

import math
import rospy
import time
import numpy as np
#import sensor_indexes
from sensor_indexes import create_sensor_indexes
from std_msgs.msg import Int16MultiArray
from std_msgs.msg import String
from std_msgs.msg import Int16

class GPS_Algorithm:
	def __init__(self):
		self.Rover_longitude = 0
		self.Rover_latitude = 0
		self.Rover_altitude = 0
		self.Rover_heading = 0
		self.Beacon_longitude = 0
		self.Beacon_latitude = 0
		self.Beacon_altitude = 0	
		
		#pub = rospy.Publisher('setMotor', String, queue_size=1)

		rospy.Subscriber('RoverGPS', Int16MultiArray, get_rover_GPS, queue_size=1)
		rospy.Subscriber('BeaconGPS', Int16MultiArray, get_beacon_GPS, queue_size=1)

		rate = rospy.Rate(1)
		while not rospy.is_shutdown():
			direction = find_Beacon()
			pub.publish(direction)
			rate.sleep()
	_
	def get_rover_GPS(self, RoverGPSArray):
		# unpack data from array
		#-----------------------
		self.Rover_longitude = RoverGPSArray.data[0]
		self.Rover_latitude = RoverGPSArray.data[1]
		self.Rover_altitude = RoverGPSArray.data[2]
		self.Rover_heading = RoverGPSArray.data[3]
		#...

	def get_beacon_GPS(self, BeaconGPSArray):
		
		self.Beacon_longitude = BeaconGPSArray.data[0]
		self.Beacon_latitude = BeaconGPSArray.data[1]
		self.Beacon_altitude = BeaconGPSArray.data[2]
		#...

	def find_bearing(self):
		latRover = math.radians(self.Rover_latitude)
		latBeacon = math.radians(self.Rover_latitude)
		longRover = math.radians(self.Beacon_longitude)
		longBeacon = math.radians(self.Beacon_longitude)

		X = (math.cos(latBeacon)) * (math.sin(longBeacon-longRover))
		print(X)
		Y = ( (math.cos(latRover)*math.sin(latBeacon))-(math.sin(latRover)*math.cos(latBeacon)*math.cos(longBeacon-longRover)) )
		print(Y)
		Bearing = math.degrees(math.atan2(X, Y))
		print(Bearing)
		return Bearing

	def find_beacon(self):
		beacon_direction = find_bearing()
		if ((self.Rover_heading-beacon_direction)>21):
			return "LEFT" #forwardSteerLeft
		if ((self.Rover_heading-beacon_direction)<-21):
			return "RIGHT" #forwardSteerRight
		else: #between -21 and 21
			return "FORWARD"

if __name__ == '__main__':

	rospy.init_node('gps_algorithm', anonymous=True)
 	try:
		find_beacon = GPS_Algorithm()
	except rospy.ROSInterruptException:  
		pass
