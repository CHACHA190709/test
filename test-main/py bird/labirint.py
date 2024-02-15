import pygame
import random

pygame.init()

WIDTH = 336
HEIGHT = 540
TICKRATE = 60 

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bird')

clock = pygame.time.Clock()


class Background():
    def __init__(self):
        self.image = pygame.image.load('assets/background.png')
        self.x_1 = 0
        self.x_2 = WIDTH

    def draw(self):
        window.blit(self.image, (self.x_1, 0))
        window.blit(self.image, (self.x_2, 0))

    def update(self):
        self.x_1 -= 1
        self.x_2 -= 1
        if self.x_1 <= -WIDTH:
            self.x_1 = WIDTH
        if self.x_2 <= -WIDTH:
            self.x_2 = WIDTH

class Ground():
    def __init__(self):
        self.image = pygame.image.load('assets/ground.png')
        self.x_1 = 0
        self.x_2 = WIDTH
        self.y = HEIGHT - 100

    def draw(self):
        window.blit(self.image, (self.x_1, self.y))
        window.blit(self.image, (self.x_2, self.y))

    def update(self):
        self.x_1 -= 2
        self.x_2 -= 2
        if self.x_1 <= -WIDTH:
            self.x_1 = WIDTH
        if self.x_2 <= -WIDTH:
            self.x_2 = WIDTH

class Pipes():
    def __init__(self):
        self.gate = random.randint(100, HEIGHT - 200)
        self.gap = random.randint(40, 50) 

        self.top_image = pygame.image.load('assets/top-pipe.png')
        self.top_rect = self.top_image.get_rect()
        self.top_rect.bottomleft = (WIDTH, self.gate  - self.gap)

        self.bot_image = pygame.image.load('assets/bot-pipe.png')
        self.bot_rect = self.bot_image.get_rect()
        self.bot_rect.topleft = (WIDTH, self.gate  + self.gap)

    def draw(self):
        window.blit(self.top_image, self.top_rect)
        window.blit(self.bot_image, self.bot_rect)

    def update(self):
        self.top_rect.x -= 2    
        self.bot_rect.x -= 2  
        if self.top_rect.right < 0:
            self.gate = random.randint(100, HEIGHT - 200)
            self.gap = random.randint(45, 55) 
            self.top_rect.bottomleft = (WIDTH, self.gate  - self.gap)
            self.bot_rect.topleft = (WIDTH, self.gate  + self.gap)
            game.score += 1
            game.update_score()  

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_orig = pygame.image.load('assets/bird.png')
        self.image = self.image_orig
        self.rect = self.image.get_rect(center = (
            WIDTH // 3,
            HEIGHT // 2
        ))
        self.base_speed = -2.5
        self.speed = self.base_speed
        self.angle = 0


    def draw(self):
        window.blit(self.image, self.rect)

    def update(self, events):
        self.rect.y -= self.speed
        if self.speed > self.base_speed:
            self.speed -= 1

        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.bottom >= HEIGHT - 100:
            self.rect.bottom = HEIGHT - 100         

        if self.speed > 0:
            self.angle += 3
            if self.angle > 25:
                self.angle = 25

        elif self.speed < 0:
            self.angle -= 1
            if self.angle < -35:
                self.angle = -35
        self.image = pygame.transform.rotate(self.image_orig, self.angle)

        if game.state == 'play':

            for e in events:
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_SPACE:
                        self.speed = 10

            if self.rect.collidelistall([pipes.top_rect, pipes.bot_rect]):
                self.image_orig = pygame.image.load('assets/die_bird.png')
                game.state = 'over'
                self.angle = -45            

class GameManager():
    def __init__(self):
        self.state = 'play'
        self.score = 0
        self.font = pygame.font.Font('assets/Flappy-Bird.ttf', 50)
        self.score_text = self.font.render('0', True, (255, 255, 255))
        self.restart_text = self.font.render('Press R to restart', True, (255, 255, 255))

    def centerx(self, surf):
        return (WIDTH // 2) - (surf.get_width () // 2)
    
    def centery(self, surf):
        return (HEIGHT // 2) - (surf.get_height() // 2)

    def draw_score(self):
        window.blit(self.score_text, (self.centerx(self.score_text), 10))
    
    def update_score(self):
        self.score_text = self.font.render(str(self.score), True, (255, 255, 255))
    
    def draw_restart(self):
        window.blit(self.restart_text, (self.centerx(self.restart_text), self.centery(self.restart_text)))
    
    def restart(self):
        self.state = 'play'
        self.score = 0
        self.update_score()
        bird.angle = 0
        bird.rect = bird.image.get_rect(center = (
            WIDTH // 3,
            HEIGHT // 2
        ))
        pipes.gate = random.randint(100, HEIGHT - 200)
        pipes.gap = random.randint(45, 55) 
        pipes.top_rect.bottomleft = (WIDTH, pipes.gate  - pipes.gap)
        pipes.bot_rect.topleft = (WIDTH, pipes.gate  + pipes.gap)
        bird.image_orig = pygame.image.load('assets/bird.png')
        bird.speed = bird.base_speed


bg = Background()
ground = Ground()
pipes = Pipes()
game = GameManager()
bird = Bird()                 

while  True:

    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_r and game.state == 'over':
                game.restart()
                

    if game.state == 'play':  
        bg.update()
        pipes.update()
        ground.update() 
    bird.update(events)
    
    bg.draw()            
    pipes.draw()
    ground.draw()
    game.draw_score()
    bird.draw()
    if game.state == 'over':
        game.draw_restart()

    pygame.display.flip()
    clock.tick(TICKRATE)




