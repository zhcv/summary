"""
https://www.learnopencv.com/pytorch-for-beginners-image-classification-using-pre-trained-models
PyTorch for Beginners: Image Classification using Pre-trained models
"""

from torchvision import models
from torchvision import transforms

import torch


# print dir(models)
alexnet = models.alexnet(pretrained=True)

# You will see a similar output as below
#  Downloading: "https://download.pytorch.org/models/alexnet-owt- 4df8aa71.pth" 
#  to /home/hp/.cache/torch/checkpoints/alexnet-owt-4df8aa71.pth
print alexnet


transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
	mean=[0.485, 0.485, 0.485],
	std=[0.229, 0.224, 0.225]
)])


from PIL import Image
img = Image.open("dog.jpg")


img_t = transform(img)
batch_t = torch.unsqueeze(img_t, 0)

alexnet.eval()
out = alexnet(batch_t)

print out.shape

with open("imagenet_classes.txt", "r") as f:
    classes = [line.strip() for line in f.readlines()]

_, index = torch.max(out, 1)
percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100

_, indices = torch.sort(out, descending=True)

# [(labels[idx], percentage[idx].item()) for idx in indices[0][:5]]

