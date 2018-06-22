#!/bin/bash
string="hello,shell,haha"
OLD_IFS="$IFS"
IFS=","
array=($string)
IFS="$OLD_IFS"
for var in ${array[@]}
do
   echo $var
done


array=(${string//,/ })  
for var in ${array[@]}
do
   echo $var
done
