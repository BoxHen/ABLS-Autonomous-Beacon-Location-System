#!/usr/bin/env python2
import math
import time
import rospy
import numpy as np
#import sensor_indexes
from sensor_indexes import create_sensor_indexes
from std_msgs.msg import Int16MultiArray
from std_msgs.msg import String
from std_msgs.msg import Int16

class Algorithm:
	def __init__(self):
		self.startup_time = time.time()
		self.heading = 0
		self.rebound_angle_degrees = 0	
		self.threshold_flag = 0	

		self.Rover_longitude = 0
		self.Rover_latitude = 0
		self.Rover_altitude = 0
		self.Rover_heading = 0
		self.Beacon_longitude = 0
		self.Beacon_latitude = 0
		self.Beacon_altitude = 0
		
		self.pub = rospy.Publisher('setMotor', String, queue_size=2)
	
		rospy.Subscriber('RoverGPS', Int16MultiArray, get_rover_GPS, queue_size=1)
		rospy.Subscriber('BeaconGPS', Int16MultiArray, get_beacon_GPS, queue_size=1)
		rospy.Subscriber('isObstacle', Int16MultiArray, self.get_angle, queue_size=1)
		rospy.Subscriber('isFlagSet', Int16, self.get_flag, queue_size=1)

		rate = rospy.Rate(1)
		while not rospy.is_shutdown():
			if self.threshold_flag == 2:
				pub.publish("BACKWARD")
			elif self.threshold_flag == 1:
				command = self.process_angle(self.rebound_angle_degrees)
				print(command)
				pub.publish(command)
			elif self.threshold_flag == 0:
				calibrate_heading() #maybe find a better way to implement this
				beacon_direction = find_beacon()
				pub.publish(beacon_direction)
			rate.sleep()

	def get_angle(self, data):
		rospy.loginfo(rospy.get_caller_id() + "I heard ANGLE: %s", data.data)
		number_of_sensors = 4
		sensor_indexes = create_sensor_indexes(number_of_sensors)
		sensor_interval = math.pi/number_of_sensors

		sensor_weight = np.dot(sensor_interval, sensor_indexes)

		rebound_angle_radians = (np.dot(sensor_weight, data.data))/(np.sum(data.data))
		self.rebound_angle_degrees = np.rad2deg(rebound_angle_radians)
		print(self.rebound_angle_degrees)
		
	def get_flag(self, data):
		rospy.loginfo(rospy.get_caller_id() + "I heard FLAG: %s", data.data)
		self.threshold_flag = data.data

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

	def calibrate_heading(): #move forward for ~15 seccs to calibrate gps to find heading
		current_time = time.time()
		if (current_time - startup_time < 15)
			self.pub.publish("FORWARD")
			continue
		

	def process_angle(self, angle_in_degrees):
		print("get_angle: ", angle_in_degrees)
		if angle_in_degrees > 0:
			return "RIGHT"
		elif angle_in_degrees < 0:
			return "LEFT"	
		else:#angle_in_degrees == 0
			return "FORWARD"

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
		bearing = find_bearing()
		if ((self.Rover_heading-bearing)>21):
			return "LEFT" #forwardSteerLeft
		if ((self.Rover_heading-bearing)<-21):
			return "RIGHT" #forwardSteerRight
		else: #between -21 and 21
			return "FORWARD"


if __name__ == '__main__':
	rospy.init_node('algorithm', anonymous=True)
 	try:
		algorithm = Algorithm()
	except rospy.ROSInterruptException:  
		pass
