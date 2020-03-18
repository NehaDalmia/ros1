        #!/usr/bin/env python
	
        import rospy
	import cv2
	import numpy as np
        import image_transport
        from cv_bridge import CvBridge, CvBridgeError
        #import os
	from sensor_msgs.msg import Image

	# Create a VideoCapture object and read from input file

	# If the input is the camera, pass 0 instead of the video file name
        def camera():
		cap = cv2.VideoCapture(0)
		rospy.init_node('camera', anonymous=True)
		pub=rospy.Publisher('videofeed',Image,queue_size=10)
		bridge=CvBridge()
		
		#fps=cap.get(cv2.CAP_PROP_FPS)
		rate=rospy.Rate(10)
        
	         
	# Check if camera opened successfully

	# Read until video is completed

		while not rospy.is_shutdown():
                  
	  # Capture frame-by-frame

	  		ret, frame = cap.read()

	  		pub.publish(bridge.cv2_to_imgmsg(frame))
			rospy.logininfo('image1')
			rate.sleep()

	 
	    # Display the resulting frame

	    		cv2.imshow('Frame',frame)
			cv2.waitKey(1)

	if __name__ == '__main__':
		try:
			camera()
		except rospy.ROSInterruptException:
			pass
