from math import atan2
from math import degrees

ab = float(input())
bc = float(input())

print(str(round(degrees(atan2(ab, bc)))) +'°')
