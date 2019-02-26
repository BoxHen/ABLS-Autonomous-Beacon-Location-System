#!/usr/bin/env python2

import RPi.GPIO as GPIO
import time
GPIO.setmode (GPIO.BCM)

class Distance:
	#set time vars
	Start_time = time.time()
	Stop_time = time.time()	
	#set speed of ultrasonic
	speed_of_sonic = 34300
	distance_there_and_back = 2

	def __init__(self, trigger_pulse, echo_pulse):
		self.trigger_pulse = trigger_pulse
		self.echo_pulse = echo_pulse
		#setup GPIO in/out direction
		GPIO.setup(Trigger_pulse, GPIO.OUT)
		GPIO.setup(Echo_pulse, GPIO.IN)
		
		self.distance_from_obj()

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

		
