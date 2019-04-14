#!/usr/bin/env/ python2
import rospy
import time
from std_msgs.msg import Int16
from std_msgs.msg import Int16MultiArray 
from ultrasonic_sensor import ultrasonic_sensor
from ultrasonic_threshold import get_threshold_flag

class ultrasonics_on_rover():
    def __init__(self, number_of_sensors, pins)
        self.distance_pub = rospy.Publisher('isObstacle', Int16MultiArray, queue_size=1)
	    self.flag_pub = rospy.Publisher('isFlagSet', Int16, queue_size=1)
        rospy.init_node('ultrasonic_sensor', anonymous = True)
        self.number_of_sensors = number_of_sensors
        self.pins = pins
        self.sensors = []
        self.distances = Int16MultiArray()
        self.threshold_flag = 0
        

    def create_sensors(self):
        j = 0
        length = len(self.pins) 
        #add parameter check in case
        for i in range(self.number_of_sensors):
            while j < length-1: 
                self.sensors.append(ultrasonic_sensor(pins[j], pins[j+1]))
                j += 2

    def get_distance(self):
        for i in range(self.number_of_sensors):
            self.distance.data.append(sensors[i].distance_from_obj())

    def check_sensor_boundaries(self):
        self.threshold_flag = get_threshold_flag()
        #FIX!!!

    def run_sensors(self):
        create_sensors()
        while not rospy.is_shutdown():
            get_distance()
            check_sensor_boundaries()

            self.distance_pub.publish(self.distances)
            self.flag_pub.publish(self.threshold_flag)
            print("sensor:", sensor_reading_array.data)
            print("flags:", threshold_flag)