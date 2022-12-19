import pathlib

filepath = pathlib.Path(__file__)

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


index = 0
elves = {}
maxer = -float('inf')
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            if index not in elves:
                elves[index] = 0
            elves[index] += int(line)
        else:
            index += 1

print(sum(list(sorted(elves.values()))[-3:]))