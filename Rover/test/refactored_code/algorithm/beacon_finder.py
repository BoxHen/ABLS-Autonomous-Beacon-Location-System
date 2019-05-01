#!/usr/bin/env python2
import math
import time
import rospy
from std_msgs.msg import Int32MultiArray

class beacon_finder:
	def __init__(self):
		self.heading = 0
		self.Rover_heading = 0
		self.Rover_latitude = 0
		self.Rover_longitude = 0
		self.startup_time = time.time()
		self.Beacon_latitude = 420885400
		self.Beacon_longitude = -759688110

		rospy.Subscriber('rover_gps', Int32MultiArray, self.get_rover_GPS, queue_size=1)
		rospy.Subscriber('beacon_gps', Int32MultiArray, self.get_beacon_GPS, queue_size=1)

	def get_rover_GPS(self, RoverGPSArray):
		self.Rover_longitude = RoverGPSArray.data[0]
		self.Rover_latitude = RoverGPSArray.data[1]
		self.Rover_heading = RoverGPSArray.data[2]

	def get_beacon_GPS(self, BeaconGPSArray):
		self.Beacon_longitude = BeaconGPSArray.data[0]
		self.Beacon_latitude = BeaconGPSArray.data[1]

	def calibrate_heading(self): #move forward for ~15 seccs to calibrate gps to find heading
		current_time = time.time()
		is_calibrated = False
		if (current_time - self.startup_time > 15):
			self.pub.publish("FORWARD")
			is_calibrated = True
		return is_calibrated	

	def find_bearing(self):
		latRover = math.radians(self.Rover_latitude/10000000)
		latBeacon = math.radians(self.Beacon_latitude/10000000)
		longRover = math.radians(self.Rover_longitude/10000000)
		longBeacon = math.radians(self.Beacon_longitude/10000000)

		X = (math.cos(latBeacon)) * (math.sin(longBeacon-longRover))
		Y = ( (math.cos(latRover)*math.sin(latBeacon))-(math.sin(latRover)*math.cos(latBeacon)*math.cos(longBeacon-longRover)) )
		print("X: ", X) 
		print("Y: ", Y)
		Bearing = math.degrees(math.atan2(X, Y))
		print(Bearing)
		return Bearing

	def find_beacon_direction(self):
		bearing = self.find_bearing()
		if ((self.Rover_heading-bearing)>21):
			return "LEFT" #forwardSteerLeft
		if ((self.Rover_heading-bearing)<-21):
			return "RIGHT" #forwardSteerRight
		else: #between -21 and 21
			return "FORWARD"

	def check_beacon_location(self):
		has_arrived = False
		tolerance = 20
		lat_check = self.Rover_latitude - tolerance < self.Beacon_latitude < self.Rover_latitude + tolerance
		long_check = self.Rover_longitude - tolerance < self.Beacon_longitude < self.Rover_longitude + tolerance
		if (lat_check and long_check): #if we are at the beacon location and within tolerance stop the rover
			self.pub.publish("STOP")
			has_arrived = True
		return has_arrived
