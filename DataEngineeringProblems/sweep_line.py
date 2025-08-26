def max_concurrent_viewers(views):
    start_events = [(e[0], 1) for e in views]
    end_events = [(e[1], -1) for e in views]
    all_events = start_events + end_events
    sorted_events = sorted(all_events, key=lambda e: (e[0], e[1]))

    max_viewers = 0
    viewers = 0
    time_ranges = []
    current_start = None
    for ts, delta in sorted_events:
        prev_viewers = viewers
        viewers += delta

        # Viewer joins
        # Viewers increase over prev max viewers
        if viewers > max_viewers:
            time_ranges.clear()
            max_viewers = viewers
            current_start = ts
        # Viewers joins, count equal to prev max viewers
        elif viewers == max_viewers and delta == 1:
            current_start = ts

        # Viewer leaves
        # Close max period
        if prev_viewers == max_viewers and viewers < max_viewers:
            time_ranges.append((current_start, ts))
            current_start = None

    return max_viewers, time_ranges


if __name__ == '__main__':
    # max_concurrent = 2
    # time_ranges = [(5, 10), (12, 15), (18, 20)]

    views = [(0, 10), (5, 15), (12, 20), (18, 25)]
    print(max_concurrent_viewers(views))