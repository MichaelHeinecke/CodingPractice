def compute_total_unique_time_watched(events: list[tuple]) -> int:
    """Returns the unique time watched across the intervals.

    Merges overlapping intervals to guarantee only unique time
    watched is considered.
    """
    events.sort(key=lambda e: e[0])
    unique_time_watched = 0

    if not events:
        return unique_time_watched

    curr_start, curr_end = events[0]

    for i in range(1, len(events)):
        next_start, next_end = events[i]
        # No overlap
        if curr_end < next_start:
            unique_time_watched += curr_end - curr_start
            curr_start, curr_end = next_start, next_end
    # Overlap
        else:
            curr_end = max(curr_end, next_end)

    # Last interval
    unique_time_watched += curr_end - curr_start

    return unique_time_watched


if __name__ == '__main__':
    no_intervals = []
    print(compute_total_unique_time_watched(no_intervals))

    single_interval = [(1, 5)]  # Expected result: 4
    print(compute_total_unique_time_watched(single_interval))

    overlapping_intervals = [(1,5), (2,3), (6,8), (7,11)]  # Expected result: 9
    print(compute_total_unique_time_watched(overlapping_intervals))

    touching_edges = [(1,5), (2,3), (6,8), (8,11)]  # Expected result: 9
    print(compute_total_unique_time_watched(touching_edges))

    duplicate_intervals = [(1,5), (1, 5), (6,8)]  # Expected result: 6
    print(compute_total_unique_time_watched(duplicate_intervals))
