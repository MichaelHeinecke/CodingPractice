def rolling_average(data, value_col):
    l = 0
    res = []
    s = 0

    for r in range(len(data)):
        s += data[r][value_col]
        num_rows = r - l + 1
        rolling_avg = round(s / num_rows, 1)
        res.append({"date": data[r]["date"], "rolling_avg": rolling_avg})
        if num_rows == 7:
            s -=  data[l][value_col]
            l += 1

    return res


if __name__ == '__main__':
    data = [
        {"date": "2024-01-01", "active_users": 100},
        {"date": "2024-01-02", "active_users": 120},
        {"date": "2024-01-03", "active_users": 130},
        {"date": "2024-01-04", "active_users": 90},
        {"date": "2024-01-05", "active_users": 150},
        {"date": "2024-01-06", "active_users": 110},
        {"date": "2024-01-07", "active_users": 140},
        {"date": "2024-01-08", "active_users": 160},
        {"date": "2024-01-09", "active_users": 180},
    ]

    print(rolling_average(data, "active_users"))

# [
#     {"date": "2024-01-01", "rolling_avg": 100.0},                     # (100) / 1
#     {"date": "2024-01-02", "rolling_avg": 110.0},                     # (100+120)/2
#     {"date": "2024-01-03", "rolling_avg": 116.7},                     # (100+120+130)/3
#     {"date": "2024-01-04", "rolling_avg": 110.0},                     # (100+120+130+90)/4
#     {"date": "2024-01-05", "rolling_avg": 118.0},                     # (100+120+130+90+150)/5
#     {"date": "2024-01-06", "rolling_avg": 115.0},                     # (100+120+130+90+150+110)/6
#     {"date": "2024-01-07", "rolling_avg": 120.0},                     # (100+120+130+90+150+110+140)/7
#     {"date": "2024-01-08", "rolling_avg": 128.6},                     # (120+130+90+150+110+140+160)/7
#     {"date": "2024-01-09", "rolling_avg": 137.1},                     # (130+90+150+110+140+160+180)/7
# ]
