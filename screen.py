import consts
import pygame
screen = pygame.display.set_mode((100, 100))
def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)


def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)

import tkinter
import sys
import random
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

pygame.display.flip()