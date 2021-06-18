@echo off

color 02
::set path=%path%;D:\Anaconda3.7\condabin:D:\Anaconda3.7\Scripts;D:\Anaconda3.7\Library\bin;
set path=%path%;D:\Anaconda3.7\condabin:D:\Anaconda3.7\Scripts;D:\Anaconda3.7\Library\bin;
cmd.exe
cmake .. -G "Visual Studio 14 2015 Win64" -T host=x64
pause 