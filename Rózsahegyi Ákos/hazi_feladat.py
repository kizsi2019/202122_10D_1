import pygame
import random

WIDTH = 1280
HEIGHT = 720
BAT_SPEED = 6
FONT_COLOR = (100, 200, 100)
GAME_TIME = 15000

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The hunt for the dark bats")
clock = pygame.time.Clock()

bg_surf = pygame.image.load("img/back_cave.png").convert_alpha()
bg_surf = pygame.transform.rotozoom(bg_surf, 0, 1.3)
bg_rect = bg_surf.get_rect(bottomleft=(0, HEIGHT))

bat_surf = pygame.image.load("img/Bat1.png").convert_alpha()
bats_rect = []
bats_timer = pygame.USEREVENT + 1
pygame.time.set_timer(bats_timer, 1000)

crosshair_surf = pygame.image.load("img/crosshair2.png").convert_alpha()
crosshair_surf = pygame.transform.rotozoom(crosshair_surf, 0, 0.7)
crosshair_rect = crosshair_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))

game_font = pygame.font.SysFont("lucidafax", 30, bold=True)
title_surf = game_font.render("THE HUNT FOR THE DARK BATS", True, FONT_COLOR)
title_rect = title_surf.get_rect(center=(WIDTH/2, 200))
run_surf = game_font.render("Press G to run", True, FONT_COLOR)
run_rect = run_surf.get_rect(center=(WIDTH/2, HEIGHT-150))

start_time = pygame.time.get_ticks()
score = 0
game_active = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair_surf.get_rect(center=event.pos)
        if event.type == bats_timer:
            bats_rect.append(bat_surf.get_rect(center=(random.randint(50, WIDTH-50), HEIGHT-50)))

    screen.blit(bg_surf, bg_rect)

    if game_active:
        for index, bat_rect in enumerate(bats_rect):
            bats_rect[index].top -= BAT_SPEED
            mov_y = random.randint(0, 3)
            if mov_y == 0:
                bats_rect[index].right += 3
            if bats_rect[index].bottom <= -10:
                del bats_rect[index]
            if bat_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed(num_buttons=3)[0]:
                del bats_rect[index]
                score += 1

            screen.blit(bat_surf, bat_rect)
        screen.blit(crosshair_surf, crosshair_rect)

        score_surf = game_font.render("Score: " + str(score), True, FONT_COLOR)
        score_rect = score_surf.get_rect(topleft=(10, 10))
        screen.blit(score_surf, score_rect)

        time_left = int((start_time + GAME_TIME - pygame.time.get_ticks()) / 1000)
        if time_left < 0:
            game_active = False
        time_left_surf = game_font.render("Time left: " + str(time_left), True, FONT_COLOR)
        time_left_rect = time_left_surf.get_rect(topleft=(10, 50))
        screen.blit(time_left_surf, time_left_rect)

    else:
        screen.blit(title_surf, title_rect)
        screen.blit(bat_surf, bat_surf.get_rect(center=(WIDTH/2, HEIGHT/2)))
        screen.blit(crosshair_surf, crosshair_surf.get_rect(center=(WIDTH/2, HEIGHT/2)))
        screen.blit(run_surf, run_rect)

        if score:
            final_score_surf = game_font.render("SCORE: " + str(score), True, FONT_COLOR)
            final_score_rect = final_score_surf.get_rect(center=(WIDTH/2, HEIGHT-220))
            screen.blit(final_score_surf, final_score_rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_g]:
            score = 0
            bats_rect = []
            start_time = pygame.time.get_ticks()
            game_active = True

    pygame.display.update()
    clock.tick(60)

pygame.quit()