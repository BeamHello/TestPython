from collections import deque

num_node = 5
neighbours_node =  [
    [1, 2],
    [0, 4],
    [0, 3],
    [1, 4],
    [1, 2, 3]
]

def BFS(start, end):
    prev = slove(start)
    return reconstuctPath(start, end , prev)

def slove(start):
    queue = deque([start])

    visited = [False] * num_node
    visited[start] = True

    prev = [None] * num_node
    while queue:
        node = queue.popleft()
       
        for neighbour in neighbours_node[node]:
            if not visited[neighbour]:
                queue.append(neighbour)
                visited[neighbour] = True
                prev[neighbour] = node
    return prev

def reconstuctPath(start, end , prev):
    path = []
    at = end
    while at is not None:
        path.append(at)
        at = prev[at]
    path.reverse()

    if path[0] == start:
        return path
    return[]


start_node = 0
end_node = 3
path = BFS(start_node, end_node)
print("Path from", start_node, "to", end_node, ":", path)