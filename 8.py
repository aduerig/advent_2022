# https://adventofcode.com/2022

from helpers import * 

import pathlib

filepath = pathlib.Path(__file__)

data_file = filepath.parent.joinpath(filepath.stem + '.dat')



grid = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        row = []
        for num in line:
            row.append(int(num))
        grid.append(row)


from copy import deepcopy
sight = deepcopy(grid)
for y in range(len(sight)):
    for x in range(len(sight[0])):
        sight[y][x] = 1


def flow(grid, pos, starting, direction):
    if pos[1] >= len(grid) or pos[1] < 0 or pos[0] >= len(grid[0]) or pos[0] < 0:
        return 0
    
    if grid[pos[1]][pos[0]] >= starting:
        return 1

    new_pos = (pos[0] + direction[0], pos[1] + direction[1])
    return 1 + flow(grid, new_pos, starting, direction)


for y in range(len(sight)):
    for x in range(len(sight[0])):
        sight[y][x] *= flow(grid, (x + 1, y), grid[y][x], (1, 0))
        sight[y][x] *= flow(grid, (x - 1, y), grid[y][x], (-1, 0))
        sight[y][x] *= flow(grid, (x, y + 1), grid[y][x], (0, 1))
        sight[y][x] *= flow(grid, (x, y - 1), grid[y][x], (0, -1))


total = 0

for row in sight:
    print(' '.join(map(str, row)))

max_sight = 0
for row in sight:
    max_sight = max(max_sight, max(row))
print_green('max sight:', max_sight)
















# # https://adventofcode.com/2022

# from helpers import * 

# import pathlib

# filepath = pathlib.Path(__file__)

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')



# grid = []
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         row = []
#         for num in line:
#             row.append(int(num))
#         grid.append(row)


# from copy import deepcopy
# seen = deepcopy(grid)
# for y in range(len(seen)):
#     for x in range(len(seen[0])):
#         seen[y][x] = 1


# def flow(grid, pos, largest, direction):
#     if pos[1] >= len(grid) or pos[1] < 0 or pos[0] >= len(grid[0]) or pos[0] < 0:
#         return

#     if grid[pos[1]][pos[0]] <= largest:
#         seen[pos[1]][pos[0]] *= pos[0]

#     largest = max(largest, grid[pos[1]][pos[0]])
    
#     new_pos = (pos[0] + direction[0], pos[1] + direction[1])
#     flow(grid, new_pos, largest, direction)


# for y in range(len(grid)):
#     flow(grid, (0, y), -1, (1, 0))

# for y in range(len(grid)):
#     flow(grid, (len(grid[0]) - 1, y), -1, (-1, 0))

# for x in range(len(grid[0])):
#     flow(grid, (x, 0), -1, (0, 1))

# for x in range(len(grid[0])):
#     flow(grid, (x, len(grid) - 1), -1, (0, -1))


# total = 0


# for y in range(len(seen)):
#     visible_row = []
#     for x in range(len(seen[0])):
#         if seen[y][x] == 4:
#             visible_row.append(green(str(grid[y][x])))
#         else:
#             visible_row.append(str(grid[y][x]))
#     print(' '.join(visible_row))

# for row in seen:
#     total += len(list(filter(lambda x: x == 4, row)))

# perimeter = len(seen) * 2 + (len(seen[0]) * 2 - 4)
# print_cyan('perimeter:', perimeter)

# area = len(seen) * len(seen[0])
# total_visible = area - total

# print_green('invisible:', total)
# print_green('visible:', total_visible)