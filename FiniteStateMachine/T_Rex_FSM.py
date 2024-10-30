import pygame
import random
from enum import Enum
from abc import ABC, abstractmethod

WIDTH, HEIGHT = 800, 600

SPEED = 1
MAX_SPEED = 2
HUNT_SIGN_RANGE = 150
ATK_SIGN_RANGE = 10

TIME_IDLE = 200
TIME_PATRO = 500
TIME_HUNGRY = 50
TIME_DEAD = 35
TIME_RESPAWN = 150
TIME_DMG = 10
HP_VALUE = 100
HUNGRY_VALUE = 100

NUM_DINOS = 1

FRAME_RATE = 0.1

## ------- Pygame Setup ------------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)
running = True
pygame.display.set_caption("State Machine")
## ----------------------------------

dino_idle = pygame.image.load("Sprite2D/idle.png")
dino_patro = pygame.image.load("Sprite2D/move.png")
dino_hunt = pygame.image.load("Sprite2D/dash.png")
dino_atk = pygame.image.load("Sprite2D/kick.png")
dino_dead = pygame.image.load("Sprite2D/dead.png")
dino_hurt = pygame.image.load("Sprite2D/hurt.png")

dino_idle = pygame.transform.scale(dino_idle, (216, 72))
dino_patro = pygame.transform.scale(dino_patro, (432, 72))
dino_hunt = pygame.transform.scale(dino_hunt, (432, 72))
dino_atk = pygame.transform.scale(dino_atk, (216, 72))
dino_dead = pygame.transform.scale(dino_dead, (360, 72))
dino_hurt = pygame.transform.scale(dino_hurt, (288, 72))

dino_idle_anim = [dino_idle.subsurface(pygame.Rect(x * 72, 0, 72, 72)) for x in range(3)]
dino_patro_anim = [dino_patro.subsurface(pygame.Rect(x * 72, 0, 72, 72)) for x in range(6)]
dino_hunt_anim = [dino_hunt.subsurface(pygame.Rect(x * 72, 0, 72, 72)) for x in range(6)]
dino_atk_anim = [dino_atk.subsurface(pygame.Rect(x * 72, 0, 72, 72)) for x in range(3)]
dino_dead_anim = [dino_dead.subsurface(pygame.Rect(x * 72, 0, 72, 72)) for x in range(5)]
dino_hurt_anim = [dino_hurt.subsurface(pygame.Rect(x * 72, 0, 72, 72)) for x in range(4)]

## ------ Dino_States --------
class Dino_State(Enum):
    DINO_IDLE_STATE = 0
    DINO_PATRO_STATE = 1
    DINO_HUNT_STATE = 2
    DINO_ATK_STATE = 3
    DINO_DEAD_STATE = 4
    DINO_HURT_STATE = 5
    DINO_FLEE = 6
## ---------------------------

class Dino_StateMachine():
    def __init__(self) -> None:
        self.states = {
            'dino_idle': Dino_Idle(),
            'dino_patro': Dino_Patro(),
            'dino_hunt': Dino_Hunt(),
            'dino_attack': Dino_Attack(),
            'dino_dead': Dino_Dead(),
            'dino_hurt': Dino_Hurt(),
            'dino_flee': Dino_Flee()
        }
        self.current_state = 'dino_idle'
    
    def update(self, dino, prey):
        new_state = self.states[self.current_state].update(dino, prey)
        if new_state:
            self.transition_to(dino, new_state)
    
    def transition_to(self, dino, new_state):
        self.states[self.current_state].exit(dino)
        self.current_state = new_state
        self.states[self.current_state].enter(dino)

class Dino_State(ABC):
    @abstractmethod
    def enter(self, dino):
        pass

    @abstractmethod
    def update(self, dino):
        pass

    @abstractmethod
    def exit(slef, dino):
        pass

