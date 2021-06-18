#include <iostream>
#include <fstream>
#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>

using namespace cv;
using namespace std;
 
 
int main(int argc, char **argv)
{
	string train_test_image[2] = { "train-images.idx3-ubyte", "t10k-images.idx3-ubyte" };
	string train_test_label[2] = { "train-labels.idx1-ubyte","t10k-labels.idx1-ubyte" };
	int label_num[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
	string dir[2] = {"./train/","./test/"};
	for (int iter = 0; iter < 2;iter++)
	{
		//读取label
		ifstream fin_label(train_test_label[iter], ios::binary);
		vector<int> label;
 
		int magic_number;
		fin_label.read((char *)(&magic_number), sizeof(magic_number));
		int number_items;
		fin_label.read((char *)(&number_items), sizeof(number_items));
		while (!fin_label.eof())
		{
			char label_tmp;
			fin_label.read((char *)&label_tmp, sizeof(label_tmp));
			label.push_back(label_tmp);
		}
 
		//读取图片
		vector<Mat> image;
		int width = 28, height = 28;
		ifstream fin_image(train_test_image[iter], ios::binary);
		int magic_number1;
		fin_image.read((char *)(&magic_number1), sizeof(magic_number1));
		int number_images;
		fin_image.read((char *)(&number_images), sizeof(number_images));
		int num_rows;
		fin_image.read((char *)(&num_rows), sizeof(num_rows));
		int num_columns;
		fin_image.read((char *)(&num_columns), sizeof(num_columns));
		while (!fin_image.eof())
		{
			unsigned char tmp;
			Mat image_tmp(width, height, CV_8UC1);
			for (int r = 0; r < image_tmp.rows; r++)
			{ 
				for (int c = 0; c < image_tmp.cols; c++)
				{
					fin_image.read((char *)&tmp, sizeof(tmp));
					image_tmp.at<uchar>(r, c) = tmp;
				}
			}
			image.push_back(image_tmp); 
		}
 
		for (int i = 0; i < label.size();i++)
		{
			char clabel[10];
			sprintf_s(clabel, "%d",label[i]);
			string slabel = clabel;
			char clabel_num[10];
			sprintf_s(clabel_num, "%d", label_num[label[i]]);
			string slabel_num = clabel_num;
 
			string name = dir[iter] + slabel + "_" + slabel_num + ".jpg";
			imwrite(name, image[i]);
			label_num[label[i]]++;
		}
	}
	return 0;
}
