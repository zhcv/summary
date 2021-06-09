### 海思的三个内存关系(MMZ,OSMEM,RAM)

OSMEM：就是我们的操作系统所用的内存，通过free可以看见

MMZ（Media Memory Zone）：此内存是供海思的媒体业务模块使用的内存，常用在音视频编解码等地方。此内存是通过linux driver实现的，在驱动内部对OSMEM没有使用的RAM部分进行内存管理。

RAM：RAM=OSMEM+MMZ

下面是一个512MB内存板子的例子（来自于海思SDK）
DDR:

——————————————————————————————————

-----|-------|  0x80000000   # Memory managed by OS.              

64M  | OS    |                                                 

     |       |                                                 

-----|-------|  0x84000000   # Memory managed by MMZ block anonymous.          

448M | MMZ   |                                                 

     |       |                                                 

-----|-------|  0xA0000000   # Memory managed by MMZ block jpeg.      
——————————————————————————————————



### 内存调整

查看MMZ内存的使用情况：
命令：cat /proc/media-mem
—MMZ_USE_INFO:
total size=159744KB(156MB),used=15164KB(14MB + 828KB),remain=144580KB(141MB + 196KB),zone_number=1,block_number=45

从这里的情况来看，mmz大概只用了15M的样子，剩余了141M的样子，造成了极大的浪费，考虑到后续对MMZ的一些需求，我这里将MMZ大小调整为26M的样子，做一定的预留。然后OSMEM扩展到230MB（以前是100MB）。然后在对我们的程序里面的使用的内存进行仔细的调整和优化（能用1byte不用2byte，此时内存依然很紧张啊，跑的东西太多了），达到了项目部署要求，不用更换硬件，造成项目成本上升。（注意，MMZ内存占用情况会根据你使用的实际内容改变，比如：流的路数、分辨率、采样率等可能会改变MMZ的占用内存大小，一般板子起来后，用上文的命令查看实际的占用情况，根据实际占用预留一部分内存，然后根据RAM大小来计算即可。）
现在的MMZ使用情况：
—MMZ_USE_INFO:
total size=26624KB(26MB),used=15164KB(14MB + 828KB),remain=11460KB(11MB + 196KB),zone_number=1,block_number=45

现在的内存示意图：
————————————————

-----|-------|  0x8000 0000   # Memory managed by OS.              

230M  | OS    |                                                 

     |       |                                                 

-----|-------|  0x8E60 0000   # Memory managed by MMZ block anonymous.          

26M | MMZ   |                                                 

     |       |                                                 

-----|-------|  0x90000000   # Memory managed by MMZ block jpeg.  