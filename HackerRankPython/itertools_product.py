import itertools

A, B = [int(i) for i in input().split()], [int(i) for i in input().split()]

product = itertools.product(A, B)
print(' '.join([str(i) for i in product]))