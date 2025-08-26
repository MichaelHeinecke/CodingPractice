from functools import reduce


if __name__ == '__main__':

    data = [(0, 15), (20, 30)]

    print(reduce(lambda x, y: x[1] - x[0] + y[1] - y[0], data))