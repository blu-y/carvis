import rospy
from sensor_msgs.msg import PointCloud2
import numpy as np
import pandas as pd
from struct import unpack
from std_msgs.msg import Float64
from morai_msgs.msg import CtrlCmd

def control(path):
	# given path point make control signal
	return 1, 1

def line_path(arr):
	left = []
	right = []
	# given avg_points make line
	for i in range(len(arr)):
		arr[i].append(arr[i][0]**2+arr[i][1]**2)
	for i in arr:
		if i[1] > 0: left.append(i)
		else: right.append(i)
	if len(left) < len(right): d = 'r'
	else: d = 'l'
	left = np.array(left)
	right = np.array(right)
	l_ind = np.argsort(left, axis=0)
	print(left)
	print(l_ind)
	if len(left) == 1: base_l = left[0]
	else: base_l = left[np.argmin(left[:][2])]
	if len(right) == 1: base_r = right[0]
	else: base_r = right[np.argmin(right[:][2])]
	#print(base_l, base_r)
	p = 0
	return p

def cb(data):
	#print('\nclustered data size: ', data.width)
	point = []
	pc = data.data
	for n in range(data.width):
		pt = pc[32*n:32*(n+1)]
		#pts = unpack("ffffBBBBIII", pt) #XYZRGB
		pts = unpack("fffffIII", pt) # XYZI
		point.append(pts)
	df = pd.DataFrame(point, columns = ['X', 'Y', 'Z', '1', 'C', '-1', '8', '0'])
	point_avg = df.groupby('C')[['X','Y']].mean().values.tolist()
	#print(point_avg[:],"\n")
	# Y value >> + : L, - : R
	ca, cs = control(line_path(point_avg))
	pub.publish(accel=ca, steering=cs)
#rostopic pub /ctrl_cmd morai_msgs/CtrlCmd "{longlCmdType: 0, accel: 0.0, bra: 0.0, steering: 0.0, velocity: 0.0, acceleration: 0.0}" 
rospy.init_node('test')
rate = rospy.Rate(1)
sub = rospy.Subscriber('/velodyne_points_clustered', PointCloud2, cb, queue_size = 1)
pub = rospy.Publisher('/ctrl_cmd', CtrlCmd, queue_size = 10)
while rospy.is_shutdown() is not True:
	rate.sleep()

