def count_substring(string, sub_string):
    n =0 
    l = len(string)
    for i in range(l):
        if string[i:].startswith(sub_string):
            n += 1
    return n

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)