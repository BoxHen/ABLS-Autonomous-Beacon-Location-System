#!/usr/bin/env python2
import math
import time
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Int32MultiArray

class beacon_finder:
	def __init__(self):
		self.Rover_heading = 0
		self.Rover_latitude = 420880397
		self.Rover_longitude = -759694612
		#self.startup_time = time.time()
		self.Beacon_latitude = 420889180
		self.Beacon_longitude = -759697600

		rospy.Subscriber('rover_gps', Int32MultiArray, self.get_rover_GPS, queue_size=1)
		rospy.Subscriber('rover_heading', Float64, self.get_rover_heading, queue_size=1)
		rospy.Subscriber('beacon_gps', Int32MultiArray, self.get_beacon_GPS, queue_size=1)

	def get_rover_GPS(self, RoverGPSArray):
		self.Rover_longitude = RoverGPSArray.data[1]
		self.Rover_latitude = RoverGPSArray.data[0]

	def get_beacon_GPS(self, BeaconGPSArray):
		self.Beacon_longitude = BeaconGPSArray.data[1]
		self.Beacon_latitude = BeaconGPSArray.data[0]
		print("lat: ", self.Beacon_latitude)
		print("long: ", self.Beacon_longitude)

	def get_rover_heading(self, roverHeading):
		self.Rover_heading = float(roverHeading.data)	

	#def calibrate_heading(self): #move forward for ~15 seccs to calibrate gps to find heading
	#	current_time = time.time()
	#	is_calibrated = False
	#	if (current_time - self.startup_time < 1):
	#		is_calibrated = True
	#	return is_calibrated	

	def find_bearing(self):
		latRover = math.radians(self.Rover_latitude/10000000.0)
		latBeacon = math.radians(self.Beacon_latitude/10000000.0)
		longRover = math.radians(self.Rover_longitude/10000000.0)
		longBeacon = math.radians(self.Beacon_longitude/10000000.0)
		print("lat rover is: ", self.Rover_latitude/10000000.0)
		print("long rover is: ", self.Rover_longitude/10000000.0)		
		print("lat beacon is: ", self.Beacon_latitude/10000000.0)		
		print("long beacon is: ", self.Beacon_longitude/10000000.0)

		X = (math.cos(latBeacon)) * (math.sin(longBeacon-longRover))
		Y = ( (math.cos(latRover)*math.sin(latBeacon))-(math.sin(latRover)*math.cos(latBeacon)*math.cos(longBeacon-longRover)) )
		Bearing = math.degrees(math.atan2(X, Y))
		print("X is: ", X)
		print("Y is: ", Y)

		print("Bearing is: ", Bearing)
		return Bearing

	def find_beacon_direction(self):
		bearing = self.find_bearing()
		print("Bearing is: ", bearing)
		print("Rover Heading is: ", self.Rover_heading)
		print("Rover_heading-bearing is: ", self.Rover_heading-bearing)
		#if ((self.Rover_heading-bearing)>21):
		#	return "LEFT"
		#if ((self.Rover_heading-bearing)<-21):
		#	return "RIGHT" 
		#else: #between -21 and 21
		#	return "FORWARD"
	
		if(bearing<0):
			bearing = bearing+360.0
		if( (bearing-15) <self.Rover_heading< (bearing+15) ):
			return "FORWARD"
		else:
			return "LEFT"

	def check_beacon_location(self):
		has_arrived = False
		tolerance = 500
		lat_check = self.Rover_latitude - tolerance < self.Beacon_latitude < self.Rover_latitude + tolerance
		long_check = self.Rover_longitude - tolerance < self.Beacon_longitude < self.Rover_longitude + tolerance
		if (lat_check and long_check): #if we are at the beacon location and within tolerance stop the rover
			has_arrived = True
		return has_arrived
