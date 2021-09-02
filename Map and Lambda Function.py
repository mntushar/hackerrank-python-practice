cube = lambda x: pow(x,3)# complete the lambda function 

def fibonacci(n):
    l = [0,1]
    for i in range(2,n):
        l.append(l[i-2] + l[i-1])
    return(l[0:n])

if __name__ == '__main__':
    n = int(input())
    print(map(cube, fibonacci(n)))