// gcc -o libpycallfoo.so -shared -fPIC rsa.c   

extern "C" int foo(int len,char *p,char* ret)
{
    __int64 a1 = 0x36;
    __int64 a2 = 0x100;
    __int64 a3 = 0xb5547;

    int j;
    char xz[100]={};
    memcpy(xz,p,len);
    printf("your input is %s,len xz=%d\n",xz,strlen(xz));

    int* pResult = new int[100];//密文
    int i;
    for(i = 0; i < strlen(xz); i++)
    {
        int result1 = rsa_mod(xz[i],0,0x101,0,0xb5547,0);
        pResult[i] = swapEndian(result1);
         //printf("0x%04X ",pResult[i]);
    }
    memcpy((char *)ret,(char *)pResult,4*strlen(xz));
    return 0;
}

