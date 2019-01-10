#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import numpy as np

def primer(maxNum):
    # calculate Number inner all primer number
    num = [2]
    for i in range(3, maxNum, 2):
        max_root = int(math.sqrt(i) + 1)
        for j in range(2, max_root):
            if i % j == 0:
                break
        else:
            num.append(i)
    return num

print primer(100)

N = 100
print [p for p in range(2, 100) if 0 not in [p%i for i in range(2, int(math.sqrt(p) + 1))]]

print [p for p in range(2, 100) if not [m for m in range(2, p) if p%m == 0]][::-1]


def primer_n(n):
    if n == 2:
        print n
        return n
    else:
        for i in range(2, n):
            if n%i == 0:
                break
        else:
            print n,
    primer_n(n-1)

primer_n(100)
