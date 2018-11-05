#!/usr/bin/env bash

<<!
mkdir /tmp/resnet
curl -s https://storage.googleapis.com/download.tensorflow.org/models/official/20181001_resnet/savedmodels/resnet_v2_fp32_savedmodel_NHWC_jpg.tar.gz \
| tar --strip-components=2 -C /tmp/resnet -xvz

 curl -o /tmp/resnet/resnet_client.py \
 https://raw.githubusercontent.com/tensorflow/serving/master/tensorflow_serving/example/resnet_client.py

ls /tmp/resnet
docker pull tensorflow/serving
!

docker run -p 8501:8501 \
    --name=tfserving_resnet \
    --mount type=bind,source=/tmp/resnet,target=/models/resnet \
    -e MODEL_NAME=resnet \
    -t tensorflow/serving &
