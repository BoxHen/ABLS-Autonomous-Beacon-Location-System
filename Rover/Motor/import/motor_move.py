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

def forwardSteerLeft(fasterSpeed, slowerSpeed):
	ser.write(convert.to_unicode(command.RIGHT_MOTOR_FORWARD))
	ser.write(convert.to_unicode(fasterSpeed))
	ser.write(convert.to_unicode(command.LEFT_MOTOR_FORWARD))
	ser.write(convert.to_unicode(slowerSpeed))

def forwardSteerRight(fasterSpeed, slowerSpeed):
	ser.write(convert.to_unicode(command.RIGHT_MOTOR_FORWARD))
	ser.write(convert.to_unicode(slowerSpeed))
	ser.write(convert.to_unicode(command.LEFT_MOTOR_FORWARD))
	ser.write(convert.to_unicode(fasterSpeed))
#STOP can be implemented by setting any of these function's speed to 0

read_one_byte = 1
msg_received = ser.read(read_one_byte)
print(msg_received)

#ser.close()
