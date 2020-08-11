# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import  permutations


s, k = input().split()
a = list(permutations(s, int(k)))
a.sort()

for i in a:
    print(''.join(i))