import os
import cv2
import numpy as np
from pyblur import *
from PIL import Image
import random


root_dir = '/data/qa/dataset_qa/training2/0'
save_dir = '/data/qa/dataset_qa/training2/0'

file_list = os.listdir(root_dir)

nt = 1

for filename in file_list:
    _filename = os.path.join(root_dir, filename)
    im = Image.open(os.path.join(root_dir, filename))
    cnt = random.choice([1,2,3,4,5])
    if cnt == 1:    # Gaussian blur blurs image using gaussian kernel
        _name = filename[:-4] + '_gb' + '.jpg'
        new_name = os.path.join(save_dir, _name)
        img = GaussianBlur(im, 5)
        img.save(_filename)
    elif cnt == 2:  # Defocus blur blurs image using disk kernel
        _name = filename[:-4] + '_df' + '.jpg'
        new_name = os.path.join(save_dir, _name)
        img = DefocusBlur(im, 7)
        img.save(_filename)
    elif cnt == 3:   # Box blur blurs image using box kernel
        _name = filename[:-4] + '_bb' + '.jpg'
        new_name = os.path.join(save_dir, _name)
        img = BoxBlur(im, 5)
        img.save(_filename)
    elif cnt == 4: # average blur blurs image with box
        _name = filename[:-4] + '_ab' + '.jpg'
        new_name = os.path.join(save_dir, _name)
        arr = np.array(im)
        avgimg = cv2.blur(arr, (10, 10))
        cv2.imwrite(_filename, avgimg)

    else:  # motion blur blurs image with kernel_motion_blur
        _name = filename[:-4] + '_mb' + '.jpg'
        new_name = os.path.join(save_dir, _name)
        img = np.array(im)
        size = 15

        # generating the kernel
        kernel_motion_blur = np.zeros((size, size))
        kernel_motion_blur[int((size - 1) / 2), :] = np.ones(size)
        kernel_motion_blur = kernel_motion_blur / size

        # applying the kernel to the input image
        output = cv2.filter2D(img, -1, kernel_motion_blur)
        cv2.imwrite(_filename, output)
    print filename, ' ', nt
    nt += 1
