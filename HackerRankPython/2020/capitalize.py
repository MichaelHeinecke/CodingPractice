#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return s.title()

def solve_re(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                  lambda mo: mo.group(0).capitalize(),
                  s)

def solve_long(s):

    def capitalize(word):
        first_char = word[:1]
        rest_chars = word[1:]

        if first_char.isalpha():
            first_char = first_char.capitalize()

        return first_char + rest_chars

    words = re.split(r'(\s+)', s)
    capitalized_lst = [capitalize(word) for word in words]
    return ''.join(capitalized_lst)

if __name__ == '__main__':
    # s = input()
    # s = '1 w 2 r 3g'
    s = 'hello   world  lol'
    print(solve(s))
    print(solve_re(s))
    print(solve_long(s))
