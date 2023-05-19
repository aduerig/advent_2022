# https://adventofcode.com/2022

from helpers import * 

import pathlib
import re

filepath = pathlib.Path(__file__)

data_file = filepath.parent.joinpath(filepath.stem + '.dat')





sensors = []
beacons = []
sensor_and_beacons = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if not line:
            continue
        print(line)


        pattern = re.compile(r"x=(-?\d+)")
        match = pattern.findall(line)
        sensor_x, beacon_x = int(match[0]), int(match[1])

        pattern = re.compile(r"y=(-?\d+)")
        match = pattern.findall(line)
        sensor_y, beacon_y = int(match[0]), int(match[1])

                
        sensor_point = (sensor_x, sensor_y)
        sensors.append(sensor_point)

        beacon_point = (beacon_x, beacon_y)
        beacons.append(beacon_point)

        sensor_and_beacons.append((sensor_point, beacon_point))


def man_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def is_in_range(p):
    # max_thing = 20
    max_thing = 4000000
    
    if p[0] < 0:
        return False
    if p[0] > max_thing:
        return False
    if p[1] < 0:
        return False
    if p[1] > max_thing:
        return False
    return True


beacon_sets = []
whole_set = set()
for index, (sensor, closest_beacon) in enumerate(sensor_and_beacons):
    x, y = sensor
    new_set = set()
    dist = man_dist(sensor, closest_beacon)
    to_process = [
        (x + (dist + 1), y, (-1, 1)),
        (x + (dist + 1), y, (-1, -1)),
        (x - (dist + 1), y, (1, 1)),
        (x - (dist + 1), y, (1, -1)),
    ]
    found_point = False
    for x, y, (x_dir, y_dir) in to_process:
        for i in range(dist + 2):
            if is_in_range((x, y)):
                whole_set.add((x, y))
                new_set.add((x, y))
                if (x, y) == (14, 11):
                    found_point = True
            x += x_dir
            y += y_dir
    # found_string = ''
    # if not found_point:
    #     found_string = red(' - NOT FOUND ')
    # lol = sorted(list(new_set))
    # print(f'{sensor}{found_string}: {green(lol)}')
    beacon_sets.append(new_set)
    print(f'finished {index}')


# mega = set()
# for beacon_set in beacon_sets:
#     mega = mega.intersection(beacon_set)
# print(list(mega))
# print(len(mega))
print_blue(f'{len(whole_set)=}')



def could_be(potential_point):
    for index, (sensor, closest_beacon) in enumerate(sensor_and_beacons):
        if man_dist(sensor, closest_beacon) >= man_dist(sensor, potential_point):
            return False
    return True


print('starting could_be')
nums = []
for index, potential_point in enumerate(whole_set):
    if index % 100000 == 0:
        print_yellow(f'finished {index}')
    if could_be(potential_point):
        nums.append(potential_point)


print_green(len(nums))
print(nums)
print_green(len(nums))

# fast_beacons = {}
# for i, beacon in enumerate(beacons):
#     x, y = beacon
#     fast_beacons[(x, y)] = True

# fast_sensors = {}
# for i, sensor in enumerate(sensors):
#     x, y = sensor
#     fast_sensors[(x, y)] = True


# def get_abs_point(relative_to, relative_point):
#     abs_point = list(relative_point)
#     abs_point[0] += relative_to[0]
#     abs_point[1] += relative_to[1]
#     return tuple(abs_point)

# rel_beacon_point = (beacon_x, beacon_y)
# beacon_point = get_abs_point(sensor_point, rel_beacon_point)



# def print_searched(grid):
#     lowest_y = min(grid.keys())
#     highest_y = max(grid.keys())
#     lowest_x = float('inf')
#     highest_x = float('-inf')
#     for y in grid.keys():
#         lowest_x = min(lowest_x, min(grid[y].keys()))
#         highest_x = max(highest_x, max(grid[y].keys()))

#     for y in range(lowest_y, highest_y+1):
#         to_print = [f'{cyan(y):<16}: ']
#         for x in range(lowest_y, highest_y+1):
#             if (x, y) in fast_beacons:
#                 to_print.append(green('B'))
#             elif (x, y) in fast_sensors:
#                 to_print.append(blue('S'))
#             elif y in grid and x in grid[y]:
#                 # to_print.append(str(grid[y][x]))
#                 to_print.append('#')
#             else:
#                 to_print.append('.')
                                
#         print(''.join(to_print))




