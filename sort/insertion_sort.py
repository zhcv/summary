

def insert_sort(s):
    """Insertion Sort, switch from back to front until t > s[index]"""
    n = len(s)
    for i in range(1, n):
        while i >= 1:
            print s
            if s[i] < s[i-1]:
                s[i-1], s[i] = s[i], s[i-1]
            i -= 1
    return s


def insert_sort2(s):
    """Find insert index
    s[index] = t
    if j >= index: s[j+1] = s[j]
    """
    n = len(s)
    for i in range(1, n):
        if s[i] < s[i-1]:
            t = s[i]
        
            index = i
            for j in range(i-1, -1, -1):
                if s[j] > t:
                    s[j+1] = s[j]
                    index = j
                else:
                    break
            s[index] = t

    return s

if __name__ == '__main__':
    a = [5,4,34,33,12,18,32,21,11,3,2,1]
    print insert_sort2(a) 
