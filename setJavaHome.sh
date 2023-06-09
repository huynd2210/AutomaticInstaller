#!/bin/bash

# Check if Java is installed
if ! command -v java &> /dev/null
then
    echo "Java is not installed. Please install Java and try again."
    exit 1
fi

# Determine the location of the Java installation directory
# shellcheck disable=SC2046
JAVA_HOME=$(dirname $(dirname $(readlink -f $(which java))))

# Set the JAVA_HOME environment variable
export JAVA_HOME=$JAVA_HOME

# Print a message indicating that JAVA_HOME has been set
echo "JAVA_HOME has been set to $JAVA_HOME"
sleep 5