#!/usr/bin/env python2
import time

class beacon_finder:
  def __init__(self):
    self.startup_time = time.time()
    
  def calibrate_heading(self):
    current_time = time.time()
    
    #print(current_time)
    #print(self.startup_time)
    is_calibrated = False
    if (current_time - self.startup_time < 2):
      print("FORWARD")
      is_calibrated = True
    
    return is_calibrated
  
if __name__ == '__main__':
  algorithm = beacon_finder()
  while True:
    x = algorithm.calibrate_heading()
    print(x)
    if (x == False):
      print("it works")
      break
