# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict


n, m = map(int, input().split())
d = defaultdict(list)
mlist = []


for i in range(0, n):
    d[input()].append(i+1)


for i in range(0, m):
    mlist.append(input())


for i in mlist:
    if i in d:
        print(' '.join(map(str, d[i])))
    else:
        print(-1)