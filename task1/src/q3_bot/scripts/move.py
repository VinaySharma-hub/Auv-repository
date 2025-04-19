#!/usr/bin/env python3
# Simple command sender
import rospy
from std_msgs.msg import String

rospy.init_node("command_node")
pub = rospy.Publisher("move_commands", String, queue_size=5)

print("Type: forward/back/left/right")
while not rospy.is_shutdown():
    cmd = input("> ")
    pub.publish(cmd)
