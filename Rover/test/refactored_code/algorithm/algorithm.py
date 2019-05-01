#!/usr/bin/env python2
import math
import time
import rospy
import numpy as np
from sensor_indexes import create_sensor_indexes
from std_msgs.msg import Int8MultiArray
from std_msgs.msg import Int16MultiArray
from std_msgs.msg import Int32MultiArray
from std_msgs.msg import String
from std_msgs.msg import Int16
from std_msgs.msg import Bool

from manual_ctrl import manual_ctrl
from beacon_finder import beacon_finder
from obstacle_avoid import obstacle_avoid
	
class algorithm:
	def __init__(self):
		self.motor_command_pub = rospy.Publisher('setMotor', String, queue_size=1)

		self.manual_ctrl = manual_ctrl()
		self.beacon_finder = beacon_finder()
		self.obstacle_avoid = obstacle_avoid()

	def run_algorithm(self): 
		rate = rospy.Rate(10)
		while not rospy.is_shutdown():
			if (self.manual_ctrl.arming_flag == True):
				command = self.manual_ctrl.get_command()
				self.motor_command_pub.publish(command)
			else:
				if (self.beacon_finder.check_beacon_location()): #breaks from loop if we are at the beacon
					break
				if self.obstacle_avoid.threshold_flag == 2:
					self.motor_command_pub.publish("BACKWARD")
				elif self.obstacle_avoid.threshold_flag == 1:
					command = self.obstacle_avoid.process_angle()
					print(command)
					self.motor_command_pub.publish(command)
				elif self.obstacle_avoid.threshold_flag == 0:
					if (self.beacon_finder.calibrate_heading()): #maybe find a better way to implement this
						continue
					beacon_direction = self.beacon_finder.find_beacon_direction()
					self.motor_command_pub.publish(beacon_direction)
			rate.sleep()

if __name__ == '__main__':
	rospy.init_node('algorithm', anonymous=True)
 	try:
		rover_nav = algorithm()
		rover_nav.run_algorithm()
	except rospy.ROSInterruptException:  
		pass
