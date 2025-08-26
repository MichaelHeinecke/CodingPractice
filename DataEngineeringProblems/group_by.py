from collections import defaultdict

def sum_group_by(records: list[dict], grouping_key: str, value_key: str) -> list[dict]:
    agg = defaultdict(int)

    for r in records:
        agg[r[grouping_key]] += r[value_key]

    return [
        {grouping_key: k, value_key: v} for k, v in agg.items()
    ]

if __name__ == '__main__':
    records = [
        {"user": "u1", "amount": 100},
        {"user": "u2", "amount": 50},
        {"user": "u1", "amount": 30},
    ]

    group_by = "user"
    agg_col = "amount"

    print(sum_group_by(records, group_by, agg_col))

    # Desired output
    # [{"user": "u1", "total": 130}, {"user": "u2", "total": 50}]
