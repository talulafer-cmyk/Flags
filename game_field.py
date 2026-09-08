import consts
import random
flag_row = consts.BOARD_ROWS - consts.FLAG_ROWS
flag_col = consts.BOARD_COLS - consts.FLAG_COLS
field=[]

def randomize_bombs():
    bombs_index_list=[]
    for bomb in range(consts.MINES_COUNT):
        rnd_col=random.randint(consts.MINE_COLS, consts.BOARD_COLS-3)
        rnd_row=random.randint(consts.MINE_ROWS,consts.BOARD_ROWS)
        item=(rnd_row,rnd_col)
        bombs_index_list.append(item)
    return bombs_index_list


def create_field():
    bombs_indexes=randomize_bombs()
    for row in range(consts.BOARD_ROWS):
        item=[]
        for col in range(consts.BOARD_COLS):
            item.append("")
        field.append(item)
     # insert bombs
    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            for bomb in bombs_indexes:
                if bomb[0]==row and bomb[1]==col:
                    field[row][col]="BOMB"
                    field[row][col+1] = "BOMB"
                    field[row][col+2] = "BOMB"
    #insert flag
    for row in range(consts.BOARD_ROWS-consts.FLAG_ROWS,consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS-consts.FLAG_COLS,consts.BOARD_COLS):
            field[row][col]="FLAG"
    # insert first pos of body solider
    for row in range(consts.SOLDIER_BODY_ROWS):
        for col in range(consts.SOLDIER_COLS):
            field[row][col]="solider_body"
    # insert first pos of feets
    for row in range(consts.SOLDIER_BODY_ROWS,consts.SOLDIER_ROWS):
        for col in range(consts.SOLDIER_COLS):
            field[row][col] = "solider_feet"







