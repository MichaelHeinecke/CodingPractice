from collections import Counter

if __name__ == '__main__':

    input()  # number of shoes; not further needed
    inventory = Counter([int(i) for i in input().split(' ')])
    num_customers = int(input())
    revenue = 0

    for _ in range(num_customers):
        size, potential_revenue = [int(i) for i in input().split(' ')]
        if size in inventory and inventory.get(size) > 0:
            revenue += potential_revenue
            inventory.subtract({size: 1})

    print(revenue)
