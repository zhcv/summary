import tensorflow as tf
import numpy as np

tf.enable_eager_execution()
tfe=tf.contrib.eager
from math import  pi
def f(x):
    return tf.square(tf.sin(x))
assert f(pi/2).numpy()==1.0
sess=tf.Session()
grad_f=tfe.gradients_function(f)
print(grad_f(np.zeros(1))[0].numpy())
