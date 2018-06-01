#!/bin/bash

mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=RELEASE -DCMAKE_INSTALL_PREFIX=/usr/local 
make "-j$(nproc)"
make install
make clean
