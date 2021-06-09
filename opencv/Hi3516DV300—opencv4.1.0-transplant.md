### Hi3516DV300—opencv4.1.0移植

1. 安装Hi3516DV300编译环境

   ```
   参考海思自带手册安装即可（我这里安装的是arm-himix200-linux工具链）
   ```

1. 下载OpenCV源码

  ```
  登录https://opencv.org/releases/，选择相应的版本进行下载。使用的版本是Open CV - 4.1.0
  ```

2. 编译前的准备工作

  2.1 如果是git clone下载的，直接进入到OpenCV源码根目录；如果下载的是zip文件，则需要先运行unzip opencv-4.1.10.zip命令解压，之后再进入到源码根目录；

  2.2 建立build文件夹和output文件夹，命令如下：

  ```
  $mkdir build
  $mkdir output
  ```

  2. 3建立build文件夹和output文件夹，命令如下：

     ```
     $cd build
     ```

3. 编译
    3.1修改源码根目录的CMakeLists.txt

  ```
  在657行ocv_include_directories(${OPENCV_CONFIG_FILE_INCLUDE_DIR})的下边添加一行内容：
  ocv_include_directories(./3rdparty/zlib/)
  ```

  3.2 如果缺少zlib库请执行以下命令

  ```
  sudo apt-get install zlib1g-dev
  ```

  3.3 使用camke进行编译

  

  

  ```cmake -D CMAKE_BUILD_TYPE=RELEASE \
  -D CMAKE_INSTALL_PREFIX=../output \
  -D CMAKE_C_COMPILER=/opt/hisi-linux/x86-arm/arm-himix200-linux/host_bin/arm-linux-gnueabi-gcc \
  -D CMAKE_CXX_COMPILER=/opt/hisi-linux/x86-arm/arm-himix200-linux/host_bin/arm-linux-gnueabi-g++ \
  -D CMAKE_EXE_LINKER_FLAGS=-lpthread -lrt -ldl \
  -D BUILD_SHARED_LIBS=ON \
  -D BUILD_ZLIB=ON \
  -D ZLIB_INCLUDE_DIR=../3rdparty/zlib \
  ../
  
  3.4 CMake完成后，执行make命令
  $ make
  $ make install
  
  3.5 最终在{OpenCV 源码根目录}/output下生成了以下内容:
  ```

至此，OpenCV在Hi3516DV300的移植任务圆满结束.

4. #### 在项目中引用opencv动态库
    4.1 在makefile文件中，加入下面内容

  ```
  #调用opencv编译生成的库文件
  CFLAGS += `pkg-config --cflags  --libs opencv`
  #设置编译器
  CC = arm-himix200-linux-g++
  
  4.2 安装pkg-config
  sudo apt install pkg-config
  1
  4.3 设置opencv的pc文件的环境变量
  vim ~/.bashrc
  加入export  PKG_CONFIG_PATH="/home/zdst/opencv/output/lib/pkgconfig"
  ```

  原文链接：https://blog.csdn.net/alipy/article/details/102575297



### Hi3516DV300 主要特性

#### 1）处理器内核

•双核 ARM Cortex A7@900MHz，32KB I-Cache， 32KB D-Cache /256KB L2 cache
• 支持 Neon 加速，集成 FPU 处理单元

####  2）智能视频分析

• 集成智能计算加速引擎（含跟踪、人脸校正）
• 1.0Tops神经网络运算性能

#### 3）ISP与图像处理

• 支持 3A（AE/AWB/AF）功能，支持第三方3A算法
• 支持两帧曝光 WDR 及 Local Tone Mapping，支持强光抑制、背光补偿
• 支持坏点校正、镜头阴影校正
• 支持多级 3D 去噪，动态对比度增强、色彩管理；视频、图形输出抗闪烁处理
• 支持区域自适应去雾
• 支持 6-Dof 数字防抖
• 支持最大 8 个区域的编码前处理 OSD 叠加

#### 4）编解码

• H.265/H.264 编解码最大分辨率：26881944
• 26881536@30fps + 720480@30fps + 360240@30fps 编码，
26881944@20fps + 720480@20fps + 360240@20fps 编码，
19201080@30fps + 720480@30fps 编码 + 19201080@30fps 解码，
• 支持JPEG抓拍16M(46083456) @10fps
• 输出码率最大50Mbps

#### 5）视频输入

• 最大输入分辨率26881944
• 支持BT.656、BT.1120视频输入接口
• Sensor串行输入支持2路视频输入，支持1x4Lane/2x2Lane

##### 1.2.2 核心板硬件资源、规格

SoC HI3516DV300
Memory Flash £NAND £NOR ReMMC £1GB £2GB R4GB £8GB
RAM RDDR3 £DDR4 £LPDDR4 £512MB R1GB £2GB
LCD屏接口 1x40p 0.5mm FPC连接器，支持4lane mipi屏
CMOS接口 1x45p 0.5mm FPC连接器，最大支持22lane路视频输入
调试接口 4p 1.25mm wafer 连接器，用于系统调试
电源接口 2p 1.50mm wafer连接器
功能接口2 1x26p 0.5mm FPC连接器，支持USB2.0、SDIO0、I2C3、GPIO5、12V、5V
功能接口1 1x36p 0.5mm FPC连接器，支持SDIO1、audio、GPIO8、韦根、UART2
网络接口 4p 1.25mm wafer 连接器，用于网络线预留
RTC RInternal RTC £External RTC
固件加密 RSupport £ Not support
温度传感器 £NTC resistor RNot support
看门狗 RInternal £External
板型尺寸 5050mm
工作温度 -25℃≤SoC≤85℃；-30℃≤Memory≤85℃；-25℃≤PHY≤80℃
单板工作电压/功耗 12V±20% @ 1A；
电源端口EMS能力 EFT ： ±1kV/5KHz surge：±0.5kV @ 1.2/50us（DM）
网络端口EMS能力 EFT ： ±1kV/5KHz surge：±1kV @ 10/700us （DM）

##### 1.2.3 接口板硬件资源

红外灯板接口 6p 1.25mm wafer 连接器
CMOS接口 1x10p 0.5mm FPC连接器
触摸屏接口 1x45p 0.5mm FPC连接器
电源接口 2p 1.50mm wafer连接器
喇叭接口 2p 1.25mm wafer 连接器
复位按键接口 2p 1.25mm wafer 连接器
MIC接口 2p 1.25mm wafer 连接器
网络接口 8p 1.25mm wafer 连接器
通讯接口 11p 1.25mm wafer 连接器，包含韦根、232、485、报警输出
功能接口2 1x26p 0.5mm FPC连接器，支持USB2.0、SDIO0、I2C3、GPIO5、12V、5V
功能接口1 1x36p 0.5mm FPC连接器，支持SDIO1、audio、GPIO8、韦根、UART2
WiFi天线接口 I-PEX插座

实现功能 2.4G/5G WiFi
RS485、RS232、韦根通讯
Micro SD存储
白光补光灯driver
触摸屏driver
扬声器driver
MIC拾音、继电器输出