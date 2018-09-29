// 边缘区域去除1.cpp : 定义控制台应用程序的入口点。
// VS2010 opencv2.4.9
 
//#include "stdafx.h"
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <iostream>
using namespace cv;
using namespace std;
 
void floodFillborder(const cv::Mat& binsrcImg,cv::Mat& bindstImg);
int main()
{
	Mat src=imread("1.jpg",1);
	imshow("src",src);
 
	//灰度化
	Mat grayImage;
	cvtColor(src,grayImage,CV_BGR2GRAY);
 
	//二值化原图像
	Mat thresImage=Mat::zeros(grayImage.rows,grayImage.cols,CV_8UC1);
	threshold(grayImage,thresImage,250,255,THRESH_BINARY);
	//imshow("thresImage",thresImage);
 
 
	////方法1：轮廓提取与阈值填充
	//vector<vector<Point>> contours;  
	//vector<Point>contours_sum;
	//// find  
	//findContours(thresImage,contours,CV_RETR_EXTERNAL,CV_CHAIN_APPROX_NONE); 
	//for(int n =0; n<contours.size();++n)
	//{
	//	cout<<contours[n].size()<<endl;
	//	for (int i=0;i<contours[n].size();++i)
	//	{
	//		contours_sum.push_back(contours[n][i]);
	//	}
	//}
	////cout<<contours_sum.size()<<endl;
	//for (int i=0;i<contours_sum.size();++i)
	//{
	//	//cout<<contours_sum[i]<<endl;
	//	floodFill(thresImage,contours_sum[i],0);//漫水填充法
	//}
	//imshow("floodFill",thresImage);
 
 
	////方法二
 
	//const int nr=thresImage.rows;
	//const int nc=thresImage.cols;
	//Mat edge[4];
	//edge[0] = thresImage.row(0);    //up
	//edge[1] = thresImage.row(nr-1); //bottom
	//edge[2] = thresImage.col(0);    //left
	//edge[3] = thresImage.col(nc-1); //right
 
	//std::vector<Point> edgePts;
	//const int minLength=std::min(nr,nc)/4;
	//for(int i=0;i<4;++i)
	//{
	//	std::vector<Point> line;
	//	Mat_<uchar>::const_iterator iter = edge[i].begin<uchar>();       //当前像素
	//	Mat_<uchar>::const_iterator nextIter = edge[i].begin<uchar>()+1; //下一个像素
	//	while(nextIter!=edge[i].end<uchar>())
	//	{
	//		if(*iter==255)
	//		{
	//			if(*nextIter==255)
	//			{
	//				Point pt = iter.pos();
	//				if(i==1)
	//					pt.y = nr-1;
	//				if(i==3)
	//					pt.x = nc-1;
	//				
	//				//line.push_back(pt);
	//				edgePts.push_back(pt);
	//			}
	//			//if(*nextIter!=255)
	//			//{
	//			//	if(line.size()>minLength)
	//			//		edgePts.push_back(line.at(line.size()/2));
	//			//	line.clear();
	//			//}
	//		}
	//		++iter;
	//		++nextIter;
	//	}
	//}
	//
	//for(int n =0; n<edgePts.size();++n)
	//	//cout<<edgePts[n];
	//	floodFill(thresImage,edgePts[n],0);//漫水填充法
	//imshow("floodFill",thresImage);
 
	//方法三：边界填充方法二的函数形式
	floodFillborder(thresImage,thresImage);
	imshow("floodFill",thresImage);
	waitKey( 0 );    
}
 
 
void floodFillborder(const cv::Mat& binsrcImg,cv::Mat& bindstImg)
{
	const int nr=binsrcImg.rows;
	const int nc=binsrcImg.cols;
	Mat edge[4];
	edge[0] = binsrcImg.row(0);    //up
	edge[1] = binsrcImg.row(nr-1); //bottom
	edge[2] = binsrcImg.col(0);    //left
	edge[3] = binsrcImg.col(nc-1); //right
 
	std::vector<Point> edgePts;
	const int minLength=std::min(nr,nc)/4;
	for(int i=0;i<4;++i)
	{
		std::vector<Point> line;
		Mat_<uchar>::const_iterator iter = edge[i].begin<uchar>();       //当前像素
		Mat_<uchar>::const_iterator nextIter = edge[i].begin<uchar>()+1; //下一个像素
		while(nextIter!=edge[i].end<uchar>())
		{
			if(*iter==255)
			{
				if(*nextIter==255)
				{
					Point pt = iter.pos();
					if(i==1)
						pt.y = nr-1;
					if(i==3)
						pt.x = nc-1;
 
					edgePts.push_back(pt);
				}
			}
			++iter;
			++nextIter;
		}
	}
 
	for(int n =0; n<edgePts.size();++n)
		floodFill(binsrcImg,edgePts[n],0);//漫水填充法
	binsrcImg.copyTo(bindstImg);
}

