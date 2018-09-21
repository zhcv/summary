#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import numpy as np
import tensorflow as tf

def load_graph(frozen_graph_filename):
    # load the protobuf file  and parse it to retrieve unserialized graph_def
    with tf.gfile.GFile(frozen_graph_filename, "rb") as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())

    # Import a graph_def into the current default Graph
    with tf.Graph().as_default() as graph:
        tf.import_graph_def(
            graph_def,
            input_map=None,
            return_elements=None,
            name="prefix",
            op_dict=None,
            producer_op_list=None
        )
    return graph

def getImage(path):
    with open(path, 'rb') as img_file:
        img = img_file.read()
    return img

frozen_model_filename = "checkpoints/frozen_model.pb"
graph = load_graph(frozen_model_filename)

def ocrImage(image):
    x = graph.get_tensor_by_name('prefix/input_image_as_bytes:0')
    y = graph.get_tensor_by_name('prefix/prediction:0')
    allProbs = graph.get_tensor_by_name('prefix/probability:0')

    img = getImage(image)

    with tf.Session(graph=graph) as sess:
        (y_out, probs_output) = sess.run([y,allProbs], feed_dict={
            x: [img]
        })
        # print(y_out)
        # print(allProbsToScore(probs_output))

        return {"predictions": [{
                "ocr": str(y_out),
                "confidence": probs_output
            }]
        };

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument("--frozen_model_filename", default="checkpoints_pruned/frozen_model.pb", type=str, help="Frozen model file to import")
    parser.add_argument("--image", default="dfbe0634-ad30-4073-bd56-82b3f5ea524c.jpg", type=str, help="Path to image")
    args = parser.parse_args()
    predictions = ocrImage(args.image)
    print(str(predictions))
