# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(n):
    nesA = int(input())
    esA = set(input().split())
    nesB = int(input())
    esB = set(input().split())
    print(esA.issubset(esB))