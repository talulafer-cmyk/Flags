import sys
import random
import pygame
from sys import exit
import consts

pygame.init()
# window = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
# pygame.display.set_caption("the flag")
clock = pygame.time.Clock()
player = pygame.Rect(0,0,40,80)

def create_screen():
    window = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    pygame.display.set_caption("THE FLAG GAME")
    window.fill('lightgreen')
    bush = pygame.image.load('grass.png')
    resize_bush = pygame.transform.scale(bush, (60, 60))
    for i in range (20):
        ran_x = random.randrange(consts.WINDOW_WIDTH)
        ran_y = random.randrange(consts.WINDOW_HEIGHT)
        window.blit(resize_bush, (ran_x, ran_y))
    pygame.display.flip()
    return window


def draw():
    # window.fill('lightgreen')
    # win = bushes()
    pygame.draw.rect(window, (255,0,0), player)

# def main():
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if player.y > consts.CELL_SIZE:
                     player.y -= consts.CELL_SIZE
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if player.y < consts.WINDOW_HEIGHT - consts.CELL_SIZE:
                    player.y += consts.CELL_SIZE
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if player.x < consts.WINDOW_WIDTH - consts.CELL_SIZE:
                    player.x += consts.CELL_SIZE
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if player.x > consts.CELL_SIZE:
                    player.x -= consts.CELL_SIZE

    draw()
    pygame.display.update()
    clock.tick(60)
# main()

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP or event.key == pygame.K_w:
#                 if player.y > consts.CELL_SIZE:
#                     player.y -= consts.CELL_SIZE
#             if event.key == pygame.K_DOWN or event.key == pygame.K_s:
#                 if player.y < consts.WINDOW_HEIGHT - consts.CELL_SIZE:
#                     player.y += consts.CELL_SIZE
#             if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
#                 if player.x < consts.WINDOW_WIDTH - consts.CELL_SIZE:
#                     player.x += consts.CELL_SIZE
#             if event.key == pygame.K_LEFT or event.key == pygame.K_a:
#                 if player.x > consts.CELL_SIZE:
#                     player.x -= consts.CELL_SIZE
#
#
#     draw()
#     pygame.display.update()
#     clock.tick(60)
