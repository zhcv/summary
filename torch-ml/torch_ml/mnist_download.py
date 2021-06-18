import torch
import torchvision
from PIL import Image
from skimage import io


mnist_test = torchvision.datasets.MNIST('./mnist', train=False, download=True)

print "test set: ", len(mnist_test)

with open("mnist_test.txt", "w") as f:
    for i, (img, label) in enumerate(mnist_test):
	img_path = "./mnist_test/" + "%06d" % i + ".jpg"
	print ">>>>", label
	img.save(img_path)
	f.write(img_path + " " + str(label) + "\n") 
