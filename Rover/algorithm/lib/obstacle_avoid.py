#!/usr/bin/python2 

import math
import time
import rospy
import numpy as np
from sensor_indexes import create_sensor_indexes
from std_msgs.msg import Int16MultiArray
from std_msgs.msg import String
from std_msgs.msg import Int16

class obstacle_avoid:
	def __init__(self):
		self.rebound_angle_degrees = 0	
		self.threshold_flag = 0	
		#self.pub = rospy.Publisher('setMotor', String, queue_size=2)
	
		rospy.Subscriber('isObstacle', Int16MultiArray, self.get_rebound_angle, queue_size=1)
		rospy.Subscriber('isFlagSet', Int16, self.get_flag, queue_size=1)

	def get_rebound_angle(self, data):
		rospy.loginfo(rospy.get_caller_id() + "I heard ANGLE: %s", data.data)
		number_of_sensors = 4
		sensor_indexes = create_sensor_indexes(number_of_sensors)
		sensor_interval = math.pi/number_of_sensors

		sensor_weight = np.dot(sensor_interval, sensor_indexes)

		rebound_angle_radians = (np.dot(sensor_weight, data.data))/(np.sum(data.data))
		self.rebound_angle_degrees = np.rad2deg(rebound_angle_radians)
		print("rebound angle is: ", self.rebound_angle_degrees)
		
	def get_flag(self, data):
		rospy.loginfo(rospy.get_caller_id() + "I heard FLAG: %s", data.data)
		self.threshold_flag = data.data

	def process_angle(self):	
		print("rebound angle in degrees: ", self.rebound_angle_degrees)
		if self.rebound_angle_degrees > 0:
			command = "RIGHT"
		elif self.rebound_angle_degrees < 0:
			command = "LEFT"	
		else:#self.rebound_angle_degrees == 0
			command = "FORWARD"
		return command
		
