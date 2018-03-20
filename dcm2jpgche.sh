#!/usr/bin/env bash

filelist=/home/zhang/Desktop/dcm.txt
savepath=/home/zhang/Desktop/wado_jpg/
ext=.jpg

for i in `cat $filelist`;do
#echo $i;
len=${#i}
FILE=${i##*/}
#echo $FILE;
#dirname "$i"
name=${FILE%.*}
#echo $name;
#name=${i##*/}
str=$savepath$name$ext
#echo ${str##.*};
# echo $savepath${name};
#echo $str;
/home/zhang/dcm4che-5.10.5/bin/dcm2jpg $i $str;
done


