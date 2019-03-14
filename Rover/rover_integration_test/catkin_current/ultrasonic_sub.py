#!/usr/bin/env python2

import rospy
import math
import numpy as np
import sensor_indexes
from rebound_angle import angle
from std_msgs.msg import Int16MultiArray

def get_rebound_angle(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data) 
    number_of_sensors = 4
    sensor_indexes = sensor_indexes.create_sensor_indexes(number_of_sensors)
     sensor_interval = math.pi/number_of_sensors
    sensor_weight = sensor_interval*sensor_indexes
            
    rebound_angle = (np.dot(sensor_weight, data.data))/(np.sum(data.data))
    if rebound_angle >
    
def listener():
    rospy.init_node('ultrasonic_sensor_listener', anonymous=True)

    rospy.Subscriber("isObstacle", Int16MultiArray, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()


