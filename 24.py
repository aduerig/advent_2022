# https://adventofcode.com/2022

from helpers import * 

import pathlib

filepath = pathlib.Path(__file__)

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


board = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            board.append(list(line))
            for index in range(len(board[-1])):
                if board[-1][index] == '.':
                    board[-1][index] = []
                else:
                    board[-1][index] = [board[-1][index]]

for line in board:
    print(line)

print(len(board))

print('later')

def print_board(board, pos):
    for row_index, row in enumerate(board):
        to_print = []
        for col_index, col in enumerate(row):
            if (col_index, row_index) == pos:
                to_print.append(bcolors.OKGREEN + 'E' + bcolors.ENDC)
            elif len(col) == 0:
                to_print.append('.')
            elif len(col) == 1:
                if col[0] in ['>', '<', '^', 'v']:
                    to_print.append(bcolors.OKCYAN + col[0] + bcolors.ENDC)
                else:
                    to_print.append(col[0])
            elif len(col) > 1:
                to_print.append(str(len(col)))
        print(''.join(to_print))

def valid_directions(board, pos):
    for x, y in [
        (pos[0], pos[1]-1),
        (pos[0], pos[1]+1),
        (pos[0]-1, pos[1]),
        (pos[0]+1, pos[1])
    ]:
        # print(f'{pos=} trying {x, y}, {board[y][x]}')
        if (x, y) == (1, 0) or (x, y) == (len(board[0]) - 2, len(board) - 1): 
            yield (x, y)
        elif 1 <= y < len(board) - 1 and 1 <= x < len(board[y]) - 1:
            if not board[y][x]:
                yield (x, y)
    if not board[pos[1]][pos[0]]:
        yield pos


direction = {
    '>': (1, 0),
    '<': (-1, 0),
    '^': (0, -1),
    'v': (0, 1)

}
def blizzards_moved(board):
    new_board = []
    for i in range(len(board)):
        new_arr = []
        for j in range(len(board[0])):
            new_arr.append([])
        new_board.append(new_arr)

    for y in range(len(board)):
        for x in range(len(board[0])):
            if (x, y) != (1, 0) and (x, y) != (len(board[0]) - 2, len(board) - 1):
                if y == len(board) - 1 or x == len(board[0]) - 1 or y == 0 or x == 0:
                    new_board[y][x].append('#')
                    continue
            for element in board[y][x]:
                d = direction[element]
                new_x, new_y = x + d[0], y + d[1]

                if new_x == 0:
                    new_x = len(board[0]) - 2
                elif new_x == len(board[0]) - 1:
                    new_x = 1
                elif new_y == 0:
                    new_y = len(board) - 2
                elif new_y == len(board) - 1:
                    new_y = 1

                new_board[new_y][new_x].append(element)
    return new_board

from copy import deepcopy
from collections import deque


init_pos = (1, 0)
print('INITIAL')
print_board(board, init_pos)

cached_minutes_to_boards = {}


visited = set()
queue = deque([(init_pos, deepcopy(board), 0, 0)])
while queue:
    pos, prev_board, minute, marker = queue.popleft()

    # if pos == (1, 0) and minute != 0:
    #     continue

    # print(f'=== curr_board: {pos=}, {minute=}')
    # print_board(prev_board, pos)

    if (pos, minute, marker) in visited:
        continue
    visited.add((pos, minute, marker))

    if minute + 1 not in cached_minutes_to_boards:
        new_board = blizzards_moved(prev_board)
        cached_minutes_to_boards[minute + 1] = new_board
    new_board = cached_minutes_to_boards[minute + 1]


    if random.randint(0, 10000) == 0:
        print(f'{minute=}, {pos=}, {len(queue)=}')


    if marker == 1 and pos == (1, 0):
        marker += 1
    elif (marker == 0 or marker == 2) and pos == ((len(board[0]) - 2, len(board) - 1)):
        marker += 1
    
    if marker == 3:
        print_board(prev_board, pos)
        print_green(f'{minute=}')
        exit()

    for new_pos in valid_directions(new_board, pos):
        queue.append((new_pos, new_board, minute+1, marker))
    
    # if minute == 14 and pos == (4, 3):
    #     print('debug above')
    #     print_board(new_board, pos)
    #     exit()

print_red('apperantly impossible...')