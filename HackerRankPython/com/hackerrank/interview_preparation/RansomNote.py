#!/bin/python3

# Complete the checkMagazine function below
from collections import Counter


def checkMagazine(magazine, note):
    ran = Counter(note)
    mag = Counter(magazine)

    if len(ran - mag) == 0:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    # magazine = "give me one grand today night".split()
    # note = "give one grand today".split()

    magazine = "o l x imjaw bee khmla v o v o imjaw l khmla imjaw x".split()
    note = "imjaw l khmla x imjaw o l l o khmla v bee o o imjaw imjaw o".split()

    checkMagazine(magazine, note)
