# -*- coding: utf-8 -*-
#使用两种方式创建生成器
a=[100,60,40,20,10,0]
b=[0.01,0.015,0.03,0.05,0.075,0.1]

#生成器函数
def f(x):
    for i in range(len(a)):
        if n>a[i]:
            #生成器推导式
            c=(a[j]-a[j+1] for j in range(i,len(a)-1))
            break
    r=sum(map(lambda x,y:x*y,b[i:],[(n-a[i])]+list(c)))
    yield r*10000

k=int(input("是否继续计算奖金？是：1， 否：0\n"))
while k:
    n=int(input('请输入利润，单位(万元):'))
    print '应发奖金为:', next(f(n)), '元'
    print()
    k=int(input("是否继续计算奖金？是：1， 否：0\n"))
print('感谢使用，程序结束！')
