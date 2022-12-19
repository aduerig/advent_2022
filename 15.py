# https://adventofcode.com/2022

from helpers import * 

import pathlib
import re

filepath = pathlib.Path(__file__)

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


sensors = []
beacons = []
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

        # if (sensor_x, sensor_y) == (8, 7):
        sensors.append((sensor_x, sensor_y))
        beacons.append((beacon_x, beacon_y))

fast_beacons = {}
for i, beacon in enumerate(beacons):
    x, y = beacon
    fast_beacons[(x, y)] = True

fast_sensors = {}
for i, sensor in enumerate(sensors):
    x, y = sensor
    fast_sensors[(x, y)] = True


def bfs(pos, grid):
    queue = [(pos, 0)]
    found = None
    while queue:
        (x, y), depth = queue.pop(0)
        if (x, y) in fast_beacons:
            print(f'found at {depth}')
            found = depth
        if y in grid and x in grid[y]:
            continue
        if y not in grid:
            grid[y] = {}
        if x not in grid[y]:
            grid[y][x] = depth
        if found is not None and found != depth:
            return
        for n_x, n_y in [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]:
            queue.append(((n_x, n_y), depth+1))

def print_searched(grid):
    lowest_y = min(grid.keys())
    highest_y = max(grid.keys())
    lowest_x = float('inf')
    highest_x = float('-inf')
    for y in grid.keys():
        lowest_x = min(lowest_x, min(grid[y].keys()))
        highest_x = max(highest_x, max(grid[y].keys()))

    for y in range(lowest_y, highest_y+1):
        to_print = [f'{cyan(y):<16}: ']
        for x in range(lowest_y, highest_y+1):
            if (x, y) in fast_beacons:
                to_print.append(green('B'))
            elif (x, y) in fast_sensors:
                to_print.append(blue('S'))
            elif y in grid and x in grid[y]:
                # to_print.append(str(grid[y][x]))
                to_print.append('#')
            else:
                to_print.append('.')
                                
        print(''.join(to_print))

grid = {}
for sensor in sensors:
    print('sensor done')
    x, y = sensor
    bfs((x, y), grid)



# print_searched(grid)

total_not_possible = len(grid[10])

print_green(total_not_possible)


