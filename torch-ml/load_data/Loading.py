from torchvision.datasets import ImageFolder
import torch
from torchvision import transforms

#加上transforms
normalize=transforms.Normalize(mean=[.5,.5,.5],std=[.5,.5,.5])
transform=transforms.Compose([
    transforms.RandomReSizedCrop(224),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(), #将图片转换为Tensor,归一化至[0,1]
    normalize
])

root = ""

dataset=ImageFolder(root,transform=transform)

#输出第0张图片的大小
print(dataset[0][0].size())
