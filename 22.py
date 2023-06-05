# # https://adventofcode.com/2022

from copy import deepcopy
import pathlib

from helpers import * 

filepath = pathlib.Path(__file__)

data_file = filepath.parent.joinpath(filepath.stem + '.dat')

facing_arrow = {
    (1, 0): '>',
    (0, 1): '^',
    (-1, 0): '<',
    (0, -1): 'v',
}

facing_direction = {
    (1, 0): lambda x: x,
    (0, 1): reversed,
    (-1, 0): reversed,
    (0, -1): lambda x: x
}

facing = {
    (1, 0): 0,
    (0, 1): 3,
    (-1, 0): 2,
    (0, -1): 1
}



grid = []
path = []
side_length = 4
whole_line = side_length * 4
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip('\n')
        if line.strip() == '':
            continue
        if len(line) > 30:
            side_length = 50
            whole_line = side_length * 4
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
            if len(line) < whole_line:
                to_add += [' '] * (whole_line - len(line))
            grid.append(to_add)

for line in grid:
    print(''.join(line), len(line))
print_cyan('path', path)




def start_row(row, func):
    for index, ele in func(list(enumerate(grid[row]))):
        if ele in ['#', '.']:
            return index
pos = (start_row(0, lambda x: x), 0)
direction = (1, 0)


# warps = {
#     (12, None, (1, 0)): ((None, 8), (0, -1), 12, 'y', True),
#     (None, 12, (0, -1)): ((None, 7), (0, 1), 0, 'x', True),
# }
warps = {
    # 2->6
    (None, -1, (0, 1), 1): ((0, None), (1, 0), side_length * 3, 'x', False),
    # 6->2
    (-1, None, (-1, 0), 3): ((None, 0), (0, -1), side_length, 'y', False),
    # 6->1
    (None, side_length * 4, (0, -1), 0): ((None, 0), (0, -1), side_length * 2, 'x', False),
    # 1->6
    (None, -1, (0, 1), 2): ((None, (side_length * 4) - 1), (0, 1), 0, 'x', False),
    # 5->2
    (-1, None, (-1, 0), 2): ((side_length, None), (1, 0), 0, 'y', True),
    # 2->5
    (side_length - 1, None, (-1, 0), 0): ((0, None), (1, 0), side_length * 2, 'y', True),
    # 4->6
    (None, side_length * 3, (0, -1), 1): ((side_length - 1, None), (-1, 0), side_length * 3, 'x', False),
    # 6->4
    (side_length, None, (1, 0), 3): ((None, (side_length * 3) - 1), (0, 1), side_length, 'y', False),
    # 4->1
    (side_length * 2, None, (1, 0), 2): (((side_length * 3) - 1, None), (-1, 0), 0, 'y', True),
    # 1->4
    (side_length * 3, None, (1, 0), 0): (((side_length * 2) - 1, None), (-1, 0), side_length * 2, 'y', True),
    # 1->3
    (None, side_length, (0, -1), 2): (((side_length * 2) - 1, None), (-1, 0), side_length, 'x', False),
    # 3->1
    (side_length * 2, None, (1, 0), 1): ((None, (side_length * 1) - 1), (0, 1), side_length * 2, 'y', False),
    # 5->3
    (None, (side_length * 2) - 1, (0, 1), 0): ((side_length * 1, None), (1, 0), side_length, 'x', False),
    # 3->5
    (side_length - 1, None, (-1, 0), 1): ((None, side_length * 2), (0, -1), 0, 'y', False),
}



