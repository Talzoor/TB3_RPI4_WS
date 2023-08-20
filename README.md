# TB3_RPI4_WS

RPI4 workspace, ros2 humble

located at ~/TB3_RPI4_WS/

to rebuild it:

	cd ~/TB3_RPI4_WS
	#rm -r build install log 		# if you wish to clean before building from scratch
	colcon build --parallel-workers 2 	# can take ~20min for clean build, rpi has 4 cores, using only 2 will allow ssh and such

github push:

	cd ~/TB3_RPI4_WS
	git add *
	git commit -m "commit message"
	git push

or copy as one line:

	cd ~/TB3_RPI4_WS; git add *; git commit -m "commit message"; git push

