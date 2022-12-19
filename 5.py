from helpers import *

import pathlib
import re


filepath = pathlib.Path(__file__)
data_file = filepath.parent.joinpath(filepath.stem + '.dat')





# height = 3
# width = 3

height = 8
width = 9

all_stacks = []
for i in range(width):
    all_stacks.append([])
lines_of_crates = []

def print_stacks():
    for h in reversed(range(height)):
        bldg = []
        for w in range(width):
            if h < len(all_stacks[w]):
                bldg.append(all_stacks[w][h])
            else:
                bldg.append(' ')
        print(' '.join(bldg))

with open(data_file) as f:
    for index in range(height):
        line = f.readline()
        line = line.strip('\n')

        crates = []
        for i in range(width):
            segment = line[(i*4):(i*4) + 3]
            if segment != '   ':
                crates.append(segment.replace('[', '').replace(']', ''))
            else:
                crates.append(None)

        lines_of_crates.append(crates)

    for line_of_crates in reversed(lines_of_crates):
        for index, crate in enumerate(line_of_crates):
            if crate:
                all_stacks[index].append(crate)

    print_blue('start')
    print_stacks()        


    f.readline()
    f.readline()
    for step, line in enumerate(f.readlines()):
        line = line.strip()

        print(line)
        # regex
        pattern = re.compile(r"move (\d+) from")
        match = pattern.search(line)
        amt = int(match.group(1))

        pattern = re.compile(r"from (\d+) to")
        match = pattern.search(line)
        from_stack = int(match.group(1)) - 1

        pattern = re.compile(r"to (\d+)")
        match = pattern.search(line)
        to_stack = int(match.group(1)) - 1 


        if to_stack == from_stack:
            print('huh')
            exit()
        all_stacks[to_stack] += all_stacks[from_stack][-amt:]
        all_stacks[from_stack] = all_stacks[from_stack][:-amt]
        

        print_blue(f'step {step}')
        print_stacks()        



ok = ''
for i in all_stacks:
    ok += i.pop()
print_cyan(f'finished:', ok)
