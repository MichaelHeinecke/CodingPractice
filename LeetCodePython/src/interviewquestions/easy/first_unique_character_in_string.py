import collections


def firstUniqChar(s: str) -> int:
    counter = collections.Counter(s)

    for index, char in enumerate(s):
        if counter.get(char) == 1:
            return index

    return -1
