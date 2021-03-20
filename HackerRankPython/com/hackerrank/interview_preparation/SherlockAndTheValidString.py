from collections import Counter


def string_check(s):
    letter_counter = Counter(s)
    occurrences_set = set(letter_counter.values())

    if len(occurrences_set) == 1:
        return "YES"
    elif len(occurrences_set) > 2:
        return "NO"
    else:
        max_occ = max(letter_counter.values())
        min_occ = min(letter_counter.values())
        if list(letter_counter.values()).count(min_occ) == 1:
            return "YES"
        if list(letter_counter.values()).count(max_occ) > 1 or max_occ - min_occ > 1:
            return "NO"
        return "YES"


if __name__ == '__main__':
    # strings = ['aabbccddeefghi', 'abcdefghhgfedecba', 'aaaabc']
    strings = ['aaaabc']

    [print(string_check(string)) for string in strings]
