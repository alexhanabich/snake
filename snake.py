import pygame
import time
import random

pygame.init()

GRAY = (128,128,128)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
WIDTH = 600
HEIGHT = 400

surface =  pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')

done = False

snake_x = WIDTH / 2
snake_y = HEIGHT / 2

delta_x = 0
delta_y = 0

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15
snake_length = 1
snake_list = []

def game_over():
    font = pygame.font.SysFont('monospace', 30)
    score = font.render(f"Score: {snake_length}", True, (0,0,0))
    score_rect = score.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    surface.blit(score, score_rect)
    pygame.display.flip()
    while True:
        event = pygame.event.wait()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    

def show_score():
        font = pygame.font.SysFont('monospace',20)
        score = font.render(f"Score: {snake_length}",True,(0,0,0))
        surface.blit(score,(0,0))

def draw_snake(snake_body):
    for x in snake_body:
        pygame.draw.rect(surface, GRAY, ([x[0], x[1], 10, 10]))

    
def draw_fruit():
    food_x = random.randrange(20, WIDTH - 20)
    food_y = random.randrange(20, HEIGHT - 20)
    pygame.draw.rect(WIN ,RED, pygame.Rect(food_x,food_y,10,10))

food_x = random.randrange(20, WIDTH - 20)
food_y = random.randrange(20, HEIGHT - 20)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                delta_x = -10
                delta_y = 0
            elif event.key == pygame.K_RIGHT:
                delta_x = 10
                delta_y = 0
            elif event.key == pygame.K_UP:
                delta_y = -10
                delta_x = 0
            elif event.key == pygame.K_DOWN:
                delta_y = 10
                delta_x = 0

    if snake_x >= WIDTH or snake_x < 0 or snake_y >= HEIGHT or snake_y < 0:
        done = True
        game_over()
    snake_x += delta_x
    snake_y += delta_y
    surface.fill(WHITE)
    pygame.draw.rect(surface, RED, pygame.Rect(food_x, food_y, snake_block, snake_block))

    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    for x in snake_list[:-1]:
        if x == snake_head:
            done = True
            game_over()
    draw_snake(snake_list)
    if pygame.Rect(snake_x,snake_y,10,10).colliderect(pygame.Rect(food_x,food_y,10,10)):
        food_x = random.randrange(20, WIDTH - 20, 10)
        food_y = random.randrange(20, HEIGHT - 20, 10)
        snake_length += 1

    show_score()

    pygame.display.update()
    clock.tick(snake_speed)
    
pygame.quit()
quit()

