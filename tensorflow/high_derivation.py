# -*- coding: utf-8 -*-

import tensorflow as tf
tf.enable_eager_execution()

from math import pi
import numpy as np

tfe = tf.contrib.eager

def  f(x):
    return tf.square(tf.sin(x))
 
def grad(f):
    return lambda x:tfe.gradients_function(f)(x)[0]
 
x=tf.lin_space(-2*pi,2*pi,100)
# print(grad(f)(x).numpy())
x=x.numpy()
import matplotlib.pyplot as plt

plt.plot(x,f(x).numpy(),label="f")
plt.plot(x,grad(f)(x).numpy(),label="first derivative")#一阶导
plt.plot(x,grad(grad(f))(x).numpy(),label="second derivative")#二阶导
plt.plot(x,grad(grad(grad(f)))(x).numpy(),label="third derivative")#三阶导
plt.legend()
plt.show()
