<!-- https://github.com/Talzoor/TB3_RPI4_WS -->
# :desktop_computer: Docker info :desktop_computer:

## TODO

02/06/2024
continue installing Prerequisites from ORB-SLAM3
(https://github.com/UZ-SLAMLab/ORB_SLAM3?tab=readme-ov-file)

--> need to start with "Pangolin"

## define display with permission

```bash
xhost +local:docker
```

## run image

```bash
docker run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -p 5000:5000 -p 8888:8888 -it talzzz/my_img_24_05_29 /bin/bash
```

## test if display is on (thru Docker)


```bash
feh /root/demo/python/result_Landmarks.jpg
```

make sure to write in docker

```bash
## will look like - 
root@DOCKER_IMG_REF:/# feh /root/demo/python/result_Landmarks.jpg
```

## save current state for image

```bash
docker commit f603476f7837 talzzz/my_img_24_05_29
#                   ˅                   ˅
#             my_container          my_image
```

## connect docker via SSH

### Creating img with Dockerfile

[Started from here](https://www.cherryservers.com/blog/ssh-into-docker-container)

```bash
mkdir ~/my_docker_img
cd ~/my_docker_img
nano Dockerfile
```

paste into file:

```bash
FROM ubuntu:16.04
RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
# Set root password for SSH access (change 'your_password' to your desired password)
RUN echo 'root:your_password' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
RUN yes 'y' | ssh-keygen -q -t rsa -f /etc/ssh/ssh_host_rsa_key -N ''
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
```

> [!IMPORTANT]
> Line 5: "your_password" should be change to ...
> 
> Line 7 was added - not in above url

Build image

```bash
sudo docker build -t talzzz/my_img_24_06_13 .
```

### Running docker container

```bash
docker run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -p 5000:5000 -p 8888:8888 -p 2222:22 --name my_latest_container -it talzzz/my_img_24_06_13:latest /bin/bash
```

> [!NOTE]  
> if still not working - need to add 'sshd' running on docker container (run on docker "root@486306ccaf17:/#")
> ```bash
> root@0baf48e12297:/# echo 'eval "$(/usr/sbin/sshd)"' >> /root/.bashrc
> ```

now - exit and run docker container again

### Find ip and connect

On Ubuntu terminal ->

```bash
sudo docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my_latest_container
```

```bash
ssh root@172.17.0.2
```

when finished, commit, and remove naming

```bash
docker commit my_latest_container talzzz/my_img_24_06_13
docker rm my_latest_container
```





