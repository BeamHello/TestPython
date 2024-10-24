import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

class Agent():
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)
    
    def moveToTarget(self, vec_target):
        distance = pygame.math.Vector2(vec_target - self.position)
        distance.normalize() * 0.1
        self.acceleration += distance
    
    def update(self):
        self.velocity = pygame.math.Vector2(self.velocity + self.acceleration)
        self.velocity * 0.9
        self.velocity.scale_to_length(1)
        self.position = pygame.math.Vector2(self.position + self.velocity)
        self.acceleration.update(0, 0)
    
    def render(self):
        pygame.draw.circle(screen, "red", [self.position.x, self.position.y], 10)

targetX = int(1280/2)
targetY = int(100)

agents = []
for i in range(5):
    agents.append(Agent(random.randint(10, 1280), random.randint(10, 720)))


## ------- Game Loop ------------
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # mouse event
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mousePosition = pygame.mouse.get_pos()
                targetX = mousePosition[0]
                targetY = mousePosition[1]
        
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")

    # RENDER YOUR GAME HERE
    for agent in agents:
        agent.moveToTarget([targetX, targetY])
        agent.update()
        agent.render()
    
    pygame.draw.circle(screen, "black", [targetX, targetY], 10, 3)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()