#!/usr/bin/env python

import RPi.GPIO as GPIO
import ultrasonic_sensor
import time

if __name__ == '__main__':
	try:
		while True:
			object = ultrasonic_sensor.Distance(2, 3)
			distance = object.distance_from_obj()
			print("distance is %d cm" %distance)
			time.sleep(1)
	except KeyboardInterrupt:
		print("exited")
		GPIO.cleanup()
		
