n = int(input())
phoneBook = {}
query_name_lst = []

for _ in range(n):
    k, v = input().split()
    phoneBook[k] = v

for _ in range(10 ** 5):
    try:
        query_name = input()
        if query_name is not None:
            query_name_lst.append(query_name)
    except(EOFError):
        break

for query_name in query_name_lst:
    if query_name in phoneBook.keys():
        print(f'{query_name}={phoneBook[query_name]}')
    else:
        print('Not found')