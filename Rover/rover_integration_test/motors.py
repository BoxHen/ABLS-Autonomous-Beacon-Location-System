#!/usr/bin/env python2

import time
import serial
import rospy
import motor_move
from std_msgs.msg import String

def move_rover(data):
	speed = 40
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
	rover_action = data.data

	if rover_action == "RIGHT":    
		print("in right")
		motor_move.right(speed)
		time.sleep(2)
	elif rover_action == "LEFT":  
		print("in left")
		motor_move.left(speed)
		time.sleep(2)
	elif rover_action == "FORWARD": 	
		print("in forward")
		motor_move.forward(speed)
		time.sleep(2)
	else:#rover_action == "BACKWARD"   	
		print("in back")
		motor_move.backward(speed)
		time.sleep(2)

def listener():
	rospy.init_node('motor', anonymous=True)
	rate = rospy.Rate(2)
	
	#while not rospy.is_shutdown():
	rospy.Subscriber("setMotor", String, move_rover)
	rate.sleep()
	rospy.spin()

if __name__ == '__main__':
	listener()
