import pathlib

filepath = pathlib.Path(__file__)

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


total = 0
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        section1, section2 = line.split(',')

        s1, e1 = map(int, section1.split('-'))
        s2, e2 = map(int, section2.split('-'))

        if s2 < s1:
            s1, e1, s2, e2 = s2, e2, s1, e1

        if s2 <= e1:
            total += 1

print(total)        
