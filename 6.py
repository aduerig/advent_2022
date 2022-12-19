from helpers import *

import pathlib

filepath = pathlib.Path(__file__)

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


with open(data_file) as f:
    line = f.readline().strip()
    
    tracking = {}
    for i in range(13):
        char = line[i]
        if char not in tracking:
            tracking[char] = 0
        tracking[char] += 1
        
    for i in range(13, len(line) - 4):

        char = line[i]
        if char not in tracking:
            tracking[char] = 0
        tracking[char] += 1


        print(blue('index'), blue(i+1), tracking)

        if len(tracking) == 14:
            print_green('found ^')
            exit()

        tracking[line[i - 13]] -= 1
        if tracking[line[i - 13]] == 0:
            del tracking[line[i - 13]]
        

        print(tracking)
