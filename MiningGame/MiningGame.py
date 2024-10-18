import pygame
from RandomnessUtility import Marblebag_random
from RandomnessUtility import Progressive_random
from RandomnessUtility import FixedRate_random
from RandomnessUtility import Predetermination_random

WIDTH = 1280
HEIGH = 720
DELAY_TIME = 50

class Character:
    def __init__(self) -> None:
        self.sprite = pygame.transform.scale(character_sprite, (6680, 477))

        self.frame_size_x = 668
        self.frame_size_y = 477
        self.fx = 0
        self.fy = 0
        self.sprite_frame = self.sprite.subsurface(pygame.Rect(self.fx * self.frame_size_x, self.fy * self.frame_size_y,
                                                               self.frame_size_x, self.frame_size_y))
        self.position = self.sprite_frame.get_rect(center = (WIDTH / 2, HEIGH / 2))
        self.time = 0
        self.frame_rate = 1
        self.animation_play = False
    
    def animation(self):
        if self.animation_play:
            if self.time > self.frame_rate:
                self.fx = self.fx + 1
                if self.fx >= 10:
                    self.fx = 0
                    self.animation_play = False
                self.sprite_frame = self.sprite.subsurface(pygame.Rect(self.fx * self.frame_size_x, self.fy * self.frame_size_y,
                                                                       self.frame_size_x, self.frame_size_y))
                self.time = 0
            else:
                self.time = self.time + 1

    def render(self):
        screen.blit(self.sprite_frame, (self.position.x + 25, self.position.y + 130))

class NoDrop:
    def __init__(self) -> None:
        self.sprite = pygame.transform.scale(no_drop_sprite, (3328, 256))
        self.frame_size = 256
        self.fx = 0
        self.fy = 0
        self.sprite_frame = self.sprite.subsurface(pygame.Rect(self.fx * self.frame_size, self.fy * self.frame_size,
                                                               self.frame_size, self.frame_size))
        self.position = self.sprite_frame.get_rect(center = (WIDTH / 2, HEIGH / 2))
        self.time = 0
        self.frame_rate = 0.8
        self.animation_play = False
        self.delay_time = 0
    
    def animation(self):
        if self.animation_play:
            if self.time > self.frame_rate:
                self.fx = self.fx + 1
                if self.fx >= 13:
                    self.delay_time += 1
                    if self.delay_time > DELAY_TIME:
                        self.fx = 0
                        self.delay_time = 0
                        self.animation_play = False
                else:
                    self.sprite_frame = self.sprite.subsurface(pygame.Rect(self.fx * self.frame_size, self.fy * self.frame_size,
                                                                           self.frame_size, self.frame_size))
                self.time = 0
            else:
                self.time = self.time + 1

    def render(self):
        if self.animation_play:
            screen.blit(self.sprite_frame, (self.position.x + 20, self.position.y - 170))

class Empty:
    def __init__(self) -> None:
        self.sprite = pygame.transform.scale(emtpy_sprite, (3328, 256))
        self.frame_size = 256
        self.fx = 0
        self.fy = 0
        self.sprite_frame = self.sprite.subsurface(pygame.Rect(self.fx * self.frame_size, self.fy * self.frame_size,
                                                               self.frame_size, self.frame_size))
        self.position = self.sprite_frame.get_rect(center = (WIDTH / 2, HEIGH / 2))
        self.time = 0
        self.frame_rate = 0.8
        self.animation_play = False
        self.delay_time = 0
    
    def animation(self):
        if self.animation_play:
            if self.time > self.frame_rate:
                self.fx = self.fx + 1
                if self.fx >= 13:
                    self.delay_time += 1
                    if self.delay_time > DELAY_TIME:
                        self.fx = 0
                        self.delay_time = 0
                        self.animation_play = False
                else:
                    self.sprite_frame = self.sprite.subsurface(pygame.Rect(self.fx * self.frame_size, self.fy * self.frame_size,
                                                                           self.frame_size, self.frame_size))
                self.time = 0
            else:
                self.time = self.time + 1

    def render(self):
        if self.animation_play:
            screen.blit(self.sprite_frame, (self.position.x + 20, self.position.y - 170))

