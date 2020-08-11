# Enter your code here. Read input from STDIN. Print output to STDOUT
e_n = int(input())
e_r = input().split()
e_r = set(e_r)
f_n = int(input())
f_r = input().split()
print(len(e_r.symmetric_difference(set(f_r))))