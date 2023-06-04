# https://adventofcode.com/2022

import random
import pathlib

from helpers import * 

filepath = pathlib.Path(__file__)

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


graph = {}
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()

        node, val = list(map(lambda x: x.strip(), line.split(':')))

        if val.isnumeric():
            graph[node] = int(val)
        else:
            first, sign, second = val.split(' ')
            graph[node] = (first, sign, second)


sign_funcs = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x // y,
}

def dfs(node):
    if type(graph[node]) == int:
        return graph[node]
    first, sign, second = graph[node]
    return sign_funcs[sign](dfs(first), dfs(second))


interest = 'wdzt', 'dffc'
if 'pppw' in graph:
    interest = 'pppw', 'sjmn'


for i in range(3952673930000, 10000000000000000):
    graph['humn'] = i
    guess = dfs(interest[0])
    guess2 = dfs(interest[1])
    if random.randint(0, 1000) == 2:
        print(f'iteration {i=}, {guess=}, {guess2}')
        if guess < guess2:
            print_yellow('LOWER')
        else:
            print_cyan('BIGGER')

    if guess == guess2:
        print(i)
        break




# # https://adventofcode.com/2022

# from helpers import * 

# import pathlib

# filepath = pathlib.Path(__file__)

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# graph = {}
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()

#         node, val = list(map(lambda x: x.strip(), line.split(':')))

#         if val.isnumeric():
#             graph[node] = int(val)
#         else:
#             first, sign, second = val.split(' ')
#             graph[node] = (first, sign, second)


# sign_funcs = {
#     '+': lambda x, y: x + y,
#     '*': lambda x, y: x * y,
#     '-': lambda x, y: x - y,
#     '/': lambda x, y: x // y,
# }

# def dfs(node):
#     if type(graph[node]) == int:
#         return graph[node]
#     first, sign, second = graph[node]
#     return sign_funcs[sign](dfs(first), dfs(second))



# print(dfs('root'))