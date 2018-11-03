import glob 
import os
import cv2

# Loop through all jpg files in the current folder

for image_filename in glob.glob('data/*.jpg'):
    img = cv2.imread(image_filename)
    img = cv2.resize(img, (size, size))


# more fast method
from concurrent import futures

def load_and_resize(image_filename):
    img = cv2.imread(image_filename)
    img = cv2.imresize(img, (size, size))


# Create a pool of processes. By default, one is created
# for each CPU in the machine

with features.ProcessPoolExecutor(max_workers=None) as executor:
    # parameter max_works specify cpu number.
    # Get a list of files to process 
    image_files = glob.glob('data/*.jpg')
    # Process pool use all CPUs
    # Loop through all jpg files in the current folder
    executor.map(load_and_resize, image_files)



