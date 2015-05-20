__author__ = 'dellcs'

from pandas import *

ser = Series(np.arange(4), index=['a', 'b', 'c', 'd'])

df = DataFrame(np.arange(8).reshape(4, 2), index=['a', 'b', 'c', 'd'], columns=['A', 'B'])

print(ser.tolist())
print(ser.values)
print(type(ser.values))
print(ser.values.tolist())

print(df.ix[1].values.tolist())
print(df)
print(df.count(axis=1))

print(df.index.values[1])

s = df.index.values.tolist()
print(s)
s.insert(0, 'insert')
print(s)