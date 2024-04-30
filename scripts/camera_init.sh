# Adding usb_cam config param file
isExFile=$(ls ~/.ros/camera_info/ | grep -c "params.yaml")
if [ $isExFile -eq 0 ]; then
    echo -e "\nCoping params.yaml to ~/.ros/camera_info/"
	mkdir ~/.ros/camera_info
	cp ~/TB3_RPI4_WS/src/usb_cam/config/params.yaml ~/.ros/camera_info/
fi