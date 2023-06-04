# https://adventofcode.com/2022

from helpers import * 

import pathlib

filepath = pathlib.Path(__file__)

data_file = filepath.parent.joinpath(filepath.stem + '.dat')

nums = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        nums.append(int(line))


nums_2 = []
for index, num in enumerate(nums):
    nums_2.append((index, num))


next_old_index = 0
def get_next_old_index(nums):
    global next_old_index
    for curr_index, (old_index, num) in enumerate(nums):
        if old_index == next_old_index:
            next_old_index += 1
            return curr_index

0, -7, 2, 3, 4, 5, 6
-4


def pos(index, num):
    sign = (int(abs(num) == num) * 2) - 1
    mag = abs(num)

    # divided, remainder = divmod(mag, len(nums_2))
    remainder = mag % len(nums_2)
    if sign == -1:
        end_index = index + (len(nums_2) - 1)
        end_index -= remainder
    else:
        end_index = index + remainder
    print(f'{index=}, {num=} {mag=} {sign=} {remainder=} {end_index=}')
    return end_index % len(nums_2)


[0, 1, 2, 3, 4, 5, 6]

def build_new(old_arr, move_ele, new_index):
    curr = 0
    new_arr = []
    while curr < len(old_arr):
        if old_arr[curr] == move_ele:
            curr += 1
            continue

        if curr == new_index:
            new_arr.append(move_ele)

        new_arr.append(old_arr[curr])        
        curr += 1
    return new_arr

def better_repr(nums_2):
    return [num for _, num in nums_2]


curr_arr = nums_2
print_cyan('STARTING:', better_repr(curr_arr))
for _ in range(len(curr_arr)):
    curr_index = get_next_old_index(curr_arr)
    num = curr_arr[curr_index][1]
    new_index = pos(curr_index, num)
    print(f'Moving {curr_arr[curr_index][1]} from {curr_index} to {new_index}, {num + curr_index=}')
    curr_arr = build_new(curr_arr, curr_arr[curr_index], new_index)
    print_blue('AFTER:', better_repr(curr_arr))
    if _ == 1:
        exit()

print_green(pos(1000, 0) + pos(2000, 0) + pos(3000, 0))