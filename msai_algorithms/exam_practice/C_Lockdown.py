import sys

sys.setrecursionlimit(200000)


# DFS approach to count reachable cities
def dfs(city, adj_list, visited):
    visited[city] = True
    reachable_count = 1  # Include the city itself
    for neighbor in adj_list[city]:
        if not visited[neighbor]:
            reachable_count += dfs(neighbor, adj_list, visited)
    return reachable_count


def main():
    # Input reading
    N, M, s = map(int, input().split())  # N: number of cities, M: number of roads, s: home city id
    adj_list = [[] for _ in range(N)]  # adjacency list to represent the graph

    # Read all the roads (edges) and construct the graph
    for _ in range(M):
        vi, ui = map(int, input().split())
        adj_list[vi].append(ui)
        adj_list[ui].append(vi)

    # Initialize visited array to keep track of visited cities
    visited = [False] * N

    # Call DFS or BFS from the home city `s`
    result = dfs(s, adj_list, visited)

    # Output the result (number of reachable cities)
    print(result)


# Run the solution
main()