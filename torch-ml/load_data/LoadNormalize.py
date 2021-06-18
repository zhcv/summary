# TODO

normalize = T.Normalize(mean=[0.4, 0.4, 0.4], std=[0.2, 0.2, 0.2])
transform  = T.Compose([
         T.RandomResizedCrop(224),
         T.RandomHorizontalFlip(),
         T.ToTensor(),
         normalize,
])
dataset = ImageFolder('data1/dogcat_2/', transform=transform)

# 深度学习中图片数据一般保存成CxHxW，即通道数x图片高x图片宽
#print(dataset[0][0].size())

to_img = T.ToPILImage()
# 0.2和0.4是标准差和均值的近似
a=to_img(dataset[0][0]*0.2+0.4)
