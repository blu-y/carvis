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

<img src="https://user-images.githubusercontent.com/102652794/183265253-73788c99-fb5b-43b9-ab84-aa8c25843c6c.png" alt="language install" width="400"/>
~~~
$ sudo reboot
$ ibus-setup
~~~
## 5. Install ROS package

~~~
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
$ sudo apt install curl
$ curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
$ sudo apt update
$ sudo apt install ros-melodic-desktop-full
$ echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
$ source ~/.bashrc
$ sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
$ sudo apt install python-rosdep
$ sudo rosdep init
$ rosdep update
~~~
