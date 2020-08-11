import itertools

(K, N) = map(int, input().strip().split(' '))

# reading the K lines and appending lists to 'L'
L = list()
for i in range(K):
    l = list(map(int, input().strip().split(' ')))
    n = l[0]
    L.append(l[1:])
    assert len(L[i]) == n
S_max = 0


# Looping through Cartesian product of list and getting max sum.
for l in itertools.product(*L):
    s = sum([x**2 for x in l]) % N
    if s > S_max:
        S_max = s
        

print(S_max)