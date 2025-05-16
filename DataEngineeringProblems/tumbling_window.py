import json
import pprint
from collections import defaultdict
from datetime import datetime, timedelta

DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


def parse_events_from_file(file_path: 'str') -> list[dict]:
    with open(file_path, 'r') as f:
        data = f.read()

    events = []
    try:
        events.extend(json.loads(data))
    except Exception as e:
        print(e)

    return events


def assign_event_to_window(
        event_dt: datetime, window_duration_in_minutes: int) -> datetime:
    """Assigning event to window by nearest window lower bound."""
    start_minute = ((event_dt.minute // window_duration_in_minutes)
                    * window_duration_in_minutes)
    window_lower_bound = event_dt.replace(minute=start_minute, second=0, microsecond=0)
    return window_lower_bound


def aggregate_events_by_window(
        events: list[dict],
        window_duration_in_minutes: int
) -> list[dict]:
    windows = defaultdict(lambda: {
        'unique_users': set(),
        'total_events': 0
    })

    for event in events:
        event_timestamp = datetime.fromisoformat(event['timestamp'])
        window_key = assign_event_to_window(event_timestamp, window_duration_in_minutes)
        window = windows[window_key]
        window['unique_users'].add(event['user_id'])
        window['total_events'] += 1

    agg_windows = []
    for start_time, window in windows.items():
        end_time = start_time + timedelta(minutes=window_duration_in_minutes)
        agg_windows.append({
            'start_time': datetime.strftime(start_time, DATETIME_FORMAT),
            'end_time': datetime.strftime(end_time, DATETIME_FORMAT),
            'unique_users': len(window['unique_users']),
            'total_events': window['total_events']
        })

    return agg_windows


if __name__ == '__main__':
    # parse events
    # assign to window by window start time
    # auxiliary data structure: {start_time: {number_of_events, set_of_users}}
    # aggregate windows

    path_to_file = './events.json'
    window_duration_mins = 15
    event_data = parse_events_from_file(path_to_file)
    aggregated_events = aggregate_events_by_window(event_data, window_duration_mins)
    pprint.pprint(aggregated_events)
