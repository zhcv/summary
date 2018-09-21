# serving compile

$ export TF_NEED_CUDA=1
$ cd serving
$ bazel build -c opt --copt=-mavx --copt=-mavx2 --copt=-mfma --copt=-mfpmath=both --copt=-msse4.2 --config=cuda -k --verbose_failures --crosstool_top=@local_config_cuda//crosstool:toolchain --spawn_strategy=standalone tensorflow_serving/model_servers:tensorflow_model_server
