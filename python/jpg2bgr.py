import cv2
 
imgpath = "./BGR_img/917.jpg"
saveimg = r"./BGR_img/917_608x608.bgr"
 
img = cv2.imread(imgpath)
save_img_size = 608
 
if img is None:
    print("img is none")
else:
    img = cv2.resize(img,(save_img_size,save_img_size))
    (B, G, R) = cv2.split(img)
    with open(saveimg,'wb')as fp:
        for i in range(save_img_size):
            for j in range(save_img_size):
                fp.write(B[i, j])
        for i in range(save_img_size):
            for j in range(save_img_size):
                fp.write(G[i, j])
        for i in range(save_img_size):
            for j in range(save_img_size):
                fp.write(R[i, j])
 
    print("save success")
