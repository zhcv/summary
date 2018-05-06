"""Import a graph_def ProtoBuf first

Load this graph_def into a actual Graph
"""

import tensorflow as tf


def load_graph(frozen_graph_filename):
    """
    load the protobuf file and retrieve the unserialized graph_def
    """
    with tf.gfile.GFile(frozen_graph_filename, "rb") as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())

    # Import the graph_def into a new Graph and returns it 
    with tf.Graph().as_default() as graph:
        # The name var will prefix every op/nodes in your graph
        # Since load everything in a new graph, this is not needed
        tf.import_graph_def(graph_def, name="prefix")
    return graph
