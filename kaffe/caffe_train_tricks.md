### Caffe Train Tricks

we have our model and solver ready, we can start training by calling the `caffe` binary:

```
caffe train \
  -gpu 0 \
  -solver my_model/solver.prototxt
```

**Note** that we only need to specify the solver, because the model is specified in the solver file, and the data is specified in the model file.

We can also resume from a snapshot, which is very common (imaging if you are playing Assasin’s Creed and you need to start from the beginning every time you quit game…):

```
caffe train \
    -gpu 0 \
    -solver my_model/solver.prototxt \
    -snapshot my_model/my_model_iter_6000.solverstate 2>&1 | tee log/my_model.log
```

**OR** to fine tune from a trained network:

```
caffe train \
    -gpu 0 \
    -solver my_model/solver.prototxt \
    -weights my_model/bvlc_reference_caffenet.caffemodel 2>&1 | tee -a log/my_model.log
```



### resume training from the half-way point snapshot

```
caffe train -solver examples/mnist/lenet_solver.prototxt -snapshot examples/mnist/lenet_iter_5000.solverstate
```



### fine-tune `CaffeNet` model weights for pascal

```
caffe train -solver examples/finetune_pascal_detection/pascal_finetune_solver.prototxt -weights models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel
```

### score the learned `LeNet` model on the validation set as defined in the model architecture `lenet_train_test.prototxt`

```
caffe test -model examples/mnist/lenet_train_test.prototxt -weights examples/mnist/lenet_iter_10000 -iterations 100
```

### (These example calls require you complete the `LeNet / MNIST` example first.)

### time `LeNet` training on `cpu` for 10 iterations

```
caffe time -model examples/mnist/lenet_train_test.prototxt -iterations 10
```

### time a model architecture with the given weights  on the first gpu for 10 iterations

### time `LeNet` training on `gpu` for the default 50 iterations 

```
caffe time -model examples/mnist/lenet_train_test.prototxt -gpu 0
```



