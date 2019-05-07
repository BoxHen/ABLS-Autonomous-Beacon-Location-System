#!/usr/bin/env python2

import motor_move

import RPi.GPIO as IO

IO.setwarnings(False)
IO.setmode (IO.BCM)

#-------------------IR 1------------------------
IO.setup(11,IO.OUT)#GPIO 11 - LED as output
IO.setup(17,IO.IN) #GPIO 17 - IR sensor input

#-------------------IR 2------------------------
IO.setup(5,IO.OUT) #GPIO 5  - LED as output
IO.setup(27,IO.IN) #GPIO 27 - IR sensor input

#-------------------IR 3------------------------
IO.setup(6,IO.OUT) #GPIO 6  - LED as output
IO.setup(22,IO.IN) #GPIO 22 - IR sensor input

#-------------------IR 4------------------------
IO.setup(13,IO.OUT)#GPIO 13 - LED as output
IO.setup(10,IO.IN) #GPIO 10 - IR sensor input

#-------------------IR 5------------------------
IO.setup(19,IO.OUT)#GPIO 19 - LED as output
IO.setup(9,IO.IN)  #GPIO 9  - IR sensor input

while 1:
	if(IO.input(18)==True): #No object detected 
		IO.output(2,False) #led OFF
		motor_move.forward(40)

	if(IO.input(18)==False): #object detected
		IO.output(2,True) #led ON
		motor_move.forward(0)

ser.close()