class Silver:
    def __init__(self) -> None:
        self.sprite = pygame.transform.scale(silver_sprite, (3328, 256))
        self.frame_size = 256
        self.fx = 0
        self.fy = 0
        self.sprite_frame = self.sprite.subsurface(pygame.Rect(self.fx * self.frame_size, self.fy * self.frame_size,
                                                               self.frame_size, self.frame_size))
        self.position = self.sprite_frame.get_rect(center = (WIDTH / 2, HEIGH / 2))
        self.time = 0
        self.frame_rate = 0.8
        self.animation_play = False
        self.delay_time = 0
    
    def animation(self):
        if self.animation_play:
            if self.time > self.frame_rate:
                self.fx = self.fx + 1
                if self.fx >= 13:
                    self.delay_time += 1
                    if self.delay_time > DELAY_TIME:
                        self.fx = 0
                        self.delay_time = 0
                        self.animation_play = False
                else:
                    self.sprite_frame = self.sprite.subsurface(pygame.Rect(self.fx * self.frame_size, self.fy * self.frame_size,
                                                                           self.frame_size, self.frame_size))
                self.time = 0
            else:
                self.time = self.time + 1

    def render(self):
        if self.animation_play:
            screen.blit(self.sprite_frame, (self.position.x + 20, self.position.y - 170))

class Gold:
    def __init__(self) -> None:
        self.sprite = pygame.transform.scale(gold_sprite, (3328, 256))
        self.frame_size = 256
        self.fx = 0
        self.fy = 0
        self.sprite_frame = self.sprite.subsurface(pygame.Rect(self.fx * self.frame_size, self.fy * self.frame_size,
                                                               self.frame_size, self.frame_size))
        self.position = self.sprite_frame.get_rect(center = (WIDTH / 2, HEIGH / 2))
        self.time = 0
        self.frame_rate = 0.8
        self.animation_play = False
        self.delay_time = 0
    
    def animation(self):
        if self.animation_play:
            if self.time > self.frame_rate:
                self.fx = self.fx + 1
                if self.fx >= 13:
                    self.delay_time += 1
                    if self.delay_time > DELAY_TIME:
                        self.fx = 0
                        self.delay_time = 0
                        self.animation_play = False
                else:
                    self.sprite_frame = self.sprite.subsurface(pygame.Rect(self.fx * self.frame_size, self.fy * self.frame_size,
                                                                           self.frame_size, self.frame_size))
                self.time = 0
            else:
                self.time = self.time + 1

    def render(self):
        if self.animation_play:
            screen.blit(self.sprite_frame, (self.position.x + 20, self.position.y - 170))

class Diamond:
    def __init__(self) -> None:
        self.sprite = pygame.transform.scale(diamond_sprite, (3328, 256))
        self.frame_size = 256
        self.fx = 0
        self.fy = 0
        self.sprite_frame = self.sprite.subsurface(pygame.Rect(self.fx * self.frame_size, self.fy * self.frame_size,
                                                               self.frame_size, self.frame_size))
        self.position = self.sprite_frame.get_rect(center = (WIDTH / 2, HEIGH / 2))
        self.time = 0
        self.frame_rate = 0.8
        self.animation_play = False
        self.delay_time = 0
    
    def animation(self):
        if self.animation_play:
            if self.time > self.frame_rate:
                self.fx = self.fx + 1
                if self.fx >= 13:
                    self.delay_time += 1
                    if self.delay_time > DELAY_TIME:
                        self.fx = 0
                        self.delay_time = 0
                        self.animation_play = False
                else:
                    self.sprite_frame = self.sprite.subsurface(pygame.Rect(self.fx * self.frame_size, self.fy * self.frame_size,
                                                                           self.frame_size, self.frame_size))
                self.time = 0
            else:
                self.time = self.time + 1

    def render(self):
        if self.animation_play:
            screen.blit(self.sprite_frame, (self.position.x + 20, self.position.y - 170))

