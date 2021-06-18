#ifndef __USE_DEBUG                                                                                                                   
#define __USE_DEBUG

#ifdef  USE_DEBUG
#define DEBUG_LINE() printf("[%s:%s] line=%d\r\n",__FILE__, __func__, __LINE__)
#define DEBUG_ERR(fmt, args...) printf("\033[47;31m[%s:%d]\033[0m   "fmt" \r\n", __func__, __LINE__,  ##args)
#define DEBUG_INFO(fmt, args...) printf("\033[33m[%s:%d]\033[0m  "fmt"  \r\n", __func__, __LINE__, ##args)
#else
#define DEBUG_LINE()
#define DEBUG_ERR(fmt, ...)
#define DEBUG_INFO(fmt, ...)
#endif

#endif




int main(int args, const char ** argv)
{
    int fd;
    
    fd = open("/dev/nothing, O_RDWR");
    if(fd < 0){
        DEBUG_ERR(“open failed， ret = %d, %m\n”, fd);
    }
}
