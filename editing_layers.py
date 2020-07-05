# in this module, all the functions for finding and changing specific spots in layers(matrices)

# debug/  print comments
debug = False


# shows all mines upon losing
def show_all_mines(bottom_matrix, top_matrix):
    row = 0
    while row != 11:
        spots = 0
        while spots != 18:
            spot = bottom_matrix[row][spots]
            if spot == 10:
                top_matrix[row][spots] = 1
            else:
                pass
            spots += 1
        row += 1


# if a tile with nothing under (0), find all close by 0 and clear the
def remove_zero_tiles(row, spots, bottom_matrix, top_matrix):

    check_zero_tiles = []  # creating a queue of zero tiles to check.
    checked_zero_tiles = []  # list of tiles already checked.

    if not check_zero_tiles:
        check_zero_tiles.append((row, spots))

    while check_zero_tiles:
        for (row, spots) in check_zero_tiles:
            # checking Right, above, left, beneath, and all the corners around.
            right = 'nothing'
            left = 'nothing'
            above = 'nothing'
            beneath = 'nothing'
            top_right = 'nothing'
            top_left = 'nothing'
            lower_right = 'nothing'
            lower_left = 'nothing'
            if debug:
                print(f'checking {(row, spots)} in \n queue {check_zero_tiles}')
            if spots != 17:  # if not the last spot on a row
                # checking for 0 or not 10 and if not flagged to the right
                if bottom_matrix[row][spots + 1] != 10:
                    if top_matrix[row][spots + 1] != 3:
                        top_matrix[row][spots + 1] = 1  # setting the spot to clear

                    # check if the new tile found is only 0 and not flagged on top.
                    if bottom_matrix[row][spots + 1] == 0:
                        if (row, spots+1) not in check_zero_tiles:  # check if not already in queue
                            if (row, spots+1) not in checked_zero_tiles:  # check i not already checked
                                check_zero_tiles.append((row, spots+1))
                                right = check_zero_tiles[-1]

            if row != 0:  # if not in the first row
                # checking for 0 or not 10 above
                if bottom_matrix[row - 1][spots] != 10:
                    if top_matrix[row - 1][spots] != 3:
                        top_matrix[row - 1][spots] = 1

                        # check if the new tile found is only 0 and not flagged on top.
                        if bottom_matrix[row-1][spots] == 0:
                            if (row - 1, spots) not in check_zero_tiles:  # check if not already in queue
                                if (row - 1, spots) not in checked_zero_tiles:  # check i not already checked
                                    check_zero_tiles.append((row-1, spots))
                                    above = check_zero_tiles[-1]

            if spots != 0:  # if not the first spot on a row
                # checking for 0 or not 10 to the left
                if bottom_matrix[row][spots - 1] != 10:
                    if top_matrix[row][spots - 1] != 3:
                        top_matrix[row][spots - 1] = 1

                        # check if the new tile found is only 0 and not flagged on top.
                        if bottom_matrix[row][spots - 1] == 0:
                            if (row, spots - 1) not in check_zero_tiles:  # check if not already in the queue
                                if (row, spots - 1) not in checked_zero_tiles:  # check i not already checked
                                    check_zero_tiles.append((row, spots - 1))  # add the tile to stack
                                    left = check_zero_tiles[-1]

            if row != 10:  # if not on the last row
                # checking for 0 or not 10 beneath
                if bottom_matrix[row + 1][spots] != 10:
                    if top_matrix[row + 1][spots] != 3:
                        top_matrix[row + 1][spots] = 1

                        # check if the new tile found is only 0 and not flagged on top.
                        if bottom_matrix[row + 1][spots] == 0:
                            if (row + 1, spots) not in check_zero_tiles:  # check if not already in the queue
                                if (row + 1, spots) not in checked_zero_tiles:  # check i not already checked
                                    check_zero_tiles.append((row + 1, spots))
                                    beneath = check_zero_tiles[-1]

            # checking all the corners around.

            # checking if not in top right corner
            if spots != 17:  # if not on the last spot
                if row != 0:  # if not in the first row
                    # checking for 0 or not 10 to the right
                    if bottom_matrix[row - 1][spots + 1] != 10:
                        if top_matrix[row - 1][spots + 1] != 3:
                            top_matrix[row - 1][spots + 1] = 1  # setting the spot to clear

                            # check if the new tile found is only 0 and not flagged on top.
                            if bottom_matrix[row - 1][spots + 1] == 0:
                                if (row-1, spots+1) not in check_zero_tiles:  # check if not already in queue
                                    if (row-1, spots+1) not in checked_zero_tiles:  # check i not already checked
                                        check_zero_tiles.append((row-1, spots+1))
                                        top_right = check_zero_tiles[-1]

            # checking if not in top left corner
            if row != 0:  # if not in the first row
                if spots != 0:  # if not in the first spot
                    # checking for 0 or not 10 above
                    if bottom_matrix[row - 1][spots - 1] != 10:
                        if top_matrix[row - 1][spots - 1] != 3:
                            top_matrix[row - 1][spots - 1] = 1

                            # check if the new tile found is only 0 and not flagged on top.
                            if bottom_matrix[row - 1][spots - 1] == 0:
                                if (row - 1, spots-1) not in check_zero_tiles:  # check if not already in queue
                                    if (row - 1, spots-1) not in checked_zero_tiles:  # check i not already checked
                                        check_zero_tiles.append((row-1, spots-1))
                                        top_left = check_zero_tiles[-1]

            # checking if not in lower left corner
            if spots != 0:  # if not the first spot on a row
                if row != 10:  # if not in the last row
                    # checking for 0 or not 10 to the left
                    if bottom_matrix[row + 1][spots - 1] != 10:
                        if top_matrix[row + 1][spots - 1] != 3:
                            top_matrix[row + 1][spots - 1] = 1

                            # check if the new tile found is only 0 and not flagged on top.
                            if bottom_matrix[row+1][spots - 1] == 0:
                                if (row+1, spots - 1) not in check_zero_tiles:  # check if not already in the queue
                                    if (row+1, spots - 1) not in checked_zero_tiles:  # check i not already checked
                                        check_zero_tiles.append((row+1, spots - 1))  # add the tile to stack
                                        lower_left = check_zero_tiles[-1]

            # checking of not in the lower right corner
            if row != 10:  # if not on the last row
                if spots != 17:  # if not on the last spot
                    # checking for 0 or not 10 lower right
                    if bottom_matrix[row + 1][spots + 1] != 10:
                        if top_matrix[row + 1][spots + 1] != 3:
                            top_matrix[row + 1][spots + 1] = 1

                            # check if the new tile found is only 0 a
                            if bottom_matrix[row + 1][spots + 1] == 0:
                                if (row + 1, spots+1) not in check_zero_tiles:  # check if not already in the queue
                                    if (row + 1, spots+1) not in checked_zero_tiles:  # check i not already checked
                                        check_zero_tiles.append((row + 1, spots+1))  # add to queue
                                        lower_right = check_zero_tiles[-1]

            checked_zero_tiles.append((row, spots))
            if debug:
                print(f'checked {row, spots} \nfound:\n right {right}\n above {above}'
                      f'\n left {left}\n beneath {beneath}\n top right {top_right}\n top left {top_left}'
                      f'\n lower right {lower_right}\n lower left {lower_left}')
            check_zero_tiles.remove((row, spots))  # remove first item in the list
    if debug:
        print(top_matrix)
        print(f'done...\n checked: {checked_zero_tiles}')


