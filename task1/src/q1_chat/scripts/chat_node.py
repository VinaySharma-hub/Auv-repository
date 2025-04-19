#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

name = input("Your name (Jolyne/Joestar): ")
rospy.init_node(f"{name}_node")
pub = rospy.Publisher("chat_topic", String, queue_size=10)

def callback(msg):
    if not msg.data.startswith(name):
        print(f"\nFriend: {msg.data}\nYou: ", end="")

rospy.Subscriber("chat_topic", String, callback)

print(f"{name}, type messages (\"exit\" to quit):")
while not rospy.is_shutdown():
    msg = input("You: ")
    if msg == "exit": break
    pub.publish(f"{name}: {msg}")
