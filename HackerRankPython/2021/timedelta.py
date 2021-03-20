#!/bin/python3

import datetime as dt
import os


# Complete the time_delta function below.
def time_delta(t1, t2):
    t1 = dt.datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2 = dt.datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    return int(abs(dt.timedelta.total_seconds(t1 - t2)))


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        print(str(delta) + '\n')
