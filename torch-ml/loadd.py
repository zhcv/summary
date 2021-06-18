import torch
import torchvision
from torchvision import transforms, utils

img_data = torchvision.datasets.ImageFolder('D:/bnu/database/flower',
                                            transform=transforms.Compose([
                                                transforms.Scale(256,256),
                                                transforms.CenterCrop(224),
                                                transforms.ToTensor()])
                                            )
data_loader = torch.utils.data.DataLoader(img_data, batch_size=20,shuffle=True)
