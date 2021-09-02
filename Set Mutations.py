# Enter your code here. Read input from STDIN. Print output to STDOUT
na = int(input())
a = set(map(int, input().split()))
n = int(input())
for i in range(n):
    ope = input().split()
    u = set(map(int, input().split()))
    if ope[0] == 'intersection_update':
        a.intersection_update(u)
    elif ope[0] == 'update':
        a.update(u)
    elif ope[0] == 'symmetric_difference_update':
        a.symmetric_difference_update(u)
    elif ope[0] == 'difference_update':
        a.difference_update(u)

print(sum(a))

