import re
from collections import OrderedDict


def read_purchases():
    purchases = OrderedDict()

    number_purchases = int(input())

    for _ in range(number_purchases):
        purchase = input()
        first_digit = re.search("\\d", purchase).start()
        item, revenue = (purchase[:first_digit], int(purchase[first_digit:]))

        purchases[item] = purchases.get(item, 0) + revenue

    return purchases


if __name__ == '__main__':
    purchase_dict = read_purchases()
    [print(k + str(v)) for k, v in purchase_dict.items()]
