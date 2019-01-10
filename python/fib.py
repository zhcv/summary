#coding:utf-8

class Fib():
    def __init__(self):
        pass
    def __call__(self, num):
        a, b = 0, 1
        self.l = []

        for i in range(num):
            self.l.append(i)
            a, b = b, a+b
        return self.l
    def __str__():
        return str(self.l)
    __rept__ = __str__


if __name__ == '__main__':
    f = Fib()
    print f(10)

    
