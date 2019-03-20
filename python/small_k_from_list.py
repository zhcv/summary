x = [int(i) for i in input().split()]
k = x.pop()
x.sort()
print(' '.join(list(map(str,x[:k]))))
