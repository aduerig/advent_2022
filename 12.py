# https://adventofcode.com/2022

from helpers import * 

import pathlib

filepath = pathlib.Path(__file__)

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


queue = []
grid = []
with open(data_file) as f:
    for y, line in enumerate(f.readlines()):
        line = line.strip()

        row = []
        for x, char in enumerate(line):
            if char == 'S':
                queue.append(((x, y), 0))
                row.append(0)
            elif char == 'E':
                end = (x, y)
                row.append(25)
            elif char == 'a':
                queue.append(((x, y), 0))
                row.append(0)
            else:
                row.append(ord(char) - 97)
        grid.append(row)


def print_grid(pos):
    for y, row in enumerate(grid):
        to_print = []        
        for x, val in enumerate(row):
            if (x, y) == pos:
                to_print.append('😚')
            elif (x, y) == end:
                to_print.append(red('E'))
            elif (x, y) == start:
                to_print.append(blue('S'))
            else:
                to_print.append(chr(val + 97))
        print(''.join(to_print))


seen = set()
while queue:
    (x, y), steps = queue.pop(0)
    if (x, y) in seen:
        continue
    # if steps > 3:
    #     continue
    # print_cyan(f'\n=== Step: {steps} ===')
    # print_grid((x, y))
    seen.add((x, y))
    if (x, y) == end:
        print_green(f'steps taken to reach {end}: {steps}')
        break

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
            if grid[ny][nx] <= grid[y][x] + 1:
                queue.append(((nx, ny), steps + 1))

