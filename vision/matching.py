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
		dat=first()
		if s==data.c:
			dat.c="match"
		else:
			dat.c="did not match"
		dat.a=data.a
		dat.b=data.b
		pub.publish(dat)
	if __name__ == '__main__':
		try:
			matching()
		except rospy.ROSInterruptException:
			pass
