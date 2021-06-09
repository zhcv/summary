**caffe*** 下将数据转为lmdb格式，这个教程写得很详细,其可选参数设置:
**convert_imageset**是Caffe提供的图像转换工具，用于将训练图像集和验证图像集转换成Caffe方便处理的lmdb或leveldb的数据集。
应用方法：
该工具通过命令行方式使用，命令行的格式如下：

```
convert_imageset [FLAGS] ROOTFOLDER/ LISTFILE DB_NAME
```

其中DB_NAME后面还可以跟一些可选的参数设置，具体有哪些可选的参数参见“可选参数设置部分”
其中ROOTFOLDER为图像集的根目录
LISTFILE 为一个文件的路径，该文件中记录了图像集中的各图样的路径和相应的标注
DB_NAME为要生成的数据库的名字

```
举个例子：
convert_imageset ImgSetRootDir/ ImgFileList.txt imgSet.lmdb
其中ImgFileList.txt（也即LISTFILE）的没一行给出一个图像的信息，如：subfolder1/file1.JPEG 7
其中subfolder1/file1.JPEG为图像路径，7为该图像的类别，并且中间空一个空格
```



可选参数设置
**gray**：bool类型，默认为false，如果设置为true，则代表将图像当做灰度图像来处理，否则当做彩色图像来处理
**shuffle**：bool类型，默认为false，如果设置为true，则代表将图像集中的图像的顺序随机打乱
**backend**：string类型，可取的值的集合为{“lmdb”, “leveldb”}，默认为”lmdb”，代表采用何种形式来存储转换后的数据
**resize_width**：int32的类型，默认值为0，如果为非0值，则代表图像的宽度将被resize成resize_width
**resize_height**：int32的类型，默认值为0，如果为非0值，则代表图像的高度将被resize成resize_height
**check_size**：bool类型，默认值为false，如果该值为true，则在处理数据的时候将检查每一条数据的大小是否相同
**encoded**：bool类型，默认值为false，如果为true，代表将存储编码后的图像，具体采用的编码方式由参数encode_type指定
**encode_type**：string类型，默认值为”“，用于指定用何种编码方式存储编码后的图像，取值为编码方式的后缀（如’png’,’jpg’,…)

```
带参数的命令：
convert_imageset ImgSetRootDir/ ImgFileList.txt imgSet.lmdb --gray=true --resize_width=160 --resize_height=160
```

今天在看caffe的代码，发现所用到的的数据都是leveldb的格式，而如果我们要是有形如imagenet的图片和标签的数据的话，就需要将他们给转化成leveldb的格式，caffe的代码中给了例子，在create_imagenet.sh 中，而这个shell文件主要就是调用了build/tools/convert_imageset.bin

举个例子

```
GLOG_logtostderr=1
$TOOLS=""

$TOOLS/convert_imageset \
	$TRAIN_DATA_ROOT \
	$DATA/train.txt \
	ilsvrc12_train_lmdb 1 \
	$RESIZE_HEIGHT $RESIZE_WIDTH
```

其TRAIN_DATA_ROOT，就是图片的路径， $DATA/train.txt，里面存放的是图片的名字，和图片的label（注意，这里的label应当从0开始编号，而且要连续，例如有20个类就是0到19，而不要0-10，12-20，这样会出错的）， ilsvrc12_train_leveldb 输出名， 1（乱序读取， 0 顺序读取）， 后面是图片归一化的大小，应为整数，为0表示不缩放
