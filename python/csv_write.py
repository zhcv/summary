#coding: utf-8

import csv


with open('csv_test.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(['姓名', '年龄', '电话'])

    data = [
    
         ('小河',25,2343454),

         ('小芳',18,235365)

    ]

 
    writer.writerows(data)
