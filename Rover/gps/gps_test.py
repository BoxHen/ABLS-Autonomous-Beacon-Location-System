import gps
import rospy
from std_msgs.msg import ______

def talker():
	pub = rospy.Publisher('gps_data', String, queue_size=1)
	rospy.init_node('gps', anonymous=True)
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		gps_data = get_gps_data()
		rospy.loginfo(gps_data) 
		pub.publish(gps_data)
		rate.sleep()

def get_gps_data():
	# Listen on port 2947 (gpsd) of localhost
	session = gps.gps("localhost", "2947")
	session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

	while True:
		report = session.next()
		# Wait for a 'TPV' report and display the current time
		# To see all report data, uncomment the line below
		# print(report)
		if report['class'] == 'TPV':
			if hasattr(report, 'time'):
				print(report.time)
				return report.time # change to what data is needed

if __name__='__main__':
	try:
		talker()
	except rospy.ROSInterruptException
		pass