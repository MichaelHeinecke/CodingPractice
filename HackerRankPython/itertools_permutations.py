import itertools

S, k = input().split()
k = int(k)

def tuple_to_string(tuple):
    string_lst = [str(i) for i in tuple]
    return ''.join(string_lst)


[print(tuple_to_string(i)) for i in sorted(itertools.permutations(S, k))]