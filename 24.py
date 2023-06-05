# https://adventofcode.com/2022

from helpers import * 

import pathlib

filepath = pathlib.Path(__file__)

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


grid = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            list(line)

