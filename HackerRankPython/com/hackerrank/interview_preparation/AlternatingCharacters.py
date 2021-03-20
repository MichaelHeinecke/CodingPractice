def alternatingCharacters(s):
    deletions = 0

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            deletions += 1

    return deletions


if __name__ == '__main__':
    strings = ['BABABA', 'AAABBB']

    [print(alternatingCharacters(string)) for string in strings]
