import pygame

import consts
import game_field
def first_position(field):
    for row in field:
        for col in row:
            if col == 'solider_body' or col == 'soldier_feet':
                position = [[row, col],[row+1,col]]
                break
    return position
def move_left(position, field):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        if position[0][1] >= 0:
            field[position[0][0]][position[0][1]] = ' '
            field[position[1][0]][position[1][1]] = ' '
            position[0][1] -= 1
            field[position[0][0]][position[0][1]] = 'solider_body'
            position[1][1] -= 1
            field[position[1][0]][position[1][1]] = 'solider_feet'
            return position, field
    return position, field

def move_right(position, field):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if position[0][1] <= consts.WINDOW_WIDTH:
            field[position[0][0]][position[0][1]] = ' '
            field[position[1][0]][position[1][1]] = ' '
            position[0][1] += 1
            field[position[0][0]][position[0][1]] = 'solider_body'
            position[1][1] += 1
            field[position[1][0]][position[1][1]] = 'solider_feet'
            return position, field
    return position, field

def move_up(position, field):
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_UP] or keys[pygame.K_w]:
        if position[0][0] >= 0:
            field[position[0][0]][position[0][1]] = ' '
            field[position[1][0]][position[1][1]] = ' '
            position[0][0] -= 1
            field[position[0][0]][position[0][1]] = 'solider_body'
            position[1][0] -= 1
            field[position[1][0]][position[1][1]] = 'solider_feet'
            return position, field
        return position, field

def move_down(position, field):
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        if position[0][0] <= len(field) - 1:
            field[position[0][0]][position[0][1]] = ' '
            field[position[1][0]][position[1][1]] = ' '
            position[0][0] += 1
            field[position[0][0]][position[0][1]] = 'solider_body'
            position[1][0] += 1
            field[position[1][0]][position[1][1]] = 'solider_feet'
            return position, field
        return position, field

def solider():
    class player(pygame.Rect):
        def __init__(self):
            pygame.Rect.__init__(self, 0, 0, 40, 80)
            solider_image = pygame.image.load('soldier.png')
            solider_image_resize = pygame.transform.scale(solider_image,
                                                          (40, 80))
            self.image = solider_image_resize
    return player
