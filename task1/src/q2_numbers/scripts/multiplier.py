#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

rospy.init_node("multiply_node")
pub = rospy.Publisher("multiplied", Int32, queue_size=5)

def callback(msg):
    pub.publish(msg.data * 10)

rospy.Subscriber("my_numbers", Int32, callback)
rospy.spin()
