import time
import os
import rospy
from std_msgs.msg import String
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
# Set up the pins what will need for us
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
p = GPIO.PWM(16,500)

# The function is the "callback" that handles the messages as they come in: 
def callback(msg):
    print msg.data
    if msg.data == "clockwise":
        # Send to the direction pin the True value
        GPIO.output(18, True)
    else:
        # Send to the direction pin the False value
        GPIO.output(18, False)
    steps = 0
    # 1000 is the 2.5 rotation for this stepper(12 V)
    while steps < 1000:
        p.start(1)
        steps += 1
        time.sleep(0.01)
    p.stop()
	
rospy.init_node('Stepper_Subscriber')
sub = rospy.Subscriber('rotation', String, callback)
rospy.spin()
