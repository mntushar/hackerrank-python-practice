# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for i in range(n):
    try:
        re.compile(input())
        is_valid = True
    except re.error:
        is_valid = False

    print(is_valid)
