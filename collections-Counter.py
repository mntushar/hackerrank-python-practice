# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter


s_n = int(input())
s_s = Counter(map(int, input().split()))
c_n = int(input())
t_money = 0


for i in range(c_n):
    size, money = map(int, input().split())
    if s_s[size]:
        t_money += money
        s_s[size] -= 1


print(t_money)
