# https://adventofcode.com/2022

from helpers import * 

import pathlib

filepath = pathlib.Path(__file__)

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


cubes = []
with open(data_file) as f:
    for line in f.readlines():
        dims = tuple(map(int, line.strip().split(',')))
        cubes.append(dims)


def sub_sides(same_1, same_2, diff_dim):
    global total_sides
    for index_1, cube_1 in enumerate(cubes):
        for index_2, cube_2 in enumerate(cubes):
            if index_2 <= index_1:
                continue

            if cube_1[same_1] == cube_2[same_1] and cube_1[same_2] == cube_2[same_2] and abs(cube_1[diff_dim] - cube_2[diff_dim]) == 1:
                total_sides -= 2


global total_sides
total_sides = len(cubes) * 6
print_yellow(f'inital total_sides: {total_sides}, {len(cubes)=}')
for same_1, same_2, diff_dim in (
    (0, 1, 2),
    (0, 2, 1),
    (1, 2, 0),
):
    sub_sides(same_1, same_2, diff_dim)

print_green(f'{total_sides=}')


