#!/usr/bin/env python2

def get_threshold_flag(*argv):
	threshold = 30
	all_sensor_blocked = True #identity for AND 
	at_least_one_sensor_blocked = False #identity for OR
	threshold_flag = 0
	for arg in argv:
		all_sensor_blocked = all_sensor_blocked and (arg < threshold)
		at_least_one_sensor_blocked = at_least_one_sensor_blocked or (arg < threshold)
	
	if all_sensor_blocked:
		threshold_flag += 1
	elif at_least_one_sensor_blocked:
		threshold_flag += 2
	return threshold_flag # no sensors are blocked