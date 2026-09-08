import consts
import pygame
import random
import tkinter
import sys

def create_screen():
    screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    pygame.display.set_caption("THE FLAG GAME")
    screen.fill('lightgreen')
    bush = pygame.image.load('grass.png')
    resize_bush = pygame.transform.scale(bush, (60, 60))
    for i in range (20):
        ran_x = random.randrange(consts.WINDOW_WIDTH)
        ran_y = random.randrange(consts.WINDOW_HEIGHT)
        screen.blit(resize_bush, (ran_x, ran_y))
    pygame.display.flip()
    return screen
# create_screen()
# pygame.init()




