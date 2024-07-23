<!-- https://github.com/Talzoor/TB3_RPI4_WS -->
# :desktop_computer: General settings :desktop_computer:

## router settings

### router

**user:** `admin`

**pass:** `zxcvb123`

### Wifi

**Wifi:** `TurtleBotWIFI` or `TBWIFI_open`

**pass:** `zxcvb123`


# :robot: TB3_RPI4_WS :robot:

RPI4 workspace, ros2 humble

located at ~/TB3_RPI4_WS/

## ssh connection

connect to Wifi: **TurtleBotWifi**

```bash
ssh t-pi@192.168.0.2
```

## rebuild ros workspace

```bash
cd ~/TB3_RPI4_WS
#rm -r build install log 		# if you wish to clean before building from scratch
colcon build --parallel-workers 2 	# can take ~20min for clean build, rpi has 4 cores, using only 2 will allow ssh and such
source ~/.bashrc    # somtimes needed
```

## github push

```bash  
cd ~/TB3_RPI4_WS
git add *
git commit -m "commit message"
git push
```

or copy as one line:

```bash
cd ~/TB3_RPI4_WS; git add *; git commit -m "commit message"; git push
```

## check turtlebot <--> pc, ros connection

### TB3

```bash
ros2 launch turtlebot3_bringup robot.launch.py 
```

### PC
```bash
ros2 run turtlebot3_teleop teleop_keyboard
```

## run image stream

### TB3
first give Ubuntu permission to open _/dev/video0_ port
```bash
sudo chmod 777 /dev/video0
```

and run streaming service
```bash
ros2 run usb_cam usb_cam_node_exe --ros-args --params-file ~/.ros/camera_info/params.yaml
```

### PC
```bash
ros2 run web_video_server web_video_server
```

## Test algorithem [ORB-SLAM2](https://github.com/raulmur/ORB_SLAM2)


### TB3

clone [Pangolin](https://github.com/stevenlovegrove/Pangolin)
```bash
git clone --recursive https://github.com/stevenlovegrove/Pangolin.git
```
install dependencies
```bash
./scripts/install_prerequisites.sh --dry-run recommended
```
build with Ninja for faster builds
```bash
sudo apt install ninja-build

 cmake -B build -GNinja
cmake --build build

```

### PC
```bash
ros2 
```

