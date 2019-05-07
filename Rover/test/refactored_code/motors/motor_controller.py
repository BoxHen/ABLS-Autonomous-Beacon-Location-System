#!/usr/bin/env python2

import time
import rospy
import serial
import convert
import hex_command_defined
from std_msgs.msg import String

from motor_command import motor_command

class motor_controller:
	def __init__(self):
		self.motor_command = motor_command()

	def move_rover(self, data):
		stop = 0
		speed = 45
		faster_speed = 55
		rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
		rover_action = data.data

		if rover_action == "RIGHT":    
			print("in right")
			self.motor_command.right(faster_speed)

		elif rover_action == "LEFT":  
			print("in left")
			self.motor_command.left(faster_speed)

		elif rover_action == "FORWARD": 	
			print("in forward")
			self.motor_command.forward(speed)

		elif rover_action == "BACKWARD":   	
			print("in back")
			self.motor_command.backward(speed)

		elif rover_action == "forwardSteerLeft":
			print("in forwardSteerLeft")
			self.motor_command.forwardSteerLeft(faster_speed, speed)

		elif rover_action == "forwardSteerRight":
			print("in forwardSteerRight")
			self.motor_command.forwardSteerRight(faster_speed, speed)

		else: # rover_action == "STOP"
			print("in STOP")
			self.motor_command.stop()

	def listener(self):
		rospy.init_node('motor', anonymous=True)
		rospy.Subscriber('setMotor', String, self.move_rover, queue_size=1)
		rospy.spin()

	def stop_motors(self):
		print("motors stopped")
		self.motor_command.stop()

if __name__ == '__main__':
 	try:
		motor_controller = motor_controller()
		motor_controller.listener()
		rospy.on_shutdown(motor_controller.stop_motors)
	except KeyboardInterrupt:  
		pass
