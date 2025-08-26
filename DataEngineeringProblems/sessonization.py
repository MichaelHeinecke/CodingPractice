from collections import defaultdict


def sessionize(logs: list[dict], id_key: str, timestamp_key: str, session_gap) -> list[dict]:
    d = defaultdict(list)

    for r in logs:
        k = r[id_key]
        v = r[timestamp_key]
        if k in d:
            last_interval = d[k][-1]
            if session_gap <= v - last_interval[-1]:
                d[k].append([v])
            else:
               last_interval.append(v)
        else:
            d[k].append([v])

    return [{id_key: k, "sessions": v} for k, v in d.items()]


if __name__ == '__main__':
    # Input: user activity logs
    logs = [
        {"user": "u1", "ts": 1},
        {"user": "u1", "ts": 2},
        {"user": "u2", "ts": 7},
        {"user": "u1", "ts": 10},
        {"user": "u2", "ts": 10},
    ]

    print(sessionize(logs, "user", "ts",  5))

    # Define a "session" as gap <= 5 mins
    # Output: 2 sessions for u1: [1,2] and [10]