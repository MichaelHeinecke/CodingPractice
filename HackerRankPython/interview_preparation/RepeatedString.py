#!/bin/python3

import math
import os
import random
import re
import sys
import math

# Complete the repeatedString function below.
def repeatedString(s, n):
    letterCount = 0
    occurrences = 0

    occurrences = s.count('a')

    rep = math.floor(n / len(s))
    occurrences *= rep

    remainder = n % len(s)
    if remainder > 0:
        occurrences += s.count('a', 0, remainder + 1)

    return occurrences


if __name__ == '__main__':
    s = input()
    n = int(input())

    result = repeatedString(s, n)

    print(result)
