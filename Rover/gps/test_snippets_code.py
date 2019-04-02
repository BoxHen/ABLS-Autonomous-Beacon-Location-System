if (self.Beacon_latitude > self.Rover_latitude):
	return "FORWARD" #north/up
elif (self.Beacon_latitude < self.Rover_latitude):
	return "BACKWARD" #south/down
else: #self.Beacon_latitude == self.Rover_latitude
	
if (self.Beacon_longitude > self.Rover_longitude):
	return "RIGHT"
elif (self.Beacon_longitude < self.Rover_longitude):
	return "LEFT"
else: #self.Beacon_longitude > self.Rover_longitude

#===================================================
def findTrueNorth(self):
	if (-10 < self.Rover_heading < 10): # tolerance for north
		return "TRUE"
	elif (self.Rover_heading < 0):
		return "RIGHT"
	elif (self.Rover_heading > 0):
		return "LEFT"


findNorth = findTrueNorth()
if (findNorth != "TRUE"):
	return findNorth

#===================================================

