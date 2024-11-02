from queue import Queue

num_node = 5
graph =  [
    [1, 2], #neighbors node that connects node 0
    [0, 4],
    [0, 3],
    [1, 2, 4],
    [1, 2, 3],
]

def BFS(start, end):
    global prev
    prev = slove(start)
    return reconstuctPath(start, end , prev)

def slove(start):
    queue = Queue()
    queue.put(start) #enqueue start node

    visited = [False] * num_node
    visited[start] = True

    prev = [None] * num_node
    #check queue is not empty
    while not queue.empty():
        print("queue: ", list(queue.queue))
        node = queue.get() #dequeue node
        print("node:", node)
        neighbours = graph[node] #get neighbour of currrent node
        #go to next neighbour
        for next in neighbours:
            if not visited[next]:
                queue.put(next) #enqueue neighbour
                visited[next] = True
                prev[next] = node
    return prev

def reconstuctPath(start, end , prev):
    #backtrack path
    path = []
    at = end
    while at is not None:
        at = prev[at]
        path.append(at)
    path.reverse()
    #check path start with start node
    if path[0] == start:
        return path
    return[]

start_node = 0
end_node = 4
BFS(start_node, end_node)
print(f"Path from {start_node} to {end_node}")