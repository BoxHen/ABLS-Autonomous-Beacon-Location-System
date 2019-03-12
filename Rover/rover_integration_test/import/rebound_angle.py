#!usr/bin/env python2

import math
import numpy as np
import sensor_indexes
#from sensor_indexes import create_sensor_indexes
 
def get_angle(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
	number_of_sensors = 4
	sensor_indexes = sensor_indexes.create_sensor_indexes(number_of_sensors)
	sensor_interval = math.pi/number_of_sensors
	sensor_weight = sensor_interval*sensor_indexes

	rebound_angle = (np.dot(sensor_weight, data.data))/(np.sum(data.data))
	return rebound_angle
