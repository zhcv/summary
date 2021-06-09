# Opencv install



查看version

```
pkg-config opencv --libs
```



### 1. install step

```
wget http: opencv && 
```

### 2. 创建编译目录(release)并进入：

```
mkdir build && cd build
```

### 3 cmake 

```
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_TBB=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_V4L=ON -D WITH_QT=ON -D WITH_OPENGL=ON ..
```

### 4 make

```
make -j$(nproc) // nproc是读取CPU的核心数量 
```

### 5 install

```
sudo make install
```

### 6  config env

```
sudo /bin/bash -c 'echo "/usr/local/lib" > /etc/ld.so.conf.d/opencv.conf'
```

### 7 updata pkg

```
sudo ldconfig
```

### config bash

```
sudo vim /etc/bash.bashrc 

export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig

sudo source /etc/bash.bashrc
```

```
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=../output \
-D CMAKE_C_COMPILER=/opt/hisi-linux/x86-arm/arm-himix200-linux/host_bin/arm-linux-gnueabi-gcc \
-D CMAKE_CXX_COMPILER=/opt/hisi-linux/x86-arm/arm-himix200-linux/host_bin/arm-linux-gnueabi-g++ \
-D CMAKE_EXE_LINKER_FLAGS=-lpthread -lrt -ldl \
-D BUILD_SHARED_LIBS=ON \
-D BUILD_ZLIB=ON \
-D ZLIB_INCLUDE_DIR=../3rdparty/zlib \
../

```





