#coding:utf-8
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.contrib.session_bundle import exporter



def main():
    model_path = 'datasets/chest_seg/exp/train_on_trainval_set_mobilenetv2/train'
    # Tensorflow specific configuration
    config = tf.ConfigProto(allow_soft_placement=True)
    config.gpu_options.allow_growth = True
    sess = tf.Session(config=config)

    latest_checkpoint = tf.train.latest_checkpoint(model_path)
    if latest_checkpoint:
        print("Loading model checkpoint {} ...\n".format(latest_checkpoint))
        metagraph_file = latest_checkpoint + '.meta'
        saver = tf.train.import_meta_graph(metagraph_file)
        graph = tf.get_default_graph()
        input_graph_def = graph.as_graph_def()
        print input_graph_def
        saver.restore(sess, latest_checkpoint)
        print("Checkpoint loaded\n\n")
    else:
        print("No checkpoints available!\n\n")

    #graph = tf.get_default_graph()

    # vars = graph.get_operations()
    # vars = graph.get_name_scope()
    # vars = graph.get_all_collection_keys()
    cnt = 1
    # vars = tf.global_variables()
    for op in vars:
        print op
        cnt += 1




    # image_data = sess.graph.get_tensor_by_name('input/Placeholder:0')
    # softmax_tensor = sess.graph.get_tensor_by_name('output/Softmax:0')
    # argmax_tensor = sess.graph.get_tensor_by_name('output/ArgMax:0')
    #
    # model_exporter = exporter.Exporter(saver)
    # model_exporter.init(sess.graph.as_graph_def(),
    #                     named_graph_signatures={
    #                     'inputs' : exporter.generic_signature({'x': image_data}),
    #                     'outputs': exporter.generic_signature({'y': softmax_tensor})}
    #                     )
    #
    # model_exporter.export('serving_model', tf.constant(1), sess)


if __name__ == '__main__':
    main()
