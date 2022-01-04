import pygame
import sys
import random
import math
from consts import *
from brickAndBall import *
import math
pygame.init()

SURFACE = pygame.display.set_mode(SCREEN_SIZE)
SURFACE.fill(pygame.Color('WHITE'))
pygame.display.set_caption('Brick Breaker')
clock = pygame.time.Clock()
FPS = 60
# game_over = False
ball_radius = 20
deltaX = random.randint(2, 7)
deltaY = random.randint(2, 7)
print(deltaX)
print(deltaY)
x = int(SCREEN_SIZE[0]/2)
y = int(SCREEN_SIZE[1]/2)
print(SCREEN_SIZE[0])
print(SCREEN_SIZE[1])
ball_radius = 20
deltaX = random.randint(-5, 5)
deltaY = random.randint(-5, 5)
livesLeft = 3
livesLeft = str(livesLeft)
score = 0

brick_sprites = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
paddle_sprite = pygame.sprite.Group()
x_rect = 320
y_rect = 420
paddle = Brick(x_rect, y_rect, 125, 30, RED)
ball = Ball(320, 210, 30, 30, RED)
all_sprites.add(paddle)
paddle_sprite.add(paddle)
all_sprites.add(ball)
for i in range(0, 5):
    brick = Brick(-5+(i*130), 0, 125, 75, ORANGE)
    brick_sprites.add(brick)
    all_sprites.add(brick)
x_change = 0
y_change = 0
while True:
    SURFACE.fill(pygame.Color('WHITE'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if paddle.rect.x <= 520:

                    print('right')
                    x_change += 20

            elif event.key == pygame.K_LEFT:

                if paddle.rect.x >= 0:
                    x_change -= 20
    if ball.rect.x <= 0 or ball.rect.x >= SCREEN_SIZE[0]-50:
        deltaX *= -1
    elif ball.rect.y <= 0:
        deltaY *= -1
    elif ball.rect.y >= SCREEN_SIZE[1]:

        livesLeft -= 1

        print('out of game')
        x = int(SCREEN_SIZE[0]/2)
        y = int(SCREEN_SIZE[1]/2)
        deltaX = random.randint(-5, 5)
        deltaY = random.randint(-5, 5)
    if pygame.sprite.spritecollide(ball, brick_sprites, True):
        deltaY *= -1
        score += 5
    if pygame.sprite.spritecollide(ball, paddle_sprite, False):
        deltaY *= -1

    if livesLeft == 0:
        break

    ball.rect.x += deltaX
    ball.rect.y += deltaY

    font = pygame.font.SysFont(None, 40)

    Score = font.render('Score: '+str(score), True, BLACK)

    Lives = font.render('Lives: '+livesLeft, True, BLACK)

    paddle.rect.x += x_change
    paddle.rect.y += y_change
    x_change = 0
    y_change = 0
    all_sprites.draw(SURFACE)
    SURFACE.blit(Score, (50, 0))
    pygame.display.update()
    clock.tick(FPS)
