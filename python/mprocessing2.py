# 进程池 ,Pool中是有return的
import multiprocessing as mp

def job(x):
    return x ** 2

def multiprocess():
    pool = mp.Pool()  # 默认是有几个核就用几个，可以自己设置processes = ？
    res = pool.map(job, range(10))  # 可以放入可迭代对象，自动分配进程
    print(res)
    # apply_async(func[, args[, kwds[, callback]]]) 它是非阻塞，apply(func[, args[, kwds]])是阻塞的
    res = pool.apply_async(job, (2,))  # 一次只能在一个进程里计算，要达到map的效果，要迭代
    print(res.get())

    multi_res = [pool.apply_async(job, (i,)) for i in range(10)]  # 迭代器
    print([res.get() for res in multi_res])


if __name__ == "__main__":
    multiprocess()
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# 4
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
