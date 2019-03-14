#!/usr/bin/env python2
import math
import rospy
import numpy as np
#import sensor_indexes
from sensor_indexes import create_sensor_indexes
from std_msgs.msg import Int16MultiArray
from std_msgs.msg import String
from std_msgs.msg import Int16

class Algorithm:
	def __init__(self):
		self.heading = 0
		self.rebound_angle_degrees = 0	
		self.threshold_flag = 0	
		
		pub = rospy.Publisher('setMotor', String, queue_size=2)

		rospy.Subscriber('isObstacle', Int16MultiArray, self.get_angle)
		rospy.Subscriber('isFlagSet', Int16, self.get_flag)
		#rospy.Subscriber("getHeading", Int16, self.get_Heading)

		while not rospy.is_shutdown():
			if self.threshold_flag == 2:
				pub.publish("BACKWARD")
			elif self.threshold_flag == 1:
				command = self.process_angle(self.rebound_angle_degrees)
				print(command)
				pub.publish(command)
			elif self.threshold_flag == 0:
				pub.publish("FORWARD")
			rate.sleep()

	#def find_beacon():
		

	def process_angle(self, angle_in_degrees):
		print("get_angle: ", angle_in_degrees)
		if angle_in_degrees > 0:
			return "RIGHT"
		elif angle_in_degrees < 0:
			return "LEFT"	
		else:#angle_in_degrees == 0
			return "FORWARD"

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

	#def get_Heading(self, data):
	#	rospy.loginfo(rospy.get_caller_id() + "I heard GPS: %s", data.data)
	#	self.heading = data.data


if __name__ == '__main__':
	rospy.init_node('algorithm', anonymous=True)
	rate = rospy.Rate(1)
 	try:
		algorithm = Algorithm()
	except rospy.ROSInterruptException:  
		pass
