#include <iostream>
#include <algorithm>
 
#include <cstdint>
#include <numeric>
#include <math.h>
#include <io.h>
 
//使用stbImage http://nothings.org/
#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"
#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "stb_image_write.h"
 
//如果是Windows的话，调用系统API ShellExecuteA打开图片
#if defined(_MSC_VER)
#include <windows.h>
#define USE_SHELL_OPEN
#endif
 
//是否使用OMP方式计时
#define USE_OMP 0
 
#if  USE_OMP
#include <omp.h>
auto const epoch = omp_get_wtime();
double now() {
    return omp_get_wtime() - epoch;
};
#else
#include <chrono>
auto const epoch = std::chrono::steady_clock::now();
double now() {
    return std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::steady_clock::now() - epoch).count() / 1000.0;
};
#endif
 
//计时函数
template<typename FN>
double bench(const FN &fn) {
    auto took = -now();
    return (fn(), took + now());
}
 
//存储当前传入文件位置的变量
std::string m_curFilePath;
 
//加载图片
void loadImage(const char* filename, unsigned char*& Output, int  &Width, int  &Height, int &Channels)
{
    Output = stbi_load(filename, &Width, &Height, &Channels, 0);
}
//保存图片
void saveImage(const char* filename, int  Width, int  Height, int Channels, unsigned char* Output, bool open = true)
{
    std::string saveFile = m_curFilePath;
    saveFile += filename;
    //保存为png,也可以调用stbi_write_bmp 保存为bmp
    stbi_write_png(saveFile.c_str(), Width, Height, Channels, Output, 0);
 
#ifdef USE_SHELL_OPEN
    if (open)
        ShellExecuteA(NULL, "open", saveFile.c_str(), NULL, NULL, SW_SHOW);
#else
    //其他平台暂不实现
#endif
}
 
//取当前传入的文件位置
void getCurrentFilePath(const char* filePath, std::string& curFilePath)
{
    char drive[_MAX_DRIVE];
    char dir[_MAX_DIR];
    char fname[_MAX_FNAME];
    char ext[_MAX_EXT];
    curFilePath.clear();
    _splitpath_s(filePath, drive, dir, fname, ext);
    curFilePath += drive;
    curFilePath += dir;
    curFilePath += fname;
    curFilePath += "_";
}
 
//算法处理,这里以一个反色作为例子
void processImage(unsigned char* Input, unsigned char* Output, unsigned int  Width, unsigned int  Height, unsigned int Channels)
{
    int WidthStep = Width*Channels;
    if (Channels == 1)
    {
        for (unsigned int Y = 0; Y < Height; Y++)
        {
            unsigned char*     pOutput = Output + (Y * WidthStep);
            unsigned char*     pInput = Input + (Y * WidthStep);
            for (unsigned int X = 0; X < Width; X++)
            {
                pOutput[0] = 255 - pInput[0];
 
                //下一个像素点
                pInput += Channels;
                pOutput += Channels;
            }
        }
    }
    else    if (Channels == 3 || Channels == 4)
    {
        for (unsigned int Y = 0; Y < Height; Y++)
        {
            unsigned char*     pOutput = Output + (Y * WidthStep);
            unsigned char*     pInput = Input + (Y * WidthStep);
            for (unsigned int X = 0; X < Width; X++)
            {
                pOutput[0] = 255 - pInput[0];
                pOutput[1] = 255 - pInput[1];
                pOutput[2] = 255 - pInput[2];
                //通道数为4时，不处理A通道反色(pOutput[3] = 255 - pInput[3];)
                //下一个像素点
                pInput += Channels;
                pOutput += Channels;
            }
        }
    }
 
}
 
//本人博客:http://tntmonks.cnblogs.com/转载请注明出处.
 
int main(int argc, char **argv) {
 
    std::cout << "Image Processing " << std::endl;
    std::cout << "Demo By Gaozhihan (Build 2016-03-22)" << std::endl;
    std::cout << "支持解析如下图片格式:" << std::endl;
    std::cout << "JPG, PNG, TGA, BMP, PSD, GIF, HDR, PIC" << std::endl;
 
    //检查参数是否正确
    if (argc < 2)
    {
        std::cout << "参数错误。" << std::endl;
        std::cout << "请拖放文件到可执行文件上，或使用命令行：imageProc.exe 图片" << std::endl;
        std::cout << "例如: imageProc.exe d:image.jpg" << std::endl;
 
        return 0;
    }
 
    std::string szfile = argv[1];
    //检查输入的文件是否存在
    if (_access(szfile.c_str(), 0) == -1)
    {
        std::cout << "输入的文件不存在，参数错误！" << std::endl;
    }
 
    getCurrentFilePath(szfile.c_str(), m_curFilePath);
 
    int Width = 0;        //图片宽度
    int Height = 0;        //图片高度
    int Channels = 0;    //图片通道数
    unsigned char* inputImage = NULL;    //输入图片指针
 
    double nLoadTime = bench([&]{
        //加载图片
        loadImage(szfile.c_str(), inputImage, Width, Height, Channels);
    });
    std::cout << " 加载耗时: " << int(nLoadTime * 1000) << " 毫秒" << std::endl;
    if ((Channels != 0) && (Width != 0) && (Height != 0))
    {
        //分配与载入同等内存用于处理后输出结果
        unsigned char* outputImg = (unsigned char*)STBI_MALLOC(Width*Channels*Height*sizeof(unsigned char));
        if (inputImage) {
            //如果图片加载成功，则将内容复制给输出内存，方便处理
            memcpy(outputImg, inputImage, Width*Channels*Height);
        }
        else     {
            std::cout << "加载文件:" << szfile.c_str() <<  " 失败!" << std::endl;
        }
 
        double nProcessTime = bench([&]{
            //处理算法
            processImage(inputImage, outputImg, Width, Height, Channels);
        });
        std::cout << " 处理耗时: " << int(nProcessTime * 1000) << " 毫秒" << std::endl;
 
        //保存处理后的图片
        double nSaveTime = bench([&]{
            saveImage("_done.png", Width, Height, Channels, outputImg);
        });
        std::cout << " 保存耗时: " << int(nSaveTime * 1000) << " 毫秒" << std::endl;
 
        //释放占用的内存
        if (outputImg)
        {
            STBI_FREE(outputImg);
            outputImg = NULL;
        }
 
        if (inputImage)
        {
            STBI_FREE(inputImage);
            inputImage = NULL;
        }
    }
    else
    {
        std::cout << " 加载文件:" << szfile.c_str() << " 失败!" << std::endl;
    }
 
    getchar();
    std::cout << "按任意键退出程序" << std::endl;
    return 0;
}
