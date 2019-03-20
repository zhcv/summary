import tensorflow as tf

m1 = tf.constant([[2, 2]])
m2 = tf.constant([[3], [3]])


ops = tf.matmul(m1, m2)

print "=" * 45
print "ops.name", ops.name
print "ops.shape", ops.shape.as_list()
print "=" * 45

with tf.Session() as sess:
    print sess.run(tf.squeeze(ops))
