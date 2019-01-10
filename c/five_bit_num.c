#include<stdio.h>

/* 利用C语言求解这样的两个数据:5位数=2*4位数，9个数字互不相同 */

int main()
{
    long x;
    int p[10],i,t,k;
    int num=0;
    int n,f,y,m;
    for(x=1000;x<=9999;x++)
    {
        for(i=0;i<=9;i++)
            p[i]=1;
            y=x;
            f=x*2;
            n=f;
        if(n>=10000)
        {
            k=0;
        for(i=1;i<=5;i++)
        {
            t=y%10;
            y=y/10;
            m=n%10;
            n=n/10;
            if(m==t){k=0;break;}
            if(i<5)
               if(p[t]==1)
               {
                 p[t]=0;
                 k++;
               }
             else
              {
                 k=0;
                 break;
              }
              if(p[m]==1)
              {
                 p[m]=0;
                 k++;
              }
              else
              {      
                 k=0;
                 break;
              }
        }
            if(k==9)
                {
                 num=num+1;
                 printf("%d\t%d\t",x,f);
                }
        }
        else
            continue;
    }
    printf("\n");
    printf("%d\n",num);
    return 0;
}
