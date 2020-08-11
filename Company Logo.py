#!/bin/python3

import math
import os
import random
import re
import sys
import collections



if __name__ == '__main__':
    s = sorted(input().strip())
    s = collections.Counter(s).most_common()
    for i in range(0, 3):
        print(s[i][0], s[i][1])
    