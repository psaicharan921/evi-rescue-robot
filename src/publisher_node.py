#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def pick_and_place_publisher():
    pub = rospy.Publisher('task_command', String, queue_size=10)
    rospy.init_node('pick_and_place_publisher', anonymous=True)
    rate = rospy.Rate(1)  # 1 Hz
    while not rospy.is_shutdown():
        command_str = "PICK: red_box at (x=0.5, y=0.2)"
        rospy.loginfo(f"Publishing command: {command_str}")
        pub.publish(command_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        pick_and_place_publisher()
    except rospy.ROSInterruptException:
        pass
