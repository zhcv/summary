# -*- coding: utf-8 -*-
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt


def measure_cardiac_transverse_diameter(img):
    """Cardiac transverse diameter measurement
    """
    img[img != 9] = 0
    kernel = np.ones((7, 7), np.uint8)
    # """
    img_erode = cv2.erode(img, kernel, iterations=5)
    closing = cv2.dilate(img_erode, kernel, iterations=5)
    
    # closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=3)
    # findContours function will change the imput image into another
    # find contours of all the components and holes
    image, contours, hierarchy = cv2.findContours(closing, cv2.RETR_TREE, 
                                                  cv2.CHAIN_APPROX_NONE)
    contours.sort(key=lambda x: x.shape[0], reverse=True)
    if contours and contours[0].shape > 500:
        # get max contours size's points
        points = contours[0]
        print "cardiac shape size", points.shape
        leftmost = tuple(points[:, 0][points[:, :, 0].argmin()])
        rightmost = tuple(points[:, 0][points[:, :, 0].argmax()])
        result = rightmost[0] - leftmost[0]
        print "leftmost", leftmost
        print "rightmost", rightmost
        print "Line:29 =======>>>", result
        if result > 100: return result
        else: return None
    else:
        return None


def measure_thoracic_transverse_diameter(img):
    """Thoracic transverse diameter measurement
    """
    img_left = img.copy()
    img[img != 13] = 0
    img_left[img_left != 12] = 0
    # lung region region
    img_temp = img + img_left
    
    kernel = np.ones((7, 7), np.uint8)
    closing = cv2.morphologyEx(img_temp, cv2.MORPH_CLOSE, kernel, iterations=3)          
    image, contours, hierarchy = cv2.findContours(closing, cv2.RETR_TREE,
                                                  cv2.CHAIN_APPROX_NONE)
    contours.sort(key=lambda x: x.shape[0], reverse=True)
    print "Line:52 ======>>> contours length", len(contours) 
    # Extreme points on both sides of the thoracic
    if len(contours) >= 2 and contours[1].shape > 1000:
        p_max = contours[0]
        p_max_left = tuple(p_max[:, 0][p_max[:, :, 0].argmin()])
        p_max_right = tuple(p_max[:, 0][p_max[:, :, 0].argmax()])
        print "=====>>> p_max_left", p_max_left
        print "=====>>> p_max_right", p_max_right

        p_min = contours[1]
        p_min_left = tuple(p_min[:, 0][p_min[:, :, 0].argmin()])
        p_min_right = tuple(p_min[:, 0][p_min[:, :, 0].argmax()])
        
        print "=====>>> p_min_left", p_min_left
        print "=====>>> p_min_right", p_min_right
        
        max_thorax_diameter = p_max_right[0] - p_max_left[0]
        min_thorax_diameter = p_min_right[0] - p_min_left[0]
        if max_thorax_diameter > 100 and min_thorax_diameter > 100:
            result = p_min_right[0] - p_max_left[0]
            print "Line:61 =======>>>", result
            if result < 0:
                result = p_max_right[0] - p_min_left[0]
                print "Line:64 =======>>>", result
            return result
        else: return None
    else:
        return None


def calculate_cardio_thoracic_proportion(image):
    """image: segmented label image
    return cardio-thoracic proportion
    """
    result = ''
    img = image.copy()
    cardiac_diameter = measure_cardiac_transverse_diameter(img)
    thoracic_diameter = measure_thoracic_transverse_diameter(image)
    if cardiac_diameter and thoracic_diameter:
        ratio = cardiac_diameter / float(thoracic_diameter)
        result = "%.2f" % ratio
    return result


if __name__ == '__main__':
    # src = 'cardio/ying_segment/1.2.156.14702.18.1.3.420180519221516014.20180519221517.png'
    src = 'cardio/ying_segment/1.2.156.14702.18.1.3.420180531223608921.20180531223614.png'
    image = cv2.imread(src, 0)
    ctr = calculate_cardio_thoracic_proportion(image)
    print ctr
