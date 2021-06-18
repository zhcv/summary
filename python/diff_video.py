import cv2
import numpy as np
import matplotlib.pyplot as plt
 

def absdiff_(frames,sThre):
    c_frames = []
    for i in range(len(frames)-2):
        #将图片灰度化
        gray_frame_front = cv2.cvtColor(frames[i],cv2.COLOR_BGR2GRAY)
        #高斯滤波 (平滑了一些)
        gray_frame_front = cv2.GaussianBlur(gray_frame_front,(3,3),0)
 
        gray_frame_later = cv2.cvtColor(frames[i+1],cv2.COLOR_BGR2GRAY)
        gray_frame_later = cv2.GaussianBlur(gray_frame_later,(3,3),0)
 
        #帧间做差
        d_frame = cv2.absdiff(gray_frame_front,gray_frame_later)
 
        #对灰度值图像进行阈值操作得到二值图像
        ret,d_frame = cv2.threshold(d_frame,sThre,255,cv2.THRESH_BINARY)
        c_frames.append(d_frame)
        
    return c_frames
        
 
def Video_to_image(Videopath):
    capture = cv2.VideoCapture(Videopath)
    #得到视频的帧率，即每一秒刷新图片的数量，framesNum是一整段视频中总的图片数
    fps = capture.get(cv2.CAP_PROP_FPS)
    #得到整个视频的帧数
    framesNum = capture.get(cv2.CAP_PROP_FRAME_COUNT)
 
    print("fps=",fps,"frames=",framesNum)
    frames = []
 
    for i in range(int(framesNum)-1):
        #获取下一帧
        ret,frame = capture.read()
        frames.append(frame)
    return frames
 
 
def Image_to_video(frames):
    #表示视频流格式
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    #30表示输出视频每秒30帧，（544,960）表示输出的视频的尺寸
    videoWriter = cv2.VideoWriter(outPath,fourcc,30,(544,960),isColor=0)
 
    for i in range(len(frames)-1):
        videoWriter.write(frames[i])


if __name__ == "__main__": 
 
    inpath = "testvideo.mp4"
    outPath = 'output_video.mp4'
    #阈值
    sThre = 5 
    frames = []
    frames = Video_to_image(inpath)
    c_frames = absdiff_(frames,sThre)
    Image_to_video(c_frames)
    print("down!")
