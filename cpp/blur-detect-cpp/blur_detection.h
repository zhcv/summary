/*  #pragma once  */

#ifndef BLUR_DETECTION_H
#define BLUR_DETECTION_H

#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <sys/types.h>

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui_c.h>
#include <opencv2/imgproc/imgproc_c.h>

double variance_of_laplacian(const IplImage* img);

void show_image(const char* winname, const IplImage* img, float waittime);

void draw_and_show_image(const IplImage* img, char* content, float waittime);

void delete_duplicates_image(const char* imgpath);

/* C substring function: It returns a pointer to the substring */
char *substring(char *string, int position, int length);

bool isImageFile(const char* img_name);

#endif   // BLUR_DETECTION_H
