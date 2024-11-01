num_node = 5
neighbours_node =  [
    [1, 2],
    [0, 4],
    [0, 3],
    [1, 4],
    [1, 2, 3]
]
count = 0
components = [-1] * num_node
visited = [False] * num_node

def FindComponets():
    global count
    for i in range(num_node):
        if not visited[i]:
            count += 1
            DFS(i)
    return count, components

def DFS(at):
    if visited[at]:
        return
    visited[at] = True
    #print(f"Visited node {at}")
    #neighbours = neighbours_node[at]
    #for next in neighbours:
    #    DFS(next)
    components[at] = count
    print(f"Visited node {at}, Componet node {components}, count {count}")
    for next in neighbours_node[at]:
        if not visited[next]:
            DFS(next)

#start_node = 0
#DFS(start_node)
FindComponets()