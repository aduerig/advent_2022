import pathlib

filepath = pathlib.Path(__file__)

data_file = filepath.parent.joinpath(filepath.stem + '.dat')



mine_to_victory = {
    'X': -1,
    'Y': 0,
    'Z': 1,
}


scores_of_shape = {
    'A': 1,
    'B': 2,
    'C': 3,
}

def points(a, b):
    if a == b:
        return 3
    elif a == 'A' and b == 'B':
        return 0
    elif a == 'A' and b == 'C':
        return 6
    elif a == 'B' and b == 'A':
        return 6
    elif a == 'B' and b == 'C':
        return 0
    elif a == 'C' and b == 'A':
        return 0
    elif a == 'C' and b == 'B':
        return 6


def to_throw(result, b):
    if result == 0:
        return b
    if result == -1:
        if b == 'A':
            return 'C'
        if b == 'B':
            return 'A'
        if b == 'C':
            return 'B'
    if result == 1:
        if b == 'A':
            return 'B'
        if b == 'B':
            return 'C'
        if b == 'C':
            return 'A'


total = 0
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            them, needed_coded = line.split()
            needed_result = mine_to_victory[needed_coded]
            you = to_throw(needed_result, them)
            total += (points(you, them) + scores_of_shape[you])

print(total)