class Button:
    def __init__(self) -> None:
        self.size = 150
        self.sprite = button_sprite
        self.sprite = pygame.transform.scale(button_sprite, (self.size, self.size))

        self.spriteClicked = buttonClicked_sprite
        self.spriteClicked = pygame.transform.scale(buttonClicked_sprite, (self.size, self.size))

        self.position = self.sprite.get_rect(bottomleft = (WIDTH - 200, HEIGH - 40))
        self.clicked = False
        self.clickable = True

        self.random_result = None
    
    def render(self):
        mouse_position = pygame.mouse.get_pos()

        if self.position.collidepoint(mouse_position) and self.clickable:
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                self.clickable = False
                character.animation_play = True
                screen.blit(self.spriteClicked, (self.position.x, self.position.y))

                empty.animation_play = True
                silver.animation_play = True
                gold.animation_play = True
                diamond.animation_play =True
                no_drop.animation_play = True

                if predtermination_random.attempt():
                    self.random_result = marble_bag.render()
                else:
                    if prossive_random.attempt():
                        fixed_rate.attempt()
                        if prossive_random.probability <= fixed_rate.base_probability:
                            self.random_result = marble_bag.render()
                            predtermination_random.attempts = 0
                        else:
                            self.random_result = empty
                    else:
                        self.random_result = no_drop
                        
                #print(prossive_random.probability)

            elif not pygame.mouse.get_pressed()[0]:
                self.clicked = False
                screen.blit(self.sprite, (self.position.x, self.position.y))
        else:
            screen.blit(self.sprite, (self.position.x, self.position.y))
        
        if self.random_result:
            self.random_result.render()

character_sprite = pygame.image.load("Sprite2D/SpriteCharacter.png")
button_sprite = pygame.image.load("Sprite2D/SpriteButton.png")
buttonClicked_sprite = pygame.image.load("Sprite2D/SpriteButtonClicked.png")
no_drop_sprite = pygame.image.load("Sprite2D/SpriteNoDrop.png")
emtpy_sprite = pygame.image.load("Sprite2D/SpriteEmpty.png")
silver_sprite = pygame.image.load("Sprite2D/SpriteSilver.png")
gold_sprite = pygame.image.load("Sprite2D/SpriteGold.png")
diamond_sprite = pygame.image.load("Sprite2D/SpriteDiamond.png")

detail_sprite = pygame.image.load("Sprite2D/SpriteDetail.png")
detail_sprite = pygame.transform.scale(detail_sprite, (450, 450))
bubble_sprite = pygame.image.load("Sprite2D/SpriteBubble.png")
bubble_sprite = pygame.transform.scale(bubble_sprite, (330, 190))


character = Character()
button = Button()
no_drop = NoDrop()
empty = Empty()
silver = Silver()
gold = Gold()
diamond = Diamond()

original_bag = [silver, gold, diamond]

marble_bag = Marblebag_random(original_bag)
prossive_random = Progressive_random(50, 0)
fixed_rate = FixedRate_random(30, 4)
predtermination_random = Predetermination_random(4)

## ------- Pygame Setup ------------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGH))
clock = pygame.time.Clock()
font = pygame.font.Font("Font/Itim-Regular.ttf", 22)
running = True

## ------- Game Loop ------------
while running:

    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("lavender")

    if not character.animation_play and not empty.animation_play and not silver.animation_play:
        button.clickable = True

    character.animation()
    no_drop.animation()
    empty.animation()
    silver.animation()
    gold.animation()
    diamond.animation()

    character.render()
    button.render()

    screen.blit(bubble_sprite, (WIDTH - 350, -30))
    text_garantee = font.render(f"Garantee one mineral in {predtermination_random.max_attempts - predtermination_random.attempts} roll", True, "black")
    screen.blit(text_garantee, (WIDTH - 325, 42))

    screen.blit(detail_sprite, (-60, 20))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()