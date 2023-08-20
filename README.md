# TB3_RPI4_WS
RPI4 workspace, ros2 humble
located at ~/TB3_RPI4_WS/

to rebuild it:

	cd ~/TB3_RPI4_WS
	rm -r build install log 	# if you wish to clean before building from scratch
	colcon build			# can take ~20min for clean build

github push:

	cd ~/TB3_RPI4_WS
	git add *
	git commit -m "commit message"
	git push origin main
