if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    mark = student_marks[query_name]
    num = len(mark)
    per = 0.0
    for i in mark:
        per = per + i

    per = per/num
    print(format(per, '.2f'))

