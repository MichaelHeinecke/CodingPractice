from collections import Counter

def makeAnagram(a, b):
    letter_count_a = Counter(a)
    letter_count_b = Counter(b)

    letter_count_diff = (letter_count_a - letter_count_b) + (letter_count_b - letter_count_a)

    diff = 0
    for count in letter_count_diff.values():
        diff += count

    return diff


if __name__ == '__main__':
    a = 'camel'
    b = 'ample'

    print(makeAnagram(a, b))


