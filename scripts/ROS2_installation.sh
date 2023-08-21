#!/bin/bash
# from https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html

echo -e "\n---ROS2 installation---\n"

locale  # check for UTF-8

sudo apt update && sudo apt install -y locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # verify settings

sudo apt install -y software-properties-common
sudo add-apt-repository universe

sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

sudo apt update
sudo apt upgrade

echo -e "\nInstalling base version:"
sudo apt install -y ros-humble-ros-base
pip install -U colcon-common-extensions
pip install -U colcon-argcomplete

# Adding auto complete to colcon
isInFile=$(cat ~/.bashrc | grep -c "source ~/.local/share/colcon_argcomplete/hook/colcon-argcomplete.bash")

if [ $isInFile -eq 0 ]; then
    echo -e "\nAdding source to /.bashrc:"
    echo "source ~/.local/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> ~/.bashrc
fi

echo -e "\nInstalling demo nodes (py and cpp):"
sudo apt-get install -y ros-humble-demo-nodes-py ros-humble-demo-nodes-cpp

isInFile=$(cat ~/.bashrc | grep -c "source /opt/ros/humble/setup.bash")

if [ $isInFile -eq 0 ]; then
    echo -e "\nAdding source to /.bashrc:"
    echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
fi

isInFile=$(cat ~/.bashrc | grep -c "export ROS_DOMAIN_ID")

if [ $isInFile -eq 0 ]; then
    echo -e "\nAdding ROS_DOMAIN_ID to /.bashrc:"
    echo "export ROS_DOMAIN_ID=30" >> ~/.bashrc
fi

source ~/.bashrc

echo -e "\nAdd email script to startup -->"
echo -e "sudo crontab -e"
echo -e "add “@reboot ~/TB3_RPI4_WS/scripts/ send_ip_2_email.py &”"