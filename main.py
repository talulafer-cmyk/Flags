import sys
import time
import pygame
import screen
import game_field
import consts
pygame.init()
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
def main():
    run=True
    while run:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                 pygame.QUIT()
                 exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                   # move solider up

                if event.type ==pygame.K_LEFT:
                    #move solider left
                if event.key==pygame.K_DOWN:
                    # move solider down
                if event.key==pygame.K_RIGHT:
                    #move solider right
            if is_lose:
                time.sleep(2.5)
                run=False


            if is_win:
              time.sleep(2.5)
              run = False


        pygame.display.update()
if __name__ == '__main__':
    main()
