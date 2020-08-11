# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
s, k = input().split()
k = int(k)
s = sorted(s)
t = map(''.join, combinations_with_replacement(s, k))
for i in sorted(t):
    print(i)