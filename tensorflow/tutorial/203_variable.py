import tensorflow as tf


var = tf.Variable(0)

add_op = tf.add(var, 1)

print dir(add_op)

update_op = tf.assign(var, add_op)


with tf.Session() as sess:
    # once define variables, you have to initialize them by doing this
    sess.run(tf.global_variables_initializer())
    for _ in range(3):
        sess.run(update_op)
        print sess.run(var)
