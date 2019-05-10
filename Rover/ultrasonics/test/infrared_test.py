#!/usr/bin/env python

import RPi.GPIO as IO
IO.setwarnings(False)
IO.setmode (IO.BCM)

IO.setup(2,IO.OUT) #GPIO 2 - LED as output
IO.setup(14,IO.IN) #GPIO 14 - IR sensor input

while 1:
	if(IO.input(14)==True): #No object detected 
		IO.output(2,False) #led OFF

	if(IO.input(14)==False): #object detected
		IO.output(2,True) #led ON
