#!/usr/bin/env python2
import time
import rospy
from std_msgs.msg import Int16MultiArray
from std_msgs.msg import String

class manual_ctrl:	
	def __init__(self):
		self.arming_flag = False
		self.manual_command = "FORWARD"
		#self.vehicle_status_array = Int16MultiArray()
		self.confirm_flag_pub = rospy.Publisher('vehicle_status', Int8MultiArray, queue_size=1)
	
		rospy.Subscriber('armingMessage', Bool, self.get_armingMessage, queue_size=1)
		rospy.Subscriber('manualCtrl', String, self.get_manualCtrl, queue_size=1)	

	def get_command(self):
		command = "FORWARD"
		if (self.manual_command == "LEFT"):
			command = "LEFT"
		elif (self.manual_command ==  "RIGHT"):
			command = "RIGHT"
		elif (self.manual_command == "FORWARD"):
			command = "FORWARD"
		elif (self.manual_command == "BACKWARD"):
			command = "BACKWARD"
		else: #STOP
			command = "STOP"
		return command

	def get_manualCtrl(self, data):
		rospy.loginfo(rospy.get_caller_id() + "I heard FLAG: %s", data.data)
		self.manual_command = data.data


	def get_armingMessage(self, arming_flag):
		rospy.loginfo(rospy.get_caller_id() + "I heard arming flag: %s", arming_flag.data)
		self.arming_flag = arming_flag.data
		
		publish_arming_Message()

	def publish_arming_Message(self):
		vehicle_status_array = Int8MultiArray()
		vehicle_status_array.data = [1]
		self.confirm_flag_pub.publish(vehicle_status_array)
