import pygame

import consts
import game_field
# def first_position(field):
#     for row in field:
#         for col in row:
#             if col == 'solider_body' or col == 'soldier_feet':
#                 position = [[row, col],[row+1,col]]
#                 break
#     return position


def move_left(field):
    position_feet = [game_field.get_solider_feet_row(),game_field.get_solider_feet_col()]
    position_body = [game_field.get_solider_row(),game_field.get_solider_col()]
    if position_body[1] > 0:
        for row in range (consts.SOLDIER_BODY_ROWS):
            field[position_body[0]+row][position_body[1]-1] = 'solider_body'
            field[position_body[0] + row][position_body[1] + 1] = ''

        field[position_feet[0]][position_feet[1]-1] = 'solider_feet'
        field[position_feet[0]][position_feet[1] + 1] = ''
        return field
    return field

def move_right(field):
    position_feet = [game_field.get_solider_feet_row(),
                     game_field.get_solider_feet_col()]
    position_body = [game_field.get_solider_row(),
                     game_field.get_solider_col()]
    if position_body[1]+1 < consts.BOARD_COLS-1:
        for row in range(consts.SOLDIER_BODY_ROWS):
            field[position_body[0] + row][position_body[1] + 1] = 'solider_body'
            field[position_body[0] + row][position_body[1] - 1] = ''

        field[position_feet[0]][position_feet[1] - 1] = 'solider_feet'
        field[position_feet[0]][position_feet[1] + 1] = ''
        return field
    return field

def move_up( field):
    position_feet = [game_field.get_solider_feet_row(), game_field.get_solider_feet_col()]
    position_body = [game_field.get_solider_row(), game_field.get_solider_col()]
    if position_body[0] < consts.BOARD_ROWS-1:
        field[position_feet[0]][position_feet[1]] = ' '
        field[position_feet[0]][position_feet[1]+1] = ' '
        position_body[0] -= 1
        position_feet[0] -= 1
        field[position_body[0]][position_body[1]] = 'solider_body'
        field[position_feet[0]][position_feet[1]] = 'solider_feet'
        field[position_body[0]][position_body[1]+1] = 'solider_body'
        field[position_feet[0]][position_feet[1]+1] = 'solider_feet'

        return field
    return field

def move_down(field):
    position_feet = [game_field.get_solider_feet_row(),game_field.get_solider_feet_col()]
    position_body = [game_field.get_solider_row(),game_field.get_solider_col()]
    if position_feet[0] < consts.BOARD_ROWS:
        field[position_feet[0]][position_feet[1]] = 'solider_body'
        field[position_body[0]][position_body[1]] = ' '
        field[position_feet[0]][position_feet[1]+1] = 'solider_body'
        field[position_body[0]][position_body[1]+1] = ' '
        position_body[0] += 1
        position_feet[0] += 1
        field[position_feet[0]][position_feet[1]] = 'solider_feet'
        field[position_feet[0]][position_feet[1]+1] = 'solider_feet'

        #position_body[0] += 1
        #position_feet[0] += 1
        #field[position_body[0]][position_body[1] + 1] = 'solider_body'
        #field[position_feet[0]][position_feet[1] + 1] = 'solider_feet'
       #
       #
       #
       #
       # field[position_feet[0]][position_feet[1]] = 'solider_body'
       # field[position_feet[0]][position_feet[1] + 1] ='solider_body'
       # field[position_feet[0]+1][position_feet[1]] = 'solider_feet'
       # field[position_feet[0] + 1][position_feet[1]+1] = 'solider_feet'


    return  field


