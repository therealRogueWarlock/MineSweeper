# MineSweeper
import pygame
import LoadSprits
from draw_functions import find_number_and_draw, draw_tile, draw_time_stamp, draw_remaining_flags
import numpy as np
import Create_game_map
import editing_layers



# screen dimensions

#win_width = 480
#win_height = 432

# tile dimensions
tile_map_width = 18
tile_map_height = 11


def flag_counter(num):
    if num < 100:
        num = '0'+str(num)

    res = [int(x) for x in str(num)]
    return res


win_width = round(26*tile_map_width)
win_height = round(39*tile_map_height)

win = pygame.display.set_mode((win_width, win_height))
# Title of game
pygame.display.set_caption('Mine Sweeper')

clock = pygame.time.Clock()


class Button:
    def __init__(self, color, x, y, width, height, text='', text_size=60, smiley = 1):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_size = text_size
        self.smiley = smiley

    def draw(self, win,):
        # Call this method to draw the button on the screen
        if self.smiley == 1:
            win.blit(LoadSprits.smiley_normal, (self.x, self.y))
        elif self.smiley == 2:
            win.blit(LoadSprits.smiley_open, (self.x, self.y))
        elif self.smiley == 3:
            win.blit(LoadSprits.smiley_dead, (self.x, self.y))
        elif self.smiley == 4:
            win.blit(LoadSprits.smiley_win, (self.x, self.y))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


smileybutton = Button((0, 0, 0), 216, 48, 48, 48, '', text_size=0)


def timer(tick_count, time_holder):

    if tick_count % 60 == 0:  # happens every second.
        if time_holder[2] >= -1:
            time_holder[2] += 1

            if time_holder[2] == 10:
                time_holder[2] = 0
                time_holder[1] += 1

                if time_holder[1] == 10:
                    time_holder[1] = 0
                    time_holder[0] += 1

    return time_holder


def check_for_win(overlay, bombs):
    row = 0
    y = 144
    tiles_removed = 0
    flags_placed = 0
    while row != 11:
        spots = 0
        x = 24
        while spots != 18:
            spot = overlay[row][spots]
            if spot == 0:
                pass

            elif spot == 1:
                tiles_removed += 1

            elif spot == 3:
                flags_placed +=1

            spots += 1
            x += 24
        row += 1
        y += 24
    if tiles_removed == (tile_map_height*tile_map_width)-bombs:
        if flags_placed == bombs:
            smileybutton.smiley = 4
            return True
    return False


def game_triggers(command, underlayer, overlay):
    if 'bomb exploded' in command:
        smileybutton.smiley = 3
        text, row, spots = command  # text, is placeholder for 'bomb exploded'
        underlayer[row][spots] = 9  # edit mine to exploded. 9 prints exploded mine
        print('you stepped on a mine :(')
        editing_layers.show_all_mines(underlayer, overlay)
        return True
    else:
        print(command)
        row, spots = command
        editing_layers.remove_zero_tiles(row, spots, underlayer, overlay)


# function that draws game window.
def re_draw_game_window(time_holder, underlayer, overlay, flag_count_holder):
    # draws game background, loaded from images.
    win.blit(LoadSprits.gamewindow, (0, 0))
    find_number_and_draw(underlayer, win)
    smileybutton.draw(win)
    draw_tile(overlay, win)
    draw_time_stamp(time_holder, win)
    draw_remaining_flags(flag_count_holder, win)

    # function needed to update game window.
    pygame.display.update()


# main game loop
def game_loop(overlay, underlayer, flag_count_holder, bombs):
    dead = False
    won = False
    run = True
    tick_count = 0
    time_holder_zero = [0, 0, -1]
    smileybutton.smiley = 1
    while run:
        clock.tick(60)

        # timer creates a time holder (a list of time)
        if not dead and not won:
            time_holder = timer(tick_count, time_holder_zero)

        # draw game window at tick rate
        re_draw_game_window(time_holder, underlayer, overlay, flag_count_holder,)

        # looking for events, mouse movement, mouse actions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            won = check_for_win(overlay, bombs)  # checking for win, returns False if not.
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if not dead:
                        smileybutton.smiley = 2
            if event.type == pygame.MOUSEBUTTONUP:
                if not dead:
                    smileybutton.smiley = 1
                if event.button == 1:  # if left mouse button clicked
                    if not dead and not won:  # if stepping on a mine
                        editing_layers.remove_tile(pos, underlayer, overlay)  # removing a tile in pos of mouse
                        # if returning other than none, like "bomb exploded".
                        if editing_layers.remove_tile(pos, underlayer, overlay) is not None:
                            # game trigger takes return statement as a command
                            print('dident return none')
                            if game_triggers((editing_layers.remove_tile(pos, underlayer, overlay)), underlayer, overlay):
                                dead = True

                if not dead and not won:
                    if event.button == 3:  # if right mouse button clicked.
                        editing_layers.flag_tile(pos, overlay, flag_count_holder)  # putting a flag on
                                                                                    # tile at pos of mouse

                if smileybutton.isOver(pos):
                    run = False
                    game_starter()

        tick_count += 1


# starts program
def game_starter():

    bombs = 31

    flag_count_holder = flag_counter(bombs)
    overlay = np.zeros((tile_map_height, tile_map_width))

    underlayer = np.zeros((tile_map_height, tile_map_width))
    # place the bombs on the map
    Create_game_map.place_bombs(underlayer, bombs)
    # gives value to spots according to how many bombs around it.
    Create_game_map.find_bombs(underlayer)
    # starts the main game loop
    game_loop(overlay, underlayer, flag_count_holder, bombs)


game_starter()

