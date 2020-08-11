def count_substring(string, sub_string):
    n =0 
    l = len(string)
    l2 = len(sub_string)
    l3 = l - (l2-1)
    s = ''
    for i in range(l3):
        for j in range(i,i+l2):
            s += string[j]
        if s == sub_string:
            n += 1
        s = ''
    return n

if __name__ == '__main__':
    s = input()
    sb = input()
    n = count_substring(s, sb)
    print(n)