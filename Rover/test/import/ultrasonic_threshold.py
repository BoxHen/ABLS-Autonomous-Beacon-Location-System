#!/usr/bin/env python2

def threshold_flag(reading_1, reading_2, reading_3, reading_4):
	threshold_flag = 0	
	threshold = 15 #in cm
	if (reading_1 < threshold) or (reading_2 < threshold) or (reading_3 < threshold) or (reading_4 < threshold)
		return threshold_flag = 1
	if (reading_1 < threshold) and (reading_2 < threshold) and (reading_3 < threshold) and (reading_4 < threshold)
		return threshold_flag = 2
	return threshold_flag = 0