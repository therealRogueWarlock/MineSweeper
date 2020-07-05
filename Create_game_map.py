import random

# debug/  print comments
debug = False

# matrix, maps out the game.
'''map = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
          
          insane !!  
[[ 1.  1.  1.  0.  0.  1.  1.  1.  0.  0.  0.  0.  0.  1. 10.  1.  1. 10.]
 [ 1. 10.  1.  0.  0.  2. 10.  2.  0.  0.  1.  1.  1.  1.  1.  1.  1.  1.]
 [ 1.  1.  1.  0.  0.  2. 10.  2.  0.  1.  2. 10.  2.  1.  1.  0.  0.  0.]
 [ 1.  1.  1.  0.  0.  2.  3.  4.  2.  2. 10.  2.  3. 10.  2.  0.  0.  0.]
 [ 1. 10.  1.  0.  0.  1. 10. 10. 10.  2.  1.  1.  2. 10.  2.  0.  0.  0.]
 [ 1.  1.  2.  1.  1.  1.  4. 10.  5.  2.  0.  0.  1.  1.  1.  0.  0.  0.]
 [ 0.  0.  2. 10.  2.  1.  3. 10. 10.  1.  1.  1.  1.  0.  0.  0.  0.  0.]
 [ 0.  0.  2. 10.  2.  1. 10.  3.  2.  1.  1. 10.  1.  0.  0.  0.  0.  0.]
 [ 0.  0.  1.  1.  1.  2.  3.  3.  1.  0.  1.  1.  1.  0.  1.  1.  2.  1.]
 [ 0.  0.  0.  1.  1.  2. 10. 10.  1.  0.  0.  0.  0.  0.  1. 10.  2. 10.]
 [ 0.  0.  0.  1. 10.  2.  2.  2.  1.  0.  0.  0.  0.  0.  1.  1.  2.  1.]]'''


# placing bombs at random locations
def place_bombs(matrix, bombs):
    # for every bomb in game, add a bomb to game map at a random spot. bombs has value of 10.
    for bomb in range(bombs):
        repeat = True
        while repeat:
            row = random.randint(0, 10)
            spots = random.randint(0, 17)
            random_spot = matrix[row][spots]
            if random_spot != 10:
                matrix[row][spots] = 10
                repeat = False


# giving the tiles a value according to the bombs around it.
def find_bombs(matrix):  # giving value to spots according to how many bombs are around it.
    row = 0
    while row != 11:
        spots = 0
        while spots != 18:
            count = 0
            spot = matrix[row][spots]
            if spot == 10:
                pass
            elif spot == 0:
                # checks for bombs close on the row above
                if row != 0:  # if no row above, don't check
                    if spots != 0:
                        if matrix[row - 1][spots - 1] == 10:  # in the corner up, left
                            if debug:
                                print('bomb found: up, left')
                            count += 1
                        else:
                            if debug:
                                print('no bomb found. up, left')
                    else:
                        if debug:
                            print('first spot in the row, no column')

                    if matrix[row - 1][spots] == 10:  # just above
                        if debug:
                            print('bomb found: above')
                        count += 1
                    else:
                        if debug:
                            print('no bomb found: above')

                    if spots != 17:
                        if matrix[row - 1][spots + 1] == 10:  # in the corner up, right
                            if debug:
                                print('bomb found: up, right')
                            count += 1
                        else:
                            if debug:
                                print('no bomb found: up, right')
                else:
                    if debug:
                        print('no row above')

                if spots != 0:  # if first spot in the row, don't check spots on column behind.
                    if matrix[row][spots - 1] == 10:  # checking to the left
                        if debug:
                            print('bomb found: left ')
                        count += 1
                    else:
                        if debug:
                            print('no bomb found: left')
                else:
                    if debug:
                        print('first in the row, no column behind')

                if spots != 17:  # if last spot in the row, don't check spots on column to the right.
                    if matrix[row][spots + 1] == 10:  # checking to the right
                        if debug:
                            print('bomb found: right ')
                        count += 1
                    else:
                        if debug:
                            print('no bomb found: right')
                else:
                    if debug:
                        print('last in the row, no column right')

                if row != 10:  # if not on the last row.
                    if spots != 0:
                        if matrix[row + 1][spots - 1] == 10:  # in the corner down, left
                            if debug:
                                print('bomb found: down, left')
                            count += 1
                        else:
                            if debug:
                                print('no bomb found: down, left')

                    if matrix[row + 1][spots] == 10:  # just below
                        if debug:
                            print('bomb found: just below')
                        count += 1
                    else:
                        if debug:
                            print('no bomb found: just below')
                    if spots != 17:
                        if matrix[row + 1][spots + 1] == 10:  # in the corner down, right
                            if debug:
                                print('bomb found: down, right')
                            count += 1
                        else:
                            if debug:
                                print('no bomb found: down, right')
                matrix[row][spots] = count
            if debug:
                print(f'spot = {spot}, ({row}, {spots})\n')
            spots += 1
        row += 1
    print(matrix)
    return matrix

