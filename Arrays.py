import numpy

def arrays(arr):
    a = numpy.array(arr,float)
    l = a[::-1]
    return l

arr = input().strip().split(' ')
result = arrays(arr)
print(result)