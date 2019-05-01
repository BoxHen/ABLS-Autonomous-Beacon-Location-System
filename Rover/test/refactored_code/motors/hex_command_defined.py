#I have swapped forward and backwards due to one motor failure
# Right motor commands for TRex Motor
RIGHT_MOTOR_BACKWARD = 0xC2 
RIGHT_MOTOR_FORWARD = 0xC1 
RIGHT_MOTOR_BRAKE = 0xC8

# Left motor commands for TRex Motor
LEFT_MOTOR_BACKWARD = 0xCA
LEFT_MOTOR_FORWARD = 0xC9  
LEFT_MOTOR_BRAKE = 0xC0

#above commands are switched since rover is now moving in other direction
#0xC9 - offcial right forward
#0xCA - offcial right backward
#0xC1 - offcial left forward
#0xC2 - offcial left backward
