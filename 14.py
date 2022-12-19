# https://adventofcode.com/2022

from helpers import * 

import pathlib

filepath = pathlib.Path(__file__)

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


grid = []
for i in range(10000):
    grid.append(['.'] * 10000)



def fill_in(curr, to):
    global lowest_rock
    while curr != to:
        lowest_rock = max(lowest_rock, curr[1])
        grid[curr[1]][curr[0]] = '#'
        if to[0] != curr[0]:
            curr[0] += int(int(to[0] > curr[0]) * 2) - 1
        if to[1] != curr[1]:
            curr[1] += int(int(to[1] > curr[1]) * 2) - 1
        grid[curr[1]][curr[0]] = '#'


lowest_rock = 0
source = [500, 0]
with open(data_file) as f:
    for index, line in enumerate(f.readlines()):
        line = list(map(lambda x: x.strip(), line.strip().split('->')))
        curr = None

        for pair in line:
            x, y = map(int, pair.split(','))
            if curr == None:
                curr = [x, y]
            else:
                fill_in(curr, [x, y])

fill_in([0, lowest_rock + 2], [len(grid[0]) - 1, lowest_rock + 2])

def print_grid(x_bounds=[], y_bounds=[]):
    if not x_bounds:
        x_bounds = (0, len(grid[0]))
    if not y_bounds:
        y_bounds = (0, len(grid))

    for y in range(y_bounds[0], y_bounds[1]):
        row = grid[y]
        to_print = []
        for x in range(x_bounds[0], x_bounds[1]):
            val = row[x]
            if [x, y] == source:
                to_print.append(red('X'))
            elif val == '#':
                to_print.append(blue('#'))
            elif val == 'o':
                to_print.append(yellow('o'))
            else:
                to_print.append(val)
        print(''.join(to_print))

print_blue(f'Lowest rock is {lowest_rock}')
print_cyan('=== STARTING ===')
print_grid(x_bounds=(490, 510), y_bounds=(0, 11))

piece_of_sand = 0
last_confirmed_piece_of_sand = 0
while True:
    piece_of_sand += 1

    if grid[source[1]][source[0]] != '.':
        print_grid(x_bounds=(490, 510), y_bounds=(0, 11))
        print_green(f'BLOCKED, last piece_of_sand: {piece_of_sand - 1}')
        exit()

    curr = [source[0], source[1]]
    grid[curr[1]][curr[0]] = 'o'
    while True:
        if curr[1] > lowest_rock + 1:
            print_grid(x_bounds=(490, 510), y_bounds=(0, 11))
            print_green(f'last_confirmed_piece_of_sand: {last_confirmed_piece_of_sand}, current piece_of_sand: {piece_of_sand}')
            exit()
        elif grid[curr[1] + 1][curr[0]] == '.':
            grid[curr[1]][curr[0]] = '.'
            curr[1] += 1
            grid[curr[1]][curr[0]] = 'o'
        elif grid[curr[1] + 1][curr[0] - 1] == '.':
            grid[curr[1]][curr[0]] = '.'
            curr[1] += 1
            curr[0] -= 1
            grid[curr[1]][curr[0]] = 'o'
        elif grid[curr[1] + 1][curr[0] + 1] == '.':
            grid[curr[1]][curr[0]] = '.'
            curr[1] += 1
            curr[0] += 1
            grid[curr[1]][curr[0]] = 'o'
        else:
            break
    last_confirmed_piece_of_sand = piece_of_sand



# # https://adventofcode.com/2022

# from helpers import * 

# import pathlib

# filepath = pathlib.Path(__file__)

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# grid = []
# for i in range(1000):
#     grid.append(['.'] * 1000)



# lowest_rock = 0
# source = [500, 0]
# with open(data_file) as f:
#     for index, line in enumerate(f.readlines()):
#         line = list(map(lambda x: x.strip(), line.strip().split('->')))
#         curr = None

#         for pair in line:
#             x, y = map(int, pair.split(','))
#             if curr == None:
#                 curr = [x, y]
#             else:
#                 while curr != [x, y]:
#                     lowest_rock = max(lowest_rock, curr[1])
#                     grid[curr[1]][curr[0]] = '#'
#                     if x != curr[0]:
#                         curr[0] += int(int(x > curr[0]) * 2) - 1
#                     if y != curr[1]:
#                         curr[1] += int(int(y > curr[1]) * 2) - 1
#                     grid[curr[1]][curr[0]] = '#'


# def print_grid(x_bounds=[], y_bounds=[]):
#     if not x_bounds:
#         x_bounds = (0, len(grid[0]))
#     if not y_bounds:
#         y_bounds = (0, len(grid))

#     for y in range(y_bounds[0], y_bounds[1]):
#         row = grid[y]
#         to_print = []
#         for x in range(x_bounds[0], x_bounds[1]):
#             val = row[x]
#             if [x, y] == source:
#                 to_print.append(red('X'))
#             elif val == '#':
#                 to_print.append(blue('#'))
#             elif val == 'o':
#                 to_print.append(yellow('o'))
#             else:
#                 to_print.append(val)
#         print(''.join(to_print))

# print_blue(f'Lowest rock is {lowest_rock}')
# print_cyan('=== STARTING ===')
# print_grid(x_bounds=(490, 510), y_bounds=(0, 11))

# piece_of_sand = 0
# last_confirmed_piece_of_sand = 0
# while True:
#     piece_of_sand += 1

#     if grid[source[1]][source[0]] != '.':
#         print_grid(x_bounds=(490, 510), y_bounds=(0, 11))
#         print_green(f'BLOCKED, current piece_of_sand: {piece_of_sand}')
#         exit()

#     curr = [source[0], source[1]]
#     grid[curr[1]][curr[0]] = 'o'
#     while True:
#         if curr[1] > lowest_rock + 1:
#             print_grid(x_bounds=(490, 510), y_bounds=(0, 11))
#             print_green(f'last_confirmed_piece_of_sand: {last_confirmed_piece_of_sand}, current piece_of_sand: {piece_of_sand}')
#             exit()
#         elif grid[curr[1] + 1][curr[0]] == '.':
#             grid[curr[1]][curr[0]] = '.'
#             curr[1] += 1
#             grid[curr[1]][curr[0]] = 'o'
#         elif grid[curr[1] + 1][curr[0] - 1] == '.':
#             grid[curr[1]][curr[0]] = '.'
#             curr[1] += 1
#             curr[0] -= 1
#             grid[curr[1]][curr[0]] = 'o'
#         elif grid[curr[1] + 1][curr[0] + 1] == '.':
#             grid[curr[1]][curr[0]] = '.'
#             curr[1] += 1
#             curr[0] += 1
#             grid[curr[1]][curr[0]] = 'o'
#         else:
#             break
#     last_confirmed_piece_of_sand = piece_of_sand