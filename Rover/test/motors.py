#!/usr/bin/env python2

import time
import serial
import rospy
import motor_move
from std_msgs.msg import String

def move_rover(data):
	stop = 0
	speed = 45
	faster_speed = 55
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
	rover_action = data.data

	if rover_action == "RIGHT":    
		print("in right")
		motor_move.right(faster_speed)

	elif rover_action == "LEFT":  
		print("in left")
		motor_move.left(faster_speed)

	elif rover_action == "FORWARD": 	
		print("in forward")
		motor_move.forward(speed)

	elif rover_action == "BACKWARD":   	
		print("in back")
		motor_move.backward(speed)

	elif rover_action == "forwardSteerLeft":
		print("in forwardSteerLeft")
		motor_move.forwardSteerLeft(faster_speed, speed)

	elif rover_action == "forwardSteerRight":
		print("in forwardSteerRight")
		motor_move.forwardSteerRight(faster_speed, speed)

	else: # rover_action == "STOP"
		print("in STOP")
		motor_move.stop()

def listener():
	rospy.init_node('motor', anonymous=True)
	rospy.Subscriber('setMotor', String, move_rover, queue_size=1)
	rospy.spin()

def stop():
	print("motors stopped")
	motor_move.stop()

if __name__ == '__main__':
 	try:
		listener()
		rospy.on_shutdown(stop)
	except KeyboardInterrupt:  
		pass
