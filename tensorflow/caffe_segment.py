#!/usr/bin/env python
# -*- coding:utf-8 -*

import sys
# sys.path.append('/home/zhp/caffe/python')

import numpy as np
from PIL import Image
import cv2
from scipy import io
import numpy as np
import os

import caffe


caffe.set_device(2)
caffe.set_mode_gpu()

# load image, switch to BGR, subtract mean, and make dims C x H x W for Caffe
"""
with open('/home/zhp/fenge/test.txt','r') as f:
    imgs_list = [l.strip() for l in f.readlines()]

# load net
net = caffe.Net('deploy.prototxt', './train_iter_10000.caffemodel', caffe.TEST)
for infile in imgs_list:
  if infile:
    imgname = infile + '.jpg'
    im = Image.open(os.path.join('/home/zhp/fenge/jpg', imgname))
    in_ = np.array(im, dtype=np.float32)
    in_ = in_[:,:,::-1]
    in_ -= np.array((104.00698793,116.66876762,122.67891434))
    imgt = in_.transpose((2,0,1))
"""

test_batch = 5
test_img_path = '/home/zhp/dataset/fenge/xp_data/test_file'
imglist=os.listdir(test_img_path)

# load net
net = caffe.Net('deploy.prototxt','./fenge_train97/fenge_train_iter_54000.caffemodel', caffe.TEST)

def segment(img_name_list):
    assert len(img_name_list) == test_batch
    data_in=[]
    for i in range(test_batch):  # len(img_name_list)):
        im_sequence = img_name_list[i]
        im = Image.open(os.path.join(test_img_path,im_sequence))
        im=im.resize((1024,1024),Image.ANTIALIAS)
        im=im.convert('RGB')
        in_ = np.array(im, dtype=np.float32)
        in_ = in_[:,:,::-1]
        in_ -= np.array((104.00698793,116.66876762,122.67891434))
        in_ = in_.transpose((2,0,1))
        #print 'in.shape',in_.shape
        if len(data_in)==0:
            data_in=in_
            data_in=data_in.reshape(1,*data_in.shape)
        else:
            data_in=np.vstack((data_in,in_.reshape(1,*in_.shape)))
    #shape for input (data blob is N x C x H x W), set data
    #net.blobs['data'].reshape(1, *in_.shape)
    #net.blobs['data'].data[...] = in_
    net.blobs['data'].data[...] = data_in
    #print '''net.blobs['data'].shape''',net.blobs['data'].data.shape
    # run net and take argmax for prediction
    net.forward()
    for i in range(test_batch):
        out = net.blobs['score_sem'].data[i].argmax(axis=0)
        #print out
        #out=out*19
        #imgray=im.convert('L')
        #gray_arr=np.asarray(imgray)
        #cv2.imwrite(os.path.join('/home/zhp/dataset/fenge/xp_data/fenge_label',img_name_list[i]),out)
        img_new_name = '/home/zhp/dataset/fenge/xp_data/fenge_mat/'+img_name_list[i][:-3]+'mat'
        io.savemat(img_new_name, {img_new_name[:-4]: mat})
 # np.hstack((out,gray_arr)))

for i in range(len(imglist)/test_batch):
    fenge(imglist[i*test_batch:i*test_batch+test_batch])
if len(imglist)%test_batch !=0:
    img_names=imglist[len(imglist)/test_batch*test_batch:len(imglist)]
    for i in range(test_batch-len(img_names)):
        img_names.append(imglist[-1])
    fenge(img_names)
