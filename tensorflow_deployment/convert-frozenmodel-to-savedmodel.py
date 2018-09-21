import tensorflow as tf
from tensorflow.python.saved_model import signature_constants
from tensorflow.python.saved_model import tag_constants

export_dir = './graph/saved_model/0001' #this dir can't exist or tf will bitch
graph_pb = 'checkpoints/frozen_model.pb'

builder = tf.saved_model.builder.SavedModelBuilder(export_dir)

with tf.gfile.GFile(graph_pb, "rb") as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())

sigs = {}

with tf.Session(graph=tf.Graph()) as sess:
    tf.import_graph_def(
        graph_def,
        input_map=None,
        return_elements=None,
        op_dict=None,
        name="",
        producer_op_list=None
    )

    g = tf.get_default_graph()

    builder.add_meta_graph_and_variables(
        sess,
        ["serve"],
        signature_def_map={
            'serving_default': tf.saved_model.signature_def_utils.predict_signature_def(
                {'input': g.get_tensor_by_name('input_image_as_bytes:0')},
                {
                    'prediction': g.get_tensor_by_name('prediction:0'),
                    'probability': g.get_tensor_by_name('probability:0')
                }
            ),
        },
        clear_devices=True
    )

builder.save()
