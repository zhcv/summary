#include "blur_detection.h"
#include <dirent.h>
#include <locale.h>

int main(int argc, char* argv[])
{
    if (argc != 2)
    {
        printf("Usage:\n./filename <image path>\n");
        return -1;
    }

    setlocale(LC_CTYPE, "");  // 处理中文命名的图像名称
    const char* img_path = argv[1];

    if (isImageFile(img_path))
    {
        // detect the blurness of image
        IplImage* img = cvLoadImage(img_path, 1);
        double stdv = variance_of_laplacian(img);
        char const * rest = NULL;
        if (stdv <= 50)
        {
            rest = "blur ";
        }
        else
        {
            rest = "not blur ";
        }
        char buffer[10];
        snprintf(buffer, 10, "%.2f", stdv);
        char content[50];
        strcpy(content, rest);
        strcat(content, buffer);
        draw_and_show_image(img, content, 0);
        cvReleaseImage(&img);
    }
    return 0;
}
