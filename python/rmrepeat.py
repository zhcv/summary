import os

with open('result.txt', 'r') as f:
    imgs = [line.strip() for line in f.readlines()]
    imgs.append('')
    print imgs[:20]
    for num, img in enumerate(imgs):
        if img != '' and imgs[num+1] != '':
            print imgs[num+1]
            os.remove(imgs[num+1]) 
        

