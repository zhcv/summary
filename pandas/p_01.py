import pandas as pd
import numpy as np


s = pd.Series([1, 3, 6, np.nan, 44, 1])

print s

print 

dates = pd.date_range('20160101', periods=6)
print dates

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])

print df
print "=" * 80

print df['d']

# help(pd.DataFrame)

df1 = pd.DataFrame(data=np.arange(12).reshape(3, 4))

print df1

print "=" * 80

df2 = pd.DataFrame({'A': 1,
    'B': pd.Timestamp('20130102'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(['test', 'train', 'test', 'train']),
    'F': 'foo',
    'G': pd.date_range('20160101',periods=4)})


print "df2:\n", df2
print "df2.dtypes:\n", df2.dtypes
print "df2.index:\n", df2.index
print "df2.columns:\n", df2.columns
print "df2.values:\n", df2.values

print
print "df2.values type:\n", type(df2.values)

print
print "df2.describe(): \n", df2.describe()


print "df2.T: \n", df2.T

print "df2: \n", df2
print
print "df2.sort_index(axis=1, ascending=False) \n", df2.sort_index(axis=1, ascending=True)
