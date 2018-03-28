"""
import numpy as np
import cv2

mri_img = cv2.imread('617.jpg')

# normalization
mri_max = np.amax(mri_img)
mri_min = np.amin(mri_img)
mri_img = ((mri_img-mri_min)/(mri_max-mri_min))*255
mri_img = mri_img.astype('uint8')

r, c, h = mri_img.shape
for k in range(h):
    temp = mri_img[:,:,k]
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    img = clahe.apply(temp)
    cv2.imshow('mri', np.concatenate([temp,img], 1))
    cv2.waitKey(0)
"""
import SimpleITK as sitk
from PIL import Image
import pydicom
import numpy as np
import cv2

def loadFile(filename):
    ds = sitk.ReadImage(filename)
    img_array = sitk.GetArrayFromImage(ds)
    frame_num, width, height = img_array.shape
    return img_array, frame_num, width, height

def loadFileInformation(filename):
    information = {}
    ds = pydicom.read_file(filename)    
    information['PatientID'] = ds.PatientID
    information['PatientName'] = ds.PatientName
    information['PatientBirthDate'] = ds.PatientBirthDate
    information['PatientSex'] = ds.PatientSex
    information['StudyID'] = ds.StudyID
    information['StudyDate'] = ds.StudyDate
    information['StudyTime'] = ds.StudyTime
    information['InstitutionName'] = ds.InstitutionName
    information['Manufacturer'] = ds.Manufacturer
    information['NumberOfFrames'] = ds.NumberOfFrames    
    return information

def showImage(img_array, frame_num = 0):
    img_bitmap = Image.fromarray(img_array[frame_num])
    return img_bitmap

def limitedEqualize(img_array, limit = 4.0):
    img_array_list = []
    for img in img_array:
        clahe = cv2.createCLAHE(clipLimit = limit, tileGridSize = (8,8))
        img_array_list.append(clahe.apply(img))
        
    img_array_limited_equalized = np.array(img_array_list)
    return img_array_limited_equalized
