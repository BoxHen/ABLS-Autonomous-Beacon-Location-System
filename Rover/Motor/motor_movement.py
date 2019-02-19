#!/usr/bin/env python2

import serial
import time
import struct

ser = serial.Serial('/dev/ttyAMA0', 19200, timeout = 1)
print(ser.name+ ' is open.')

'''
Set Motor Right:
	0xC8: brake low
	0xC9: backward
	0xCA: forward
	0xCB: brake low
Set Motor Left:
	0xC0: brake low
	0xC1: backward
	0xC2: forward
	0xC3: brake low
'''

def forward(speed):
	ser.write(chr(0xCA)) #right side 
	ser.write(chr(speed)) 
	ser.write(chr(0xC2)) #left side
	ser.write(chr(speed))

def backward(speed):
	ser.write(chr(0xC9)) #right side
	ser.write(chr(speed)) 
	ser.write(chr(0xC1)) #left side
	ser.write(chr(speed))

def left(speed):
	ser.write(chr(0xCA)) #right side
	ser.write(chr(speed)) 
	ser.write(chr(0xC1)) #left side
	ser.write(chr(speed))

def right(speed):
	ser.write(chr(0xC9)) #right side
	ser.write(chr(speed)) 
	ser.write(chr(0xC2)) #left side
	ser.write(chr(speed))

msg = ser.read(10)
print(msg)

ser.write(chr(0xCB))
ser.write(chr(0xC3))


ser.close()
