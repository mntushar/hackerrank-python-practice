from itertools import groupby
S = input()
for k, g in groupby(S):
    m = len(list(g)), int(k)
    print(m, end=' ')