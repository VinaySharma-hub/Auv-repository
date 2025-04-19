#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

rospy.init_node("number_sender")
pub = rospy.Publisher("my_numbers", Int32, queue_size=5)

count = 0
while not rospy.is_shutdown():
    count += 2
    pub.publish(count)
    rospy.sleep(1)
