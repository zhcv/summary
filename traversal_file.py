#coding:utf-8
import os
import sys

root = 'pdffdp'

if len(sys.argv) > 1:
    root = sys.argv[1]

def func(args,dire,fis): #回调函数的定义      
    for f in fis:      
        args[0].append(os.path.join(root, f))      
filelist=[]  
os.path.walk(root,func,(filelist,)) #遍历 

for i in filelist:
    print (i )
