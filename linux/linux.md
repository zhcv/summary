# wenjian tong bu geng xin
rsync -zvp -r --delete imaging/ zhp@180.167.46.105:/home/zhp/imaging/
# rsync specify port
rsync -arvz -e 'ssh -p 22222' file zhp@117.40.83.208:/home/zhp

# wenjian hash cha chong
find -not -empty -type f -printf "%s\n" | sort -rn |uniq -d | xargs -I{} -n1 find -type f -size {}c -print0 | xargs -0 md5sum | sort | uniq -w32 --all-repeated=separate | cut -b 37- > result.txt

# recurrsive computer file md5 value
find dir -type f -print0 | xargs -0 md5sum > dir.md5  
# wenjian tong bu geng xin 
* 注意源目录斜杠， 不加斜杠表示 源目录放在目标目录内，加上斜杠 两个目录等价
rsync -zvp -r --delete zhp@180.167.46.105:/home/zhp/bodydata /data/homezh/bodypart/


## ls 命令
1、列出当前目录的文件、文件夹完整路径
ls -1 |awk '{print i$0}' i=`pwd`'/'
find `pwd` -maxdepth 1 -type f -print



##2、列出当前目录及子目录的文件、文件夹完整路径
ls -R |awk '{print i$0}' i=`pwd`'/'

##2b） 列出当前目录及子目录下的文件夹完整路径
ls -FR | grep /$ | sed "s:^:`pwd`/:"

##3、用find实现，好像运行要慢些
find / -name "*.*" -exec ls {} \;

##4、递归列出当前目录及子目录名称
ls -FR | grep /$

##5、递归列出当前目录及子目录名称，包括相关属性
ls -lR | grep "^d"
# drwxr-xr-x 3 idea idea 4096 Aug 2 2009 images

##6、只列出当前目录下的子目录 用ls只列出子目录
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

## 查找连个文件内同名文件
for f in `find folder1 -type f | awk -F "/" '{print $NF}'`;do find folder2: -type f -iname "$f" | awk -F "/" '{print $NF}';done > result.txt

find `pwd` -type f | perl -nle 's/(.*\/)/\1 /;print' | sort -k2 | uniq -f 1 -D | sed -e 's/ //' >> result.txt

find . -type f | perl -nle 's/(.*\/)/\1 /;print' | sort -k2 | uniq -f 1 -D | sed -e 's/ //' > result





## I think you can kill the uninterruptable processes by running 
$ sudo kill -HUP 1. 

## It will restart init without ending the running processes and after running it, 
## my uninterruptable processes were gone.
## awk cut string
$ find `pwd` -type f -print | awk -F '/' '{print $8}'

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


## curl Post
curl -v -include --form "jpgfile=@1.2.410.200048.776.20171109073139.1.1.1.jpg" http://117.40.83.208:8927/tb

# mysql 查重语句
select filename, count(*) as count from `chinaset_test` group by filename having count>1 
# utf8 code
# alter table `imageq` modify reasion varchar(30) character set utf8

# linux 换行符 convert windows  换行符
cat result.txt | cut -c 36- | tr -s '\n'  


# DCM file to jpg fast method
convert dcm_file jpg_file


# RGB image ---> gray image
convert input.jpg -colorspace Gray output.jpg
convert -type Grayscale input-picture.png output-picture.png
mogrify -type Grayscale input-picture.png
## overwrite 'my-pics-grayscale/*'? 
 mogrify -type Grayscale /home/user/my-pics-grayscale/*
 ======================================================

# gray image ---> color image
$ convert input.jpg -colorspace sRGB -type truecolor result.jpg

# To make the make the black pixels transparent and keeps the white pixels as they are
# convert source.png -alpha copy -fx '#fff' result.png
# make the white pixels transparent while keeping the black as-is
# convert source.png -alpha copy -channel alpha -negate +channel -fx '#000' result.png


# 查找所有的jpg 文件，并且压缩它们：
* $ find . -type f -name "*.jpg" -print | xargs tar -czvf images.tar.gz

# 假如你有一个文件包含了很多你希望下载的URL，你能够使用xargs下载所有链接：
* $  cat url-list.txt | xargs wget -c

# 统计文件行数
find . -type f | xargs wc -l
find . -name *.java | xargs wc -l

# 统计目录结构
 tree -L 1 -F -C dir
*//


# VPN-set
Browser: chrome / firefox Web ---> 
Extension: 
[SwithchyOmega](https://github.com/FelisCatus/SwitchyOmega)
