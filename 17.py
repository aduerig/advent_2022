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

def get_counts(chamber):
    saving = {}
    for i in chamber:
        if any([x == '#' for x in i]):
            save = ''.join(i)
            if ''.join(i) not in saving:
                saving[save] = 0
            saving[save] += 1
    return saving



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


actual_heights = []
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
            actual_heights.append(highest_rock + 1)
            # print('done with rock')
            return

print_board()
up_to = 100001
for i in range(up_to):
    rock, y_offset = spawn()
    move_until_done(rock, y_offset)
print_green(f'{up_to=}, {highest_rock + 1=}')


last = 0
actual_diffs = []
for index, height in enumerate(actual_heights):
    diff = height - last
    actual_diffs.append((height, diff))
    last = height

# for index, (height, diff) in enumerate(actual_diffs):
#     print(f'{index=}: {diff=}, {height=}')
#     if index > 100:
#         exit()


index = len(actual_diffs) // 2
max_inc = 20000
goal = 1000000000000
to_math = goal - index
inc = 2
while inc < max_inc:
    subset = list(map(lambda x: x[1], actual_diffs[index:index + inc]))
    next_subset = list(map(lambda x: x[1], actual_diffs[index + inc:index + (2 * inc)]))
    next_next_subset = list(map(lambda x: x[1], actual_diffs[index + inc:index + (2 * inc)]))
    print(f'{len(subset)=}, {len(next_subset)=}')

    if tuple(subset) == tuple(next_subset):
        print('found it! 2x', inc)
        if tuple(subset) == tuple(next_next_subset):
            print('found it! 3x', inc)
            incrementing_by = sum(subset)
            just_under = to_math // inc
            remaining = (to_math % inc)
            rest = sum(subset[:remaining])
            answer = actual_diffs[index - 1][0] + (just_under * incrementing_by) + rest
            print(answer)
            break
    inc += 1



# # print(f'{actual_heights[8000]=}, {actual_heights[9000]=}, {actual_heights[10000]=}, {actual_heights[10000] - actual_heights[9000]=}, {actual_heights[9000] - actual_heights[8000]=}')
# print(f'{actual_heights[9999]=}, {actual_heights[8999]=}, {actual_heights[9999] - actual_heights[8999]=}')
# print(f'{actual_heights[8999]=}, {actual_heights[7999]=}, {actual_heights[8999] - actual_heights[7999]=}')



# start = 99999
# incrementing_unit = 10000
# # goal = 1000000000000 - (start + 1)
# goal = 1000000 - (start + 1)
# print(f'{goal=}')
# incrementing_per_unit = (actual_heights[start] - actual_heights[start-incrementing_unit])
# diffy = ((goal / incrementing_unit) * incrementing_per_unit)
# some = (actual_heights[9999] + diffy)
# 285714280.0
# print(some, diffy)
# exit()



# start = 9999
# incrementing_unit = 1000
# goal = 1000000000000
# incrementing_per_unit = (actual_heights[start] - actual_heights[start-incrementing_unit])
# diffy = (((goal - (start + 1)) / incrementing_unit) * incrementing_per_unit)
# some = actual_heights[9999] + diffy
# 285714280.0
# print(some, diffy)
# exit()

# chamber_small = get_counts(chamber)
# print('Final small')

# chamber = []
# curr_rock = 0
# jet_index = 0

# for i in range(10000):
#     rock, y_offset = spawn()
#     move_until_done(rock, y_offset)


# print_green(highest_rock + 1)



# def print_saved(counts):
#     stuff = sorted([(count, thing) for thing, count in counts.items()])
#     for count, thing in stuff:
#         print(thing, count)


# print_blue('SMALL CHAMBER')
# print_saved(chamber_small)
# print_blue('BIG CHAMBER')
# print_saved(get_counts(chamber))



# for dist in range(2, len(chamber)):
#     print(f'testing {dist=}')
#     buildin = []
#     for j in range(dist):
#         buildin.append(''.join(chamber[j]))
#     thingy = ''.join(buildin)

#     curr = dist
#     loopers = 1
#     while True:

#         buildin = []
#         for j in range(dist):
#             if curr + j >= len(chamber):
#                 break
#             buildin.append(''.join(chamber[curr + j]))
#         if curr + j >= len(chamber):
#             break

#         thingy_2 = ''.join(buildin)

#         if thingy == thingy_2:
#             print(f'Success on dist of {i=}, {loopers=}')
#         else:
#             break
#         curr += dist
#         loopers += 1