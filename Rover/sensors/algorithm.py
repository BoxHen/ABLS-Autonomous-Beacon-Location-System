#!/usr/bin/env python2

import math
import rospy
import numpy as np
import sensor_indexes
#from sensor_indexes import create_sensor_indexes
from rebound_angle import get_angle
from std_msgs.msg import Int16MultiArray

class Algorithm:
	go_forward = 0
	rebound_angle = 0	
	threshold_flag = false	

	def __init__(self):
		rospy.Subscriber("isObstacle", Int16MultiArray, self.get_angle)
		rospy.Subscriber("isFlagSet", Bool, self.get_flag)
		pub = rospy.Publisher('setMotor', Int16MultiArray, queue_size=10)

		while not rospy.is_shutdown():
			if threshold_flag == True:
				pub.publish(rebound_angle)
			elif threshold_flag == False:
				pub.publish(go_forward)

	def get_angle(data):
		rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
		number_of_sensors = 4
		sensor_indexes = sensor_indexes.create_sensor_indexes(number_of_sensors)
		sensor_interval = math.pi/number_of_sensors
		sensor_weight = sensor_interval*sensor_indexes

		rebound_angle = (np.dot(sensor_weight, data.data))/(np.sum(data.data))
		
	def get_flag(data):
		rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
		threshold_flag = data.data


if __name__ == '__main__':
    rospy.init_node('algorithm', anonymous=True)
    try:
        algorithm = Algorithm()
    except rospy.ROSInterruptException:  
	pass
