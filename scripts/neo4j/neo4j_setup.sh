#!/bin/bash

# Script to install and set up Neo4j on a Unix-like system

echo "Starting Neo4j installation..."

# Define Neo4j version
NEO4J_VERSION="5.13.0"
NEOSEMANTIC_VERISON="5.11.0.0"


# Update package lists
echo "Updating package lists..."
sudo apt-get update
sudo apt install openjdk-17-jdk python3.8-venv python3-pip

# Check if Java is installed
echo "Checking java is installed..."

if type -p java; then
    echo "Java is already installed."
    java -version
elif [ -n "$JAVA_HOME" ] && [ -x "$JAVA_HOME/bin/java" ];  then
    echo "Java found in JAVA_HOME."
    "$JAVA_HOME/bin/java" -version
else
    echo "Java is not installed. Installing Java..."
    sudo apt-get update
    sudo apt-get install default-jdk -y
    echo "Java installation completed."
fi

echo "Downloading Neo4j Community Edition..."
wget -O neo4j.tar.gz "https://neo4j.com/artifact.php?name=neo4j-community-$NEO4J_VERSION-unix.tar.gz"

# Extract Neo4j
echo "Extracting Neo4j..."
tar -xf neo4j.tar.gz

# Rename Neo4j directory
mv "neo4j-community-$NEO4J_VERSION" neo4j

# Change directory to neo4j
cd neo4j

# Installing Neosemantic 
RELEASE_URL="https://github.com/neo4j-labs/neosemantics/releases/download/$NEOSEMANTIC_VERISON/neosemantics-$NEOSEMANTIC_VERISON.jar"
OUTPUT_FILE="neosemantics-$NEOSEMANTIC_VERISON.jar"

echo "Downloading Neosemantic..."
curl -L -o "$OUTPUT_FILE" "$RELEASE_URL"

echo "Download Neosemantic successfully..."

# Move extension into correct directory
mv "$OUTPUT_FILE" plugins

# Append neosemantic config into conf file
echo "dbms.unmanaged_extension_classes=n10s.endpoint=/rdf" >> conf/neo4j.conf

# Clean after installation
rm ../neo4j.tar.gz

echo "installation package is been cleaned..."

echo "Neo4j installation and setup completed."