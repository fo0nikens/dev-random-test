#!/usr/bin/env python

import matplotlib.pyplot as plt
import sys
import os

infile = sys.argv[1]
f = open(infile,"r")
x = []
x2 = []
x3 = []
v = []

for line in f:
  x += line.split(' ')

k = 1
for item in x:
  if len(item) > 3:
    pass
  else:
    x2.append(item.strip('\n'))
    v.append(int(k))
    k += 1

for item in x2:
  x3.append(int(item,16))

# lenth check
#print(len(x2))
#print(len(v))

# ensure no newline characters remain in x2 vector
#for item in x2:
 # print(item)

plt.plot(v,x3)
plt.show()
