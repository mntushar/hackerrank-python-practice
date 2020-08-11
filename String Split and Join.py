def split_and_join(line):
    line = line.split()
    l = ''
    for i in line:
        l = l + i + '-'
    l = l[:-1]
    return l

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)