# Enter your code here. Read input from STDIN. Print output to STDOUT


m = int(input())
mv = set(map(int, input().split()))
n = int(input())
nv = set(map(int, input().split()))
t = mv.difference(nv)
t.update(nv.difference(mv))
s = sorted(t)
[print(i) for i in s]
