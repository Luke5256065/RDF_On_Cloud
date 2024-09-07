#!/bin/bash

# Install Virtuoso Universal Server (Open Source) on Debian-based systems

# Update and install necessary tools
sudo apt-get update
sudo apt-get install -y git autoconf automake libtool flex bison gperf gawk m4 make openssl libssl-dev libncurses5 libreadline-dev

wget https://github.com/openlink/virtuoso-opensource/releases/download/v7.2.12/virtuoso-opensource.x86_64-generic_glibc25-linux-gnu.tar.gz

tar -xf virtuoso-opensource.x86_64-generic_glibc25-linux-gnu.tar.gz
mkdir results
mkdir data
mkdir query

touch results/result.csv
touch results/error.log
cd virtuoso-opensource
