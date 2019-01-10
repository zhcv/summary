#!/usr/bin/env bash

count=8   # total number of processes
paracount=5  # parallel degreen


size=$((${count}/${paracount}))

for((i=1;i<=${size};i++))
do
    for((j=1;j<=${paracount};j++))
    do {
        echo $j
        sleep $j
        }&
    done
    wait
done
wait

for((i=1; i<=$((${count}%${paracount}));i++))
do {
    echo $i
    sleep $j
    }&
done
wait

echo "done"
