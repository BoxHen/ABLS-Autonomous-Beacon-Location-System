#!/usr/bin/env python2
import time
import math
import board
import busio
import adafruit_lsm303

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lsm303.LSM303(i2c)

while True:
    acc_x, acc_y, acc_z = sensor.acceleration
    mag_x, mag_y, mag_z = sensor.magnetic

    print('Acceleration (m/s^2): ({0:10.3f}, {1:10.3f}, {2:10.3f})'.format(acc_x, acc_y, acc_z))
    print('Magnetometer (gauss): ({0:10.3f}, {1:10.3f}, {2:10.3f})'.format(mag_x, mag_y, mag_z))
    print('')
	heading = (math.atan2(mag_y, mag_x) * 180) / Pi;
	if (heading < 0): #Normalize to 0-360
		heading = 360 + heading;

	print("Compass Heading: ", heading) 
	time.sleep(1.0)
