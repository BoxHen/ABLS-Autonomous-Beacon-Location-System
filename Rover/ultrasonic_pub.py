#!/usr/bin/env python2

import rospy
import time
import ultrasonic_sensor

from std_msgs.msg import Bool 

def ultrasonic_sensor():
	pub = rospy.Publisher('isObstacle', Int16MultiArray, queue_size=10)
	rospy.init_node('ultrasonic_sensor', anonymous = True) # Initializing the node

	while not rospy.is_shutdown():# The function will return True if the node is ready to be shut down
		# This node publishes the input data on the topic "rotation"
		rate = rospy.Rate(1)
			
		reading_1 = ultrasonic_sensor.Distance(2, 3)
		reading_2 = ultrasonic_sensor.Distance(4, 17)
		reading_3 = ultrasonic_sensor.Distance(27, 22)
		reading_4 = ultrasonic_sensor.Distance(10, 9)
		
		sensor_reading_array = Int16MultiArray()
		sensor_reading_array.data = [reading_1, reading_2, reading_3, reading_4]
		pub.publish(sensor_reading_array)
		
	
	rate.sleep()

