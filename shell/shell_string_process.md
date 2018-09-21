Shell脚本8种字符串截取方法总结

Linux 的字符串截取很有用。有八种方法。

假设有变量 var=http://www.aaa.com/123.htm.

1. # 号截取，删除左边字符，保留右边字符。

复制代码 代码如下:

echo ${var#*//}

其中 var 是变量名，# 号是运算符，*// 表示从左边开始删除第一个 // 号及左边的所有字符
即删除 http://
结果是 ：www.aaa.com/123.htm

2. ## 号截取，删除左边字符，保留右边字符。

复制代码 代码如下:

echo ${var##*/}

##*/ 表示从左边开始删除最后（最右边）一个 / 号及左边的所有字符
即删除 http://www.aaa.com/

结果是 123.htm

3. %号截取，删除右边字符，保留左边字符

复制代码 代码如下:

echo ${var%/*}

%/* 表示从右边开始，删除第一个 / 号及右边的字符

结果是：http://www.aaa.com

4. %% 号截取，删除右边字符，保留左边字符

复制代码 代码如下:

echo ${var%%/*}

%%/* 表示从右边开始，删除最后（最左边）一个 / 号及右边的字符
结果是：http:

5. 从左边第几个字符开始，及字符的个数

复制代码 代码如下:

echo ${var:0:5}

其中的 0 表示左边第一个字符开始，5 表示字符的总个数。
结果是：http:

6. 从左边第几个字符开始，一直到结束。

复制代码 代码如下:

echo ${var:7}

其中的 7 表示左边第8个字符开始，一直到结束。
结果是 ：www.aaa.com/123.htm

7. 从右边第几个字符开始，及字符的个数

复制代码 代码如下:

echo ${var:0-7:3}

其中的 0-7 表示右边算起第七个字符开始，3 表示字符的个数。
结果是：123

8. 从右边第几个字符开始，一直到结束。

复制代码 代码如下:

echo ${var:0-7}

表示从右边第七个字符开始，一直到结束。
结果是：123.htm

注：（左边的第一个字符是用 0 表示，右边的第一个字符用 0-1 表示）

Shell 字符串处理、获取文件名和后缀名
 【http://www.lichaozheng.info/2012/03/20/shell-获取文件名和后缀名/】
代码：
file=”thisfile.txt”
echo “filename: ${file%.*}”
echo “extension: ${file##*.}”
输出：
filename: thisfile
extension: txt
附：
Bash字符串处理
基于Pattern Matching的子串替换
${STR/$OLD/$NEW}
替换第一个。
${STR//$OLD/$NEW}
替换所有。
注意：不能使用正则表达式，只能使用?*的Shell扩展。只能用shell通配符如 * ?  [list] [!list] [a-z]。
${STR/#$OLD/$NEW}
替换开头。如果STR以OLD串开头，则替换。
${STR/%$OLD/$NEW}
替换结尾。如果STR以OLD串结尾，则替换。
 
[user@laptop ~]# STR=”Hello World” 
[user@laptop ~]# echo ${STR/o/O} 
HellO World
[user@laptop ~]# echo ${STR//o/O} 
HellO WOrld
[user@laptop ~]# STR=”Hello World” 
[user@laptop ~]# echo ${STR/#He/he} 
hello World
[user@laptop ~]# echo ${STR/#o/he} 
Hello World
[user@laptop ~]# echo ${STR/%He/he} 
Hello World
[user@laptop ~]# echo ${STR/%ld/lD} 
Hello WorlD
 
如果被替换串包含/字符，那么要转义，写成\/。
 
[user@laptop ~]# filename=”/user/admin/monitoring/process.sh” 
[user@laptop ~]# echo ${filename/#\/user/\/tmp} 
/tmp/admin/monitoring/process.sh
[user@laptop ~]# echo ${filename/%.*/.ksh} 
/user/admin/monitoring/process.ksh
[user@laptop ~]#
 
将环境变量PATH的各个目录分开，每行显示一个。
echo -e ${PATH/:/\n}
 
[user@laptop ctmw]# echo $PATH 
/usr/kerberos/sbin:/usr/kerberos/bin:/usr/apache/apache-ant-1.7.1/bin:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/user/bin
[user@laptop ctmw]# echo -e ${PATH//:/’\n’} 
/usr/kerberos/sbin
/usr/kerberos/bin
/usr/apache/apache-ant-1.7.1/bin
/usr/local/sbin
/usr/local/bin
/sbin
/bin
/usr/sbin
/usr/bin
/user/bin
[user@laptop ctmw]# echo “${PATH//:/$’\n’}” 
/usr/kerberos/sbin
/usr/kerberos/bin
/usr/apache/apache-ant-1.7.1/bin
/usr/local/sbin
/usr/local/bin
/sbin
/bin
/usr/sbin
/usr/bin
/user/bin
 
基于Pattern Matching的子串删除
子串删除是一种特殊的替换
${STR/$SUB}
将STR中第一个SUB子串删除
${STR//$SUB}
将STR中所有SUB子串删除
${STR#$PREFIX}
去头，从开头去除最短匹配前缀
${STR##$PREFIX}
去头，从开头去除最长匹配前缀
${STR%$SUFFIX}
去尾，从结尾去除最短匹配后缀
${STR%%$SUFFIX}
去尾，从结尾去除最长匹配后缀
注意：经常会记错#和%的含义，有一个帮助记忆的方法
看一下键盘，#在$之前，%在$之后，就知道#去头，%去尾。
注意：不能使用正则表达式，只能使用?*的Shell扩展。
 
[user@laptop ~]# STR=”Hello World” 
[user@laptop ~]# echo ${STR#He} 
llo World
[user@laptop ~]# echo ${STR#He*o} 
World
[user@laptop ~]# echo ${STR##He*o} 
rld
[user@laptop ~]# PREFIX=”*o” 
[user@laptop ~]# echo ${STR#$PREFIX} 
World
[user@laptop ~]# echo ${STR##$PREFIX} 
rld
[user@laptop ~]# echo ${STR%o*} 
Hello W
[user@laptop ~]# echo ${STR%%o*} 
Hell
[user@laptop ~]# SUFFIX=”o*” 
[user@laptop ~]# echo ${STR%$SUFFIX} 
Hello W
[user@laptop ~]# echo ${STR%%$SUFFIX} 
Hell
 
典型应用：得到文件的扩展名
[user@laptop ~]# FILE=hello.jpg 
[user@laptop ~]# echo ${FILE##*.} 
jpg
 
使用sed命令实现正则表达式替换
使用sed命令可以进行正则表达式的替换。
echo “$STR” | sed “s/$OLD/$NEW/”
将STR中的OLD子串替换成NEW。
 
[user@laptop ~]# STR=”123456789″ 
[user@laptop ~]# echo “$STR” | sed s/345/OK/ 
12OK6789
[user@laptop ~]# OLD=345 
[user@laptop ~]# NEW=OK 
[user@laptop ~]# echo “$STR” | sed “s/$OLD/$NEW/” 
12OK6789
 
使用tr命令实现字符集合的替换
使用tr命令可以实现字符的替换，并且可以是从一批字符到另一批字符的替换。比如小写字母变成大写字母，或者反过来。
 
[user@laptop ~]# echo “bash” | tr “[a-z]” “[b-z]” 
cbti
上面的命令是将原串中的a替换成b，被替换成c，以此类推。
 
网上问题：Linux中 有没有一个命令可以将 字符串中出现的 +或者- 替换成对应的-或者+  即 “+” ——> “-”  “-”——>”+”  例如 GMT+8-9变成 GMT-8+9
 
[user@laptop ~]# echo “GMT+8-9″ | sed ‘s/-/#/g’ | sed ‘s/+/-/g’ | sed ‘s/#/+/g’ 
GMT-8+9
上面是网上提供的答案。如果用tr来实现，更简洁些。 
[user@laptop ~]# echo “GMT+8-9″ | tr “+-” “-+” 
GMT-8+9
 
路径字符串的处理
dirname ${FULLPATH}
取目录部分。
basename ${FULLPATH}
取文件名部分。
basename ${FULLPATH} ${EXT}
取文件名部分，并且去掉指定的扩展名。
[user@laptop ~]# FULLPATH=/user/work/project/backup.tar.gz 
[user@laptop ~]# dirname “$FULLPATH” 
/user/work/project
[user@laptop ~]# basename “$FULLPATH”    
backup.tar.gz
[user@laptop ~]# basename “$FULLPATH” .gz 
backup.tar
[user@laptop ~]# basename “$FULLPATH” .tar 
backup.tar.gz
[user@laptop ~]# basename “$FULLPATH” .tar.gz 
backup
取目录部分：${FULLPATH%/*}    
（类似 dirname “$FULLPATH”）
取文件名称：FILE=${FULLPATH##*/}
（类似 basename “$FULLPATH”）
取最短基本名称：${FILE%%.*}
取最长基本名称：${FILE%.*}
取最短扩展名：${FILE##*.}  或者  ${FULLPATH##*.}
取最长扩展名：${FILE#*.}  或者  ${FULLPATH#*.}
 
[user@laptop ~]# FULLPATH=/user/work/project/backup.tar.gz 
[user@laptop ~]# echo ${FULLPATH%/*} 
/user/work/project
[user@laptop ~]# dirname “$FULLPATH” 
/user/work/project
[user@laptop ~]# FILE=${FULLPATH##*/} 
[user@laptop ~]# echo $FILE 
backup.tar.gz
[user@laptop ~]# basename “$FULLPATH” 
backup.tar.gz
[user@laptop ~]# echo ${FILE%%.*} 
backup
[user@laptop ~]# echo ${FILE%.*} 
backup.tar
[user@laptop ~]# echo ${FILE##*.} 
gz
[user@laptop ~]# echo ${FILE#*.} 
tar.gz


