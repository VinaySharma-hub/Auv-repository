#!/usr/bin/env python3
# Handles movement
import rospy
from std_msgs.msg import String
from q3_bot.msg import bot_pose

x, y = 0.0, 0.0
direction = "north"

rospy.init_node("bot_node")
pub = rospy.Publisher("bot_position", bot_pose, queue_size=5)

def move_bot(cmd):
    global x, y
    if cmd.data == "forward":
        y += 1
    elif cmd.data == "back":
        y -= 1
    elif cmd.data == "left":
        x -= 1
    elif cmd.data == "right":
        x += 1
    
    pos = bot_pose()
    pos.x = x
    pos.y = y
    pos.direction = direction
    pub.publish(pos)
    print(f"Position: ({x}, {y}), Facing: {direction}")

rospy.Subscriber("move_commands", String, move_bot)
rospy.spin()
