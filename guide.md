# CARVIS
## 1. Get ubuntu iso image
https://releases.ubuntu.com/18.04.6/
## 2. Make USB Installer
https://www.pendrivelinux.com/universal-usb-installer-easy-as-1-2-3/
## 3. Update ubuntu-driver
~~~
$ sudo apt-get update
$ sudo apt-get updrade
$ sudo ubuntu-drivers autoinstall
~~~
## 4. Korean setting
~~~
$ gnome-control-center
~~~

Region & Language > Manage Installed Languages > Install

<img src="https://user-images.githubusercontent.com/102652794/183265253-73788c99-fb5b-43b9-ab84-aa8c25843c6c.png" alt="language install" width="500"/>

~~~
$ sudo reboot
$ ibus-setup
~~~

IBus Preferences > Input Method > Add > Korean > Hangul

<img src="https://user-images.githubusercontent.com/102652794/183265434-70672774-7c12-4c7c-891f-4d4ce4c5e9d6.png" alt="ibus" width="500"/>

Korean - Hangul > Preferences > Hangul Toggle Key > Add [toggle key]
~~~
$ gnome-control-center
~~~
Region & Language > Input Sources > + > Korean > Korean (Hangul) > Add > English (US) > - 

<img src="https://user-images.githubusercontent.com/102652794/183265578-fd17c0c9-52ea-4961-becd-273cf62c00c8.png" alt="ibus" width="500"/>

## 5. Install ROS Melodic

~~~
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
$ sudo apt install curl
$ curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
$ sudo apt update
$ sudo apt install ros-melodic-desktop-full
$ echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
$ source ~/.bashrc
$ sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
$ sudo rosdep init
$ rosdep update
~~~

## 6. Install Anaconda & create env
Download anaconda
https://www.anaconda.com/products/distribution
~~~
$ cd ~/Downloads/
$ sha256sum Anaconda3-2022.05-Linux-x86_64.sh
$ bash Anaconda3-2022.05-Linux-x86_64.sh
$ source ~/.bashrc
(base)$ conda --version
(base)$ conda search python
(base)$ conda create -n vision python=3.9
(base)$ conda activate vision
(vision)$ conda deactivate
(base)$ 
~~~

# 6.1. Anaconda auto activation setting 
`$ conda config --set auto_activate_base false # auto activation off`

`$ conda config --set auto_activate_base true # auto activation on`

relaunch terminal

# 6.2 Difference between conda and default terminal

<img src="https://user-images.githubusercontent.com/102652794/183282401-4b97f8dc-c145-4b31-92ed-a23280893728.png" alt="conda python" width="500"/>

## 7. Git
~~~
(base)$ cd ~/Desktop/
(base)$ git clone https://github.com/blu-y/carvis.git
~~~

## 8. Python setting
~~~
(base)$ conda activate vision
(vision)$ conda install pyqt
(vision)$ conda install opencv
(vision)$ cd ~/Desktop/carvis/yolov5-master
(vision)$ pip install -r requirements.txt
~~~
~~~
# if error or required
(vision)$ pip install --upgrade pip
(vision)$ pip install --upgrade setuptools
(vision)$ pip install -r requirements.txt
~~~
