#!/usr/bin/env python2

import rospy
from std_msgs.msg import Int16MultiArray

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def listener():
    rospy.init_node('ultrasonic_sensor_listener', anonymous=True)

    rospy.Subscriber("isObstacle", Int16MultiArray, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()


