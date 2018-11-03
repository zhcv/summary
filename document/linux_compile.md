1.查看当前是否已经打开了此开关
  通过命令：ulimit -c 如果输出为 0 ，则代表没有打开。如果为unlimited则已经打开了,就没必要在做打开。
  2.通过命令打开
   ulimit -c unlimited .然后通过步骤1，可以监测是否打开成功。
   3.如果你要取消，很简单：ulimit -c 0 就可以了
   通过上面的命令修改后，一般都只是对当前会话起作用，当你下次重新登录后，还是要重新输入上面的命令，所以很麻烦。我们可以把通过修改 /etc/profile文件 来使系统每次自动打开。
   步骤如下：
   1.首先打开/etc/profile文件
   一般都可以在文件中找到 这句语句：ulimit -S -c 0 > /dev/null 2>&1.ok，根据上面的例子，我们只要把那个0 改为 unlimited 就ok了。然后保存退出。
   2.通过source /etc/profile 使当期设置生效。
   3.通过ulimit -c 查看下是否已经打开。
# 打开内核调试
ulimit -c unlimited

# git video
[link]:(https://classroom.udacity.com/)
zhp@sina.com passwd:90zhp
