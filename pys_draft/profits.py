#!/usr/bin/env python


i = int(raw_input("Please input last month's profits: "))

arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]

bonus = 0

for idx in range(6):
    if  i > arr[idx]:
        bonus += (i-arr[idx]) * rat[idx]
        print (i - arr[idx]) * rat[idx]
        i = arr[idx]


print bonus
