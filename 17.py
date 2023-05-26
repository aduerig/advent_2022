# https://adventofcode.com/2022

from helpers import * 

import pathlib

filepath = pathlib.Path(__file__)

data_file = filepath.parent.joinpath(filepath.stem + '.dat')

jets = ''
global curr_rock, jet_index, highest_rock
highest_rock = -1
jet_index = 0
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        jets = line

directions = {'>': (1, 0), '<': (-1, 0)}

rocks = [
    [1, [(0, 0), (1, 0), (2, 0), (3, 0),]],
    [3, [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2),]],
    [3, [(2, 0), (2, 1), (2, 2), (1, 0), (0, 0),]],
    [4, [(0, 0), (0, 1), (0, 2), (0, 3)]],
    [2, [(0, 0), (0, 1), (1, 1), (1, 0)]],
]

curr_rock = 0
chamber = []
def spawn():
    global curr_rock, jet_index, highest_rock
    y_offset = highest_rock + 4

    rock_selected = rocks[curr_rock]
    curr_rock = (curr_rock + 1) % len(rocks)
    height, points = rock_selected


    for i in range(len(chamber), y_offset + height):
        chamber.append(['.'] * 7)
    
    for x, y in points:
        chamber[y_offset + y][x + 2] = '#'

    # print('OK')
    # print_board()
    # print("SPAWNED")
    return rock_selected, y_offset

def print_board():
    for row in chamber:
        print(''.join(row))

def try_move(height_of_rook, points, set_of_points, y_offset, x_offset, dir):
    global curr_rock, jet_index, highest_rock
    to_check = points
    for x, y in points:
        new_point = (x + dir[0], y + dir[1])
        if new_point in set_of_points:
            continue
        # print('checking new point', new_point, set_of_points)

        real_point = (x_offset + new_point[0], y_offset + new_point[1])
        if real_point[0] < 0 or real_point[0] > 7:
            # print('outta luck sideways')
            return False, x_offset, y_offset
        
        # print_board()
        # print(real_point)
        if real_point[1] == -1 or real_point[0] > 6 or real_point[0] < 0 or chamber[real_point[1]][real_point[0]] == '#':
            if dir[1] == -1:
                # print(f'assigning {highest_rock=}')
                highest_rock = max(highest_rock, (y_offset + height_of_rook) - 1)
                # print(f'assigning {highest_rock=} after')
            return False, x_offset, y_offset

    for x, y in points:
        chamber[y_offset + y][x_offset + x] = '.'

    x_offset += dir[0]
    y_offset += dir[1]

    for x, y in points:
        chamber[y_offset + y][x_offset + x] = '#'

    # print('moved!')
    return True, x_offset, y_offset


def move_until_done(rock, y_offset):
    global jet_index, curr_rock
    height_of_rook, points = rock
    set_of_points = set(points)
    x_offset = 2
    while True:
        dir = directions[jets[jet_index]]
        jet_index = (jet_index + 1) % len(jets)

        success, x_offset, y_offset = try_move(height_of_rook, points, set_of_points, y_offset, x_offset, dir)


        # print('eeee')
        # print('moved l/r', dir, success)
        # print_board()
        success, x_offset, y_offset = try_move(height_of_rook, points, set_of_points, y_offset, x_offset, (0, -1))

        # print_board()
        # print('moved down', dir, success)

        if not success:
            print('done with rock')
            return


print_board()
for i in range(2022):
    # print('rock', i)
    rock, y_offset = spawn()
    move_until_done(rock, y_offset)
    # print_board()
    print(f'{highest_rock=}')

print_green(highest_rock + 1)

