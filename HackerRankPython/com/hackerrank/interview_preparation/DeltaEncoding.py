# Problem
# Given a list of numbers, e.g.:
#
# 25626 25757 24367 24267 16 100 2 7277 Output a delta encoding for the sequence. In a delta encoding,
# the first element is reproduced as is. Each subsequent element is represented as the numeric difference from the
# element before it. E.g. for the sequence above, the delta encoding would be:
#
# 25626 131 -1390 -100 -24251 84 -98 7275 However, if a difference value does not fit in a single signed byte,
# i.e. -127 <= x <= 127, then, instead of the difference, we would like to use an escape token, printing it.
#
# This will denote that the value following the escape token is a full four-byte difference value, rather than a
# one-byte different value.
#
# For this exercise, we'll declare -128 as the escape token.
#
# Following the same example above, the final result would be:
#
# 25626 -128 131 -128 -1390 -100 -128 -24251 84 -98 -128 7275


def get_escape_sequence(list_of_numbers, token):
    escaped = [list_of_numbers[0]]

    for idx in range(1, len(list_of_numbers)):
        num = list_of_numbers[idx] - list_of_numbers[idx - 1]
        # escaped.append(num)
        if num < -127 or num > 127:
            escaped.append(token)

        escaped.append(num)

    return escaped


if __name__ == '__main__':
    ESCAPE_TOKEN = -128

    list_of_numbers = [25626, 25757, 24367, 24267, 16, 100, 2, 7277]

    seq = get_escape_sequence(list_of_numbers, ESCAPE_TOKEN)
    print(" ".join([str(item) for item in seq]))
