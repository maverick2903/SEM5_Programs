
from collections import deque

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfid(graph, start, depth, visited=None):
    if visited is None:
        visited = set()
    if depth > 0:
        print(start, end=' ')
        visited.add(start)
        for neighbor in graph[start]:
            if neighbor not in visited:
                dfid(graph, neighbor, depth - 1, visited)

# Example usage:

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage:
print("\nBFS traversal:")
bfs(graph, 'A')
print("\nDFID traversal:")
dfid(graph, 'A', 2)
print("\nDFS traversal:")
dfs(graph, 'A')
