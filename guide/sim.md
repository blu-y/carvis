# Simulation
## 1. Install MORAI Simulator (Editing)
Download [MORAI Launcher](https://morai-sim-for-wego-help.scrollhelp.site/user-manual/-10) amd extract at /home/
~~~
$ cd ~/MoraiLauncher_Lin/
$ chmod +x MORAISim.sh
$ chmod +x MoraiLauncher_Lin.x86_64
$ sudo apt install ros-melodic-rosbridge-server
$ sudo apt install ros-melodic-velodyne
~~~

### 1.1 Launch
~~~
$ cd ~/MoraiLauncher_Lin/
$ ./MORAISim.sh
~~~

## 2. ROS connection
~~~
$ roslaunch rosbridge_server rosbridge_websocket.launch
~~~

### 2.1 Camera
MORAI simulator에서 F3을 눌러 카메라를 추가하고 ROS로 연결한다

<img src="https://user-images.githubusercontent.com/102652794/183429535-76548a48-ab3d-43eb-bb42-f684987ee815.png" alt="sensor" width="250"/>

`$ rostopic list` 와 `$ rviz` 를 통해 확인할 수 있다

<img src="https://user-images.githubusercontent.com/102652794/183430128-01c45491-c5e1-4ce6-ad8b-9e7316ec10a0.png" alt="rostopic" width="600"/>

`$ rviz` > `Add` > `By topic` > `/image_jpeg/compressed` > `image`

<img src="https://user-images.githubusercontent.com/102652794/183430760-80a2c438-3fe4-4066-9c18-9372c65ab362.png" alt="rviz" width="650"/>

~~~
$ conda activate vision
(vision)$ cd ~/carvis/Curved-Lane-Lines-master/
(vision)$ python curved_sim.py
~~~

<img src="https://user-images.githubusercontent.com/102652794/183444521-3c0b787b-281f-438a-85b3-ede82c187e85.png" alt="curved_sim" width="900"/>

### 2.2 LiDAR
같은 방법으로 Lidar 또한 연결할 수 있다.

<img src="https://user-images.githubusercontent.com/102652794/183824024-1c9cafa1-5104-4326-a190-e000e694443a.png" alt="lidar setting" width="250"/>

rviz status error 시 
`$ rostopic echo /lidar3D --noarr` 로 frame_id를 확인한다

<img src="https://user-images.githubusercontent.com/102652794/183824087-aa02c147-403c-4e5b-b6ef-b3223cc1bc44.png" alt="lidar echo" width="500"/>

rviz에서 Fixed Frame을 frame_id로 변경하여 실행하면 정상적으로 Pointcloud를 확인할 수 있다.

<img src="https://user-images.githubusercontent.com/102652794/183826350-2f4ce3de-62f3-481d-9b55-8507bca8997e.png" alt="rviz" width="650"/>
