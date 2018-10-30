import tensorflow as tf
import tensorflow_hub as hub
import cv2
import numpy as np

module = hub.Module("https://tfhub.dev/google/imagenet/resnet_v2_101/feature_vector/1")
height, width = hub.get_expected_image_size(module)

print "height = %s, width = %s\n" % (height, width)
# A batch of images with shape [batch_size, height, width, 3].
images = cv2.imread('atc.png')
images = cv2.resize(images, (224,224), interpolation=cv2.INTER_LINEAR)  
images = np.expand_dims(images, 0)
# Features with shape [batch_size, num_features].
features = module(images) 
 
print features
