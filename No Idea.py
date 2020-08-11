# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
na = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
h = 0
for i in na:
    if i in a:
        h += 1
    if i in b:
        h += -1 
print(h)
