# https://adventofcode.com/2022

from helpers import * 

import pathlib

filepath = pathlib.Path(__file__)

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


grid = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            grid.append(list(line))

wanted_size = 5000
larger_grid = []
for _ in range(1000):
    larger_grid.append(['.'] * wanted_size)

for row in grid:
    larger_grid.append((['.'] * ((wanted_size // 2) - len(row))) + row + (['.'] * ((wanted_size // 2) - len(row))))

for _ in range(1000):
    larger_grid.append(['.'] * wanted_size)

grid = larger_grid



def smallest_grid_with_elves():
    smallest_x = float('inf')
    smallest_y = None
    largest_x = -float('inf')
    largest_y = 0
    
    for y, row in enumerate(grid):
        x_index = ''.join(row).find('#')
        if x_index != -1:
            if smallest_y is None:
                smallest_y = y
            smallest_x = min(smallest_x, x_index)
            largest_x = max(largest_x, ''.join(row).rfind('#'))
        for x, col in enumerate(row):
            if col == '#':
                largest_y = y
    return (smallest_x, smallest_y, largest_x, largest_y)

def print_grid(grid):
    for row in grid:
        print(''.join(row))


def all_elf_locations():
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == '#':
                yield (x, y)

def all_eight(pos):
    return [
        (pos[0], pos[1]-1),
        (pos[0], pos[1]+1),
        (pos[0]-1, pos[1]),
        (pos[0]+1, pos[1]),
        (pos[0]-1, pos[1]-1),
        (pos[0]+1, pos[1]-1),
        (pos[0]-1, pos[1]+1),
        (pos[0]+1, pos[1]+1),
    ]

def is_elf(pos):
    return grid[pos[1]][pos[0]] == '#'


curr_decision = 0
forward = [
    ((0, -1), (-1, -1), (1, -1)),
    ((0, 1), (-1, 1), (1, 1)),
    ((-1, 0), (-1, -1), (-1, 1)),
    ((1, 0), (1, -1), (1, 1)),
]
from copy import deepcopy
def step():
    global curr_decision, grid

    new_grid = deepcopy(grid)
    going_to_go = {}
    pending_moves = {}
    for x, y in all_elf_locations():
        elf = False
        for pos in all_eight((x, y)):
            if is_elf(pos):
                elf = True
                break
        if not elf:
            continue
        print('looking at elf', x, y)
            
        next_pos = None
        for decision in range(4):
            dir_to_go, dir_banned_1, dir_banned_2 = forward[(decision + curr_decision) % len(forward)]
            to_go = (x + dir_to_go[0], y + dir_to_go[1])
            banned_1 = (x + dir_banned_1[0], y + dir_banned_1[1])
            banned_2 = (x + dir_banned_2[0], y + dir_banned_2[1])
            if not is_elf(to_go) and not is_elf(banned_1) and not is_elf(banned_2):
                print('found a move', to_go, banned_1, banned_2)
                next_pos = to_go
                break
        
        # if next_pos is None:
        #     print_grid()
        #     print_red('okay weird, cleared to go is NONE')

        if next_pos in going_to_go:
            # print(f'{going_to_go[next_pos]=}')
            # print(f'{pending_moves=}')
            if going_to_go[next_pos] in pending_moves:
                del pending_moves[going_to_go[next_pos]]
        else:
            going_to_go[next_pos] = (x, y)
            pending_moves[(x, y)] = next_pos
            print(f'{(x, y)=} {next_pos=}')

    for (x, y), _ in pending_moves.items():
        new_grid[y][x] = '.'

    for _, (x, y) in pending_moves.items():
        new_grid[y][x] = '#'

    grid = new_grid
    curr_decision = (curr_decision + 1) % len(forward)


print('STARTING GRID')
# print_grid(grid)
for i in range(10):
    step()
    print('AFTER STEP', i+1, 'GRID')
    # print_grid(grid)
    # exit()



x, y, x2, y2 = smallest_grid_with_elves()
print('SMALLEST GRID WITH ELVES', x, y, x2, y2)

blank_spaces = 0
for a in range(y, y2+1):
    row = grid[a]
    for b in range(x, x2+1):
        if row[b] == '.':
            blank_spaces += 1

print_green(blank_spaces)