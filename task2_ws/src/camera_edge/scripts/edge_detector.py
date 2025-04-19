#!/usr/bin/env python3
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

rospy.init_node('edge_detector')
bridge = CvBridge()

def callback(msg):
    try:
        img = bridge.imgmsg_to_cv2(msg, "bgr8")
        edges = cv2.Canny(img, 100, 200)
        cv2.imshow("Edges", edges)
        cv2.waitKey(1)
    except Exception as e:
        print(f"Error: {e}")

rospy.Subscriber('/cam/raw', Image, callback)
rospy.spin()
