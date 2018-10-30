"""Reference
https://github.com/antonilo/TensBlur
"""

import numpy as np
import tensorflow as tf

from PIL import Image
from smoother import Smoother

tf.app.flags.DEFINE_string('image_path', './Colosseum_in_Rome,_Itay_-_April_2007.jpg',
    'Path to the image to blur.')

FLAGS = tf.app.flags.FLAGS

SIGMA = 2.0
FILTER_SIZE = 13

def smooth():
    input_image = tf.placeholder(tf.float32, shape=[1, None, None, 3])
    smoother = Smoother({'data': input_image}, FILTER_SIZE, SIGMA)
    smoothed_image = smoother.get_output()

    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)
        image = Image.open(FLAGS.image_path)
        image = np.array(image, dtype=np.float32)
        image = image.reshape((1, image.shape[0], image.shape[1], 1))
        smoothed = sess.run(smoothed_image, 
            feed_dict={image_input: image})
        smoothed = smoothed / np.max(smoothed)

        out_image = np.squeeze(smoothed)
        out_image = Image.fromarray(np.squeeze(np.uint8(out_image * 255)))

def main(_):
    smooth()

if __name__ == '__main__':
    tf.app.rum()

