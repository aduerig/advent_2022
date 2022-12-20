# https://adventofcode.com/2022

from helpers import * 

import re
import pathlib

filepath = pathlib.Path(__file__)

data_file = filepath.parent.joinpath(filepath.stem + '.dat')



graph = {}
flow_rates = {}
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
    
        pattern = re.compile(r"Valve (.*) has")
        match = pattern.findall(line)
        name = match[0]

        pattern = re.compile(r"=(\d+);")
        match = pattern.findall(line)
        flow_rate = int(match[0])

        pattern = re.compile(r"valves? (.*)$")
        the_match = pattern.findall(line)
        children = map(lambda x: x.strip(), the_match[0].strip().split(','))

        flow_rates[name] = flow_rate

        if name not in graph:
            graph[name] = set()
        for i in children:
            graph[name].add(i)

            if i not in graph:
                graph[i] = set()
            graph[i].add(name)


all_distances = {}
def dfs_distance(orig, valve, depth):
    if valve in all_distances[orig]:
        return

    if orig != valve:
        all_distances[orig][valve] = depth

    for next_valve in graph[valve]:
        dfs_distance(orig, next_valve, depth+1)

for valve in graph:
    all_distances[valve] = {}
    dfs_distance(valve, valve, 0)



queue = [('AA', 0, 0, 30, ())]

highest_value = 0
seen = set()
while queue:
    the_tuple = queue.pop(0)
    valve, flow, value, minutes_left, visited = the_tuple
    highest_value = max(highest_value, value)

    print(valve, minutes_left, visited, len(queue))
    if minutes_left <= 0:
        continue
    if the_tuple in seen:
        continue
    seen.add(the_tuple)

    
    if valve in all_distances:
        for next_valve in all_distances[valve]:
            cost = all_distances[valve][next_valve]
            if 1 + cost <= minutes_left:
                new_visited = tuple(sorted(visited + (next_valve,)))
                queue.append((next_valve, value + flow_rates[next_valve], minutes_left - (1 + cost), new_visited))

print_green(highest_value)