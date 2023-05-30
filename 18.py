# https://adventofcode.com/2022

import pathlib
import sys
sys.setrecursionlimit(100000) 

from helpers import * 


filepath = pathlib.Path(__file__)

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


cubes = []
with open(data_file) as f:
    for line in f.readlines():
        dims = tuple(map(int, line.strip().split(',')))
        cubes.append(dims)


max_dims = [-float('inf'), -float('inf'), -float('inf')]
min_dims = [float('inf'), float('inf'), float('inf')]
for i in cubes:
    for dim in (0, 1, 2):
        if i[dim] > max_dims[dim]:
            max_dims[dim] = i[dim]
        if i[dim] < min_dims[dim]:
            min_dims[dim] = i[dim]

print(f'{max_dims=}, {min_dims=}')


cubes_set = set(cubes)
visited_air = set()
global total_moves_stopped
total_moves_stopped = 0
def dfs(position):
    global total_moves_stopped
    x, y, z = position
    if x < -10 or x > 30 or y < -10 or y > 30 or z < -10 or z > 30:
        return

    if position in visited_air:
        return

    visited_air.add(position)

    for direction in (
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1),
        (-1, 0, 0),
        (0, -1, 0),
        (0, 0, -1),
    ):
        new_position = tuple(map(sum, zip(position, direction)))
        if new_position in cubes_set:
            total_moves_stopped += 1
            continue
        dfs(new_position)

dfs((-9, -9, -9))
print_green(total_moves_stopped)




# # https://adventofcode.com/2022

# from helpers import * 

# import pathlib

# filepath = pathlib.Path(__file__)

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# cubes = []
# with open(data_file) as f:
#     for line in f.readlines():
#         dims = tuple(map(int, line.strip().split(',')))
#         cubes.append(dims)


# def sub_sides(same_1, same_2, diff_dim):
#     global total_sides
#     for index_1, cube_1 in enumerate(cubes):
#         for index_2, cube_2 in enumerate(cubes):
#             if index_2 <= index_1:
#                 continue

#             if cube_1[same_1] == cube_2[same_1] and cube_1[same_2] == cube_2[same_2] and abs(cube_1[diff_dim] - cube_2[diff_dim]) == 1:
#                 total_sides -= 2


# global total_sides
# total_sides = len(cubes) * 6
# print_yellow(f'inital total_sides: {total_sides}, {len(cubes)=}')
# for same_1, same_2, diff_dim in (
#     (0, 1, 2),
#     (0, 2, 1),
#     (1, 2, 0),
# ):
#     sub_sides(same_1, same_2, diff_dim)

# print_green(f'{total_sides=}')


