import heapq

graph = {
    0: [{'to': 1, 'cost': 3}],
    1: [{'to': 2, 'cost': 1}, {'to': 3, 'cost': 3}],
    2: [{'to': 3, 'cost': 3}],
    3: [{'to': 4, 'cost': 4}],
    4: []
}

num_node = 5
start_node = 0
end_node = 4

def Dijkstra(graph, num_node, start):
    visited = [False] * num_node
    dist = [float('inf')] * num_node
    dist[start] = 0
    prev = [None] * num_node

    priority_queue = []
    heapq.heappush(priority_queue, (0, start)) #enqueue

    while len(priority_queue) != 0: #priority_queue size != 0
        minValue, index = heapq.heappop(priority_queue) #dequeue (node:index, short dist:minValue)
        visited[index] = True
        if dist[index] < minValue:
            continue
        for edge in graph[index]:
            if visited[edge['to']]:
                continue
            newDist = dist[index] + edge['cost'] #dist to neighbour + cost
            #update: short dist, previous node
            if newDist < dist[edge['to']]:
                dist[edge['to']] = newDist
                prev[edge['to']] = index
                heapq.heappush(priority_queue, (newDist, edge['to'])) #enqueue
    return dist, prev

def findShortesrPath(graph, num_node, start, end):
    dist, prev = Dijkstra(graph, num_node, start)
    path = []

    if dist[end] == float('inf'): #check dist to end is infinity
        return path
    #reconstruct path: backtrack end to start
    at = end
    while at is not None:
        path.append(at)
        at = prev[at]
    path.reverse()
    return path

distance, _ = Dijkstra(graph, num_node, start_node)
shortest_path = findShortesrPath(graph, num_node, start_node, end_node)
print("Summary shortest distance:", distance[end_node])
print("Shortest node path:", shortest_path)