#!/usr/bin/python2 

import serial
import time
import convert
import hex_command_defined

class motor_command:
	def __init__(self):
		self.ser = serial.Serial('/dev/ttyAMA0', 19200, timeout = 1)
		print(self.ser.name+ ' is open.')

	def forward(self, speed):
		self.ser.write(convert.to_unicode(hex_command_defined.RIGHT_MOTOR_FORWARD))
		self.ser.write(convert.to_unicode(speed))
		self.ser.write(convert.to_unicode(hex_command_defined.LEFT_MOTOR_FORWARD))
		self.ser.write(convert.to_unicode(speed))

	def backward(self, speed):
		self.ser.write(convert.to_unicode(hex_command_defined.RIGHT_MOTOR_BACKWARD))
		self.ser.write(convert.to_unicode(speed))
		self.ser.write(convert.to_unicode(hex_command_defined.LEFT_MOTOR_BACKWARD))
		self.ser.write(convert.to_unicode(speed))

	def left(self, speed):
		self.ser.write(convert.to_unicode(hex_command_defined.RIGHT_MOTOR_FORWARD))
		self.ser.write(convert.to_unicode(speed))
		self.ser.write(convert.to_unicode(hex_command_defined.LEFT_MOTOR_BACKWARD))
		self.ser.write(convert.to_unicode(speed))

	def right(self, speed):
		self.ser.write(convert.to_unicode(hex_command_defined.RIGHT_MOTOR_BACKWARD))
		self.ser.write(convert.to_unicode(speed))
		self.ser.write(convert.to_unicode(hex_command_defined.LEFT_MOTOR_FORWARD))
		self.ser.write(convert.to_unicode(speed))

	def forwardSteerLeft(self, faster_speed, speed):
		self.ser.write(convert.to_unicode(hex_command_defined.RIGHT_MOTOR_FORWARD))
		self.ser.write(convert.to_unicode(faster_speed))
		self.ser.write(convert.to_unicode(hex_command_defined.LEFT_MOTOR_BACKWARD))
		self.ser.write(convert.to_unicode(speed))

	def forwardSteerRight(self, faster_speed, speed):
		self.ser.write(convert.to_unicode(hex_command_defined.RIGHT_MOTOR_BACKWARD))
		self.ser.write(convert.to_unicode(speed))
		self.ser.write(convert.to_unicode(hex_command_defined.LEFT_MOTOR_FORWARD))
		self.ser.write(convert.to_unicode(faster_speed))

	def stop(self):
		self.ser.write(convert.to_unicode(hex_command_defined.RIGHT_MOTOR_BRAKE))
		self.ser.write(convert.to_unicode(hex_command_defined.LEFT_MOTOR_BRAKE))

	#read_one_byte = 1
	#msg_received = ser.read(read_one_byte)
	#print(msg_received)
	#ser.close()
