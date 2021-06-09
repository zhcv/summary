//image_src is the source image, image_dst is the converted image
void NV21_YUV420P(const unsigned char* image_src, unsigned char* image_dst,
	int image_width, int image_height)
{
	unsigned char* p = image_dst;
	memcpy(p, image_src, image_width * image_height * 3 / 2);
	const unsigned char* pNV = image_src + image_width * image_height; 
	unsigned char* pU = p + image_width * image_height;
	unsigned char* pV = p + image_width * image_height + ((image_width * image_height)>>2);
	for (int i=0; i<(image_width * image_height)/2; i++)
	{
		if ((i%2)==0) 
		{
			*pV++ = *(pNV + i);
		}
		else 
		{
			*pU++ = *(pNV + i);
		}
	}
}


//image_src is the source image, image_dst is the converted image
void NV12_YUV420P(const unsigned char* image_src, unsigned char* image_dst,
	int image_width, int image_height)
{
	unsigned char* p = image_dst;
	memcpy(p, image_src, image_width * image_height * 3 / 2);
	const unsigned char* pNV = image_src + image_width * image_height; 
	unsigned char* pU = p + image_width * image_height;
	unsigned char* pV = p + image_width * image_height + ((image_width * image_height)>>2);
	for (int i=0; i<(image_width * image_height)/2; i++)
	{
		if ((i%2)==0) {
			*pU++ = *(pNV + i);
		}
		else {
			*pV++ = *(pNV + i);
		}
	}
}