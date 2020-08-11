import textwrap

def wrap(string, max_width):
    result = ''
    l = len(string)
    l2 = 0
    while l2<l:
        result += string[l2:l2+max_width]
        l2 += max_width
        result += '\n'


    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)