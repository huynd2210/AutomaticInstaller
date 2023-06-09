#!/bin/bash

# Set the path to your Maven installation directory
MAVEN_HOME=/path/to/maven

# Check if the MAVEN_HOME directory exists
if [ ! -d "$MAVEN_HOME" ]; then
  echo "Maven directory not found."
  exit 1
fi

# Add Maven bin directory to PATH
export PATH=$MAVEN_HOME/bin:$PATH

# Print a message indicating that Maven has been added to the PATH
echo "Maven has been added to your PATH."