class Dino_Idle(Dino_State):
    def enter(self, dino):
        dino.current_anim = dino_idle_anim
        dino.anim_timer = 0

    def update(self, dino, prey):
        dino.velocity = pygame.Vector2(0, 0)
        dino.position += dino.velocity

        dino.anim_timer += 1
        if dino.anim_timer > TIME_IDLE:
            dino.anim_timer = 0
            return 'dino_patro'
        
        dist = (prey - dino.position).length()
        if dist < HUNT_SIGN_RANGE:
            return 'dino_hunt'
        
        if dino.dmg:
            return 'dino_hurt'
        
        if dino.hp_value <= 0:
            return 'dino_dead'
        
        if dist < HUNT_SIGN_RANGE and dino.hp_value <= 30:
            return 'dino_flee'
        
    
    def exit(self, dino):
        pass

class Dino_Patro(Dino_State):
    def enter(self, dino):
        dino.current_anim = dino_patro_anim
        dino.anim_timer = 0

    def update(self, dino, prey):
        dino.velocity.x = random.randint(0, 100)
        dino.velocity.y = random.randint(0, 30)
        if dino.velocity.length() > SPEED:
            dino.velocity.scale_to_length(SPEED)
        dino.position += dino.velocity

        dino.anim_timer += 1
        if dino.anim_timer > TIME_PATRO:
            dino.anim_timer = 0
            return 'dino_idle'
        
        dist = (prey - dino.position).length()
        if dist < HUNT_SIGN_RANGE:
            return 'dino_hunt'
        
        if dino.dmg:
            return 'dino_hurt'
        
        if dino.hp_value <= 0:
            return 'dino_dead'
        
        if dist < HUNT_SIGN_RANGE and dino.hp_value <= 30:
            return 'dino_flee'
    
    def exit(self, dino):
        pass

class Dino_Hunt(Dino_State):
    def enter(self, dino):
        dino.current_anim = dino_hunt_anim

    def update(self, dino, prey):
        distance = (prey - dino.position).normalize() * 5
        dino.velocity += distance
        if dino.velocity.length() > MAX_SPEED:
            dino.velocity.scale_to_length(MAX_SPEED)
        dino.position += dino.velocity

        dist = (prey - dino.position).length()
        if dist > HUNT_SIGN_RANGE:
            return 'dino_patro'
        
        if dist < ATK_SIGN_RANGE:
            return 'dino_attack'
        
        if dino.dmg:
            return 'dino_hurt'
        
        if dino.hp_value <= 0:
            return 'dino_dead'
        
        if dist < HUNT_SIGN_RANGE and dino.hp_value <= 30:
            return 'dino_flee'
    
    def exit(self, dino):
        pass

class Dino_Attack(Dino_State):
    def enter(self, dino):
        dino.current_anim = dino_atk_anim

    def update(self, dino, prey):
        dist = (prey - dino.position).length()
        if dist > ATK_SIGN_RANGE:
            return 'dino_hunt'
        
        if dino.dmg:
            return 'dino_hurt'
        
        if dino.hp_value <= 0:
            return 'dino_dead'
        
        if dist < HUNT_SIGN_RANGE and dino.hp_value <= 30:
            return 'dino_flee'
    
    def exit(self, dino):
        pass

class Dino_Dead(Dino_State):
    def enter(self, dino):
        dino.current_anim = dino_dead_anim
        dino.anim_timer = 0

    def update(self, dino, prey):
        dino.anim_timer += 1
        if dino.anim_timer > TIME_DEAD:
            dino.anim_timer = 0
            dino.alive = False
    
    def exit(self, dino):
        pass

class Dino_Hurt(Dino_State):
    def enter(self, dino):
        dino.anim_timer = 0

    def update(self, dino, prey):
        if dino.dmg:
            dino.current_anim = dino_hurt_anim
            dino.anim_timer += 1
            if dino.anim_timer > TIME_DMG:
                dino.anim_timer = 0
                dino.dmg = False
        
        if not dino.dmg:
            return 'dino_attack'

        if dino.hp_value <= 0:
            return 'dino_dead'
        
        dist = (prey - dino.position).length()
        if dist < HUNT_SIGN_RANGE and dino.hp_value <= 30:
            return 'dino_flee'
    
    def exit(self, dino):
        pass

