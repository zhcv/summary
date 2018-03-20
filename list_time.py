from timeit import timeit

def list_append():
    nums = 10 ** 8
    list1 = []
    for i in range(nums):
        list1.append(i)


def list_insert():
    nums = 10 ** 8
    list2 = []
    for i in range(nums):
        list2.insert(0, i)

if __name__ == '__main__':
    ## timeit(function_name_string, runtime_environment_string, number=run_number)
    t1 = timeit('list_append()', 'from __main__ import list_append', number=10)
    print t1
    t2 = timeit('list_append()', 'from __main__ import list_append', number=10)
    print t2
