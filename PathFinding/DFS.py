num_node = 5
graph =  [
    [1, 2], #neighbors node that connects node 0
    [0, 4],
    [0, 3],
    [1, 2, 4],
    [1, 2, 3],
]

count = 0 #label when visit that node
components = [-1] * num_node #value each node before is visited, set to -1
visited = [False] * num_node #set node isn't visited is False

def FindComponets():
    global count
    for i in range(num_node):
        #check node is visited (not visit, count +1)
        if not visited[i]:
            count += 1
            DFS(i)
    return count, components

def DFS(at):
    visited[at] = True
    components[at] = count #label when node is visited
    print(f"Visited node {at}, Componet node {components}, count {count}")
    #go to next node
    for next in graph[at]:
        if not visited[next]:
            DFS(next)

start_node = 0
DFS(start_node)
FindComponets()