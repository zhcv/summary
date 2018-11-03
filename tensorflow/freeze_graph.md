# How to freeze a graph in Tensorflow
###  January 15, 2018 lipman Python, Tensorflow	


## Saving the structure
```
# "g" will be your Graph
g = sess.graph
# In my case, I use the default Graph
gdef = g.as_graph_def()
# Parameters: 1) graph, 2) directory where we want to save the pb file,
#             3) name of the file, 4) text format (True) or binary format.
tf.train.write_graph(gdef,".","graph.pb",False)
```
Note: if we save our graph as text, setting the boolean value to True, we can have a 
look at it with any text editor and see how it looks like. Since it uses Protocol Buffers it is 
easily readable.

## Saving the weights

We also call this the checkpoints. We have to get a Saver object and use it after the
network is trained so it will contained the weights obtained after the optimization.
```
# When defining the model
saver = tf.train.Saver()
# ....
# After the model is trained
saver.save(sess, 'tmp/my-weights')
```

## Freezing the Graph

Now it’s time to combine both files. We can see the commands in the original tutorial in github.

Since I didn’t want to mess up with my current tensorflow library, I downloaded
tensorflow again in a separate folder
```git clone https://github.com/tensorflow/tensorflow.git```

After I installed Bazel (following their website instructions) I tried to build the
freeze_graph (make sure you are in the right path. If you download again tensorflow
from github note that it has a “WORKSPACE” file. You should be there to run Bazel) by
doing:
```bazel build tensorflow/python/tools:freeze_graph```

It takes a while to build it. In MacOS Sierra I didn’t have any problem, but in Ubuntu
16.04 I did, and after searching I found on github how to solve it.
```bazel build -c opt --copt=-msse4.1 --copt=-msse4.2 tensorflow/python/tools:freeze_graph```


After this, in the same folder, we just need to execute the command provided in the
tutorial:
```shell
bazel-bin/tensorflow/python/tools/freeze_graph\
    --input_graph=/tmp/mobilenet_v1_224.pb \
    --input_checkpoint=/tmp/checkpoints/mobilenet-10202.ckpt \
    --input_binary=true --output_graph=/tmp/frozen_mobilenet_v1_224.pb \
    --output_node_names=MobileNet/Predictions/Reshape_1
```

input_graph: location of the structure of the graph (first part of the tutorial, pb file)
input_checkpoint: weights stored using the Saver (second part of the tutorial)
input_binary=true: remember to save the graph in binary format. They recommend 
that this value has to be true, so do not use text format generating the pb file.
output_graph: location of the new frozen graph
output_node_names: name of the output node. You can check this using 
Tensorboard, but assuming you are naming all the tensors, this should be easy to 
figure out. You can also check the name of all the operations, or check the pb file (text 
mode), but probably the most intuitive way is using Tensorboard.

After executing this, we will have our frozen graph.


## Bonus: How to use the frozen Graph in Python
Here I found a very easy to follow code that explains itself how to read a frozen Graph
to use it.

```python
import tensorflow as tf

def load_graph(frozen_graph_filename):
    # We load the protobuf file from the disk and parse it to retrieve the
    # unserialized graph_def
    with tf.gfile.GFile(frozen_graph_filename, "rb") as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())

    # Then, we import the graph_def into a new Graph and returns it
    with tf.Graph().as_default() as graph:
        # The name var will prefix every op/nodes in your graph
        # Since we load everything in a new graph, this is not needed
        tf.import_graph_def(graph_def, name="prefix")
    return graph
```
