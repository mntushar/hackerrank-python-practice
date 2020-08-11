if __name__ == '__main__':
    mark_sheet = []
    mark = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        mark_sheet.append([name,score])
        mark.append(score)

    
    s = set(mark)
    l = list(s)
    l.sort()
    c = l[1]
    
    for a, d in sorted(mark_sheet):
        if c == d:
            print(a)