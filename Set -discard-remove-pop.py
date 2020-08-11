n = int(input())
s = set(map(int, input().split()))
cn = int(input())
ss = 0
for i in range(cn):
    c = input().split()
    if c[0] == 'pop':
        s.pop()
    elif c[0] == 'remove':
        s.remove(int(c[1]))
    elif c[0] == 'discard':
        s.discard(int(c[1]))
for i in s:
    ss += i
print(ss)

