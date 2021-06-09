#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main(int argc, char** argv) {
    Mat image = imread("ttest.jpg");
    // imshow("input", image);

    // 色彩空间转换
    Mat hsv, mask;
    cvtColor(image, hsv, COLOR_BGR2HSV);
    inRange(hsv, Scalar(40,43, 46), Scalar(50, 255, 255), mask);
    // imshow("mask", mask);
    imwrite("mask.png", mask);

    // 形态学开操作
    Mat se = getStructuringElement(MORPH_RECT, Size(5, 5), Point(-1, -1));
    morphologyEx(mask, mask, MORPH_OPEN, se);
    // imshow("binary", mask);
    imwrite("binary.png", mask);

    // 轮廓发现
    vector<vector<Point> > contours;
    vector<Vec4i> hiearchy;
    findContours(mask, contours, hiearchy, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE);
    for (int i = 0; i < contours.size(); i++) {
        // 圆拟合
        RotatedRect rrt = fitEllipse(contours[i]);
        Point ct = rrt.center;
        int h = rrt.size.height;
        int w = rrt.size.width;
        printf("height : %d, width : %d \n", h, w);
        circle(image, ct, 2, Scalar(0, 0, 255), 2, 8);
        circle(image, ct, (h + w) / 4, Scalar(255, 0, 0), 2, 8, 0);
    }

    // 显示输出
    // imshow("result", image);
    imwrite("result.png", image);
    // waitKey(0);
    return 0;
}