# def bfs(pos, grid):
#     queue = [(pos, 0)]
#     found = None
#     while queue:
#         (x, y), depth = queue.pop(0)
#         if (x, y) in fast_beacons:
#             print(f'found at {depth}')
#             found = depth
#         if y in grid and x in grid[y]:
#             continue
#         if y not in grid:
#             grid[y] = {}
#         if x not in grid[y]:
#             grid[y][x] = depth
#         if found is not None and found != depth:
#             return
#         for n_x, n_y in [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]:
#             queue.append(((n_x, n_y), depth+1))






# # https://adventofcode.com/2022

# from helpers import * 

# import pathlib
# import re

# filepath = pathlib.Path(__file__)

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')




# beacon_set_on_row = set()
# relavent_row = 2000000


# sensors = []
# beacons = []
# sensor_and_beacons = []
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         if not line:
#             continue
#         print(line)


#         pattern = re.compile(r"x=(-?\d+)")
#         match = pattern.findall(line)
#         sensor_x, beacon_x = int(match[0]), int(match[1])

#         pattern = re.compile(r"y=(-?\d+)")
#         match = pattern.findall(line)
#         sensor_y, beacon_y = int(match[0]), int(match[1])

                
#         sensor_point = (sensor_x, sensor_y)
#         sensors.append(sensor_point)

#         beacon_point = (beacon_x, beacon_y)
#         beacons.append(beacon_point)

#         if beacon_y == relavent_row:
#             beacon_set_on_row.add(beacon_x)

#         sensor_and_beacons.append((sensor_point, beacon_point))


# def man_dist(p1, p2):
#     return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])



# counting_set = set()
# for index, (sensor, closest_beacon) in enumerate(sensor_and_beacons):
#     dist = man_dist(sensor, closest_beacon)
#     cost = abs(sensor[1] - relavent_row)
#     left = (dist - cost)
#     print(f'{sensor=} {closest_beacon=} {dist=} {left=}')
#     before = len(counting_set)
    
#     if left >= 0:
#         counting_set.add(sensor[0])
#     for iter in range(left):
#         iter += 1
#         inspected_point_1 = sensor[0] - iter
#         inspected_point_2 = sensor[0] + iter

#         counting_set.add(inspected_point_1)
#         counting_set.add(inspected_point_2)
#     print_yellow(f'{before=} {len(counting_set)=}')




# # print(sorted(list(counting_set)))
# # print(sorted(list(beacon_set_on_row)))


# # 4803046 is too low
# print_green(f'{len(counting_set)=}')
# print_green(f'{len(beacon_set_on_row.symmetric_difference(counting_set))=}')




# # fast_beacons = {}
# # for i, beacon in enumerate(beacons):
# #     x, y = beacon
# #     fast_beacons[(x, y)] = True

# # fast_sensors = {}
# # for i, sensor in enumerate(sensors):
# #     x, y = sensor
# #     fast_sensors[(x, y)] = True


# # def get_abs_point(relative_to, relative_point):
# #     abs_point = list(relative_point)
# #     abs_point[0] += relative_to[0]
# #     abs_point[1] += relative_to[1]
# #     return tuple(abs_point)

# # rel_beacon_point = (beacon_x, beacon_y)
# # beacon_point = get_abs_point(sensor_point, rel_beacon_point)



# # def print_searched(grid):
# #     lowest_y = min(grid.keys())
# #     highest_y = max(grid.keys())
# #     lowest_x = float('inf')
# #     highest_x = float('-inf')
# #     for y in grid.keys():
# #         lowest_x = min(lowest_x, min(grid[y].keys()))
# #         highest_x = max(highest_x, max(grid[y].keys()))

# #     for y in range(lowest_y, highest_y+1):
# #         to_print = [f'{cyan(y):<16}: ']
# #         for x in range(lowest_y, highest_y+1):
# #             if (x, y) in fast_beacons:
# #                 to_print.append(green('B'))
# #             elif (x, y) in fast_sensors:
# #                 to_print.append(blue('S'))
# #             elif y in grid and x in grid[y]:
# #                 # to_print.append(str(grid[y][x]))
# #                 to_print.append('#')
# #             else:
# #                 to_print.append('.')
                                
# #         print(''.join(to_print))




# # def bfs(pos, grid):
# #     queue = [(pos, 0)]
# #     found = None
# #     while queue:
# #         (x, y), depth = queue.pop(0)
# #         if (x, y) in fast_beacons:
# #             print(f'found at {depth}')
# #             found = depth
# #         if y in grid and x in grid[y]:
# #             continue
# #         if y not in grid:
# #             grid[y] = {}
# #         if x not in grid[y]:
# #             grid[y][x] = depth
# #         if found is not None and found != depth:
# #             return
# #         for n_x, n_y in [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]:
# #             queue.append(((n_x, n_y), depth+1))
