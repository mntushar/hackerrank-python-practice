import string
def print_rangoli(size):
    size = size
    alphabet = string.ascii_lowercase[:size]
    
    height = size * 2 - 1
    width = size * 4 - 3
    lines = [None] * height
    for i in range(size):
        sub_alphabet = alphabet[(-i - 1):]
        letters = ''.join(reversed(sub_alphabet)) + sub_alphabet[1:]
        lines[i] = lines[-i - 1] = '-'.join(letters).center(width, '-')
    
    print(*lines, sep='\n')
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)