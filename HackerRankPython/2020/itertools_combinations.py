import itertools

S, k = input().split()
k = int(k)

def tuple_to_string(tuple):
    string_lst = [str(i) for i in tuple]
    return ''.join(string_lst)

def generate_combinations(string, k):
    lst = []
    for length in range (1, k+1):
        lst.extend(itertools.combinations(sorted(string), length))
    return lst

[print(tuple_to_string(i)) for i in generate_combinations(S, k)]
