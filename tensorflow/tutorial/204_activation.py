import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 400)  # x data, shape(100, 1)

# following are popular activation functions
y_relu = tf.nn.relu(x)
y_sigmoid = tf.nn.sigmoid(x)
y_tanh = tf.nn.tanh(x)
y_softplus = tf.nn.softplus(x)

# softmax is a special kind of activation fucntion, it is about probability 
y_softmax = tf.nn.softmax(x) 

sess = tf.Session()

y_relu_v, y_sigmoid_v, y_tanh_v, y_softplus_v = sess.run([y_relu, y_sigmoid, y_tanh, y_softplus])
y_softmax_v = tf.nn.softmax(x)

# plt to visualize these activation function
plt.figure(1, figsize=(8,6 ))
plt.subplot(221)
plt.plot(x, y_relu_v, c='red', label='relu')
plt.ylim((-1, 5))
plt.legend(loc='best')

plt.subplot(222)
plt.plot(x, y_sigmoid_v, c='red', label='sigmoid')
plt.ylim((-0.2, 1.2))
plt.legend(loc='best')

plt.subplot(223)
plt.plot(x, y_tanh_v, c='red', label='tanh')
plt.ylim((-1.2, 1.2))
plt.legend(loc='best')

plt.subplot(224)
plt.plot(x, y_softplus_v, c='red', label='softplus')
plt.ylim((-0.2, 6))
plt.legend(loc='best')

plt.show()
