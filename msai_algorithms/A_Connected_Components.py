def find_connected_components(N, edges):
    from collections import defaultdict, deque

    # Create an adjacency list for the graph
    graph = defaultdict(list)
    for v, u in edges:
        graph[v].append(u)
        graph[u].append(v)

    visited = [False] * N
    components = []

    def bfs(start):
        queue = deque([start])
        component = []
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            component.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return component

    for vertex in range(N):
        if not visited[vertex]:
            component = bfs(vertex)
            components.append(component)

    return components

# Read input
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

# Find connected components
components = find_connected_components(N, edges)

# Output the results
print(len(components))
for component in components:
    print(len(component))
    print(" ".join(map(str, component)))