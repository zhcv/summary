import tensorflow as tf

a = tf.constant(2)
b = tf.constant(3)

x = tf.add(a, b)

with tf.Session() as sess:
    write = tf.summary.FileWriter('./grahps', sess.graph)
    print sess.run(x)

write.close()
