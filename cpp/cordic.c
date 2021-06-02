#include <stdio.h>
#include <stdlib.h>

double my_tan2(double z);   

int main(viod)
{
    double x = my_tan2(51.0);
    return 0;
}

double my_tan2(double z)
{
    const double theta[] = { 45.0, 26.56505118, 14.03624347, 7.125016349, 
        3.576334375, 1.789910608, 0.8951737102, 0.4476141709, 
        0.2238105004, 0.1119056771, 0.05595289189, 0.02797645262, 
        0.01398822714, 0.006994113675, 0.003497056851, 0.001748528427
    };

    int i = 0;
    double angle_new = 0;
    double angle_remain = z;
    char detection;

    for( i=0; i<16;i++)
    {
        if(angle_remain > 0)
        {
            angle_remain = angle_remain - theta[i];
            detection = '+';
        }
        
        else
        {
            angle_remain = angle_remain + theta[i];
            detection = '-';
             
        }
        printf(" 旋转次数 = %-8d 旋转角度 = %-12f  旋转方向：%-8c  剩余角度 = %-8f\n", i, theta[i],detection, angle_remain);
        
    }
    return angle_remain;
}
