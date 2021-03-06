#!usr/bin/env python2

import numpy as np

def create_sensor_indexes(number_of_sensors):
	array_of_sensor_indexes = np.zeros(number_of_sensors, dtype=int)
	arr_index = 0

	leftmost_sensor_index = -(number_of_sensors/2)
	rightmost_sensor_index = number_of_sensors/2
	sensor_index = leftmost_sensor_index
	
	while sensor_index <= rightmost_sensor_index:
		if sensor_index == 0:
			sensor_index +=1
			continue
		else:
			array_of_sensor_indexes[arr_index] = sensor_index
			arr_index += 1
			sensor_index +=1

	return array_of_sensor_indexes