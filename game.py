import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

class Agent():
    def __init__(self, x, y) -> None:
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(1, 0)
        self.acceleration = pygame.Vector2(0, 0)

        self.sight_range = 100
    
    def update(self):
        self.velocity = self.velocity + self.acceleration
        self.position = self.position + self.velocity
        self.acceleration = pygame.Vector2(0, 0)
    
    def draw(self):
        pygame.draw.circle(screen, "red", self.position, 10)

agent1 = Agent(300, 200)

## ------- Game Loop ------------
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill("gray")

    agent1.update()
    agent1.draw()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()