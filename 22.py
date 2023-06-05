# https://adventofcode.com/2022

from helpers import * 

import pathlib

filepath = pathlib.Path(__file__)

data_file = filepath.parent.joinpath(filepath.stem + '.dat')

facing_arrow = {
    (1, 0): '>',
    (0, 1): '^',
    (-1, 0): '<',
    (0, -1): 'v',
}


grid = []
path = []
max_length = 0
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip('\n')
        if line.strip() == '':
            continue
        if line[0] not in ['.', '#', ' ']:
            for index1, segment in enumerate(line.split('L')):
                for index2, part in enumerate(segment.split('R')):
                    path.append(int(part))
                    if index2 != len(segment.split('R')) - 1:
                        path.append('R')
                if index1 != len(line.split('L')) - 1:
                    path.append('L')
        else:
            to_add = list(line)
            if len(line) < max_length:
                to_add += [' '] * (max_length - len(line))
            grid.append(to_add)
            max_length = max(max_length, len(line))

for line in grid:
    print(''.join(line))
print_cyan('path', path)


def start_row(row, func):
    for index, ele in func(list(enumerate(grid[row]))):
        if ele in ['#', '.']:
            return index
    # return min(grid[row].index('#'), grid[row].index('.'))

def start_col(col, func):
    for index, row in func(list(enumerate(grid))):
        print(row, len(row), col)
        if row[col] in ['#', '.']:
            return index


def print_board():
    for index, line in enumerate(grid):
        print_line = line.copy()
        if index == pos[1]:
            print_line[pos[0]] = facing_arrow[direction]
        print(''.join(print_line))

pos = (start_row(0, lambda x: x), 0)
direction = (1, 0)

facing_direction = {
    (1, 0): lambda x: x,
    (0, 1): reversed,
    (-1, 0): reversed,
    (0, -1): lambda x: x
}

print_red('===STARTING===')
for step in path:
    # print_board()
    # input(f'enter to continue, going to perform {step}')
    if step == 'L':
        direction = (-direction[1], direction[0])
    elif step == 'R':
        direction = (direction[1], -direction[0])
    else:
        for i in range(step):
            new_pos = [pos[0] + direction[0], pos[1] - direction[1]]
            print(f'{i=}, {new_pos=}, {direction=}')

            out_of_bounds = new_pos[0] < 0 or new_pos[0] >= len(grid[0]) or new_pos[1] < 0 or new_pos[1] >= len(grid)
            if out_of_bounds or grid[new_pos[1]][new_pos[0]] == ' ':
                if direction[0]:
                    new_pos[0] = start_row(new_pos[1], func=facing_direction[direction])
                else:
                    new_pos[1] = start_col(new_pos[0], func=facing_direction[direction])
            if grid[new_pos[1]][new_pos[0]] == '#':
                print(f'hit wall at {new_pos}')
                break
            pos = tuple(new_pos)


facing = {
    (1, 0): 0,
    (0, 1): 3,
    (-1, 0): 2,
    (0, -1): 1
}

pos = list(pos)
pos[0] += 1
pos[1] += 1
ans = (1000 * pos[1]) + (4 * pos[0]) + facing[direction]
print_green(f'{ans=}, {pos=}, {direction=}, {facing[direction]}')


# # https://adventofcode.com/2022

# from helpers import * 

# import pathlib

# filepath = pathlib.Path(__file__)

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# facing_arrow = {
#     (1, 0): '>',
#     (0, 1): '^',
#     (-1, 0): '<',
#     (0, -1): 'v',
# }


# grid = []
# path = []
# max_length = 0
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip('\n')
#         if line.strip() == '':
#             continue
#         if line[0] not in ['.', '#', ' ']:
#             for index1, segment in enumerate(line.split('L')):
#                 for index2, part in enumerate(segment.split('R')):
#                     path.append(int(part))
#                     if index2 != len(segment.split('R')) - 1:
#                         path.append('R')
#                 if index1 != len(line.split('L')) - 1:
#                     path.append('L')
#         else:
#             to_add = list(line)
#             if len(line) < max_length:
#                 to_add += [' '] * (max_length - len(line))
#             grid.append(to_add)
#             max_length = max(max_length, len(line))

# for line in grid:
#     print(''.join(line))
# print_cyan('path', path)


# def start_row(row, func):
#     for index, ele in func(list(enumerate(grid[row]))):
#         if ele in ['#', '.']:
#             return index
#     # return min(grid[row].index('#'), grid[row].index('.'))

# def start_col(col, func):
#     for index, row in func(list(enumerate(grid))):
#         print(row, len(row), col)
#         if row[col] in ['#', '.']:
#             return index


# def print_board():
#     for index, line in enumerate(grid):
#         print_line = line.copy()
#         if index == pos[1]:
#             print_line[pos[0]] = facing_arrow[direction]
#         print(''.join(print_line))

# pos = (start_row(0, lambda x: x), 0)
# direction = (1, 0)

# facing_direction = {
#     (1, 0): lambda x: x,
#     (0, 1): reversed,
#     (-1, 0): reversed,
#     (0, -1): lambda x: x
# }

# print_red('===STARTING===')
# for step in path:
#     # print_board()
#     # input(f'enter to continue, going to perform {step}')
#     if step == 'L':
#         direction = (-direction[1], direction[0])
#     elif step == 'R':
#         direction = (direction[1], -direction[0])
#     else:
#         for i in range(step):
#             new_pos = [pos[0] + direction[0], pos[1] - direction[1]]
#             print(f'{i=}, {new_pos=}, {direction=}')

#             out_of_bounds = new_pos[0] < 0 or new_pos[0] >= len(grid[0]) or new_pos[1] < 0 or new_pos[1] >= len(grid)
#             if out_of_bounds or grid[new_pos[1]][new_pos[0]] == ' ':
#                 if direction[0]:
#                     new_pos[0] = start_row(new_pos[1], func=facing_direction[direction])
#                 else:
#                     new_pos[1] = start_col(new_pos[0], func=facing_direction[direction])
#             if grid[new_pos[1]][new_pos[0]] == '#':
#                 print(f'hit wall at {new_pos}')
#                 break
#             pos = tuple(new_pos)


# facing = {
#     (1, 0): 0,
#     (0, 1): 3,
#     (-1, 0): 2,
#     (0, -1): 1
# }

# pos = list(pos)
# pos[0] += 1
# pos[1] += 1
# ans = (1000 * pos[1]) + (4 * pos[0]) + facing[direction]
# print_green(f'{ans=}, {pos=}, {direction=}, {facing[direction]}')