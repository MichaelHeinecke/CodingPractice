def deduplicate_by(records: list[dict], key: str) -> list[dict]:
    d = {}

    for r in records:
        if r[key] not in d:
            d[r[key]] = r

    return [v for _, v in d.items()]

if __name__ == '__main__':
    records = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 1, "name": "Alice Dup"},
    ]

    group_by = "id"

    print(deduplicate_by(records, group_by))

# Deduplicate by "id" → keep first occurrence
# Output: [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
