#!/usr/bin/env bash

filelist=/home/zhang/Desktop/dcmxinyingzd.txt
filepath=/home/zhang/Desktop/imgs/
savepath=/home/zhang/Desktop/imgs_jpg/
ext=.jpg
if [ ! -d $filepath ];then 
    mkdir -p $filepath
else
    echo "文件夹已存在"
fi

if [ ! -d $savepath ];then
    mkdir -p $savepath
else
    echo "文件夹已存在"
fi






for filename in `cat abc.txt`;do
#echo $filename;
FULLNAME=$filename
FILE=${FULLNAME##*/}
# echo $FILE;
#dirname "$i"
name=${FILE%.*}
#echo $name;
#name=${i##*/}
str=$savepath$name$ext
#echo ${str##.*};
# echo $savepath${name};
# echo $str;
/opt/dcm4che-5.10.5/bin/dcm2jpg $FULLNAME $str;
done


