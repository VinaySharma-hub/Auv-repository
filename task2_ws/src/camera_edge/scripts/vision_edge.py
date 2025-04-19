#!/usr/bin/env python3
# Edge detection node
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

bridge = CvBridge()

def process(img_msg):
    try:
        cv_img = bridge.imgmsg_to_cv2(img_msg, "bgr8")
        edges = cv2.Canny(cv_img, 100, 200)
        edge_msg = bridge.cv2_to_imgmsg(edges, "mono8")
        edge_pub.publish(edge_msg)
        cv2.imshow("Edge Detection", edges)
        cv2.waitKey(1)
    except Exception as e:
        rospy.logerr(f"Processing error: {e}")

rospy.init_node('vision_processor')
edge_pub = rospy.Publisher('/vision/edges', Image, queue_size=10)
rospy.Subscriber('/vision/raw', Image, process)
rospy.spin()
