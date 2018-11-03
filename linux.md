File synchronous update
=======================

rsync -zvp -r --delete imaging/ zhp@180.167.46.105:/home/zhp/imaging/


## File recheck repetition with hash
find -not -empty -type f -printf "%s\n" | sort -rn |uniq -d | xargs -I{} -n1 find -type f -size {}c -print0 | xargs -0 md5sum | sort | uniq -w32 --all-repeated=separate | cut -b 36- > result.txt

# wenjian tong bu geng xin
rsync -zvp -r --delete zhp@180.167.46.105:/home/zhp/bodydata /data/homezh/bodypart/

# rm remote repository *.pyc
git status | grep pyc | sed -e 's/    new file:   //g' | xargs -I {} git rm --cached {}
find . -name '*.pyc' -exec git rm {} \;

# mysql cha xun zhiding ziduan chongfu wenjian
SELECT * FROM `bodypart_prob_new` WHERE filename in (select FILENAME from bodypart_prob_new group by FILENAME having count(1) > 1)))
ls -l |grep "^-"|wc -l

或
find ./company -type f | wc -l
查看某文件夹下文件的个数，包括子文件夹里的。
ls -lR|grep "^-"|wc -l
查看某文件夹下文件夹的个数，包括子文件夹里的。
ls -lR|grep "^d"|wc -l
说明：
ls -l
长列表输出该目录下文件信息(注意这里的文件，不同于一般的文件，可能是目录、链接、设备文件等)
grep "^-"
这里将长列表输出信息过滤一部分，只保留一般文件，如果只保留目录就是 ^d
wc -l
统计输出信息的行数，因为已经过滤得只剩一般文件了，所以统计结果就是一般文件信息的行数，又由于
一行信息对应一个文件，所以也就是文件的个数。

查找gpu 用户进程
this will list processes that have NVIDIA GPU device nodes open
sudo fuser -v /dev/nvidia*

清除指定用户所有进程
pkill -u zhp

1.服务器端口转发本地.
ssh -L 16006:127.0.0.1:6006 zhp@180.167.46.105

2.在服务器上使用6006端口正常启动tensorboard：
tensorboard --logdir=xxx --port=6006

3.在本地浏览器中输入地址：
127.0.0.1:16006


统计文件夹下文件数量包含子文件下的
ls -lR | grep "^-" | wc -l


mysql 
create VIEW tb.beijing_part_test_2 as SELECT * FROM tb_000002.vbeijing_test WHERE id in (SELECT id from tb.beijing_part_test_4)

# 查看监听端口
# netstat  -tnl

# vim
# 空格换成行, 逗号换成行
:%s/ /\r/g
:%s/,/\r/g
:%s/xx/^M/g  (^M的输入方法是：先按CTRL+V，松开然后按回车键）)

# 修改普通用户名
```
su - 或 su - root（到root用户下。 注意要使用su -，原因见下文）
usermod  -l  新用户名  -d  /home/新用户名  -m  老用户名
注意：网上有些人方法是usermod -l 新用户名 老用户名，

但这种方法只改了表面，你用pwd命令看一下，路径还是之前的用户名。
```
--------------------- 
