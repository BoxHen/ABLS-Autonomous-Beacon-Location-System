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
	
heading = 0
rebound_angle_degrees = 0	
threshold_flag = 0	
count = 0

def callback():	
	global heading 
	global rebound_angle_degrees 
	global threshold_flag 
	global count 

	rospy.init_node('algorithm', anonymous=True)
	pub = rospy.Publisher('setMotor', String, queue_size=1)

	rospy.Subscriber('isObstacle', Int16MultiArray, get_angle, queue_size=1)
	rospy.Subscriber('isFlagSet', Int16, get_flag, queue_size=1)
	#rospy.Subscriber("getHeading", Int16, get_Heading)

	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		if threshold_flag == 2:
			pub.publish("BACKWARD")
		elif threshold_flag == 1:
			command = process_angle(rebound_angle_degrees)
			print(command)
			pub.publish(command)
			count = count + 1
			print(count)
			#pub.publish(command + str(count))
		else: #self.threshold_flag == 0:
			pub.publish("FORWARD")
			count = count + 1
			print(count)
			#pub.publish("FORWARD" + str(count))
		rate.sleep()

#def find_beacon():
		

def process_angle(angle_in_degrees):
	#print("get_angle: ", angle_in_degrees)
	if angle_in_degrees > 0:
		return "RIGHT"
	elif angle_in_degrees < 0:
		return "LEFT"	
	else:#angle_in_degrees == 0
		return "FORWARD"

def get_angle(data):
	global rebound_angle_degrees 

	rospy.loginfo(rospy.get_caller_id() + "I heard ANGLE: %s", data.data)
	number_of_sensors = 4
	sensor_indexes = create_sensor_indexes(number_of_sensors)
	sensor_interval = math.pi/number_of_sensors
	
	sensor_weight = np.dot(sensor_interval, sensor_indexes)

	rebound_angle_radians = (np.dot(sensor_weight, data.data))/(np.sum(data.data))
	rebound_angle_degrees = np.rad2deg(rebound_angle_radians)
	#print(rebound_angle_degrees)
		
def get_flag(data):
	global threshold_flag	

	rospy.loginfo(rospy.get_caller_id() + "I heard FLAG: %s", data.data)
	threshold_flag = data.data

#def get_Heading(data):
#	rospy.loginfo(rospy.get_caller_id() + "I heard GPS: %s", data.data)
#	heading = data.data


if __name__ == '__main__':

	#rospy.init_node('algorithm', anonymous=True)
 	try:
		callback()
	except rospy.ROSInterruptException:  
		pass
