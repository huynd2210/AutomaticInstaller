#!/bin/bash

# Add the Azul scoop bucket
scoop bucket add java

# Install Zulu 8
scoop install openjdk

echo %PATH%

# Verify that Java is installed and check the version
java -version
