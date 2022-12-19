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


queue = [('AA', 0, 30, (), ())]

highest_value = 0
seen = set()
while queue:
    the_tuple = queue.pop(0)
    valve, value, minutes_left, opened, visited = the_tuple
    highest_value = max(highest_value, value)
    print(valve, minutes_left, visited)
    if minutes_left <= 0:
        continue
    if the_tuple in seen:
        continue
    seen.add(the_tuple)

    
    if valve not in opened:
        new_opened = tuple(sorted(opened + (valve,)))
        queue.append((valve, value + flow_rates[valve], minutes_left - 1, new_opened, visited))

    if valve in graph:
        for next_valve in graph[valve]:
            new_visited = tuple(sorted(visited + (valve,)))
            queue.append((next_valve, value, minutes_left - 1, opened, new_visited))

