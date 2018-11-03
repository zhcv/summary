def twosum(target, lists):
    for i, num in enumerate(lists):
        if target - num in lists:
            return i, lists.index(target-num)


if __name__ == '__main__':
    lists = [2,3,4,5,7,9]
    target = 11
    print twosum(target, lists)
