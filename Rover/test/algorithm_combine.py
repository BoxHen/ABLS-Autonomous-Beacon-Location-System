#!/usr/bin/env python2
import math
import time
import rospy
import numpy as np
from sensor_indexes import create_sensor_indexes
from std_msgs.msg import Int8MultiArray
from std_msgs.msg import Int16MultiArray
from std_msgs.msg import Int32MultiArray
from std_msgs.msg import String
from std_msgs.msg import Int16
from std_msgs.msg import Bool

class Algorithm:
	def __init__(self):
		self.startup_time = time.time()
		self.heading = 0
		self.rebound_angle_degrees = 0	
		self.threshold_flag = 0	

		self.Rover_longitude = 0
		self.Rover_latitude = 0
		self.Rover_heading = 0
		self.Beacon_longitude = -759688110
		self.Beacon_latitude = 420885400
		self.arming_flag = False
		self.manual_command = "FORWARD"
		#self.vehicle_status_array = Int16MultiArray()
		
		self.pub = rospy.Publisher('setMotor', String, queue_size=2)
		self.confirm_flag_pub = rospy.Publisher('vehicle_status', Int8MultiArray, queue_size=1)
	
		rospy.Subscriber('rover_gps', Int32MultiArray, self.get_rover_GPS, queue_size=1)
		#rospy.Subscriber('beacon_gps', Int32MultiArray, self.get_beacon_GPS, queue_size=1)
		rospy.Subscriber('isObstacle', Int16MultiArray, self.get_angle, queue_size=1)
		rospy.Subscriber('isFlagSet', Int16, self.get_flag, queue_size=1)
		rospy.Subscriber('armingMessage', Bool, self.get_armingMessage, queue_size=1)
		rospy.Subscriber('manualCtrl', String, self.get_manualCtrl, queue_size=1)

		rate = rospy.Rate(10)
		while not rospy.is_shutdown():
			if (self.arming_flag == True):
				command = self.process_manual_ctrl()
				self.pub.publish(command)
			else:
				if (self.check_beacon_location()): #breaks from loop if we are at the beacon
					break
				if self.threshold_flag == 2:
					self.pub.publish("BACKWARD")
				elif self.threshold_flag == 1:
					command = self.process_angle(self.rebound_angle_degrees)
					print(command)
					self.pub.publish(command)
				elif self.threshold_flag == 0:
					if (self.calibrate_heading()): #maybe find a better way to implement this
						continue
					beacon_direction = self.find_beacon_direction()
					self.pub.publish(beacon_direction)
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
		self.Rover_longitude = RoverGPSArray.data[0]
		self.Rover_latitude = RoverGPSArray.data[1]
		self.Rover_heading = RoverGPSArray.data[2]

	def get_armingMessage(self, arming_flag):
		rospy.loginfo(rospy.get_caller_id() + "I heard FLAG: %s", arming_flag.data)
		self.arming_flag = arming_flag.data
		
		vehicle_status_array = Int16MultiArray()
		vehicle_status_array.data = [0]
		self.confirm_flag_pub.publish(vehicle_status_array.data)

	def get_manualCtrl(self, data):
		rospy.loginfo(rospy.get_caller_id() + "I heard FLAG: %s", data.data)
		self.manual_command = data.data

	#def get_beacon_GPS(self, BeaconGPSArray):
		#self.Beacon_longitude = BeaconGPSArray.data[0]
		#self.Beacon_latitude = BeaconGPSArray.data[1]
		#self.Beacon_altitude = BeaconGPSArray.data[2]

	def calibrate_heading(self): #move forward for ~15 seccs to calibrate gps to find heading
		current_time = time.time()
		is_calibrated = False
		if (current_time - self.startup_time < 15):
			self.pub.publish("FORWARD")
			is_calibrated = True
		return is_calibrated

	def process_angle(self, angle_in_degrees):
		print("get_angle: ", angle_in_degrees)
		if angle_in_degrees > 0:
			return "RIGHT"
		elif angle_in_degrees < 0:
			return "LEFT"	
		else:#angle_in_degrees == 0
			return "FORWARD"

	def process_manual_ctrl(self):
		command = "FORWARD"
		if (self.manual_command == "LEFT"):
			command = "LEFT"
		elif (self.manual_command ==  "RIGHT"):
			command = "RIGHT"
		elif (self.manual_command == "FORWARD"):
			command = "FORWARD"
		elif (self.manual_command == "BACKWARD"):
			command = "BACKWARD"
		else: #STOP
			command = "STOP"
		return command

	def find_bearing(self):
		latRover = math.radians(self.Rover_latitude/10000000)
		latBeacon = math.radians(self.Beacon_latitude/10000000)
		longRover = math.radians(self.Rover_longitude/10000000)
		longBeacon = math.radians(self.Beacon_longitude/10000000)

		X = (math.cos(latBeacon)) * (math.sin(longBeacon-longRover))
		print(X)
		Y = ( (math.cos(latRover)*math.sin(latBeacon))-(math.sin(latRover)*math.cos(latBeacon)*math.cos(longBeacon-longRover)) )
		print(Y)
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
		lat_check = self.Rover_latitude + tolerance < self.Beacon_latitude < self.Rover_latitude + tolerance
		long_check = self.Rover_longitude + tolerance < self.Beacon_longitude < self.Rover_longitude + tolerance
		if (lat_check and long_check): #if we are at the beacon location and within tolerance stop the rover
			self.pub.publish("STOP")
			has_arrived = True
		return has_arrived
		
if __name__ == '__main__':
	rospy.init_node('algorithm', anonymous=True)
 	try:
		algorithm = Algorithm()
	except rospy.ROSInterruptException:  
		pass
		
