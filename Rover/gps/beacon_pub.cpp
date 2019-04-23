#include "../rc-switch/RCSwitch.h"
#include "std_msgs/Int32MultiArray.h"
#include "ros/ros.h"
#include <sstream>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

RCSwitch mySwitch;

int get_coordinates(int argc, char *argv[]) {
     int PIN = 29;
     
     if(wiringPiSetup() == -1) {
       printf("wiringPiSetup failed, exiting...");
       return 0;
     }

     int pulseLength = 0;
     if (argv[1] != NULL) pulseLength = atoi(argv[1]);

     mySwitch = RCSwitch();
     if (pulseLength != 0) mySwitch.setPulseLength(pulseLength);
     mySwitch.enableReceive(PIN);  // Receiver on interrupt 0 => that is pin #2
    
     while(1) {
      if (mySwitch.available()) {
        int value = mySwitch.getReceivedValue();
	int lon; int lat;
        if (value == 0) {
          printf("Unknown encoding\n");
        } else {
	  if(value < 500000){
	    lat = value + 42000000;
	    printf("Lat is %i\n",lat);
	    return lat;
	  }
	  else {lon = -1 * value - 75000000;
	    printf("Lon is %i", lon);
	    return lon;
	  }
	  
        }
        fflush(stdout);
        mySwitch.resetAvailable();
      }
      usleep(100); 
  }
  exit(0);
}

int process_coordinates(int argc, char *argv[]) {
  coordinates = get_coordinates(argc, argv)
  /*
  ADD proccessing
  lat = 
  lon = 
  */

int main(int argc, char **argv, ){
  ros::init(argc, argv, "beacon_publisher");
  ros::NodeHandle nh;
  ros::Publisher beacon_pub = nh.advertise<std_msgs::String>("beacon_gps", 100);

  ros::Rate loop_rate(1);

  while (ros::ok()){
    lat = 0
    lon = 1
    std_msgs::Int32MultiArray beacon_msg;

    coordinates_arr = process_coordinates(argc, argv)

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

