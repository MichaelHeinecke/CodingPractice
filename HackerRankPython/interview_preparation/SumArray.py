# Problem
# Identify whether there exists a pair of numbers in an array such that their sum is equal to N.
#
# Input: The first line contains one integer N, which is the sum we are trying to find. The second line contains one integer M, which is the length of the array. This is followed by M lines each containing one element of the array.
#
# Output: Output 1 if there exists a pair of numbers in the array such that their sum equals N. If such a pair does not exist, output 0.
#
# Sample Input:
#
# 66
# 10
# 18
# 11
# 21
# 28
# 31
# 38
# 40
# 55
# 60
# 62
# Sample Output:
#
# 1

from itertools import combinations


def find_sum(sum_to_find, list_of_numbers):
    combs = list(combinations(list_of_numbers, 2))
    sums = [sum(tup) for tup in combs]
    print(sums)

    if sum_to_find in sums:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    # N, M = [int(i) for i in input().split(' ')]
    # print(N, M)
    #
    # numbers = []
    # for i in range(M):
    #     numbers.append(int(input()))

    value = 66
    numbers = [10, 18, 11, 21, 28, 31, 38, 40, 55, 60, 62]

    find_sum(value, numbers)

