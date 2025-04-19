#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def callback(msg):
    print("RESULT:", msg.data + 5)

rospy.init_node("result_node")
rospy.Subscriber("multiplied", Int32, callback)
rospy.spin()
