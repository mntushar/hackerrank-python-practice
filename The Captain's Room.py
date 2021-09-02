# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
m = list(map(int, input().split()))
mset = set(m)
print(((sum(mset)*k)-(sum(m)))//(k-1))
