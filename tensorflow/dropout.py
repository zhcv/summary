import tensorflow as tf

tf.set_random_seed(1024)
dropout = tf.placeholder(tf.float32)
x = tf.Variable(tf.ones([10, 10]))
y = tf.nn.dropout(x, dropout)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print sess.run(y, feed_dict={dropout: .1})
