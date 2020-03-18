        #!/usr/bin/env python
	import cv2
        import rospy
	from msg.msg import first
	def matching():
		rospy.init_node('matching',anonymous=True)
		sub1=rospy.Subscriber('detection_result', first,callback)
		ros.spin()
		
		
	
	def callback(data):
		
		pub=rospy.Publisher('match_result', first)
		s="фйыцйчд".encode('cp1251')
		if s==data.c:
			data.c="match"
		else:
			data.c="did not match"
		pub.publish(data)
	if __name__ == '__main__':
		try:
			matching()
		except rospy.ROSInterruptException:
			pass
