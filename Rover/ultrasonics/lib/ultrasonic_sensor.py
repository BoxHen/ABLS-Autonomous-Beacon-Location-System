#!/usr/bin/python2 

import time
import RPi.GPIO as GPIO
GPIO.setmode (GPIO.BCM)

class ultrasonic_sensor:
	#set time vars
	#Start_time = time.time()
	#Stop_time = time.time()	
	#set speed of ultrasonic
	speed_of_sonic = 34300
	distance_there_and_back = 2

	def __init__(self, trigger_pulse, echo_pulse):
		self.trigger_pulse = trigger_pulse
		self.echo_pulse = echo_pulse
		#setup GPIO in/out direction
		GPIO.setup(trigger_pulse, GPIO.OUT)
		GPIO.setup(echo_pulse, GPIO.IN)
		self.Start_time = time.time()
		self.Stop_time = time.time()
		self.max_wait_time = 0
		self.time_delta = 0

	def create_trigger_pulse(self):
		GPIO.output(self.trigger_pulse, True) 
		time.sleep(0.00001)
		GPIO.output(self.trigger_pulse, False)

	def receive_echo_pulse(self):
		self.max_wait_time = 0
		self.Start_time = time.time()
		start_loop_time = time.time() # time at which this loop started
		while ((GPIO.input(self.echo_pulse) == 0) and (self.max_wait_time < 0.009)):
			self.Start_time = time.time()
			self.max_wait_time = self.Start_time - start_loop_time 

		self.time_delta = 0
		while ((GPIO.input(self.echo_pulse) == 1) and (self.time_delta < 0.004)):
			self.Stop_time = time.time()	
			self.time_delta = self.Stop_time - self.Start_time

	def distance_from_obj(self):
		self.create_trigger_pulse()
		self.receive_echo_pulse()
		distance = (self.time_delta * self.speed_of_sonic) / self.distance_there_and_back
		return distance

		
