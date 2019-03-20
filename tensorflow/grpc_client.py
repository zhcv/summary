import json
import os
from grpc.beta import implementations
import numpy as np
import tensorflow as tf
from PIL import Image
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2
from google.protobuf.json_format import MessageToJson
import cv2
tf.app.flags.DEFINE_string('server', 'localhost:8500',
                           'PredictionService host:port')
FLAGS = tf.app.flags.FLAGS


host, port = FLAGS.server.split(':')
channel = implementations.insecure_channel(host, int(port))
stub = prediction_service_pb2.beta_create_PredictionService_stub(channel)

# Send request
request = predict_pb2.PredictRequest()
request.model_spec.name = 'default'

# Generate test data
test_path='/home/zhp/img_seg/Semantic_Segmentation/data/data_road/testing/image_2'
test_list=os.listdir(test_path)
for fn in test_list[:1]:
    #img = Image.open(os.path.join(test_path,fn)).convert('RGB')
    keep_prob = 1.0
    print fn
    img = cv2.imread(os.path.join(test_path,fn))
    data = np.expand_dims(np.asarray(img, dtype='float32'), 0)
    feed_dict = {'x':data,'keep_prob':keep_prob}
    ## Send request
    ## request = predict_pb2.PredictRequest()
    ## request.model_spec.name = 'segment'
    
    # request.model_spec.version = model_version # 2 
    #for k,v in feed_dict.items():
    request.inputs['x'].CopyFrom(tf.contrib.util.make_tensor_proto(data,shape=[1,1024,1024,3]))
    request.inputs['keep_prob'].CopyFrom(tf.contrib.util.make_tensor_proto(keep_prob,shape=[1]))
    
    #request.inputs['x'].CopyFrom(tf.contrib.util.make_tensor_proto(data))
    #request.inputs['keep_prob'].CopyFrom(tf.contrib.util.make_tensor_proto(keep_prob))

    result = stub.Predict(request, 10.0)  # 10 secs timeout
    jresult = json.loads(MessageToJson(result))
    #print jresult
    # outputs = jresult["outputs"]["y"]["floatVal"]
    # print outputs.index(max(outputs)),outputs

