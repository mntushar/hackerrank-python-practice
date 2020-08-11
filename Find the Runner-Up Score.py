if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max_v = max(arr)

    for i in range(len(arr)):
        if max_v == max(arr):
            arr.remove(max_v)

    lent = len(arr)
    print(lent)
    print(arr[lent-1])
    print(max(arr))

    
    

