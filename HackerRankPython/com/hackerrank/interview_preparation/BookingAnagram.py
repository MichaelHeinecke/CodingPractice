# Problem: An anagram is a word that can be written as a permutation of the characters of another word, like "dirty
# room" and "dormitory" (ignore spaces). However, "the" and "thee" are not anagrams, since "the" only has a single
# "e" whereas "thee" has two "e" characters (spaces can occur zero, or multiple times, however.)
#
# Given a list of words as strings, you should return another list of strings, each containing words that are mutual
# anagrams.
#
# Each string of the output should be a single group of anagrams joined with commas.
#
# Within an output string, the expression should be sorted lexicographically. If a group contains only a single
# element, output that one-element group as a single string. And the string should be also output in lexicographical
# order. Given e.g.:
#
# pear
# amleth
# dormitory
# tinsel
# dirty room
# hamlet
# listen
# silnet
# ... the output would be:
#
# amleth,hamlet
# dirty room,dormitory
# listen,silnet,tinsel
# pear

from collections import defaultdict


def clean_word(word):
    word = word.replace(' ', '').lower()
    return word


def find_anagrams(words):
    d = defaultdict(list)

    for word in words:
        key = "".join(sorted(clean_word(word)))
        d[key].append(word)

    d = dict(d)
    anagrams = sorted([sorted(lst) for lst in d.values()])

    return anagrams


if __name__ == '__main__':
    list_of_words = ['pear', 'amleth', 'dormitory', 'tinsel', 'dirty room', 'hamlet', 'listen', 'silnet']

    # list_of_words = ["hi", "hello", "bye", "helol", "abc", "cab", "bac", "silenced", "licensed", "declines"]

    anagrams_lst = find_anagrams(list_of_words)

    [print(",".join(ana)) for ana in anagrams_lst]
