#!/usr/bin/env python2

import rospy
import motor_move
from std_msgs.msg import String

def move_rover(data):
	speed = 30
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
	rover_action = data.data
	if rover_action == "RIGHT":    
		motor_move.right(speed)
	elif rover_action == "LEFT":  
		motor_move.left(speed)
	elif rover_action == "FORWARD": 	
		motor_move.forward(speed)
	else:#rover_action == "BACKWARD"   	
		motor_move.backward(speed)

def listener():
	rospy.init_node('motor', anonymous=True)
	rospy.Subscriber("setMotor", String, move_rover)
	rospy.spin()

if __name__ == '__main__':
	listener()
