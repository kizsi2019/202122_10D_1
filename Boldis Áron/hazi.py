
import pygame
import random
  
WIDTH = 1280
HEIGHT = 620
DRAGON_SPEED = 4
FONT_COLOR = (0, 0, 0)
GAME_TIME = 8000
  
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('dragons in crosshair')
clock = pygame.time.Clock()
  
bg_surf = pygame.image.load('img/desert.png').convert_alpha()
bg_surf = pygame.transform.rotozoom(bg_surf, 0, 1.3)
bg_rect = bg_surf.get_rect(bottomleft=(0, HEIGHT))
  
drag_surf = pygame.image.load('img/tile000.png').convert_alpha()
drag_surf2 = pygame.image.load('img/tile001.png').convert_alpha()
drag_surf3 = pygame.image.load('img/tile002.png').convert_alpha()
dragons = [drag_surf, drag_surf2, drag_surf3]
dragon_index = 0
dragons_rect = []
dragons_timer = pygame.USEREVENT + 1
pygame.time.set_timer(dragons_timer, 1000)
  
crosshair_surf = pygame.image.load('img/crosshair065.png').convert_alpha()
crosshair_surf = pygame.transform.rotozoom(crosshair_surf, 0, 0.7)
crosshair_rect = crosshair_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))    
   
game_font = pygame.font.SysFont('arial', 30, bold=True)
  # nyitó- és záróképernyő feliratai
title_surf = game_font.render('DRAGONS IN CROSSHAIR', True, FONT_COLOR)
title_rect = title_surf.get_rect(center=(WIDTH/2, 200))
run_surf = game_font.render('Press space to run', True, FONT_COLOR)
run_rect = run_surf.get_rect(center=(WIDTH/2, HEIGHT-150))
   
start_time = pygame.time.get_ticks()
counter = 0
score = 0
game_active = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair_surf.get_rect(center=event.pos)
          # lufik létrehozása megadott időközönként
        if event.type ==  dragons_timer:
            dragons_rect.append(dragon.get_rect(center=(random.randint(50, WIDTH-100), HEIGHT-50)))
  
    screen.blit(bg_surf, bg_rect)
  
    if game_active:
        for index, dragon_rect in enumerate(dragons_rect):
              # lufik emelkedése
            dragons_rect[index].top -= DRAGON_SPEED
              # lufik oldalirányí mozgása
            mov_y = random.randint(0, 3)
            if mov_y == 0:
                dragons_rect[index].left -= 2
            else:
                dragons_rect[index].left += 2
              # lufik törlése a képernyő elhagyásakor
            if dragons_rect[index].bottom <= -10:
                del dragons_rect[index]
              # találat viszgálata
            if dragon_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed(num_buttons=3)[0]:
                del dragons_rect[index]
                score += 1

            screen.blit(dragon, dragon_rect)
        screen.blit(crosshair_surf, crosshair_rect)
  
          # pontszám megjelenítése
        score_surf = game_font.render('score: ' + str(score), True, FONT_COLOR)
        score_rect = score_surf.get_rect(topleft=(10, 10))
        screen.blit(score_surf, score_rect)
  
          # a hátralévő játékidő számítása és megjelenítése
        time_left = int((start_time + GAME_TIME - pygame.time.get_ticks()) / 1000)
        if time_left < 0:
            game_active = False
        time_left_surf = game_font.render('time left: ' + str(time_left), True, FONT_COLOR)
        time_left_rect = time_left_surf.get_rect(topleft=(10, 50))
        screen.blit(time_left_surf, time_left_rect)
  
      # nyitó- és záróképernyő
    else:
        screen.blit(title_surf, title_rect)
        screen.blit(drag_surf, drag_surf.get_rect(center=(WIDTH/2, HEIGHT/2)))
        screen.blit(crosshair_surf, crosshair_surf.get_rect(center=(WIDTH/2, HEIGHT/2)))
        screen.blit(run_surf, run_rect)
  
          # pontszám, ha az értéke nagyobb, mint nulla
        if score:
            final_score_surf = game_font.render('SCORE: ' + str(score), True, FONT_COLOR)
            final_score_rect = final_score_surf.get_rect(center=(WIDTH/2, HEIGHT-220))
            screen.blit(final_score_surf, final_score_rect)
  
          # játék indítáa
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            score = 0
            dragons_rect = []
            start_time = pygame.time.get_ticks()
            game_active = True

    counter += 1
    if counter % 14 == 0:
      dragon_index += 1
      if dragon_index > len(dragons) -1:
        dragon_index = 0 

    dragon = dragons[dragon_index]
    pygame.display.update()
    clock.tick(60)
  
pygame.quit()    
  