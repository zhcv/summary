def isPlalind(s):
    if len(s) == 1:
        return True
    else:
        return s[0] == s[-1] and isPlalind(s[1:-1])

if __name__ == '__main__':
    while(True):
        x = input('enter your string:')
        print(isPlalind(x))
