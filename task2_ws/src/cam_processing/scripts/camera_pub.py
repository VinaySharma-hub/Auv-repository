#!/usr/bin/env python3
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def main():
    rospy.init_node('camera_publisher')
    pub = rospy.Publisher('camera/image_raw', Image, queue_size=1)
    bridge = CvBridge()
    
    cap = cv2.VideoCapture(0)
    print("Publishing camera feed...")
    
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if ret:
            ros_image = bridge.cv2_to_imgmsg(frame, "bgr8")
            pub.publish(ros_image)
        cv2.waitKey(1)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

