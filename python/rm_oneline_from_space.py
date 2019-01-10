#coding:utf-8

imgs = []
imgs_all = []

with open('result.txt','r') as f:
        da = f.readlines()
        # print da
        for num, line in enumerate(da):
            print line.strip()
            if line == '\n':
                imgs.append(da[num+1])
            if line != '\n':
                imgs_all.append(line)

# ret = list(set(a) ^ set(b))  # b 中有, a 中没有
# ret = list(set(imgs_all).difference(set(imgs)))  # b 中有, a 中没有
ret = ret = [ i for i in imgs_all if i not in imgs ]
rm_imgs = ret

with open('jpglist.txt', 'w+') as f:
    for line in rm_imgs:
        print >> f, line.strip()
