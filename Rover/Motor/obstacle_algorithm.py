<<<<<<< HEAD
#!usr/bin/env python2

import math
import sensor_indexes

number_of_sensors = 4
sensor_indexes = sensor_indexes.create_sensor_indexes(number_of_sensors)
sensor_interval = math.pi/number_of_sensors

=======
#!usr/bin/env python2

import math
import sensor_indexes

number_of_sensors = 4
sensor_indexes = sensor_indexes.create_sensor_indexes(number_of_sensors)
sensor_interval = math.pi/number_of_sensors

>>>>>>> 3d109c0952e36bd1987c1169d2c09b910aeb253d
sensor_weight = sensor_interval*sensor_indexes