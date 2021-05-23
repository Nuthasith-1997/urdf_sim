#!/usr/bin/env python

import rospy
import rospkg
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import SetModelState
from nav_msgs.msg import Odometry

class setPose:
	def __init__(self):
		rospy.init_node('set_pose')
		rospy.Subscriber('/odom', Odometry, self.set_gazebo_pose)
		self.state_msg = ModelState()

	def set_gazebo_pose(self, msg):
		self.state_msg.model_name = 'apt_prototype'
		#self.state_msg.model_name = 'turtlebot3'
		self.state_msg.pose.position.x = msg.pose.pose.position.x
		self.state_msg.pose.position.y = msg.pose.pose.position.y
		self.state_msg.pose.position.z = 0 #msg.pose.pose.position.z
		self.state_msg.pose.orientation.x = msg.pose.pose.orientation.x
		self.state_msg.pose.orientation.y = msg.pose.pose.orientation.y
		self.state_msg.pose.orientation.z =	msg.pose.pose.orientation.z
		self.state_msg.pose.orientation.w =	msg.pose.pose.orientation.w

		rospy.wait_for_service('/gazebo/set_model_state')
		try:
			set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
			set_state(self.state_msg)

		except rospy.ServiceException, e:
			print "Service call failed: %s" % e

if __name__ == '__main__':
	setPose()
	rospy.spin()