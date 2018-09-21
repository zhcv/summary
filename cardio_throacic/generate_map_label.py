# -*- coding: utf-8 -*-
from PIL import Image
import os
import cv2
import numpy as np

imgPath = 'label_map'
src = 'imgs/1.2.156.14702.18.1.3.420180519221516014.20180519221517.png'

image = cv2.imread(src, 0)
imgr_name = os.path.basename(src)[:-4] + '_right_lung.png'
cardiac = image.copy()
"""
imgr = image.copy()
imgr[imgr != 13] = 0
cv2.imwrite(os.path.join(imgPath, imgr_name), imgr * 19)

imgl_name = os.path.basename(src)[:-4] + '_left_lung.png'
imgl = image.copy()
imgl[imgl != 12] = 0
cv2.imwrite(os.path.join(imgPath,imgl_name), imgl * 19)
"""

cardiac[cardiac != 9] = 0
cv2.imwrite('cardiac.png', cardiac * 19)

# save two lung label image
Image.fromarray(image * 19).save(os.path.join(imgPath, src[5:]))


