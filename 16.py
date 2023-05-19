# https://adventofcode.com/2022

from helpers import * 

import re
import pathlib

filepath = pathlib.Path(__file__)

data_file = filepath.parent.joinpath(filepath.stem + '.dat')



graph = {}
flow_rates = {}
zero_fellas = set()

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
        if flow_rate == 0:
            zero_fellas.add(name)

        if name not in graph:
            graph[name] = set()
        for i in children:
            graph[name].add(i)

            if i not in graph:
                graph[i] = set()
            graph[i].add(name)


all_distances = {}
def bfs_all(orig):
    queue = [(orig, 0, set())]
    while queue:
        the_tuple = queue.pop(0)
        node, depth, the_set = the_tuple
        
        if node in the_set:
            continue

        if depth > 0:
            all_distances[orig][node] = depth
        
        new_set = the_set.union(set([node]))

        for next_valve in graph[node]:
            queue.append((next_valve, depth + 1, new_set))
        


for valve in graph:
    all_distances[valve] = {}
    bfs_all(valve)


distances_without_zero = {}
for node, distances in all_distances.items():
    if node in zero_fellas and node != 'AA':
        continue
    distances_without_zero[node] = {}
    for other_node, real_dist in distances.items():
        if other_node not in zero_fellas:
            distances_without_zero[node][other_node] = real_dist

for node, distances in distances_without_zero.items():
    print(green(node), distances)
# exit()


queue = [('AA', [], 0, 0, 30, set())]
path_finished = []
max_pres = 0
while queue:
    the_tuple = queue.pop(0)
    valve, path, total_pressure, rate, minutes_left, visited = the_tuple

    # print(valve, path, minutes_left, visited, len(queue))
    if valve in visited:
        continue
    new_visited = visited.union(set([valve]))
    if minutes_left <= 0:
        continue
    if path:
        path_finished.append(list(path))
    
    max_pres = max(max_pres, total_pressure + (rate * minutes_left))

    for next_valve in distances_without_zero[valve]:
        cost = distances_without_zero[valve][next_valve]
        if 1 + cost <= minutes_left:
            copy = list(path)
            copy.append((next_valve, flow_rates[next_valve], minutes_left - (cost)))
            blah = total_pressure + (cost * rate)
            print(f'from {valve} to {next_valve} with {total_pressure=}, {cost=}, {rate=}, {blah=}')
            next_rate = rate + flow_rates[next_valve]
            print(red(copy), next_rate)
            queue.append((next_valve, copy, blah, next_rate, minutes_left - (1 + cost), new_visited))

print_green(f'Maybe: {max_pres}')
exit()

print_green(len(path_finished))
print_green(path_finished)
print_green(len(path_finished))

increment = 0
max_money = (0, -1, 0)
for path in path_finished:
    money = 0
    for i in range(1, 31):
        for added in path:
            valve, flow_rate, minute_added = added

            if minute_added < i:
                money += flow_rate
    max_money = max(max_money, (money, increment, path))
    increment += 1

print_green(max_money)


for node, distances in distances_without_zero.items():
    print(blue(node), distances)