if __name__ == '__main__':
    N = int(input())

    l = []
    for i in range(N):
        token = input().split()
        if token[0] == 'insert':
            l.insert(int(token[1]), int(token[2]))
        elif token[0] == 'print':
            print(l)
        elif token[0] == 'remove':
            l.remove(int(token[1]))
        elif token[0] == 'append':
            l.append(int(token[1]))
        elif token[0] == 'sort':
            l.sort()
        elif token[0] == 'pop':
            l.pop()
        elif token[0] == 'reverse':
            l.reverse()


