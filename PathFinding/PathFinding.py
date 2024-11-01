import pygame

WIDTH, HEIGHT = 800, 600
NODE_COLOR = 'blue'
EDGE_COLOR = 'orange'
VISITED_COLOR = 'green'
VISITED_COLOR_EDGE = 'yellow'

## ------- Pygame Setup ------------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)
running = True
## ---------------------------------

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
node_pos = [
    (400, 100),
    (200, 280),
    (600, 280),
    (700, 500),
    (100, 500)
]
visit_step = []
current_stap = 0
delay_time = 1000
time = pygame.time.get_ticks()

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

def Draw_Graph():
    for i, neighbours in enumerate(neighbours_node):
        '''if visited[i]:
            edge_color = VISITED_COLOR_EDGE
        else:
            edge_color = NODE_COLOR'''
        for neighbour in neighbours:
            if visited[i] and visited[neighbour]:
                edge_color = VISITED_COLOR_EDGE
            else:
                edge_color = EDGE_COLOR
            pygame.draw.line(screen, edge_color, node_pos[i], node_pos[neighbour], 10)
    for i, (x, y) in enumerate(node_pos):
        if visited[i]:
            color = VISITED_COLOR
        else:
            color = NODE_COLOR
        pygame.draw.circle(screen, color, (x, y), 50)
        label = font.render(str(i), True, 'black')
        screen.blit(label, (x - 5, y - 10))

#start_node = 0
#DFS(start_node)
FindComponets()

## ------- Game Loop ------------
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("gray")

    Draw_Graph()

    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()