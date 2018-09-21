# wenjian tong bu geng xin
rsync -zvp -r --delete imaging/ zhp@180.167.46.105:/home/zhp/imaging/


# wenjian hash cha chong
find -not -empty -type f -printf "%s\n" | sort -rn |uniq -d | xargs -I{} -n1 find -type f -size {}c -print0 | xargs -0 md5sum | sort | uniq -w32 --all-repeated=separate | cut -b 36- > result.txt

# wenjian tong bu geng xin 
# 注意源目录斜杠， 不加斜杠表示 源目录放在目标目录内，加上斜杠 两个目录等价
rsync -zvp -r --delete zhp@180.167.46.105:/home/zhp/bodydata /data/homezh/bodypart/


## ls 命令
1、列出当前目录的文件、文件夹完整路径
ls -1 |awk '{print i$0}' i=`pwd`'/'
find `pwd` -maxdepth 1 -type f -print



2、列出当前目录及子目录的文件、文件夹完整路径
ls -R |awk '{print i$0}' i=`pwd`'/'

2b） 列出当前目录及子目录下的文件夹完整路径
ls -FR | grep /$ | sed "s:^:`pwd`/:"

3、用find实现，好像运行要慢些
find / -name "*.*" -exec ls {} \;

4、递归列出当前目录及子目录名称
ls -FR | grep /$

5、递归列出当前目录及子目录名称，包括相关属性
ls -lR | grep "^d"
# drwxr-xr-x 3 idea idea 4096 Aug 2 2009 images

6、只列出当前目录下的子目录
用ls只列出子目录
ls -d */


# git 删除远程垃圾文件

git rm 遠程文件
git rm *.pyc --cached
git commmit -a -m'remove pyc from index'
git push


find . -name '*.pyc' | xargs -n 1 git rm --cached && git commit -m "remove pyc file from index" && git push


# find file from computer in linux system
#1
for i in `cat dcm.txt`;do locate $i ;done >> dcm_path.txt

#2
for i in `cat dcm.txt`;do locate $i | awk '{print $0}';done >> result.txt

# 查找连个文件内同名文件
for f in `find folder1 -type f | awk -F "/" '{print $NF}'`;do find folder2: -type f -iname "$f" | awk -F "/" '{print $NF}';done > result.txt

find `pwd` -type f | perl -nle 's/(.*\/)/\1 /;print' | sort -k2 | uniq -f 1 -D | sed -e 's/ //' >> result.txt

find . -type f | perl -nle 's/(.*\/)/\1 /;print' | sort -k2 | uniq -f 1 -D | sed -e 's/ //' > result





 ## I think you can kill the uninterruptable processes by running 
 sudo kill -HUP 1. 
 ## It will restart init without ending the running processes and after running it, 
 ## my uninterruptable processes were gone.
# awk cut string
find `pwd` -type f -print | awk -F '/' '{print $8}'

# linux process Based on feedback by sigjuice command
ps axopid,comm,wchan


# 批量修改当前目录文件扩展名
rename 's//.c//.h/' ./*

# 批量递归修改文件扩展名
find ./ -name "*.c" | awk -F "." '{print $2}' | xargs -i -t mv ./{}.c  ./{}.h



# ssh免密码登录 
ssh user@host 'mkdir -p .ssh && cat >> .ssh/authorized_keys' < ~/.ssh/id_rsa.pub
# ssh specify file name 
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" -f $HOME/.ssh/id_rsa

# xunhuan
B=" "
for i in `cat valChina.txt`;do echo $i$B${i:0-5:1};done > val_China.txt
