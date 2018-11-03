sess = tf.Session()
sess.run(tf.global_variables_initializer())

tf.train.write_graph(sess.graph.as_graph_def(),'.','tensorflowModel.pbtxt', as_text=True)

saver.save(sess, './my_test_model.ckpt')

freeze_graph.freeze_graph('./tensorflowModel.pbtxt', "",False,'./my_test_model.ckpt', "output/predictions", "save/restore_all",  "save/Const:0",'frozen.pb', True,"")
