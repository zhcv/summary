#!/usr/bin/env bash

src="/data3/tb/dcm/xinjiang/"
des="/home/zhp/xinjiang_jpg/"


# make same directory structure with raw directory
# rsync -avz --progress -f "+ */" -f "- *" $src $des 
rsync -av --include='*/' --exclude='*' $src $des

for dname in $src/*.dcm
    do
        temp=${dname/$src/$dsc}
        jname=`echo ${temp%.*}.jpg`
        # echo $jname

	    /home/jiufeng/dcm4che-5.10.5/bin/dcm2jpg $dname $jname; 
    done


