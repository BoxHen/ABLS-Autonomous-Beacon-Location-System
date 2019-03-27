#!/usr/bin/env python2

import serial
import time
import convert
import command

ser = serial.Serial('/dev/ttyAMA0', 19200, timeout = 1)
print(ser.name+ ' is open.')

def forward(speed):
	ser.write(convert.to_unicode(command.RIGHT_MOTOR_FORWARD))
	ser.write(convert.to_unicode(speed))
	ser.write(convert.to_unicode(command.LEFT_MOTOR_FORWARD))
	ser.write(convert.to_unicode(speed))

def backward(speed):
	ser.write(convert.to_unicode(command.RIGHT_MOTOR_BACKWARD))
	ser.write(convert.to_unicode(speed))
	ser.write(convert.to_unicode(command.LEFT_MOTOR_BACKWARD))
	ser.write(convert.to_unicode(speed))

def left(speed):
	ser.write(convert.to_unicode(command.RIGHT_MOTOR_FORWARD))
	ser.write(convert.to_unicode(speed))
	ser.write(convert.to_unicode(command.LEFT_MOTOR_BACKWARD))
	ser.write(convert.to_unicode(speed))

def right(speed):
	ser.write(convert.to_unicode(command.RIGHT_MOTOR_BACKWARD))
	ser.write(convert.to_unicode(speed))
	ser.write(convert.to_unicode(command.LEFT_MOTOR_FORWARD))
	ser.write(convert.to_unicode(speed))

read_one_byte = 1
msg_received = ser.read(read_one_byte)
print(msg_received)

#ser.close()
