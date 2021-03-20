from collections import Counter


def twoStrings(s1, s2):
    chars1 = Counter(s1)
    chars2 = Counter(s2)

    if chars1 - chars2 != chars1:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    twoStrings('aardvark', 'apple')