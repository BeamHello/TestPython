import pygame
import random

WIDTH = 1280
HEIGH = 720

class Agent():
    def __init__(self, x, y) -> None:
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)
        self.mass = 1
    
    def update(self):
        self.velocity = self.velocity + self.acceleration
        self.position = self.position + self.velocity
        self.acceleration = pygame.Vector2(0, 0)
    
    def apply_force(self, x, y):
        force = pygame.Vector2(x, y)
        self.acceleration = self.acceleration + (force / self.mass)
    
    def draw(self):
        pygame.draw.circle(screen, "red", self.position, 10)

agents = []
for i in range(100):
    agents.append(Agent(random.uniform(0, WIDTH), random.uniform(0, HEIGH)))

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGH))
clock = pygame.time.Clock()
running = True

## ------- Game Loop ------------
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill("gray")

    for agent in agents:
        agent.update()
        agent.draw()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()