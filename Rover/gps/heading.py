#!/usr/bin/env python2

import math

lat1 = math.radians(39.099912)
lat2 = math.radians(38.627089)
long1 = math.radians(-94.581213)
long2 = math.radians(-90.200203)

X = (math.cos(lat2)) * (math.sin(long2-long1))
print(X)

Y = ( (math.cos(lat1)*math.sin(lat2)) - (math.sin(lat1)*math.cos(lat2)*math.cos(long2-long1)) )
print(Y)

Bearing = math.degrees(math.atan2(X, Y))
print(Bearing)
return Bearing

