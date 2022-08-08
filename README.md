# Vision
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
## 4. Useful settings and softwares
### 4-1. Korean setting
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

### 4-2. Editing ~/.bashrc to use shortcut command using alias
`$ gedit ~/.bashrc`

~/.bashrc를 수정하여 단축키를 설정할 수 있다.

use alias `alias [shortcut]='[command]'` ex) `alias sb='source ~/.bashrc'`

<img src="https://user-images.githubusercontent.com/102652794/183287749-6744f4a4-f2f8-4cad-94cf-b58363b35dd2.png" alt="alias" width="600"/>

파일을 수정한 후, terminal을 재시작하거나 `$ source ~/.bashrc` 명령어를 이용하여 ~/.bashrc 의 수정사항을 적용할 수 있다.

위 이미지대로 수정 후 한번 적용하였다면, 앞으로는 `$ source ~/.bashrc` 를 `$ sb` 로 실행할 수 있다

### 4-3. Terminator
`$ sudo apt install terminator -y`

Ctrl + Shift + E : split vertically

Ctrl + Shift + O : split horizontally

Ctrl + Shift + W : close window

Alt + Arrow : move between window

### 4-4. Useful softwares
[Chrome](https://www.google.com/chrome/)

[Slack](https://slack.com/intl/ko-kr/downloads/linux)

[VS Code](https://code.visualstudio.com/)


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
$ sha256sum Anaconda3-2022.05-Linux-x86_64.sh # downloaded file name, tab key will help autofill existing file
$ bash Anaconda3-2022.05-Linux-x86_64.sh
$ source ~/.bashrc
(base)$ conda --version # check version
(base)$ conda search python # check available python version
(base)$ conda create -n vision python=3.7
(base)$ conda activate vision
(vision)$ conda deactivate
(base)$ 
~~~

### 6.1. Anaconda auto activation setting 
`$ conda config --set auto_activate_base false # auto activation off`

`$ conda config --set auto_activate_base true # auto activation on`

relaunch terminal

### 6.2 Difference between conda and default terminal

<img src="https://user-images.githubusercontent.com/102652794/183288282-b767f929-f457-4429-bd87-28b7db62965c.png" alt="conda env" width="600"/>

기본에서 실행하면 python=2.7, python3=3.6, (base)에서는 python=3.9, (vision)에서는 python=3.7을 확인할 수 있다.

## 7. Python setting
~~~
(base)$ conda activate vision
(vision)$ cd ~/carvis/yolov5-master
(vision)$ pip install -r requirements.txt
(vision)$ pip install rospkg
~~~
