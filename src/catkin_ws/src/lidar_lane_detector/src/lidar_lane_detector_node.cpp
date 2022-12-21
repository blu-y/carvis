#include "lidar_lane_detector.h"
#include "point_xyzir.h"

int main(int argc, char **argv) {
	ros::init(argc, argv, "lidar_lane_detector_node");

	LaneDetector ld;

	ros::spin();

	return 0;
}

