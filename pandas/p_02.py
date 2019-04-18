from __future__ import print_function

import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])


print("df", df)

print

print("df[:3]", df[:3])

print("df.loc['20130102']\n", df.loc['20130102'])

print("df[df.A > 8]", df[df.A > 8])

print("df.ix[:3,['A','C']]\n", df.ix[:3,['A','C']])

"""
print()

print("df['A']\n", df['A'])

print("df.A\n", df.A)

print("=" * 80)

print(df[0:3], df['20130102':'20130104'])

# select by label: loc
print(df.loc['20130102'])
print(df.loc[:,['A','B']])
print(df.loc['20130102', ['A','B']])

# select by position: iloc
print(df.iloc[3])
print(df.iloc[3, 1])
print(df.iloc[3:5,0:2])
print(df.iloc[[1,2,4],[0,2]])

# mixed selection: ix
print(df.ix[:3, ['A', 'C']])
# Boolean indexing
print(df[df.A > 0])

"""
