#!/usr/bin/env bash

dcmpath="/data3/tb/dcm/xinjiang/"
jpgpath="/home/zhp/xinjiang_jpg/"

function copy_dir_structure()
{
    for i in `find $dcmpath -type d`
	do 
	    mkdir -p ${i/$dcmpath/$jpgpath}
	done
}

# make same directory structure with raw directory
copy_dir_structure


for filename in `find $dcmpath -name "*.dcm"`
    do
        # temp=`echo ${filename#*xinjiang/} | awk '{print i$0}' i=$jpgpath`
        temp=${filename/$dcmpath/$jpgpath}
        jname=`echo ${temp%.*}.jpg`
        # echo $filename

	# echo $filename;
    	# FULLNAME=$filepath$filename
    	# FILE=${FULLNAME##*/}
	# echo $FILE;
	# dirname "$i"
    	# name=${FILE%.*}
	# name=${i##*/}
    	# str=$savepath$name$ext
	# echo ${str##.*};
	# echo $savepath${name};
	# echo $str;
	/home/jiufeng/dcm4che-5.10.5/bin/dcm2jpg $filename $jname; 
    done


