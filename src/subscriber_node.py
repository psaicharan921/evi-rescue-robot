#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def task_callback(data):
    rospy.loginfo(f"Received task: {data.data}")
    # Simulate performing pick and place
    rospy.sleep(2)
    rospy.loginfo("Task completed")

def pick_and_place_subscriber():
    rospy.init_node('pick_and_place_subscriber', anonymous=True)
    rospy.Subscriber("task_command", String, task_callback)
    rospy.spin()

if __name__ == '__main__':
    pick_and_place_subscriber()
