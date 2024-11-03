import pygame
from queue import Queue

WIDTH, HEIGHT = 800, 600

# ------- Pygame Setup ------------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)
running = True

class DFS():
    def __init__(self) -> None:
        self.num_node = 5
        self.graph = [
            [1, 2], #neighbors node that connects this node
            [0, 4],
            [0, 3],
            [1, 2, 4],
            [1, 2, 3],
        ]
        self.count = 0 # label
        self.components = [-1] * self.num_node #value each node before is visited, set to -1
        self.visited = [False] * self.num_node #set node isn't visited is False
        self.node_pos = [
            (400, 100),
            (200, 300),
            (600, 300),
            (700, 500),
            (100, 500)
        ]
    
    def findComponents(self):
        for i in range(self.num_node):
                #check node is visited (not visit, count +1)
                if not self.visited[i]:
                    self.count += 1
                    self.dsf(i)
        return self.count, self.components

    def dsf(self, at):
        self.visited[at] = True
        self.components[at] = self.count
        print(f"Visited node {at}, Componet node {self.components}, count {self.count}")
        self.drawGraph()
        pygame.display.update()
        pygame.time.delay(500)

        #go to next node
        for next in self.graph[at]:
            if not self.visited[next]:
                self.dsf(next)

    def drawGraph(self):
        for i in range(self.num_node):
            for neighbour in (self.graph[i]):
                color_edge = "yellow" if self.visited[i] else "black"
                pygame.draw.line(screen, color_edge, self.node_pos[i], self.node_pos[neighbour], 5)
        for i, pos in enumerate(self.node_pos):
            color = "orange" if self.visited[i] else "blue"
            pygame.draw.circle(screen, color, pos, 30)
            node_text = font.render(str(i), True, "white")
            screen.blit(node_text, (pos[0] - node_text.get_width() // 2, pos[1] - node_text.get_height() // 2))

class BFS():
    start_node = 0
    end_node = 4

    def __init__(self) -> None:
        self.num_node = 5
        self.graph = [
            [1, 2], #neighbors node that connects this node
            [0, 4],
            [0, 3],
            [1, 2, 4],
            [1, 2, 3],
        ]

        self.queue = Queue()
        self.visited = [False] * self.num_node
        self.prev = [None] * self.num_node
        
        self.node_pos = [
            (400, 100),
            (200, 300),
            (600, 300),
            (700, 500),
            (100, 500)
        ]
    
    def bfs(self, start, end):
        prev = self.slove(start)
        return self.reconstuctPath(start, end , prev)
    
    def slove(self, start):
        self.queue.put(start) #enqueue start node
        self.visited[start] = True

        #check queue is not empty
        while not self.queue.empty():
            print("queue: ", list(self.queue.queue))
            node = self.queue.get() #dequeue node
            print("node:", node)
            neighbours = self.graph[node] #get neighbour of currrent node
            self.drawGraph()
            pygame.display.update()
            pygame.time.delay(500)
            #go to next neighbour
            for next in neighbours:
                if not self.visited[next]:
                    self.queue.put(next) #enqueue neighbour
                    self.visited[next] = True
                    self.prev[next] = node
        return self.prev
    
    def reconstuctPath(self, start, end , prev):
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
    
    def drawGraph(self):
        for node in range(self.num_node):
            for neighbor in self.graph[node]:
                if node < neighbor:
                    color = "yellow" if self.visited[node] and self.visited[neighbor] else "black"
                    pygame.draw.line(screen, color, self.node_pos[node], self.node_pos[neighbor], 5)

        for i, pos in enumerate(self.node_pos):
            color = "orange" if self.visited[i] else "blue"
            pygame.draw.circle(screen, color, pos, 30)
            node_text = font.render(str(i), True, "white")
            screen.blit(node_text, (pos[0] - node_text.get_width() // 2, pos[1] - node_text.get_height() // 2))

dfs = DFS()
Dsf = False

bfs = BFS()
Bfs = False

## ------- Game Loop ------------
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                Dsf = True
            else:   Dsf = False
            if event.key == pygame.K_b:
                Bfs = True
            else:   Bfs = False

    screen.fill("gray")

    if Dsf:
        dfs.drawGraph()
        dfs.findComponents()
    
    if Bfs:    
        bfs.bfs(bfs.start_node, bfs.end_node)
        bfs.drawGraph()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()