def is_special(s):
    # check if all letters are the same
    if len(set(s)) == 1:
        return 1
    elif len(s) % 2 == 0:
        return 0

    # all are the same but the one in the middle
    without_middle_char = s[0:len(s) // 2] + s[len(s) // 2 + 1:]
    if len(set(without_middle_char)) == 1:
        return 1
    else:
        return 0


def substrCount(n, s):
    special_count = 0

    # list of all possible substrings
    substrings = (s[i: j] for i in range(len(s))
           for j in range(i + 1, len(s) + 1))

    for substr in substrings:
        special_count += is_special(substr)

    return special_count


if __name__ == '__main__':

    string = 'mononopoo' \
         ''
    print(substrCount(len(string), string))