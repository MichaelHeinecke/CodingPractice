import string

def print_rangoli(size):
    alphabet_index = size
    lower_bound = alphabet_index - 1

    rangoli_list = []
    alphabet = list(string.ascii_lowercase)

    for row in range(alphabet_index):

        letters = alphabet[lower_bound:alphabet_index]
        letters = letters[:-(alphabet_index-lower_bound):-1] + letters
        row = '-'.join(letters)
        # row = row[:lower_bound-1:-1] + row
        rangoli_list.append(row)
        lower_bound -=1

    width = len(rangoli_list[-1])
    [print(row.center(width, "-")) for row in rangoli_list]
    [print(row.center(width, "-")) for row in rangoli_list[-2::-1]]

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
