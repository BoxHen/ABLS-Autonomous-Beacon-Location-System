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
		GPIO.setup(trigger_pulse, GPIO.OUT)
		GPIO.setup(echo_pulse, GPIO.IN)

	def create_trigger_pulse(self):
		GPIO.output(self.trigger_pulse, True) 
		time.sleep(0.00001)
		GPIO.output(self.trigger_pulse, False)

	def receive_echo_pulse(self):
		while GPIO.input(self.echo_pulse) == 0:
			self.Start_time = time.time()

		while GPIO.input(self.echo_pulse) == 1:
			self.Stop_time = time.time()	

	def distance_from_obj(self):
		self.create_trigger_pulse()
		self.receive_echo_pulse()
		Time_elapsed = self.Stop_time - self.Start_time
		distance = (Time_elapsed * self.speed_of_sonic) / self.distance_there_and_back
		return distance

		
