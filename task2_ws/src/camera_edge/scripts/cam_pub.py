#!/usr/bin/env python3
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

rospy.init_node('camera_pub')
pub = rospy.Publisher('/cam/raw', Image, queue_size=1)
bridge = CvBridge()

cap = cv2.VideoCapture(0)
print("Camera publishing...")

while not rospy.is_shutdown():
    ret, frame = cap.read()
    if ret:
        pub.publish(bridge.cv2_to_imgmsg(frame, "bgr8"))
    cv2.waitKey(1)
