#!/usr/bin/env python

import RPi.GPIO as IO
import time
IO.setmode (IO.BCM)
#=====================Variables======================
#set GPIO pins
Trigger_pulse = 18
Echo_pulse = 24

#set time vars
Start_time = time.time()
Stop_time = time.time()	

#set speed of ultrasonic
speed_of_sonic = 34300

distance_there_and_back = 2
#====================================================
#setup GPIO in/out direction
GPIO.setup(Trigger_pulse, GPIO.OUT)
GPIO.setup(Echo_pulse, GPIO.IN)

def create_trigger_pulse():
	GPIO.output(Trigger_pulse, True) 
	time.sleep(0.00001)
	GPIO.output(Trigger_pulse, False)

def receive_echo_pulse():
	while GPIO.input(Echo_pulse) == 0:
		Start_time = time.time()
	
	Stop_time = time.time()	

def distance_from_obj():
	create_trigger_pulse()
	receive_echo_pulse()
	Time_elapsed = Stop_time - Start_time
	distance = (Time_elapsed * speed_of_sonic) / distance_there_and_back
	return distance

if __name__ = '__main__'
	try:
		while True:
			distance_from_obj = distance_from_obj()
			print("distance is %.1f cm" %distance_from_obj)
			time.sleep(1)
	except KeyboardInterrupt:
		print("exited")
		GPIO.cleanup()
		
