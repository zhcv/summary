#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

random.seed(40)

print random.random() # Randomly generated a number between [0, 1)
print random.randint(1, 10)  # [1, 10]
print random.uniform(0.5, 0.98) # Random generated a float number [a, b]
print random.choice('tensorflow') 
print random.randrange(1, 100, 2) # Generare a int number, step 2, in [1,3,5,...,99]


for i in range(100):
    pass

a = [1, 3, 5, 6, 7]
random.shuffle(a)

print a
