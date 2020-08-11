def print_formatted(number):
    number = number
    start = 1
    width = len(bin(number)[2:])
    while start<=number:
        print(' '.join(map(lambda x: x.rjust(width), [str(start), oct(start)[2:], hex(start)[2:].upper(), bin(start)[2:]])))
        start += 1
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)