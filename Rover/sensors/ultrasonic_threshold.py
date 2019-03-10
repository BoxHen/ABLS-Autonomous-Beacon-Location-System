#!/usr/bin/env python2

def threshold_flag(reading_1, reading_2, reading_3, reading_4):
	threshold_flag = false	
	threshold = 15 #in cm
	if (reading_1 < threshold) or (reading_2 < threshold) or (reading_3 < threshold) or (reading_4 < threshold)
		threshold_flag = true
	return threshold_flag
