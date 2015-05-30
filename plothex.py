#!/usr/bin/env python

import matplotlib.pyplot as plt
import sys

index = []
point = []
trash = []
hexPoint = []

def populateVectors(item):
  if len(item) == 8:
    pass
  elif len(item) == 2:
    hexPoint.append(item)
  elif len(item) > 8:
    trash.append(item)

with open(sys.argv[1], 'r') as f:
  for line in f:
    handle = line.split(' ')
    for x in handle:
      populateVectors(x)

for x in hexPoint:
  try:
    point.append(int(x, 16))
  except ValueError:
    pass

k = 0
for item in point: 
  index.append(int(k))
  k +=1

plt.plot(index, point, )
plt.show()
