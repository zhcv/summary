# General Makefile by zhanghaipeng

CXX ?= g++                             
   

all:  
	# $(CXX) -o main main.cpp blur_detection.cpp `pkg-config opencv --cflags --libs` -Wno-write-strings 
	$(CXX) -o main main.cpp blur_detection.cpp `pkg-config opencv --cflags --libs`
 
clean:
	rm -f main
