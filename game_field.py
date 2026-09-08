import consts
import random
flag_row = consts.BOARD_ROWS - consts.FLAG_ROWS
flag_col = consts.BOARD_COLS - consts.FLAG_COLS
field=[]
bombs_index_list=[]
def randomize_bombs():

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
            item.append(" ")
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


# function that check if solider's body on flag location:
def is_in_flag_location(solider_row,solider_col):
    for row in range(flag_row,consts.BOARD_ROWS):
        for col in range(flag_col,consts.BOARD_COLS):
            if field[row][col]=="solider_body":
                return True
    return False

# function that check if solider's feet are on bomb location:
def is_in_bomb_location(solider_row,solider_col):
    for index in bombs_index_list:
        current_bomb_location_row = index[0]  # current index row
        current_bomb_location_col = index[1]  # current index col
        for col in range(current_bomb_location_col,current_bomb_location_col+consts.MINE_COLS):
            if field[current_bomb_location_row][col]=="solider_feet":
                return True
    return False

# function the find the first solider's location:
#for col:
def get_solider_col():
    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            if field[row][col]=="solider_body":
                return col
    return -1
#for row:
def get_solider_row():
    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            if field[row][col] == "solider_body":
                return row
    return -1
# function the find the first solider feet's location:
#for col:
def get_solider_feet_col():
    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            if field[row][col] == "solider_feet":
                return col
    return -1
#for row:
def get_solider_feet_row():
    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            if field[row][col] == "solider_feet":
                return row
    return -1







