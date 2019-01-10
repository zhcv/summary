#!/usr/bin/env bash

usage()
{
    cat <<EOF
Usage: curl-config [OPTION]

Available values for OPTION include:

  --built-shared says 'yes' if libcurl was built shared
  --ca        ca bundle install path
  --cc        compiler
  --cflags    pre-processor and compiler flags
  --checkfor [version] check for (lib)curl of the specified version
  --configure the arguments given to configure when building curl
  --features  newline separated list of enabled features
  --help      display this help and exit
  --libs      library linking information
  --prefix    curl install prefix
  --protocols newline separated list of enabled protocols
  --ssl-backends output the SSL backends libcurl was built to support
  --static-libs static libcurl library linking information
  --version   output version information
  --vernum    output the version information as a number (hexadecimal)
EOF

    exit $1
}


hello()
{
echo how many parameters in the function:$#;
echo the name of this function is $0;
echo the first parameters is :$1;
echo the second parameters is :$2;

}


funWithParam(){
    echo "The value of the first parameter is $1 !"
    echo "The value of the second parameter is $2 !"
    echo "The value of the tenth parameter is $10 !"
    echo "The value of the tenth parameter is ${10} !"
    echo "The value of the eleventh parameter is ${11} !"
    echo "The amount of the parameters is $# !"
    echo "The string of the parameters is $* !"
}



# usage
hello "hello" "world"
# funWithParam 1 2 3 4 5 6 7 8 9 34 73
