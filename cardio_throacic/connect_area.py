import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

srcPath = 'abnormal_ctr'
dstPath = 'label_map'

# src = 'imgs/1.2.156.14702.18.1.3.420180519221516014.20180519221517.png'
imgs_list = os.listdir(srcPath)
# imgs_list = ['1.2.156.14702.18.1.3.420180520000629250.20180520000629.png']

for infile in imgs_list[:1]:
    print infile, " ---> ",
    src = os.path.join(srcPath, infile)
    dst = os.path.join(dstPath, infile)
    img = cv2.imread(src)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgr = gray.copy()
    imgr[imgr != 13] = 0

    imgl = gray.copy()
    imgl[imgl != 12] = 0

    gray_temp = imgr + imgl
    img_temp = gray_temp.copy()

    # #find contours of all the components and holes
    # gray_temp = gray.copy() #copy the gray image because function
    #                         #findContours will change the imput image into another
    _, contours, hierarchy = cv2.findContours(gray_temp, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #
    #show the contours of the imput image
    cnt = sorted(contours, key=lambda x: x.shape[0], reverse=True)[:2]
    pentagram = cnt[0]
    print pentagram[:, 0]
    print pentagram[:, :, 0].argmin()
    print pentagram[:,:, 0].argmax()

    img = img * 19

    leftmost = tuple(pentagram[:, 0][pentagram[:, :, 0].argmin()])
    rightmost = tuple(pentagram[:, 0][pentagram[:, :, 0].argmax()])
    print "leftmost", leftmost,
    print "rightmost", rightmost

    cv2.circle(img, leftmost, 12, (0, 255, 0), 15)
    cv2.circle(img, rightmost, 12, (0, 0, 255), 15)


    pentagram = cnt[1]
    print pentagram.shape



    leftmost = tuple(pentagram[:, 0][pentagram[:, :, 0].argmin()])
    rightmost = tuple(pentagram[:, 0][pentagram[:, :, 0].argmax()])
    print "leftmost", leftmost,
    print "rightmost", rightmost

    cv2.circle(img, leftmost, 12, (0, 255, 0), 15)
    cv2.circle(img, rightmost, 12, (0, 0, 255), 15)



    cv2.drawContours(img, cnt, -1, (255, 0 , 0), 3)
    cv2.imwrite(dst, img)

    # plt.figure('original image with contours'), plt.imshow(img, cmap='gray')





# #find the max area of all the contours and fill it with 0
# area = []
# for i in xrange(len(contours)):
#     area.append(cv2.contourArea(contours[i]))
#
# #area = sorted(area, reverse=True)
# max_idx = np.argmax(area)
# cv2.fillConvexPoly(img_temp, contours[max_idx], 0)
# #show image without max connect components
# # plt.figure('remove max connect com'), plt.imshow(img_temp, cmap='gray')
#
# plt.show()
