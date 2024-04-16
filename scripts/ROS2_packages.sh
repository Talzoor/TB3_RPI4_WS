#!/bin/bash

echo -e "\nInstall ROS packs:"
cd ~/TB3_RPI4_WS/src

echo -e "\nInstall cv_bridge:" # https://index.ros.org/p/cv_bridge/
sudo apt-get install -y python3-numpy
sudo apt-get install -y libboost-python-dev
git clone https://github.com/ros-perception/vision_opencv.git -b humble

echo -e "\nInstall Dynamixel SDK:" # https://index.ros.org/p/dynamixel_sdk/
git clone https://github.com/ROBOTIS-GIT/DynamixelSDK.git -b ros2

echo -e "\nInstall rosdep and Check dependencies:"
sudo apt-get install -y python3-rosdep2
sudo rosdep init
rosdep update
rosdep install -i --from-path ~/TB3_RPI4_WS/src/ --rosdistro humble -y