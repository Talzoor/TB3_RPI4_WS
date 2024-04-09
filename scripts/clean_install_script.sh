#!/bin/bash

echo -e "\nSet time:"
sudo date -s "$(wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d' ' -f5-8)Z"

echo -e "\nInstall base packs:"
source ~/TB3_RPI4_WS/scripts/Raspbian_packages.sh

echo -e "\nInstall ROS2:"
source ~/TB3_RPI4_WS/scripts/ROS2_installation.sh

echo -e "\nInstall OpenCV:"
sudo apt-get install -y python3-opencv

echo -e "\nInstall ROS2 packs:"
source ~/TB3_RPI4_WS/scripts/ROS2_packages.sh

echo -e "\nAdd email script to startup -->"
echo -e "sudo crontab -e"
echo -e "add “@reboot ~/TB3_RPI4_WS/scripts/send_ip_2_email.py &”"

echo -e "\nClean."
sudo apt-get autoclean

