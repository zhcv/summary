#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################################################
"""Single Reader, Single Example
"""

import tensorflow as tf

# Generate a first-in, first-out queue QueueRunner
filenames = ['A.csv', 'B.csv', 'C.csv']
filename_queue = tf.train.string_input_producer(filenames, shuffle=False)
# 定义Reader
reader = tf.TextLineReader()
key, value = reader.read(filename_queue)
# 定义Decoder
example, label = tf.decode_csv(value, record_defaults=[['null'], ['null']])
# Run Graph
with tf.Session() as sess:
    sess.run(tf.local_variables_initializer())
    coord = tf.train.Coordinator()  # Create a coordinat
    # Start QueueRunner, the file name queue has been entered or to manage threads
    threads = tf.train.start_queue_runners(coord=coord) 
    for i in range(10):
        # When sampling, a Reader first reads out the file name from the file name queue 
        # and reads out the data, and the Decoder resolves into the sample queue.
        image = sess.run([example])
        # label = sess.run([label])
        print label.eval(),  ' ----> '
    coord.request_stop()
    coord.join(threads)
    


##############################################################################################################
"""Single Reader，muliti example """


# import tensorflow as tf
# filenames = ['A.csv', 'B.csv', 'C.csv']
# filename_queue = tf.train.string_input_producer(filenames, shuffle=False)
# reader = tf.TextLineReader()
# key, value = reader.read(filename_queue)
# example, label = tf.decode_csv(value, record_defaults=[['null'], ['null']])
# # 使用tf.train.batch()会多加了一个样本队列和一个QueueRunner。Decoder解后数据会进入这个队列，再批量出队。
# # 虽然这里只有一个Reader，但可以设置多线程，相应增加线程数会提高读取速度，但并不是线程越多越好。
# example_batch, label_batch = tf.train.batch(
#       [example, label], batch_size=5)
# with tf.Session() as sess:
#     coord = tf.train.Coordinator()
#     threads = tf.train.start_queue_runners(coord=coord)
#     for i in range(10):
#         print example_batch.eval()
#     coord.request_stop()
#     coord.join(threads)


###############################################################################################################
"""Multi-Reader，Multi-Example """
 
# import tensorflow as tf
# filenames = ['A.csv', 'B.csv', 'C.csv']
# filename_queue = tf.train.string_input_producer(filenames, shuffle=False)
# reader = tf.TextLineReader()
# key, value = reader.read(filename_queue)
# record_defaults = [['null'], ['null']]
# example_list = [tf.decode_csv(value, record_defaults=record_defaults)
#                   for _ in range(2)]  # Set Reader=2
# # with tf.train.batch_join()， can use multi-reader, Read data in parallel. Each Reader uses one thread.
# example_batch, label_batch = tf.train.batch_join(
#       example_list, batch_size=5)
# with tf.Session() as sess:
#     coord = tf.train.Coordinator()
#     threads = tf.train.start_queue_runners(coord=coord)
#     for i in range(10):
#         print example_batch.eval()
#     coord.request_stop()
#     coord.join(threads)


################################################################################################################
# Iteration Control 

# import tensorflow as tf
# filenames = ['A.csv', 'B.csv', 'C.csv']
# filenames = ['A.csv']
# filename_queue = tf.train.string_input_producer(filenames, 
#                                                 shuffle=False,
#                                                 num_epochs=16)  # num_epoch:set iteration No.
# reader = tf.TextLineReader()
# key, value = reader.read(filename_queue)
# record_defaults = [['null'], ['null']]
# example_list = [tf.decode_csv(value, record_defaults=record_defaults) for _ in range(2)]
# example_batch, label_batch = tf.train.batch_join(example_list, batch_size=5)
# init_local_op = tf.local_variables_initializer()
# with tf.Session() as sess:
#     sess.run(init_local_op)   # initializer local variable
#     coord = tf.train.Coordinator()
#     threads = tf.train.start_queue_runners(coord=coord)
#     try:
#         while not coord.should_stop():
#             print example_batch.eval(), ' ----> ', label_batch.eval()
#             # print example_batch.eval()
#     except tf.errors.OutOfRangeError:
#         print('Epochs Complete!')
#     finally:
#         coord.request_stop()
#     coord.join(threads)
#     coord.request_stop()
#     coord.join(threads)
# 
# 

#############################################################################################################
