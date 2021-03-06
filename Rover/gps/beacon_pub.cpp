#include "../rc-switch/RCSwitch.h"
#include "std_msgs/Int32MultiArray.h"
#include "ros/ros.h"
#include <vector>
#include <sstream>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <iostream>

using namespace std;

RCSwitch mySwitch;

vector<int> get_coordinates(int argc, char *argv[]) {
	int lon;
	int lat;
	int PIN = 29;
	int pulseLength = 0;
	vector<int> coordinate_arr; 

	if(wiringPiSetup() == -1) {
		printf("wiringPiSetup failed, exiting...");
		//return 0;
	}
	if (argv[1] != NULL) pulseLength = atoi(argv[1]);

	mySwitch = RCSwitch();
	if (pulseLength != 0) mySwitch.setPulseLength(pulseLength);
	mySwitch.enableReceive(PIN);  // Receiver on interrupt 0 => that is pin #2

	while(1) {
		if (mySwitch.available()) {
			int value = mySwitch.getReceivedValue();
			if (value == 0) {
				printf("Unknown encoding\n");
			} 	
			else {
				if(value < 500000){
					lat = value + 42000000;
					printf("Latitude is %i\n: ",lat);
				}
				else {
					lon = -1 * value - 75000000;
					printf("Longitude is %i\n: ", lon);
				}
			}
			fflush(stdout);
			mySwitch.resetAvailable();
		}
		usleep(100); 
	}
	coordinate_arr.push_back(lat);
	coordinate_arr.push_back(lon);
	return coordinate_arr;
}

int main(int argc, char **argv){
	ros::init(argc, argv, "beacon_publisher");
	ros::NodeHandle nh;
	ros::Publisher beacon_pub = nh.advertise<std_msgs::Int32MultiArray>("beacon_gps", 100);

	ros::Rate loop_rate(1);

	while (ros::ok()){
		std_msgs::Int32MultiArray beacon_msg;

		vector<int> coordinates_arr = get_coordinates(argc, argv)
	
		int lat = 0;
		int lon = 1;

		beacon_msg.data.clear();
		beacon_msg.data.push_back(coordinates_arr[lat]);
		beacon_msg.data.push_back(coordinates_arr[lon]);

		ROS_INFO("latitude: %d", beacon_msg.data[0]);
		ROS_INFO("longitude: %d", beacon_msg.data[1]);
		beacon_pub.publish(beacon_msg);

		ros::spinOnce();
		loop_rate.sleep();
	}
	return 0;
}

