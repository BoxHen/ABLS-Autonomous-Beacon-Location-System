#!usr/bin/env python2

import math
import numpy as np
import sensor_indexes

class obstacle_avoidance:
    def __init__():
        rospy.Subscriber("isObstacle", Int16MultiArray, callback)
        pub = rospy.Publisher('rebound_angle', float32, queue_size=10)
        while not rospy.is_shutdown():
             rebound_angle = get_rebound_angle()
             pub.publish(rebound_angle)
        
    def get_rebound_angle(data):
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
        number_of_sensors = 4
            sensor_indexes = sensor_indexes.create_sensor_indexes(number_of_sensors)
            sensor_interval = math.pi/number_of_sensors
            sensor_weight = sensor_interval*sensor_indexes
            
            rebound_angle = (np.dot(sensor_weight, data.data))/(np.sum(data.data))
            return rebound_angle
