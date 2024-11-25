from collections import deque


def bfs_shortest_path(park_map, start, end):
    # Directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    visited = set()
    visited.add(start)
    steps = 0

    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if (x, y) == end:
                return steps

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(park_map) and 0 <= ny < len(park_map[0]) and (nx, ny) not in visited:
                    if park_map[nx][ny] != '#':  # Check if it's not a barrier
                        visited.add((nx, ny))
                        queue.append((nx, ny))

        steps += 1

    return -1  # If we exhaust the queue without finding the exit


# Read input
N, M = map(int, input().split())
park_map = [input().strip() for _ in range(N)]

# Find the positions of 'E' and 'X'
start = end = None
for i in range(N):
    for j in range(M):
        if park_map[i][j] == 'E':
            start = (i, j)
        elif park_map[i][j] == 'X':
            end = (i, j)

# Calculate the shortest path
result = bfs_shortest_path(park_map, start, end)

# Output the result
print(result)