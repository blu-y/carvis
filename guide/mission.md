# Mission

## 1. Backup topic with Rosbag

Rosbag을 이용하면 지정한 topic의 정보를 녹화하거나 재생할 수 있다.
현장에서 rosbag을 이용하여 topic을 저장한 뒤, bag 파일을 재생하여 재현 및 debug가 가능하다.
다음과 같이 녹화할 topic을 지정하여 bag_record.launch 파일을 생성하여 실행하면 rosbag에 해당 토픽을 담아 추후에 재생할 수 있다.
~~~
<launch>
  <node pkg="rosbag" type="record" name="rosbag" 
    args="-o /home/car/bag/ 
        /velodyne_points
        /camera/color/image_raw/compressed 
        /camera/color/image_raw 
        /vectornav/IMU 
        /vectornav/GPS 
        /vectornav/INS 
        /vectornav/Mag 
        /vectornav/Odom 
        /vectornav/Pres 
        --split --duration=1m"
    output="screen"/>
</launch>
~~~
`$ roslaunch bag_record.launch` 명령을 통해 해당 topic을 녹화할 수 있으며,
`$ rosbag play [bagfile]` 명령을 통해 해당 bag file을 재생할 수 있다.

<!--
## 2. Cone driving

LiDAR만을 이용하여 cone으로 이루어진 도로를 주행하는 미션이다.
LiDAR의 pointcloud를 voxel 필터를 이용하여 간소화 한 후, 거리 필터와 euclidean clustering을 이용하여 각각의 cone을 clustering한다.
-->