class Dino_Flee(Dino_State):
    def enter(self, dino):
        dino.current_anim = dino_hunt_anim

    def update(self, dino, prey):
        distance = (prey - dino.position).normalize() * 5
        dino.velocity += distance
        if dino.velocity.length() > MAX_SPEED:
            dino.velocity.scale_to_length(MAX_SPEED)
        dino.position -= dino.velocity
        
        dist = (prey - dino.position).length()
        if dist > HUNT_SIGN_RANGE:
            return 'dino_patro'

        if dino.dmg:
            return 'dino_hurt'

        if dino.hp_value <= 0:
            return 'dino_dead'
    
    def exit(self, dino):
        pass

class Dino():
    def __init__(self) -> None:
        self.position = pygame.Vector2(random.uniform(100, WIDTH - 100), random.uniform(100, HEIGHT - 100))
        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize()
        
        self.frame_index = 0
        self.state_machine = Dino_StateMachine()
        self.current_anim = dino_idle_anim
        self.anim_timer = 0

        self.hp_value = HP_VALUE
        self.hungry_value = HUNGRY_VALUE
        self.hungry_timer = 0
        self.respawn_timer = 0
        self.dmg_hungry_timer = 0
        self.alive = True
        self.dmg = False
    
    def hungry(self):
        self.hungry_timer += 1
        if self.hungry_timer > TIME_HUNGRY:
            self.hungry_value -= 1
            self.hungry_timer = 0
        if self.hungry_value < 0:
            self.hungry_value = 0
            self.dmg_hungry_timer += 1
            if self.dmg_hungry_timer > TIME_DMG:
                self.hp_value -= 10
                self.dmg_hungry_timer = 0
    
    def hp(self, prey):
        dist = (prey - self.position).length()
        if dist < ATK_SIGN_RANGE:
            self.hp_value -= 10
            self.dmg = True
        if self.hp_value < 0:
            self.hp_value = 0
            self.dmg = False

    def update(self, prey):
        if self.alive:
            self.state_machine.update(self, prey)
            self.hungry()
        elif not self.alive:
            self.respawn_timer += 1
            if self.respawn_timer >= TIME_RESPAWN:
                self.__init__()

        if self.position.x > WIDTH:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = WIDTH
        if self.position.y > HEIGHT:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = HEIGHT

        return True
    
    def render(self, screen):
        if self.alive:
            self.frame_index = (self. frame_index + FRAME_RATE) % len(self.current_anim)
            current_frame = self.current_anim[int(self.frame_index)]

            if self.velocity.x < 0:
                current_frame = pygame.transform.flip(current_frame, True, False)
            if self.state_machine.current_state == 'dino_flee':
                current_frame = pygame.transform.flip(current_frame, True, False)

            screen.blit(current_frame, (int(self.position.x) - 36, int(self.position.y) - 36))

        hungry_text = font.render(f"Hungry: {self.hungry_value}", True, "black")
        hp_text = font.render(f"HP: {self.hp_value}", True, "black")
        screen.blit(hungry_text, (10, 10))
        screen.blit(hp_text, (10, 40))

dinos = [Dino() for _ in range(NUM_DINOS)]

## ------- Game Loop ------------
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if pygame.mouse.get_pressed()[0]:
            for dino in dinos:
                dino.hp(prey)

        prey = pygame.Vector2(pygame.mouse.get_pos())

    screen.fill("gray")

    dinos = [target for target in dinos if target.update(prey)]
    for dino in dinos:
        dino.render(screen)
    
    pygame.draw.circle(screen, ('black'), (int(prey.x), int(prey.y)), 5, 3)

    pygame.display.flip()

    clock.tick(60)
    
pygame.quit()