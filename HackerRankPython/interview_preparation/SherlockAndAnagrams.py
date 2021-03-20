from collections import Counter


def sherlockAndAnagrams(s):
    slices = (tuple(sorted(s[i: j])) for i in range(len(s))
              for j in range(i + 1, len(s) + 1) if len(s[i: j]) < len(s))

    slices_counter = Counter(slices)
    res = 0
    for count in slices_counter.values():
        res += int(count * (count - 1) / 2)

    return res


if __name__ == '__main__':
    s = 'ifailuhkqq'
    result = sherlockAndAnagrams(s)

    print(result)
