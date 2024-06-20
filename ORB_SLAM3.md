<!-- https://github.com/Talzoor/TB3_RPI4_WS -->
# :desktop_computer: ORB_SLAM3 installation steps :desktop_computer:

[Github page](https://github.com/UZ-SLAMLab/ORB_SLAM3?tab=readme-ov-file)

## TODO

13/06/2024

--> need to 

## Install Prerequisites

### [Homebrew](https://brew.sh/)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

```bash
# Homebrew "Next steps"
(echo; echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"') >> /root/.bashrc
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"

# run 'sudo' if available
# sudo apt-get install build-essential
apt-get install build-essential
brew install gcc
```

### [Pangolin](https://github.com/stevenlovegrove/Pangolin)

#### Download code

```bash
cd /
git clone --recursive https://github.com/stevenlovegrove/Pangolin.git
```

#### Dependencies

```bash
cd Pangolin/
# Override the package manager choice and install all packages
./scripts/install_prerequisites.sh -m brew all
```

#### Fix error message - Could NOT find OpenGL (missing: OPENGL_opengl_LIBRARY)

open file "Pangolin/components/pango_opengl/CMakeLists.txt"

add line:
```cmake
set(OPENGL_opengl_LIBRARY "${OPENGL_gl_LIBRARY}") # after line 48: set(OpenGL_GL_PREFERENCE "GLVND")
```

#### Fix epoxy - Could NOT find epoxy (missing: epoxy_LIBRARIES epoxy_INCLUDE_DIRS)

try:
```bash
apt-get install -y libepoxy-dev
```

or check [URL](https://stackoverflow.com/a/78586150)


