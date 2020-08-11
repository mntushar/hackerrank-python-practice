# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict


n = int(input())
dic = OrderedDict()
for i in range(n):
    w = input()
    if w in dic:
        dic[w] += 1
    else:
        dic[w] = 1
print(len(dic))
[print(dic[i], end=' ') for i in dic]