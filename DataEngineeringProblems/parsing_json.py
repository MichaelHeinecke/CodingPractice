# Task:
# Parse the JSON payload.
# Group activities by user_id.
# For each user, summarize:
# Total number of activities
# The first event timestamp
# The last event timestamp
# Output a dictionary (or JSON) with the aggregated information.
import json
from collections import defaultdict
from datetime import datetime

def aggregate_events(event_data: list[dict[str, str]]) -> dict[str, dict[str, int | datetime]]:
    agg = defaultdict(lambda: {
        'total_activities': 0,
        'first_event': None,
        'last_event': None,
    })

    for e in event_data:
        user = e.get('user_id',)
        event = e.get('event')
        timestamp_str = e.get('timestamp')
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%SZ")

        agg_user = agg[user]
        agg_user['total_activities'] += 1
        agg_user['first_event'] = timestamp if not agg_user['first_event'] else min(timestamp, agg_user['first_event'])
        agg_user['last_event'] = timestamp if not agg_user['last_event'] else max(timestamp, agg_user['last_event'])

    return agg

if __name__ == '__main__':
    with open('events.json', 'r') as f:
        data = f.read()

    res = aggregate_events( json.loads(data))
    print(res)
