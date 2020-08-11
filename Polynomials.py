import numpy
p = list(map(float, input().split()))
x = float(input())
print(numpy.polyval(p, x))