def get_new_pos(pos, direction):
    try_pos = [pos[0] + direction[0], pos[1] - direction[1]]
    # print(f'{i=}, {try_pos=}, {direction=}')
    og_direction = direction

    performed_warp = False
    out_of_bounds = try_pos[0] < 0 or try_pos[0] >= len(grid[0]) or try_pos[1] < 0 or try_pos[1] >= len(grid)
    if out_of_bounds or grid[try_pos[1]][try_pos[0]] == ' ':
        print(f'{out_of_bounds=}, {try_pos=}')
        for (x, y, req_direction, at_least), (to_warp, new_dir, start, relevent_dir, to_reverse) in warps.items():
            if ((x is None and (try_pos[0] // side_length == at_least)) or try_pos[0] == x) and ((y is None and (try_pos[1] // side_length == at_least)) or try_pos[1] == y) and req_direction == direction:
                print(f'warping! {(x, y, req_direction)}')
                direction = new_dir

                if relevent_dir == 'x':
                    remainder = try_pos[0] % side_length
                    if to_reverse:
                        remainder = (side_length - 1) - remainder
                elif relevent_dir == 'y':
                    remainder = try_pos[1] % side_length
                    if to_reverse:
                        remainder = (side_length - 1) - remainder
                print(f'{remainder=}, {side_length=}')

                if to_warp[0] is None:
                    try_pos[1] = to_warp[1]
                    try_pos[0] = start + remainder
                elif to_warp[1] is None:
                    try_pos[0] = to_warp[0]
                    try_pos[1] = start + remainder
                performed_warp = (x, y, req_direction, at_least)
                break
        if not performed_warp:
            print_red('no warp no go')
            exit()
    print(f'before: {pos}, {direction}, after ATTEMPT: {try_pos=}, {direction}')

    if grid[try_pos[1]][try_pos[0]] == '#':
        direction = og_direction
        print(f'uh oh hit wall, going back to: {pos}, {direction}')
    else:
        pos = tuple(try_pos)
    return pos, direction, performed_warp



def print_board_2(grid):
    new_grid = deepcopy(grid)
    relative_pos = (pos[0] // side_length, pos[1] // side_length)
    for square_y in range(4):
        for square_x in range(3):
            if (square_x, square_y) == relative_pos:
                for row_index in range(square_y * side_length, (square_y + 1) * side_length):
                    new_grid[row_index][square_x * side_length] = f'{bcolors.FAIL}' + new_grid[row_index][square_x * side_length]
                    new_grid[row_index][((square_x + 1) * side_length) - 1] += f'{bcolors.ENDC}'
    print_board(new_grid)

def print_board(grid):
    for index, line in list(enumerate(grid)):
        print_line = line.copy()
        if index == pos[1]:
            print_line[pos[0]] = f'{bcolors.OKGREEN}{facing_arrow[direction]}{bcolors.ENDC}'
        print(''.join(print_line))

print_red('===STARTING===')
for index, step in enumerate(path):
    print_board_2(grid)
    print(f'step {index}, {100 * (index / len(path)):.2f}% done, going to perform {step} steps forward')
    # input(red('enter to continue'))

    # if index == 471:
    #     exit()

    if step == 'L':
        direction = (-direction[1], direction[0])
    elif step == 'R':
        direction = (direction[1], -direction[0])
    else:
        for i in range(step):
            old_pos = pos
            pos, direction, performed_warp = get_new_pos(pos, direction)
            if performed_warp not in [
                False,

                # 2->6
                (None, -1, (0, 1), 1),
                # 6->2
                (-1, None, (-1, 0), 3),


                # 6-1
                (None, 4 * side_length, (0, -1), 0),
                # 1-6
                (None, -1, (0, 1), 2),

                # 4->6
                (None, side_length * 3, (0, -1), 1),
                # 6->4 (wall hit on first, couldnt exactly check)
                (side_length, None, (1, 0), 3),

                # 5->3
                (None, (side_length * 2) - 1, (0, 1), 0),
                # 3->5
                (side_length - 1, None, (-1, 0), 1),

                # 5->2
                (-1, None, (-1, 0), 2),
                # 2->5
                (side_length - 1, None, (-1, 0), 0),

                # 3->1
                (side_length * 2, None, (1, 0), 1),
                # 1->3
                (None, side_length, (0, -1), 2),

                # 1->4
                (side_length * 3, None, (1, 0), 0),
                # 4->1
                (side_length * 2, None, (1, 0), 2),

            ]:                    
                print_board_2(grid)
                print_yellow(f'==== WARPED ==== {performed_warp}')
                input()
            if old_pos == pos:
                break

pos = list(pos)
pos[0] += 1
pos[1] += 1
ans = (1000 * pos[1]) + (4 * pos[0]) + facing[direction]
print_green(f'{ans=}, {pos=}, {direction=}, {facing[direction]}')

# 141010 is too high
# 159103 is too high

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