#!/usr/bin/env python2

import rospy
#import motor_move
import RPi.GPIO as IO

from std_msgs.msg import Bool 

IO.setwarnings(False)
IO.setmode (IO.BCM)

IO.setup(18,IO.IN) #GPIO 18 - IR sensor input

def infrared_sensor():
	pub = rospy.Publisher('isObstacle', Bool, queue_size=10)
	rospy.init_node('infrared_sensor', anonymous = True) # Initializing the node

while not rospy.is_shutdown():# The function will return True if the node is ready to be shut down
	# This node publishes the input data on the topic "rotation"
	rate = rospy.Rate(1)
	if(IO.input(18)==True): #No object detected 
		pub.publish(True)
	if(IO.input(18)==False): #object detected
		pub.publish(False)
	
	rate.sleep()



