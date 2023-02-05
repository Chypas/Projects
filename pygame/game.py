import pygame
import random
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT
from os import listdir
pygame.init()

FPS = pygame.time.Clock()

# screen = pygame.display.set_mode((1200, 800))
screen = width, heigth = 1200, 800

IMGS_PASS = "goose"
BLACK = 0, 0, 0
WHITE = 255, 255, 255
YELLOW = 255, 255, 0
BLUE = 0, 0, 255
RED = 255, 0, 0
GREEN = 0, 255, 0

font = pygame.font.SysFont("Verdana", 20)

main_surface = pygame.display.set_mode(screen)
bg = pygame.transform.scale(pygame.image.load(
    "background.png").convert(), screen)
bg_x = 0
bg_x2 = bg.get_width()
bg_speed = 3

player_images = [pygame.image.load(
    IMGS_PASS + "/" + file).convert_alpha() for file in listdir(IMGS_PASS)]
player = pygame.image.load("player.png").convert_alpha()
player_rect = player.get_rect()
player_speed = 10


def create_bonus():
    bonus = pygame.transform.scale(pygame.image.load(
        "bonus.png").convert_alpha(), (100, 120))
    # bonus.fill(GREEN)
    bonus_rect = pygame.Rect(random.randint(60, width - 60), 0, *bonus.get_size())
    bonus_speed = random.randint(2, 5)
    return [bonus, bonus_rect, bonus_speed]


def create_enemy():
    enemy = pygame.transform.scale(pygame.image.load(
        "enemy.png").convert_alpha(), (100, 40))
    # enemy.fill(RED)
    enemy_rect = pygame.Rect(
        width, random.randint(50, heigth - 50), *enemy.get_size())
    enemy_speed = random.randint(2, 5)
    return [enemy, enemy_rect, enemy_speed]


is_working = True

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 1500)

CHANGE_IMG = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMG, 125)

img_index = 0
enemies = []
bonuses = []
scores = 0

while is_working:
    if scores >= 0 :
        FPS.tick(60)
    elif scores >= 10:
        FPS.tick(120)

    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())
        if event.type == CHANGE_IMG:
            img_index += 1
            if img_index == len(player_images):
                img_index = 0
            player = player_images[img_index]

    preset_keys = pygame.key.get_pressed()

    bg_x -= bg_speed
    bg_x2 -= bg_speed

    if bg_x < -bg.get_width():
        bg_x = bg.get_width()
    if bg_x2 < -bg.get_width():
        bg_x2 = bg.get_width()

    main_surface.blit(bg, (bg_x, 0))
    main_surface.blit(bg, (bg_x2, 0))

    main_surface.blit(player, player_rect)
    main_surface.blit(font.render(str(scores), True, BLUE), (width - 75, 20))


    for enemy in enemies:
        enemy[1] = enemy[1].move(-enemy[2], 0)
        main_surface.blit(enemy[0], enemy[1])
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))
        if player_rect.colliderect(enemy[1]):
            is_working = False

    for bonus in bonuses:
        bonus[1] = bonus[1].move(0, bonus[2])
        main_surface.blit(bonus[0], bonus[1])
        if bonus[1].bottom > heigth:
            bonuses.pop(bonuses.index(bonus))
        if player_rect.colliderect(bonus[1]):
            scores += 1
            bonuses.pop(bonuses.index(bonus))

    if preset_keys[K_DOWN] and not player_rect.bottom >= heigth:
        player_rect = player_rect.move(0, player_speed)
    if preset_keys[K_UP] and not player_rect.height <= 0:
        player_rect = player_rect.move(0, -player_speed)
    if preset_keys[K_RIGHT] and not player_rect.right >= width:
        player_rect = player_rect.move(player_speed, 0)
    if preset_keys[K_LEFT] and not player_rect.left <= 0:
        player_rect = player_rect.move(-player_speed, 0)

    pygame.display.flip()
