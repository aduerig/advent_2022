# https://adventofcode.com/2022

from helpers import * 

from collections import deque
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

for lol, ok in graph.items():
    print(lol, ok)


all_distances = {}
def bfs_all(orig):
    queue = [(orig, 0, set())]
    while queue:
        the_tuple = queue.pop(0)
        node, depth, the_set = the_tuple
        
        if node in the_set:
            continue

        if depth > 0 and node not in all_distances[orig]:
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


queue = deque([('AA', 'AA', 0, 0, 0, 26, 26, set())])
# path_finished = []
max_pres = 0
while queue:
    print(len(queue))
    the_tuple = queue.popleft()
    valve_1, valve_2, total_pressure, rate_1, rate_2, minutes_left_1, minutes_left_2, visited = the_tuple

    # print(valve, path, minutes_left, visited, len(queue))
    if valve_1 in visited or valve_2 in visited:
        continue
    new_visited = visited.union(set([valve_1, valve_2]))
    if minutes_left_1 <= 0 and minutes_left_2 <= 0:
        continue
    # if path:
    #     path_finished.append(list(path))
    
    max_pres = max(max_pres, total_pressure + (rate_1 * max(minutes_left_1, 0)) + (rate_2 * max(minutes_left_2, 0)))

    for index1, next_valve_1 in enumerate(distances_without_zero[valve_1]):
        for index2, next_valve_2 in enumerate(distances_without_zero[valve_2]):
            # if index2 < index1:
            #     continue
            if index1 == index2:
                continue
            
            cost_1 = distances_without_zero[valve_1][next_valve_1]
            cost_2 = distances_without_zero[valve_2][next_valve_2]
            blah = total_pressure

            temp_rate_1 = rate_1
            if cost_1 + 1 <= minutes_left_1:
                blah += ((cost_1 + 1) * temp_rate_1)
                temp_rate_1 += flow_rates[next_valve_1]

            temp_rate_2 = rate_2
            if cost_2 + 1 <= minutes_left_2:
                blah += ((cost_2 + 1) * temp_rate_2)
                temp_rate_2 += flow_rates[next_valve_2]


            print(f'{minutes_left_1=}, {cost_1=}, {minutes_left_2=}, {cost_2=}, {max_pres=}, {temp_rate_1=}, {temp_rate_2=}, {blah=}')
            if cost_1 + 1 <= minutes_left_1 or cost_2 + 1 <= minutes_left_2:
                queue.append((next_valve_1, next_valve_2, blah, temp_rate_1, temp_rate_2, minutes_left_1 - (cost_1 + 1), minutes_left_2 - (cost_2 + 1), new_visited))
            
            # if next_valve_2 == 'DD' and next_valve_1 == 'JJ':
            #     exit()

print_green(f'{max_pres=}')



# # https://adventofcode.com/2022

# from helpers import * 

# import re
# import pathlib

# filepath = pathlib.Path(__file__)

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')



# graph = {}
# flow_rates = {}
# zero_fellas = set()

# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
    
#         pattern = re.compile(r"Valve (.*) has")
#         match = pattern.findall(line)
#         name = match[0]

#         pattern = re.compile(r"=(\d+);")
#         match = pattern.findall(line)
#         flow_rate = int(match[0])

#         pattern = re.compile(r"valves? (.*)$")
#         the_match = pattern.findall(line)
#         children = map(lambda x: x.strip(), the_match[0].strip().split(','))

#         flow_rates[name] = flow_rate
#         if flow_rate == 0:
#             zero_fellas.add(name)

#         if name not in graph:
#             graph[name] = set()
#         for i in children:
#             graph[name].add(i)

#             if i not in graph:
#                 graph[i] = set()
#             graph[i].add(name)

# for lol, ok in graph.items():
#     print(lol, ok)


# all_distances = {}
# def bfs_all(orig):
#     queue = [(orig, 0, set())]
#     while queue:
#         the_tuple = queue.pop(0)
#         node, depth, the_set = the_tuple
        
#         if node in the_set:
#             continue

#         if depth > 0 and node not in all_distances[orig]:
#             all_distances[orig][node] = depth
        
#         new_set = the_set.union(set([node]))

#         for next_valve in graph[node]:
#             queue.append((next_valve, depth + 1, new_set))
        


# for valve in graph:
#     all_distances[valve] = {}
#     bfs_all(valve)


# distances_without_zero = {}
# for node, distances in all_distances.items():
#     if node in zero_fellas and node != 'AA':
#         continue
#     distances_without_zero[node] = {}
#     for other_node, real_dist in distances.items():
#         if other_node not in zero_fellas:
#             distances_without_zero[node][other_node] = real_dist

# for node, distances in distances_without_zero.items():
#     print(green(node), distances)
# # exit()


# queue = [('AA', [], 0, 0, 30, set())]
# path_finished = []
# max_pres = 0
# while queue:
#     the_tuple = queue.pop(0)
#     valve, path, total_pressure, rate, minutes_left, visited = the_tuple

#     # print(valve, path, minutes_left, visited, len(queue))
#     if valve in visited:
#         continue
#     new_visited = visited.union(set([valve]))
#     if minutes_left <= 0:
#         continue
#     if path:
#         path_finished.append(list(path))
    
#     max_pres = max(max_pres, total_pressure + (rate * minutes_left))

#     for next_valve in distances_without_zero[valve]:
#         cost = distances_without_zero[valve][next_valve]
#         if cost + 1 <= minutes_left:
#             copy = list(path)
#             copy.append((next_valve, flow_rates[next_valve], minutes_left - (cost + 1)))
#             blah = total_pressure + ((cost + 1) * rate)
#             # print(f'from {valve} to {next_valve} with {total_pressure=}, {cost=}, {rate=}, {blah=}')
#             next_rate = rate + flow_rates[next_valve]
#             # print(red(copy), next_rate)
#             # if next_valve == 'DD':
#             #     exit()

#             # if len(path) == 2 and path[0][0] == 'DD' and path[1][0] == 'BB' and next_valve == 'JJ':
#             #     exit()
#             queue.append((next_valve, copy, blah, next_rate, minutes_left - (cost + 1), new_visited))

# print_green(f'{max_pres=}')