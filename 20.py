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
    if num == 0:
        print(f'0 found {index=}')
    nums_2.append((index, num * 811589153))


next_old_index = 0
def get_next_old_index(nums):
    global next_old_index
    for curr_index, (old_index, num) in enumerate(nums):
        if old_index == next_old_index:
            next_old_index += 1
            return curr_index


def pos(index, num):
    sign = (int(abs(num) == num) * 2) - 1
    mag = abs(num)

    # divided, remainder = divmod(mag, len(nums_2))    
    # remainder += divided

    remainder = mag % (len(nums_2) - 1)
    if sign == -1:
        end_index = index + (len(nums_2) - 1)
        end_index -= remainder
    else:
        end_index = index + remainder
        # if end_index >= len(nums_2):
        #     end_index += 1
    # print(f'{index=}, {num=} {mag=} {sign=} {remainder=} {end_index=}')
    return end_index % (len(nums_2) - 1)


#     a
# [0, 1, 2, 3, 4, 5, 6]


# []

def build_new(old_arr, move_ele, new_index):
    curr = 0
    new_arr = []
    while curr < len(old_arr):
        if old_arr[curr] == move_ele:
            curr += 1
            continue

        if len(new_arr) == new_index:
            new_arr.append(move_ele)

        new_arr.append(old_arr[curr])        
        curr += 1
    if len(new_arr) == new_index:
        new_arr.append(move_ele)
    return new_arr


def better_repr(nums_2):
    return [num for _, num in nums_2]

curr_arr = nums_2
print_cyan('STARTING:', better_repr(curr_arr))

for __ in range(10):
    for _ in range(len(curr_arr)):
        curr_index = get_next_old_index(curr_arr)
        num = curr_arr[curr_index][1]
        new_index = pos(curr_index, num)
        # print(f'Moving {curr_arr[curr_index][1]} from {curr_index} to {new_index}, {num + curr_index=}')
        curr_arr = build_new(curr_arr, curr_arr[curr_index], new_index)
        if len(curr_arr) != len(nums):
            print_red(f'mismatch! {len(curr_arr)=}, {len(nums)=}')
            exit()
        # print_blue('AFTER:', better_repr(curr_arr))
        # if _ == 0:
        #     exit()
    print(f'finished {__}')
    next_old_index = 0


for start, (_, num) in enumerate(curr_arr):
    if num == 0:
        break

print(f'{start=}')

thousand = curr_arr[(start + 1000) % len(curr_arr)][1]
thousand_2 = curr_arr[(start + 2000) % len(curr_arr)][1]
thousand_3 = curr_arr[(start + 3000) % len(curr_arr)][1]

# -7320 (not correct)
# -850 (not correct)
print_green(f'{thousand=}, {thousand_2=}, {thousand_3=}, {thousand + thousand_2 + thousand_3=}')



# # https://adventofcode.com/2022

# from helpers import * 

# import pathlib

# filepath = pathlib.Path(__file__)

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# nums = []
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         nums.append(int(line))


# nums_2 = []
# for index, num in enumerate(nums):
#     if num == 0:
#         print(f'0 found {index=}')
#     nums_2.append((index, num))


# next_old_index = 0
# def get_next_old_index(nums):
#     global next_old_index
#     for curr_index, (old_index, num) in enumerate(nums):
#         if old_index == next_old_index:
#             next_old_index += 1
#             return curr_index


# def pos(index, num):
#     sign = (int(abs(num) == num) * 2) - 1
#     mag = abs(num)

#     # divided, remainder = divmod(mag, len(nums_2))    
#     # remainder += divided

#     remainder = mag % (len(nums_2) - 1)
#     if sign == -1:
#         end_index = index + (len(nums_2) - 1)
#         end_index -= remainder
#     else:
#         end_index = index + remainder
#         # if end_index >= len(nums_2):
#         #     end_index += 1
#     print(f'{index=}, {num=} {mag=} {sign=} {remainder=} {end_index=}')
#     return end_index % (len(nums_2) - 1)


# #     a
# # [0, 1, 2, 3, 4, 5, 6]


# # []

# def build_new(old_arr, move_ele, new_index):
#     curr = 0
#     new_arr = []
#     while curr < len(old_arr):
#         if old_arr[curr] == move_ele:
#             curr += 1
#             continue

#         if len(new_arr) == new_index:
#             new_arr.append(move_ele)

#         new_arr.append(old_arr[curr])        
#         curr += 1
#     if len(new_arr) == new_index:
#         new_arr.append(move_ele)
#     return new_arr


# def better_repr(nums_2):
#     return [num for _, num in nums_2]

# curr_arr = nums_2
# print_cyan('STARTING:', better_repr(curr_arr))
# for _ in range(len(curr_arr)):
#     curr_index = get_next_old_index(curr_arr)
#     num = curr_arr[curr_index][1]
#     new_index = pos(curr_index, num)
#     # print(f'Moving {curr_arr[curr_index][1]} from {curr_index} to {new_index}, {num + curr_index=}')
#     curr_arr = build_new(curr_arr, curr_arr[curr_index], new_index)
#     if len(curr_arr) != len(nums):
#         print_red(f'mismatch! {len(curr_arr)=}, {len(nums)=}')
#         exit()
#     # print_blue('AFTER:', better_repr(curr_arr))
#     # if _ == 0:
#     #     exit()


# for start, (_, num) in enumerate(curr_arr):
#     if num == 0:
#         break

# print(f'{start=}')

# thousand = curr_arr[(start + 1000) % len(curr_arr)][1]
# thousand_2 = curr_arr[(start + 2000) % len(curr_arr)][1]
# thousand_3 = curr_arr[(start + 3000) % len(curr_arr)][1]

# # -7320 (not correct)
# # -850 (not correct)
# print_green(f'{thousand=}, {thousand_2=}, {thousand_3=}, {thousand + thousand_2 + thousand_3=}')