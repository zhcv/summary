/* 'pwd' to get path to the current file in C Program */

#include <stdio.h>  /* defines FILENAME_MAX */
//#define WINDOWS  /* uncomment this line to use it for windows.*/
#ifdef WINDOWS
#include <direct.h>
#define GetCurrentDir _getcwd
#else
#include <unistd.h>
#define GetCurrentDir getcwd
#endif


int main(){
  char buff[FILENAME_MAX];
  GetCurrentDir( buff, FILENAME_MAX );
  /* printf("Current working dir: %s\n", buff);  */
  printf("%s\n", buff);
  return 0;
}
/*
OUTPUT:
Current working dir: /home/your_dir_name
*/
