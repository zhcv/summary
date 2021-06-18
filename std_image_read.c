#include <iostream>
#include <fstream>
#include <stbi/stb_image.h>

const unsigned char * loadfile(const std::string &file, int &size)
{
    std::ifstream fs(file.c_str(), std::ios::binary);
    fs.seekg(0, std::ios::end);
    size = fs.tellg();
    char * data = new char[size + 1];
    fs.seekg(0);
    fs.read(data, size);
    fs.close();
    data[size] = 0;
    return (unsigned char *)data;
}


int main()
{
    int w;
    int h;
    int channels;
    int size;
    const unsigned char * data = loadfile("D:/1.jpg", size);
    const unsigned char * logo = stbi_load_from_memory(data, size, &w, &h, &channels, 0);
    for (int i = 0; i < 3; ++i)
    {
        std::cout << (int)logo[i] << std::endl;
    }
}
