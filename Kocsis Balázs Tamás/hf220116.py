# Kicsit túl nagy a kép

import pygame
import random
  
WIDTH = 1280
HEIGHT = 600
SPEED = 5
  
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
  
balloon_surf = pygame.image.load('Kocsis Balázs Tamás\img/flare_0.png').convert_alpha()
balloons_rect = []
for _ in range(5):
    balloon_rect = balloon_surf.get_rect(
        center=(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)))
    balloons_rect.append(balloon_rect)
  
bird_fw_1 = pygame.image.load('Kocsis Balázs Tamás\img/ufo_enemy_game_character2.png').convert_alpha()
bird_fw_2 = pygame.image.load('Kocsis Balázs Tamás\img/ufo_enemy_game_character2.png').convert_alpha()
bird_fw_3 = pygame.image.load('Kocsis Balázs Tamás\img/ufo_enemy_game_character2.png').convert_alpha()
bird_fw_4 = pygame.image.load('Kocsis Balázs Tamás\img/ufo_enemy_game_character2.png').convert_alpha()
birds_fw = [bird_fw_1, bird_fw_2, bird_fw_3, bird_fw_4]
bird_b_1 = pygame.image.load('Kocsis Balázs Tamás\img/ufo_enemy_game_character.png').convert_alpha()
bird_b_2 = pygame.image.load('Kocsis Balázs Tamás\img/ufo_enemy_game_character.png').convert_alpha()
bird_b_3 = pygame.image.load('Kocsis Balázs Tamás\img/ufo_enemy_game_character.png').convert_alpha()
bird_b_4 = pygame.image.load('Kocsis Balázs Tamás\img/ufo_enemy_game_character.png').convert_alpha()
birds_b = [bird_b_1, bird_b_2, bird_b_3, bird_b_4]
  
bird_x = WIDTH / 2
bird_y = HEIGHT / 2
bird_index = 0
bird_rect = birds_fw[bird_index].get_rect(center=(bird_x, bird_y))
  
counter = 0
forward = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
  
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and bird_rect.right <= WIDTH:
        forward = True
        bird_x += SPEED
    elif keys[pygame.K_LEFT] and bird_rect.left >= 0:
        forward = False
        bird_x -= SPEED
  
    if keys[pygame.K_UP] and bird_rect.top >= 0:
        bird_y -= SPEED
    elif keys[pygame.K_DOWN] and bird_rect.bottom <= HEIGHT:
        bird_y += SPEED
  
    screen.fill((140, 137, 246))
  
    counter += 1
    if counter % 7 == 0:
        bird_index += 1
    if bird_index > len(birds_fw) - 1:
        bird_index = 0
  
    if forward:
        bird_rect = birds_fw[bird_index].get_rect(center=(bird_x, bird_y))
        screen.blit(birds_fw[bird_index], bird_rect)
    else:
        bird_rect = birds_b[bird_index].get_rect(center=(bird_x, bird_y))
        screen.blit(birds_b[bird_index], bird_rect)
  
    for index, balloon_rect in enumerate(balloons_rect):
        if balloon_rect.colliderect(bird_rect):
            del balloons_rect[index]
        else:
            screen.blit(balloon_surf, balloon_rect)
  
    pygame.display.update()
    clock.tick(60)
  
pygame.quit()