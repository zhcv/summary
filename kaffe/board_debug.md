#### 安装nfs文件系统
在开发调试过程中，我们需要在linux服务器上安装nfs，以便开发代码可以mount到板子来运行。

```
sudo apt-get install nfs-kernel-server          //install sw

sudo apt-get install nfs-common             //install sw

sudo service nfs-kernel-server restart              // Start service
```

#### 使nfs目录生效

sudo mkdir xx/xx/nfs   //创建一个目录

路径以及nfs目录名由自己指定

这个目录下的内容将来会被mount到板子上

sudo vi /etc/exports 并且添加一行：/home/tt/nfs      *(rw,sync,no_root_squash)

exportfs -rf  来使得上面nfs目录设置生效。

板子网络配置
板子插上网线，上电后，在板子的shell里面输入ifconfig

如果显示eth0  192.168.1.100，说明kernel已经将板子自动配置成一个IP了

这时，一定要输入 ping linux服务器ip来验证板子和服务器网络通信是否正常。我这边服务器ip是192.168.0.121，它们不在一个网段，是ping不通的。我这里将板子ip进行了修改（比如ifconfig eth0 192.168.0.100）就能ping通了。

回到第二步，如果ifconfig完后，啥也没有显示，可以考虑下面的命令来进行配置：

```
ip link set eth0 up
ip addr add 192.168.1.40/24 dev eth0
ip route add default via 192.168.1.1
ip route show     
```

将服务器上的nfs目录mount到板子上

```
mount -t nfs 192.168.0.121:/xx/xx/nfs /nfsroot -o nolock
```



该命令就是将前面步骤中服务器上创建的目录mount到板子的/nfsroot。