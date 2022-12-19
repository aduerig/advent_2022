import pathlib

filepath = pathlib.Path(__file__)

data_file = filepath.parent.joinpath(filepath.stem + '.dat')

total = 0

letters = []
seen = set()
elf_trios = []

building = []
with open(data_file) as f:
    for index, line in enumerate(f.readlines()):
        if index % 3 == 0 and index != 0:
            elf_trios.append(building)
            building = []
        line = line.strip()
        building.append(line)
elf_trios.append(building)

for sack1, sack2, sack3 in elf_trios:
    print(sack1)
    ok = set(sack1).intersection(set(sack2)).intersection(set(sack3))
    for shared in ok:
        break
    lol = ord(shared) - 64

    if shared.islower():
        lol -= 6
    
    # if shared == 'b':
    #     print(lol)
    #     exit()
    if lol <= 27:
        lol += 26
    else:
        lol -= 26
    if shared not in seen:
        letters.append((shared, lol))
        seen.add(shared)
    total += lol

letters.sort()
for l in letters:
    print(l)


print(total)