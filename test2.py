import sys
import random
import time

import pygame
from sys import exit
import consts
import soldier
import game_field
import screen


# state = {
#     "is_window_open": True,
#     "state": consts.RUNNING_STATE,
# }

def is_win():
    # get solider pos:
    solider_row=game_field.get_solider_row()
    solider_col=game_field.get_solider_col()
    if game_field.is_in_flag_location(solider_row,solider_col):
       screen.draw_win_message()
       return True
    return False
def is_lose():

    #get solider pos:
    solider_row=game_field.get_solider_feet_row()
    solider_col=game_field.get_solider_feet_col()
    if game_field.is_in_bomb_location(solider_row,solider_col):
        screen.draw_lose_message()
        return True
    return False

bush_indexes=[]
item=()
for i in range(20):
   ran_x = random.randrange(consts.WINDOW_WIDTH)
   ran_y = random.randrange(consts.WINDOW_HEIGHT)
   item = (ran_x, ran_y)
   bush_indexes.append(item)

def create_screen():
    window = pygame.display.set_mode(
            (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    pygame.display.set_caption("the flag")
    clock = pygame.time.Clock()
    player_image = pygame.image.load('soldier.png')
    player_image = pygame.transform.scale(player_image, (40, 80))
    return window


def draw(window,player_image, player):
    window.fill('lightgreen')
    # win = bushes()
    window.blit(player_image, player)
    flag_image = pygame.image.load('flag.png')
    flag_image = pygame.transform.scale(flag_image, (consts.FLAG_COLS * 20,
                                                     consts.FLAG_ROWS * 20))
    window.blit(flag_image,
                (game_field.flag_col * 20, game_field.flag_row * 20))

def main():
    pygame.init()
    window = pygame.display.set_mode(
            (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    pygame.display.set_caption("the flag")
    clock = pygame.time.Clock()
    player_image = pygame.image.load('soldier.png')
    player_image = pygame.transform.scale(player_image, (40, 80))


    class Player(pygame.Rect):
        def __init__(self):
            pygame.Rect.__init__(self, 0, 0, 40, 80)
            self.image = player_image

    player = Player()
    game_field.create_field()
    run = True

    while run :

        bush = pygame.image.load('grass.png')
        resize_bush = pygame.transform.scale(bush, (60, 60))
        for i in range(20):
            # ran_x = random.randrange(consts.WINDOW_WIDTH)
            # ran_y = random.randrange(consts.WINDOW_HEIGHT)
            window.blit(resize_bush, (bush_indexes[i][0],bush_indexes[i][1]))
        pygame.display.update()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if player.y > consts.CELL_SIZE:
                         player.y -= consts.CELL_SIZE
                         soldier.move_up(game_field.field)
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if player.y < consts.WINDOW_HEIGHT - consts.CELL_SIZE:
                        player.y += consts.CELL_SIZE
                        soldier.move_down(game_field.field)
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if player.x < consts.WINDOW_WIDTH - consts.CELL_SIZE:
                        player.x += consts.CELL_SIZE
                        soldier.move_right(game_field.field)
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if player.x > consts.CELL_SIZE:
                        player.x -= consts.CELL_SIZE
                        soldier.move_left(game_field.field)
            if is_lose:
                time.sleep(2.5)
                run = False

            if is_win:
                time.sleep(2.5)
                run = False

        draw(window,player_image, player)
        pygame.display.update()
        clock.tick(60)
main()

