# Enter your code here. Read input from STDIN. Print output to STDOUT
n1 = int(input())
e = set(input().split())
n2 = int(input())
f = input().split()
u = e.union(f)
print(len(u))