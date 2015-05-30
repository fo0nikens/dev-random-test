#!/usr/bin/env python

import matplotlib.pyplot as plt
import sys

infile = sys.argv[1]
f = open(infile,"r")
x = []
x2 = []
v = []

k = 1
for line in f:
  line_list = line.split(' ')
  relevant = line_list[-(len(line_list)-1)::]
  x += relevant
  v.append(int(k))
  k += 1

for item in x:
  x2.append(int(item,8))

# lenth check
#print(len(x2))
#print(len(v))

# ensure no newline characters remain in x2 vector
#for item in x2:
 # print(item)

plt.plot(v,x2)
plt.show()
