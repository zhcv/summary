
quick_sorts = (lambda array: array if len(array) <= 1 
    else quick_sort([item for item in array[1:] 
    if item <= array[0]]) + [array[0]] + quick_sort([item for item in array[1:] 
    if item > array[0]]))

"""
def quick_sort(s, l, r):
    # s : array, l: left_value, r: right_value
    if l > r:
        return
    low = l
    high = r
    key = s[low]
    while l < r:
        while l < r and s[r] > key:
            r -= 1
        s[l] = s[r]
        while l < r and s[l] <= key:
            l += 1
        s[r] = s[l]
    s[r] = key
    quick_sort(s, low, l-1)
    quick_sort(s, l+1, high)


def quick_sort(array, l, r):
    '''Algorithm introduction'''
    if l < r:
        q = partition(array, l, r)
        quick_sort(array, l, q-1)
        quick_sort(array, q+1, r)

def partition(array, l, r):
    x = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i+1]
    return i + 1
"""

def quick_sort(array, l, r):
    '''implementation non-recursive quicksort with stack'''
    if l >= r:
        return 
    stack = []
    stack.append(l)
    stack.append(r)

    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high - low <= 0:
            continue
        x = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i+1], array[high] = array[high], array[i+1]
        stack.extend([low, i, i+2, high])

    
if __name__ == '__main__':
    a = [3,1,9,25,4, 15,2,23,6]
    quick_sort(a, 0, len(a)-1)
    print a

