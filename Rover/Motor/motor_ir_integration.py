#!/usr/bin/env python2

import motor_move

import RPi.GPIO as IO

IO.setwarnings(False)
IO.setmode (IO.BCM)

IO.setup(2,IO.OUT) #GPIO 2 - LED as output
IO.setup(18,IO.IN) #GPIO 14 - IR sensor input

while 1:
	if(IO.input(18)==True): #No object detected 
		IO.output(2,False) #led OFF
		motor_move.forward(40)

	if(IO.input(18)==False): #object detected
		IO.output(2,True) #led ON
		motor_move.forward(0)

ser.close()
