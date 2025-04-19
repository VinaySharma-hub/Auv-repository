#!/usr/bin/env python3
# Camera publisher node
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def main():
    rospy.init_node('vision_publisher')
    pub = rospy.Publisher('/vision/raw', Image, queue_size=10)
    bridge = CvBridge()
    
    cap = cv2.VideoCapture(0)
    print("Camera stream started...")
    
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if ret:
            ros_img = bridge.cv2_to_imgmsg(frame, "bgr8")
            pub.publish(ros_img)
        cv2.waitKey(1)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
