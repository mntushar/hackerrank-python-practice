# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x = map(int ,input().split())
m = [map(float, input().split()) for i in range(x)]
    
for i in zip(*m):
    print(sum(i)/x)
