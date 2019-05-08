#!/usr/bin/env python3
import time
import math
import board
import busio
import Adafruit_LSM303

lsm303 = Adafruit_LSM303.LSM303() # Create a LSM303 instance

print('Printing accelerometer & magnetometer X, Y, Z axis values, press Ctrl-C to quit...')

while True:
	accel, mag = lsm303.read()     # Read the X, Y, Z axis acceleration values and print them.
	
	# Grab the X, Y, Z components from the reading and print them out.
	accel_x, accel_y, accel_z = accel
	mag_x, mag_y, mag_z = mag
	print('Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5}'.format(accel_x, accel_y, accel_z, mag_x, mag_y, mag_z))
   
	heading = (math.atan2(mag_y, mag_x) * 180) / math.pi;
	if (heading < 0): #Normalize to 0-360
		heading = 360 + heading;

	print("Compass Heading: ", heading) 
	
	# Wait half a second and repeat.
	time.sleep(0.5)
