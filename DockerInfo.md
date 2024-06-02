<!-- https://github.com/Talzoor/TB3_RPI4_WS -->
# :desktop_computer: Docker info :desktop_computer:

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
root@DOCKER_IMG_REF:/# feh /root/demo/python/result_Landmarks.jpg
```