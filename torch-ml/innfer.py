#加载训练好的分类CNN网络
model=torch.load('model.pkl')

#假设proposal_img是我们提取的候选框，是需要输入到CNN网络的数据

#先定义transforms对输入cnn的网络数据进行处理，常包括resize、totensor等操作
data_transforms=transforms.Compose([transforms.RandomSizedCrop(224),
transforms.ToTensor()])

#由于transforms是对PIL格式数据操作，所以必要时转化格式

def tensor_to_PIL(tensor):
    image = tensor.cpu().clone()
    image = image.squeeze(0)
    image = unloader(image)
    return image
    
#unqueeze（0）是加多一维，对应原来batchsiaze
data=data_transforms(proposal_img).unqueeze(0)

#新版本pytorch已经不用variable，可以省略这句
data=Variable（data）
#貌似这句也是多余的
torch.no_grad()

predict=F.softmax(model(data.cuda()).cuda())

