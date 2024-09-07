#!/bin/bash

echo "Gstore installation"

# Install git 
echo "downloading git..."
sudo apt-get update
sudo apt-get install git

# prerequirements
echo "downloading required packaging..."
sudo apt-get install -y libjemalloc-dev

# clone repo from github
echo "Cloning gstore from github...."
git clone https://github.com/pkumod/gStore.git --depth=1
echo "Clone done"

# run make according to instruction on github
echo "starting install gstore here..."
cd gStore
sudo bash scripts/setup/setup_ubuntu.sh

make pre
make

echo "gStore installed successfully..."