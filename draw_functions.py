import LoadSprits


# using the map matrix(lower layer), reading values and drawing tile with number.
def find_number_and_draw(underlayer, win):
    row = 0
    y = 144
    while row != 11:
        spots = 0
        x = 24
        while spots != 18:
            spot = underlayer[row][spots]
            if spot == 0:
                win.blit(LoadSprits.cleartile, (x, y))

            elif spot == 1:
                win.blit(LoadSprits.clear1, (x, y))

            elif spot == 2:
                win.blit(LoadSprits.clear2, (x, y))

            elif spot == 3:
                win.blit(LoadSprits.clear3, (x, y))

            elif spot == 4:
                win.blit(LoadSprits.clear4, (x, y))

            elif spot == 5:
                win.blit(LoadSprits.clear5, (x, y))

            elif spot == 6:
                win.blit(LoadSprits.clear6, (x, y))

            elif spot == 7:
                win.blit(LoadSprits.clear7, (x, y))

            elif spot == 8:
                win.blit(LoadSprits.clear8, (x, y))

            elif spot == 9:
                win.blit(LoadSprits.explodebomb, (x, y))

            elif spot == 10:
                win.blit(LoadSprits.clearbomb, (x, y))

            spots += 1
            x += 24
        row += 1
        y += 24


# draws every tile(the layer on top) from info from overlay matrix
def draw_tile(overlay, win):
    # drawing a tile for evey spot on the map, using overlay(the layer on top of the map layer)
    row = 0
    y = 144
    while row != 11:
        spots = 0
        x = 24
        while spots != 18:
            spot = overlay[row][spots]
            if spot == 0:
                win.blit(LoadSprits.tile, (x, y))

            elif spot == 1:
                pass

            elif spot == 3:
                win.blit(LoadSprits.flag, (x, y))

            spots += 1
            x += 24
        row += 1
        y += 24


def draw_time_stamp(time, win):
    y = 48
    x = 288
    for number in time:
        if number == 0:
            win.blit(LoadSprits.number0, (x, y))
        if number == 1:
            win.blit(LoadSprits.number1, (x, y))
        if number == 2:
            win.blit(LoadSprits.number2, (x, y))
        if number == 3:
            win.blit(LoadSprits.number3, (x, y))
        if number == 4:
            win.blit(LoadSprits.number4, (x, y))
        if number == 5:
            win.blit(LoadSprits.number5, (x, y))
        if number == 6:
            win.blit(LoadSprits.number6, (x, y))
        if number == 7:
            win.blit(LoadSprits.number7, (x, y))
        if number == 8:
            win.blit(LoadSprits.number8, (x, y))
        if number == 9:
            win.blit(LoadSprits.number9, (x, y))
        x += 48


def draw_remaining_flags(flag_count_holder, win):
    y = 48
    x = 48
    for number in flag_count_holder:
        if number == 0:
            win.blit(LoadSprits.number0, (x, y))
        if number == 1:
            win.blit(LoadSprits.number1, (x, y))
        if number == 2:
            win.blit(LoadSprits.number2, (x, y))
        if number == 3:
            win.blit(LoadSprits.number3, (x, y))
        if number == 4:
            win.blit(LoadSprits.number4, (x, y))
        if number == 5:
            win.blit(LoadSprits.number5, (x, y))
        if number == 6:
            win.blit(LoadSprits.number6, (x, y))
        if number == 7:
            win.blit(LoadSprits.number7, (x, y))
        if number == 8:
            win.blit(LoadSprits.number8, (x, y))
        if number == 9:
            win.blit(LoadSprits.number9, (x, y))
        x += 48
