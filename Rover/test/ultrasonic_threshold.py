#!/usr/bin/env python2

def get_threshold_flag(reading_1, reading_2, reading_3, reading_4):
	threshold_flag = 0	
	threshold = 30 #in cm
	all_sensor_blocked = (reading_1 < threshold) and (reading_2 < threshold) and (reading_3 < threshold) and (reading_4 < threshold)
	at_least_one_sensor_blocked = (reading_1 < threshold) or (reading_2 < threshold) or (reading_3 < threshold) or (reading_4 < threshold)
	
	if all_sensor_blocked:
		threshold_flag = 2
		return threshold_flag
	if at_least_one_sensor_blocked:
		threshold_flag = 1
		return threshold_flag
	#no sensor blocked
	threshold_flag = 0
	return threshold_flag
