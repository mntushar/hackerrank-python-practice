# method 1
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    s = ''.join(l)
    return s

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)



# method 2
def mutate_string(string, position, character):
    string = string[:position]+character+string[position+1:]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)