import sys
import random
import pygame
from sys import exit
import consts

pygame.init()
window = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption("the flag")
clock = pygame.time.Clock()
player_image = pygame.image.load('soldier.png')
player_image = pygame.transform.scale(player_image, (40, 80))

class Player(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,40,80)
        self.image = player_image

player = Player()

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
    window.fill('lightgreen')
    # win = bushes()
    window.blit(player_image, player)

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
