def get_threshold_flag(argv):
  threshold = 30
  threshold_flag = 0
  all_sensor_blocked = True #identity for AND 
  at_least_one_sensor_blocked = False #identity for OR
  for arg in argv:
    all_sensor_blocked = all_sensor_blocked and (arg < threshold)
    at_least_one_sensor_blocked = at_least_one_sensor_blocked or (arg < threshold)
  
  #print("all_sensor_blocked : ", all_sensor_blocked)
  #print("at_least_one_sensor_blocked : ", at_least_one_sensor_blocked)	
  
  if all_sensor_blocked:
    threshold_flag += 1
  elif at_least_one_sensor_blocked:
    threshold_flag += 2
  return threshold_flag # no sensors are blocked

print("testing no sensors blocked case")
test1 = get_threshold_flag(63, 63, 63, 63)
if(test1 == 0):
  print("OK")
else:
  print("case failed")

print("testing at least one sensors blocked case")
test2 = get_threshold_flag(6, 63, 63, 63)
if(test2 == 2):
  print("OK")
else:
  print("case failed")

print("testing all sensors blocked case")
test3 = get_threshold_flag(6, 6, 6, 6)
if(test3 == 1):
  print("OK")
else:
  print("case failed")
