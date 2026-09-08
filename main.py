import sys
import tkinter
import pygame

import game_field
import screen
import consts
import soldier
from screen import create_screen

# def drew():


def main():
    pygame.init()
    screens = create_screen()
    field = game_field.field
    position = (0,0)
    # player = soldier.solider()
    run = True

    class player(pygame.Rect):
        def __init__(self):
            pygame.Rect.__init__(self, 0, 0, 40, 80)

            solider_image = pygame.image.load('soldier.png')
            solider_image_resize = pygame.transform.scale(solider_image,
                                                          (40, 80))
            self.image = solider_image_resize
    while run:
        pygame.display.update()
        # # player = soldier.solider()
        # solider_image = pygame.image.load('soldier.png')
        # solider_image_resize = pygame.transform.scale(solider_image, (40, 80))
        # screens.blit(solider_image_resize, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if pygame.K_UP or pygame.K_w:
                    # soldier.move_right(position, field
                    player.y -=  consts.CELL_SIZE

    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         pygame.quit()
    #         sys.exit()
    #     if event.type == pygame.KEYDOWN:
    #         if pygame.K_RIGHT or pygame.K_d:
    #             soldier.move_right(position, field)
    #
    #             player.y -= consts.CELL_SIZE





if __name__ == '__main__':
    main()

# def handle_user_events():
#     for event in pygame.event.get():
#
#         if event.type == pygame.QUIT:
#             state["is_window_open"] = False
#
#         elif state["state"] != consts.RUNNING_STATE:
#             continue
#
#         if event.type == pygame.MOUSEMOTION:
#             rotate_arrow()
#
#         elif event.type == pygame.MOUSEBUTTONDOWN and \
#                 not state["is_bubble_fired"] and \
#                 not state["bubbles_popping"]:
#             fire_bubble()
