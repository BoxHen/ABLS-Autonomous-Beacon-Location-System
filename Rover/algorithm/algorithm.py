#!/usr/bin/python2 

import rospy
from std_msgs.msg import String

import lib
	
class algorithm:
	def __init__(self):
		self.motor_command_pub = rospy.Publisher('setMotor', String, queue_size=1)

		self.manual_ctrl = lib.manual_ctrl()
		self.beacon_finder = lib.beacon_finder()
		self.obstacle_avoid = lib.obstacle_avoid()

	def run_algorithm(self): 
		rate = rospy.Rate(10)
		while not rospy.is_shutdown():
			if (self.manual_ctrl.arming_flag == True):
				command = self.manual_ctrl.get_command()
				self.motor_command_pub.publish(command)
			else:
				if (self.beacon_finder.check_beacon_location()): #breaks from loop if we are at the beacon
					self.motor_command_pub.publish("STOP")
					break
				if self.obstacle_avoid.threshold_flag == 1:
					print("in flag 2")
					self.motor_command_pub.publish("BACKWARD")
				elif self.obstacle_avoid.threshold_flag == 2:
					print("in flag 1")
					command = self.obstacle_avoid.process_angle()
					print(command)
					self.motor_command_pub.publish(command)
				elif self.obstacle_avoid.threshold_flag == 0:
					print("in flag 0")
					#if (self.beacon_finder.calibrate_heading()):
					#	self.motor_command_pub.publish("FORWARD")
					#	continue
					beacon_direction = self.beacon_finder.find_beacon_direction()
					print("beacon direction is: ", beacon_direction)
					self.motor_command_pub.publish(beacon_direction)
			rate.sleep()

if __name__ == '__main__':
	rospy.init_node('algorithm', anonymous=True)
 	try:
		rover_nav = algorithm()
		rover_nav.run_algorithm()
	except rospy.ROSInterruptException:  
		pass
