#include "std_msgs/Int32MultiArray.h"
#include "ros/ros.h"
#include <vector>
#include <sstream>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <iostream>

using namespace std;

vector<int> get_coordinates(int argc, char *argv[]) {
	int lon = 200;
	int lat = 100;
	vector<int> coordinate_arr; 

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

		coordinates_arr = get_coordinates(argc, argv)
	
		int lat = 0;
		int lon = 1;

		beacon_msg.data.clear();
		beacon_msg.data.push_back(coordinates_arr[lat]);
		beacon_msg.data.push_back(coordinates_arr[lon]);

		ROS_INFO("%s", beacon_msg.data);
		beacon_pub.publish(beacon_msg);

		ros::spinOnce();
		loop_rate.sleep();
	}
	return 0;
}

