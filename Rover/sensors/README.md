# Sensor Folder

ultrasonic_pub.py
	python file that publishes to sensors values for the algorithm to process

import folder - files called upon by ultrasonic_pub.py
ultrasonic_sensor.py
	controls the ultrasonic sensors by sending the trigger and echo pulses for the sensors 

sensor_indexes.py
	generates a sensor index that looks like [-2 -1 1 2] if we have 4 sensors. This is needed to calculate the rebound angle as each senspr is weighted based on 		position. (check out the "Obstacle Avoidance.pdf" for more info in "Conceptual Design"/resources)
