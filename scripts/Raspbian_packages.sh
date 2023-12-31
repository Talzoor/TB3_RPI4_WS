#!/bin/bash

echo -e "Installing python3...\n"

sudo apt-get update
sudo apt-get install python3

isInFile=$(cat ~/.bash_aliases | grep -c "alias python=python3")

if [ $isInFile -eq 0 ]; then
    echo -e "\nAdding 'Python' alias"
    echo alias python=python3 >> ~/.bash_aliases
else
    echo -e "\nAlias exist, continue."
fi

source ~/.bashrc
echo -e "\nPython3 version:"
python3 --version

echo -e "\nInstall pip:"
sudo apt-get -y install python3-pip

sudo apt-get install -y net-tools
sudo apt-get install -y python3-gpiozero

echo -e "\nInstall git and credentials:"
sudo apt-get -y install git

wget "https://github.com/git-ecosystem/git-credential-manager/releases/download/v2.3.2/gcm-linux_amd64.2.3.2.deb" -O /tmp/gcmcore.deb
sudo dpkg -i /tmp/gcmcore.deb
git-credential-manager configure

sudo apt-get -y install gh

echo -e "\ngithub login:"
gh auth login