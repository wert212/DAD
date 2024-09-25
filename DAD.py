import pygame
import random
from db import db

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Моя игра")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

square_size = 50
square_x = screen_width // 2
square_y = screen_height - square_size

ball_radius = 15
ball_x = random.randint(0, screen_width)
ball_y = random.randint(0, screen_height // 2)
balls = [[ball_x, ball_y]]

score = 0
lives = 3
font = pygame.font.Font(None, 36)
points = db.get_points()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()        
    if keys[pygame.K_LEFT] and square_x > 0:
        square_x = square_x - 10
    if keys[pygame.K_RIGHT] and square_x < screen_width - square_size:
        square_x = square_x + 10
    if keys[pygame.K_UP] and square_y > 0:
        square_y = square_y - 10
    if keys[pygame.K_DOWN] and square_y < screen_height - square_size:
        square_y = square_y + 10

    for b in balls:
        b[1] += 5
        if b[1] > screen_height:
            b[1] = 0
            b[0] = random.randint(0, screen_width)
            lives -= 1
        if (square_x < ball_x < square_x + square_size) and \
            (square_y < ball_y < ball_y + ball_radius):
            score += 1    
            ball_y = 0
            ball_x = random.randint(0, screen_width - ball_radius)        

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (square_x, square_y, square_size, square_size))
    for b in balls:
        pygame.draw.circle(screen, GREEN, (b[0], b[1]), ball_radius)
    
    score_text = font.render(f"Очки: {score}", True, (0, 0, 0))
    lives_text = font.render(f"Жизней: {lives}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 50))
    for i in range(len(points)):
        score_text = font.render(f"Очки: {points[i][0]}",True,(0,0,0))
        screen.blit(score_text, (screen_width -150, i*30))
    pygame.display.update()

    if lives < 1:
        db.write_point(score)
        exit()

    print("Количество очков", score)
    print("Количество жизней", lives)