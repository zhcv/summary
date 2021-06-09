cmake_minimum_required(VERSION 3.1)

list(APPEND CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake/Modules)

# else can not fin nullptr and so on.
set (CMAKE_CXX_STANDARD 11)

#project name
project(thread_test)

#debug
set(CMAKE_BUILD_TYPE debug )
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC -march=native -fopenmp -g2 -ggdb -lpthread")

# thread_create
set( EXE_NAME thread_create_test )
set(APP_SRC thread_create.cpp)
add_executable(${EXE_NAME} ${APP_SRC} )
target_link_libraries(${EXE_NAME})
