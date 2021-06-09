# ubuntu无法添加PPA的解决办法

使用apt-get安装软件经常需要先添加PPA，这样才能下载到apt-cache以外的软件。

然而，我在输入"sudo add-apt-repository ppa:xxx"以后，会遇到两个问题：1. 长时间没有响应； 2，添加失败(ERROR: user or team does not exist)

以上主要由两种原因导致：1. CA证书损坏；2. 没有绕过代理；

我们先重装一遍CA证书：

sudo apt-get install --reinstall ca-certificates
如果还不行，我们就绕过代理，加一个"-E"：

sudo -E add-apt-repository --update ppa:ubuntu-toolchain-r/test
我采用上述2步，解决了困扰我好几个月的问题~

非常感谢这篇文章：https://blog.bflyer.com/2016/03/27/Fix-Cannot-Add-PPA-Error-In-Ubuntu-14-04-Linux-Mint-17/
