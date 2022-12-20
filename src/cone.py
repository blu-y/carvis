
import rospy
from sensor_msgs.msg import PointCloud2
import numpy as np
import pandas as pd
from struct import unpack
from std_msgs.msg import Float64
from morai_msgs.msg import CtrlCmd
from erp_driver.msg import erpCmdMsg
import math

def control(path):
	# given path point, make control signal
	# accel 0 ~ 1
	# steer -1 ~ 1 37deg
	accel = 35
	if path == None: return accel, 0
	maxsteer = 37
	deg = math.degrees(math.acos(path[0]/np.linalg.norm(path))) / maxsteer
	steer = np.sign(path[1]) * min(deg*2000, 2000) 
	return accel, steer

def line_path(arr):
	left = []
	right = []
	# given avg_points, make path point
	for i in range(len(arr)):
		arr[i].append(arr[i][0]**2+arr[i][1]**2)
	for i in arr:
		if i[1] > 0: left.append(i)
		else: right.append(i)
	if len(left) < len(right): d = -1 # left
	else: d = 1 # right
	left = np.array(left)
	right = np.array(right)
	if len(left)<=1 or len(right)<=1: return None
	base_l = left[np.argmin(left[:][2])]
	left = np.delete(left, np.argmin(left[:,2]), axis=0)
	base_r = right[np.argmin(right[:][2])]
	right = np.delete(right, np.argmin(right[:,2]), axis=0)
	if d == -1 : # left turn, use base_r, right ref
		base = base_r
		ref = right[np.argmin(right[:,2])]
	else: # right turn, use base_l, left ref
		base = base_l
		ref  = left[np.argmin(left[:,2])]
	b2r = ref[0:2] - base[0:2]
	b2r = b2r / np.linalg.norm(b2r)
	p = [ref[0]-b2r[1], ref[1]+b2r[0]]
	return p

def cb(data):
	global ca
	global cs
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
	print(ca, cs)
	if cs.isnumeric(): pub.publish(speed=int(ca), steer=int(cs))
	else: pub.publish(speed=int(ca))

#rostopic pub /ctrl_cmd morai_msgs/CtrlCmd "{longlCmdType: 0, accel: 0.0, bra: 0.0, steering: 0.0, velocity: 0.0, acceleration: 0.0}" 

ca = 0
cs = 0
rospy.init_node('test')
rate = rospy.Rate(1)
sub = rospy.Subscriber('/velodyne_points_clustered', PointCloud2, cb, queue_size = 1)
pub = rospy.Publisher('/control', erpCmdMsg, queue_size = 1)
while rospy.is_shutdown() is not True:
	#pub.publish(speed=0, brake=1, steer=cs)
	rate.sleep()