# if clicking a tile, remove it from the top layer.
def remove_tile(pos, bottom_matrix, top_matrix):
    if debug:
        print(f'finding tile to remove in {pos}')
    row = 0
    y = 144
    while row != 11:
        spots = 0
        x = 24
        while spots != 18:
            # Pos is the mouse position or a tuple of (x,y) coordinates
            if x < pos[0] < x + 24:  # 24 is the size of the tiles
                if y < pos[1] < y + 24:
                    if top_matrix[row][spots] == 3:  # check if the tile is flagged, if flagged tile cant be removed.
                        if debug:
                            print(f'tile is flagged ({row},{spots})')
                        pass
                    if top_matrix[row][spots] == 0:  # check if tile is not removed
                        top_matrix[row][spots] = 1  # if not removed, removing tile
                        # if debug:
                        #     print(f'tile removed ({row},{spots})')

                    # TODO somthing fishy here.

                    if top_matrix[row][spots] == 1:

                        if bottom_matrix[row][spots] == 0:
                            # return row, and spots to function that removes all close 0 tiles.
                            print('clicked on 0')
                            return row, spots

                        elif bottom_matrix[row][spots] in range(1, 10):
                            # return row, and spots to function that removes all close 1-9 tiles.
                            print('clicked 1-9')
                            return row, spots

                        elif bottom_matrix[row][spots] == 10:
                            print('clicked on bomb')
                            return 'bomb exploded', row, spots

            spots += 1
            x += 24
        row += 1
        y += 24
    if debug:
        print(top_matrix)


def flag_tile(pos, top_matrix, flag_count):
    if debug:
        print(f'finding tile to put or remove a flag, in {pos}')
    row = 0
    y = 144
    while row != 11:
        spots = 0
        x = 24
        while spots != 18:
            # Pos is the mouse position or a tuple of (x,y) coordinates
            if x < pos[0] < x + 24:  # 24 is the size of the tiles
                if y < pos[1] < y + 24:
                    if top_matrix[row][spots] == 3:  # if already flagged
                        if debug:
                            print(f'removed flag from tile ({row},{spots})')

                        top_matrix[row][spots] = 0

                        # shit code for editing the flag holder list
                        if flag_count[2] >= -1:
                            flag_count[2] += 1

                            if flag_count[2] == 10:
                                flag_count[2] = 0
                                flag_count[1] += 1

                                if flag_count[1] == 10:
                                    flag_count[1] = 0
                                    flag_count[0] += 1

                    elif top_matrix[row][spots] != 1:  # if the tile is already removed, don't put a flag.
                        if debug:
                            print(f'tile flagged ({row},{spots})')

                            # shit code for editing the flag holder list
                        if flag_count[0] or flag_count[1] or flag_count[2] != 0:
                            top_matrix[row][spots] = 3
                            if flag_count[2] > 0:
                                flag_count[2] -= 1

                            elif flag_count[2] == 0:
                                flag_count[2] = 9
                                flag_count[1] -= 1

                            elif flag_count[1] == 0:
                                flag_count[1] = 9
                                flag_count[0] -= 1

            spots += 1
            x += 24
        row += 1
        y += 24
