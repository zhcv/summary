
export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/home/zhp/.local/lib/pkgconfig
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/zhp/.local/lib
export PATH=/home/zhp/.local/bin:$PATH



cmake -DCMAKE_PREFIX_PATH=/home/zhp/.local \
      -DCMAKE_TOOLCHAIN_FILE=../toolchains/host.gcc.toolchain.cmake \
      -DNCNN_BUILD_TOOLS=ON \
      ..
