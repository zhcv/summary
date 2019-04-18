import pandas as pd
import numpy as np


data = np.array(['a', 'b', 'c', 'd'])


s = pd.Series(data, index=None)
print s


da = {'a' : 0., 'b' : 1., 'c' : 2.}

ss = pd.Series(da)
print ss


data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])

print s
