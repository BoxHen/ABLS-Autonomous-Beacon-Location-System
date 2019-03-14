#!/usr/bin/env python2

import rospy
import time
import RPi.GPIO as GPIO
GPIO.setmode (GPIO.BCM)
from ultrasonic_sensor import Distance
from ultrasonic_threshold import get_threshold_flag
from std_msgs.msg import Int16MultiArray 
from std_msgs.msg import Int16

def ultrasonic_sensor():
	distance_pub = rospy.Publisher('isObstacle', Int16MultiArray, queue_size=2)
	flag_pub = rospy.Publisher('isFlagSet', Int16, queue_size=2)
	rospy.init_node('ultrasonic_sensor', anonymous = True) # Initializing the node

	sensor_1 = Distance(2, 3)
	sensor_2 = Distance(4, 17)
	sensor_3 = Distance(27, 22)
	sensor_4 = Distance(10, 9)

	while not rospy.is_shutdown():
		# This node publishes the input data on the topic "rotation"
		rate = rospy.Rate(1)

		reading_1 = sensor_1.distance_from_obj()
		reading_2 = sensor_1.distance_from_obj()
		reading_3 = sensor_1.distance_from_obj()
		reading_4 = sensor_1.distance_from_obj()
		
		threshold_flag = get_threshold_flag(reading_1, reading_2, reading_3, reading_4)

		sensor_reading_array = Int16MultiArray()
		sensor_reading_array.data = [reading_1, reading_2, reading_3, reading_4]

		distance_pub.publish(sensor_reading_array)
		flag_pub.publish(threshold_flag)
		print("sensor:", sensor_reading_array)
		print("flags:", threshold_flag)
		rate.sleep()

if __name__ == '__main__':
    try:
	ultrasonic_sensor()
    except rospy.ROSInterruptException:
        pass
