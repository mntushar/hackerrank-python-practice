def average(array):
    # your code goes here
    se = set(array)
    l = len(se)
    s = sum(se)
    a = s/l
    return a

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)