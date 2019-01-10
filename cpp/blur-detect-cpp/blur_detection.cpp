#include "blur_detection.h"

void show_image(const char* winname, const IplImage* img, float waittime)
{
    cvNamedWindow(winname, CV_WINDOW_AUTOSIZE);
    cvShowImage(winname, img);
    int timedelay = (int)(waittime * 1000);
    cvWaitKey(timedelay);
    cvDestroyWindow(winname);
}

void draw_and_show_image(const IplImage* img, char* content, float waittime)
{
    IplImage* draw = cvCreateImage(cvGetSize(img), IPL_DEPTH_8U, 3);
    if (img->nChannels == 1)
    {
        cvCvtColor(img, draw, CV_GRAY2BGR);
    }
    else
    {
        cvCopy(img, draw, NULL);
    }

    CvPoint org;
    org.x = 10;
    org.y = 30;
    CvFont font;
    cvInitFont(&font, CV_FONT_HERSHEY_SIMPLEX, 1.0, 1.0, 0, 2, 8);
    cvPutText(draw, content, org, &font, CV_RGB(160, 32, 240));
    show_image("label", draw, waittime);
    cvReleaseImage(&draw);
}

double variance_of_laplacian(const IplImage* img)
{
    if (img == NULL)
    {
        return 0.0;
    }
    const int imgrows = img->height;
    const int imgcols = img->width;
    IplImage* gray = cvCreateImage(cvSize(imgcols, imgrows), IPL_DEPTH_8U, 1);
    if (img->nChannels == 3)
    {
        cvCvtColor(img, gray, CV_BGR2GRAY);
    }
    else if (img->nChannels == 1)
    {
        cvCopy(img, gray, NULL);
    }
    else
    {
        cvCvtColor(img, gray, CV_BGRA2GRAY);
    }

    IplImage* lap = cvCreateImage(cvSize(imgcols, imgrows), IPL_DEPTH_64F, 1);
    cvLaplace(gray, lap, 3);
    cvReleaseImage(&gray);

    CvScalar lap_mean, lap_stddev;
    cvAvgSdv(lap, &lap_mean, &lap_stddev, NULL);
    cvReleaseImage(&lap);

    return lap_stddev.val[0];
}

void delete_duplicates_image(const char* imgpath)
{
    int status;
    status = remove(imgpath);
    if (status == 0)
    {
        printf("%s file deleted successfully.\n", imgpath);
    }
    else
    {
        printf("Unable to delete the file\n");
        perror("Error");
    }
}


char *substring(const char *string, int position, int length)
{
    // char *pointer = NULL;
    // pointer = malloc(length + 1);
    char *pointer = (char *)malloc(1);
    if (pointer == NULL)
    {
        printf("Unable to allocate memory.\n");
        exit(1);
    }
    int c = 0;
    for (c = 0; c < length; c++)
    {
        *(pointer + c) = *(string + position - 1);
        string++;
    }
    *(pointer + c) = '\0';
    return pointer;
}

// bool isImageFile(const char* img_name)
bool isImageFile(const char* img_name)
{
    // find last '.' of img_name
    int lastIdx = 0;
    int lenStr = strlen(img_name);
    int len = lenStr;
    while (--len)
    {
        char c = img_name[len];
        if (c == '.')
        {
            lastIdx = len;
            break;
        }
    }

    // substr
    char* imgpox = substring(img_name, lastIdx + 2, lenStr - lastIdx + 1);
    int r1 = strcmp(imgpox, "jpg");
    int r2 = strcmp(imgpox, "JPG");
    int r3 = strcmp(imgpox, "jpeg");
    int r4 = strcmp(imgpox, "JPEG");

    if (r1 == 0 || r2 == 0 || r3 == 0 || r4 == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}
