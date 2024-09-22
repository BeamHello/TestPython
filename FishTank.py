import pygame
import random
import pygame_gui

WIDTH = 1280
HEIGH = 720
MAX_SPEED = 5

SEPARATION_FACTOR = 0.1
ALIGNMENT_FACTOR = 0.1
COHERENCE_FACTOR = 0.1
SEPARATION_DIST = 30

NUMBER_AGENT = 20

targetX = int(WIDTH / 2)
targetY = int(HEIGH / 2)

class Agent:
    def __init__(self, x, y) -> None:
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(random.uniform(-MAX_SPEED, MAX_SPEED), random.uniform(-MAX_SPEED, MAX_SPEED))
        self.acceleration = pygame.Vector2(0, 0)
        self.mass = 1

        self.sign_range = 50
    
    def apply_force(self, x, y):
        force = pygame.Vector2(x, y)
        self.acceleration += force / self.mass

    def moveToTargetInRange(self, vec_target):
        distance = vec_target - self.position
        dist = pygame.Vector2.magnitude(distance)
        if dist <= self.sign_range:
            energy = dist / self.sign_range
            max_speed = 1
            speed = energy * max_speed
            distance.normalize() * speed
            seeking_force = distance
            self.apply_force(seeking_force.x, seeking_force.y)
    
    def coherence(self, agents):
        center_of_mass = pygame.Vector2(0, 0)
        agent_in_range_count = 0
        for agent in agents:
            if agent != self:
                dist = self.position.distance_to(agent.position)
                if dist < 100:
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
            if agent != self:
                dist = self.position.distance_to(agent.position)
                if dist < SEPARATION_DIST:
                    d += self.position - agent.position

        separation_force = d * SEPARATION_FACTOR
        self.apply_force(separation_force.x, separation_force.y)
    
    def alignment(self, agents):
        v = pygame.Vector2(0, 0)
        agent_in_range_count = 0
        for agent in agents:
            if agent != self:
                dist = self.position.distance_to(agent.position)
                if dist < 100:
                    v += agent.velocity
                    agent_in_range_count += 1

        if agent_in_range_count > 0:
            v /= agent_in_range_count
            alignment_force = v * ALIGNMENT_FACTOR
            self.apply_force(alignment_force.x, alignment_force.y)

    def update(self):
        self.velocity += self.acceleration
        if self.velocity.length() > 1:
            self.velocity = self.velocity.normalize() * 1
        self.position += self.velocity
        self.acceleration = pygame.Vector2(0, 0)
    
    def render(self):
        pygame.draw.circle(screen, "blue", self.position, 5)
        pygame.draw.circle(screen, "red", self.position, self.sign_range, 1)

agents = [Agent(random.uniform(0, WIDTH), random.uniform(0, HEIGH))
          for _ in range(NUMBER_AGENT)]

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGH))
clock = pygame.time.Clock()
manager = pygame_gui.UIManager((WIDTH, HEIGH)) # GUI
running = True

## ------- Game Loop ------------
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("gray")

    mousePosition = pygame.mouse.get_pos()
    pygame.draw.circle(screen, "black", mousePosition, 5, 2)

    for agent in agents:
        agent.moveToTargetInRange(mousePosition)
        agent.coherence(agents)
        agent.separation(agents)
        agent.alignment(agents)
        agent.update()
        agent.render()

        if agent.position.x > WIDTH:
            agent.position.x = 0
        elif agent.position.x < 0:
            agent.position.x = WIDTH
        if agent.position.y > HEIGH:
            agent.position.y = 0
        elif agent.position.y < 0:
            agent.position.y = HEIGH
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()