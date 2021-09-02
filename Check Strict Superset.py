a = set(input().split())
n = int(input())
o = True

for i in range(n):
    b = set(input().split())
    if not b.issubset(a):
        o = False
    if len(b) >= len(a):
        o = False

print(o)