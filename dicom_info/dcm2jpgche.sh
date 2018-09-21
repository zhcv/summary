#!/usr/bin/env bash

filelist=/home/zhang/Desktop/dcmxinyingzd.txt
filepath=/data/dcms/
savepath=/home/zhang/Desktop/dcms_jpg2/
ext=.jpg

for filename in `ls $filepath`;do
#echo $filename;
FULLNAME=$filepath$filename
FILE=${FULLNAME##*/}
#echo $FILE;
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


