# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict


n = int(input())
item_a = []
ordered_dictionary = OrderedDict()
for i in range(n):
    item, price = input().rsplit(' ', 1)
    ordered_dictionary[item] = ordered_dictionary.get(item, 0)+int(price)
[print(i, ordered_dictionary[i]) for i in ordered_dictionary]