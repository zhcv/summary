#include<stdio.h> 

int main() 
{ 
    int a; 
  
    // Let we input 10 20, we get output as 20 
    // (First input is ignored) 
    // If we remove * from below line, we get 10. 
    scanf("%*d%d", &a); 
  
    printf( "%d ",  a);   
  
    return 0;      
} 

