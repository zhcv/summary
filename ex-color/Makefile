# g++ extract_color.cpp -o ext `pkg-config opencv --libs --cflags`
CXX = g++
LIBS +=`pkg-config --libs opencv`
INC +=`pkg-config --cflags opencv`
CPPFLAGS += -g -std=c++11 -Wall

SRCS = extract_color.cpp
TARGET = detect
OBJS = detect.o

$(TARGET):$(OBJS)
    $(CXX) $(INC) $(CPPFLAGS) $(OBJS) -o $(TARGET) $(LIBS)
$(OBJS):%.o:%.cpp
    $(CXX) $(INC) $(CPPFLAGS) -c $< -o $@

.PHONY:clean
clean:rm -r *.o $(TARGET)
