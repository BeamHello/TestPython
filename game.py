import pygame
import random
import math

WIDTH = 1280
HEIGH = 720
MAX_SPEED = 3

SEPARATION_FACTOR = 0.1
ALIGNMENT_FACTOR = 0.1
COHERENCE_FACTOR = 0.1
SEPATARATION_DIST = 25

class Agent():
    def __init__(self, x, y) -> None:
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)
        self.mass = 1
    
    def update(self):
        self.velocity = self.velocity + self.acceleration
        if self.velocity.length() > MAX_SPEED:
            self.velocity = self.velocity.normalize() * MAX_SPEED
        self.position = self.position + self.velocity
        self.acceleration = pygame.Vector2(0, 0)
    
    def apply_force(self, x, y):
        force = pygame.Vector2(x, y)
        self.acceleration = self.acceleration + (force / self.mass)
    
    def seek(self, x, y):
        d = pygame.Vector2(x, y) - self.position
        d = d.normalize() * 0.1 # normalize = run by one frame
        seeking_force = d
        self.apply_force(seeking_force.x, seeking_force.y)

    def conherence(self, agent):
        center_of_mass = pygame.Vector2(0, 0)
        agent_in_range_count = 0
        for agent in agents:
            if agent != self:
                dist = math.sqrt((self.position.x - agent.position.x)**2
                             + (self.position.y - agent.position.y)**2)

                if dist < 200:
                    center_of_mass += agent.position
                    agent_in_range_count += 1
        if agent_in_range_count > 0:
            center_of_mass /= agent_in_range_count

            d = center_of_mass - self.position
            f = d * COHERENCE_FACTOR
            self.apply_force(f.x, f.y)

    def separation(self, agents):
        d = pygame.Vector2(0, 0)
        for agent in agents:
            dist = math.sqrt((self.position.x - agent.position.x)**2
                             + (self.position.y - agent.position.y)**2)

            if dist < SEPATARATION_DIST:
                d += self.position - agent.position
        
        separation_force = d * SEPARATION_FACTOR
        self.apply_force(separation_force.x, separation_force.y)
    
    def alignment(self, agents):
        v = pygame.Vector2(0, 0)
        for agent in agents:
            if agent != self:
                v += agent.velocity
        
        v /= len(agents) - 1
        alignmnent_force = v * ALIGNMENT_FACTOR
        self.apply_force(alignmnent_force.x, alignmnent_force.y)
    
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
        #agent.seek(400, 400)
        agent.conherence(agents)
        agent.separation(agents)
        agent.alignment(agents)
        agent.update()
        agent.draw()
    
    for agent in agents:
        if agent.position.x > WIDTH + 1:
            agent.position.x = 1
        elif agent.position.x < 0:
            agent.position.x = WIDTH
        if agent.position.y > HEIGH + 1:
            agent.position.y = 1
        elif agent.position.y < 0:
            agent.position.y = HEIGH
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()