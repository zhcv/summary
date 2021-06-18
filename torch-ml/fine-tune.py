import torch
from torch import nn
from torch import optim
from torchvision import models

resnet_model = models.resnet18(pretrained=True)


