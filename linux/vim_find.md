1.{}和之间有一个空格 
2.find . -name 之间也有空格 
3.exec 是一个后续的命令,{}内的内容代表前面查找出来的文件

 
linux下批量删除空文件（大小等于0的文件）的方法
find . -name "*" -type f -size 0c | xargs -n 1 rm -f

用这个还可以删除指定大小的文件，只要修改对应的 -size 参数就行，例如：

find . -name "*" -type f -size 1024c | xargs -n 1 rm -f

   

就是删除1k大小的文件。（但注意不要用 -size 1k，这个得到的是占用空间1k，不是文件大小1k的）。
查询出所有的空文件夹

find -type d -empty

列出搜索到的文件  删除文件
find . -name "test.txt" 

     
批量删除搜索到的文件 
find . -name "shuaige.txt" |xargs rm -rf

删除前有提示 
find . -name "test.txt" -ok rm -rf {} ;  

删除当前目录下面所有 test 文件夹下面的文件 

find . -name "test" -type d -|rm -rf {} ;

注://删除文件夹下面的所有的.svn文件
find . -name '.svn' | rm -rf {} ;


# vim删除空行和注释
* [html](http://jpuyy.com/2015/06/vim-delete-lines-using-regexp.html)

# 删除空行

:g/^$/d

# 删除空行以及只有空格的行

:g/^\s*$/d

# 删除以 # 开头或 空格# 或 tab#开头的行

:g/^\s*#/d

# 对于 php.ini 配置文件，注释为 ; 开头

:g/^\s*;/d

# 使用正则表达式删除行,如果当前行包含 bbs ，则删除当前行

:/bbs/d

# 删除从第二行到包含 bbs 的区间行

:2,/bbs/d

删除从包含 bbs 的行到最后一行区间的行

:/bbs/,$d

删除所有包含 bbs 的行

:g/bbs/d

删除匹配 bbs 且前面只有一个字符的行

:g/.bbs/d

删除匹配 bbs 且以它开头的行

:g/^bbs/d

删除匹配 bbs 且以它结尾的行

:g/bbs$/d

.ini 的注释是以 ; 开始的，如果注释不在行开头，那么删除 ; 及以后的字符

:%s/\;.\+//g

删除 # 之后所有字符

%s/\#.*//g

# vim usage

remove jishu hang
:g/^/+1 d
:%nork jkdd


remove oushu hang
:g/^/d|m

:%norm jdd

# awk print 倒数第一列
cat images.list | awk -F '/' '{print $(NF)}'
# 倒数第二列
cat images.list | awk -F '/' '{print $(NF-1)}'
