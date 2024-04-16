TurtleBot3 RPI steps:

RPI image writer:	
ubuntu server 22.04.3 LTS (64 bit)
user: ubuntu/t-pi, pass: ubuntu  T12345678

connecting wifi networks –
	backup –
		sudo cp /etc/netplan/50-cloud-init.yaml /etc/netplan/original_50-cloud-init.yaml
	sudo nano /etc/netplan/50-cloud-init.yaml

	should look like –
		wifis:
        			wlan0:
            				access-points:
                				"YOUR-SSID-NAME":
                    					password: "YOUR-NETWORK-PASSWORD"
            				dhcp4: true

In order to connect BGU-WIFI, need desktop:
	Wifi over hotspot, TalSpot
	(https://phoenixnap.com/kb/how-to-install-a-gui-on-ubuntu)
	sudo apt install slim
	sudo apt install lxde

signup to BGU-WIFI and load webpage – bgu.ac.il

check ssh conection:
	find IP for RPI –
		ip a
	connect from PC –
		ssh ubuntu@IP
		pass: T12345678
	connect without password – (https://serverfault.com/questions/241588/how-to-automate-ssh-login-with-password)
		ssh-keygen -t rsa -b 2048
		ssh-copy-id ubuntu@IP
	set timezone –
		sudo timedatectl set-timezone Asia/Jerusalem
			
disable GUI desktop: (https://linuxconfig.org/how-to-disable-enable-gui-on-boot-in-ubuntu-20-04-focal-fossa-linux-desktop)
sudo systemctl set-default multi-user
gnome-session-quit
run GUI manually:
	sudo systemctl start slim

change ‘ubuntu’ hostname  TB3_RPI:	(https://www.cyberciti.biz/faq/ubuntu-change-hostname-command/)

gmail account to send IP at boot:	(https://gist.github.com/slayton/3913056)
	tal.turtlebot.mail@gmail.com
	Pass12345678!

Create synced folder via ssh:	(https://www.golinuxcloud.com/how-to-transfer-files-over-ssh-with-sshfs/)
	mkdir ~/remote_dir
	sudo apt install sshfs
	sshfs ubuntu@192.168.43.10:/home/ubuntu/remote_dir /home/tal/remote_dir



Copy script “send_ip_2_email.py” to /bin –
	sudo cp ~/scripts/send_ip_2_email.py /bin
	sudo chmod +x /bin/send_ip_2_email.py

Run this scipt at startup – (https://askubuntu.com/questions/814/how-to-run-scripts-on-start-up)
	sudo crontab -e
	add “@reboot /bin/ send_ip_2_email.py &”
	Check crontab script (https://superuser.com/questions/1549286/how-to-test-cron-reboot-entry) –
		sudo rm /var/run/crond.reboot 
sudo service cron restart
	
git passkey: # https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
	#create ssh key
	ssh-keygen -t ed25519 -C "tal.turtlebot.mail@gmail.com"
	#Adding your SSH key to the ssh-agent
	eval "$(ssh-agent -s)"
	ssh-add ~/.ssh/id_ed25519
	#show key
	cat ~/.ssh/id_ed25519.pub
	# add to github : https://github.com/settings/keys
	
git:
	# Clone git
	# if there is an error with CA certificates - set date
	# sudo date -s "$(wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d' ' -f5-8)Z"
	git clone https://github.com/Talzoor/TB3_RPI4_WS.git

	

Install Python  ROS:
	

ROS2 talking on the same network – (https://roboticsbackend.com/ros2-multiple-machines-including-raspberry-pi/)
	
	RPI:	
		export ROS_DOMAIN_ID=5
		source /opt/ros/humble/setup.bash
		ros2 run demo_nodes_cpp talker

	PC:	
		export ROS_DOMAIN_ID=30 #default TurtleBot ID
		source /opt/ros/humble/setup.bash
		ros2 run demo_nodes_cpp listener

