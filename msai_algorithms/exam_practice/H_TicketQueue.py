from heapq import heappush, heappop


def solve():
    # Read input
    n, k = map(int, input().split())
    times = list(map(int, input().split()))

    # Initialize priority queue for windows
    # Each element is (time_when_window_becomes_free, window_number)
    windows = []

    # Process first K people
    person_idx = 0
    while person_idx < min(k, n):
        heappush(windows, (times[person_idx], person_idx))
        person_idx += 1
        print(windows)
    # Process remaining people
    while person_idx < n:
        # Get earliest free window
        cur_time, _ = heappop(windows)
        # Add next person to this window
        heappush(windows, (cur_time + times[person_idx], person_idx))
        person_idx += 1

    # Final answer is when the last person finishes
    result = max(time for time, _ in windows)
    print(result)


if __name__ == "__main__":
    solve()