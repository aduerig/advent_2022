# https://adventofcode.com/2022

from helpers import * 

import pathlib

filepath = pathlib.Path(__file__)

data_file = filepath.parent.joinpath(filepath.stem + '.dat')



def in_right_order(first, second, level=0):
    if type(first) == int and type(second) == int:
        print(f'{" " * (level * 4)}- Compare {first} vs {second}')
        if first > second:
            print_red(f'{" " * ((level + 1) * 4)}- Right side is smaller, so inputs are not in the right order')
            return False
        elif first < second:
            print_green(f'{" " * ((level + 1) * 4)}- Left side is smaller, so inputs are in the right order')
            return True
        return None

    print(f'{" " * (level * 4)}- Compare {first} vs {second}')
    

    if type(first) != type(second):
        print(f'{" " * (level * 4)}- Mixed types; converting and retry comparison')
        if type(first) == int:
            return in_right_order([first], second, level)
        else:
            return in_right_order(first, [second], level)
    
    while len(first) and len(second):
        ele1, ele2 = first.pop(0), second.pop(0)
        result = in_right_order(ele1, ele2, level+1)
        if result == None:
            continue
        return result

    if len(second) == 0 and len(first) == 0:
        print_cyan(f'{" " * (level * 4)}- Same time, idk what to do')
        return None
    if len(second) == 0:
        print_red(f'{" " * ((level + 1) * 4)}- Right side ran out of items, so inputs are not in the right order')
        return False
    if len(first) == 0:
        print_green(f'{" " * ((level + 1) * 4)}- Left side ran out of items, so inputs are in the right order')
        return True
    print('NEVER GET HERE')
    exit()

packets = [
    [[2]],
    [[6]],
]
with open(data_file) as f:
    index = 0
    while first := f.readline().strip():
        second, blank_line = f.readline().strip(), f.readline()

        index += 1

        print(f'\n== Pair {index} ==')
        # if index != 2:
        #     continue

        first, second = eval(first), eval(second)
        print(first)
        packets.append(first)
        packets.append(second)


from copy import deepcopy
finished = []
for new_packet in packets:
    for index, sorted_packet in enumerate(finished):
        if in_right_order(deepcopy(new_packet), deepcopy(sorted_packet)):
            finished.insert(index, new_packet)
            break
    else:
        finished.append(new_packet)

print('\n\n === PRINTING ALL ===')
save_index = 0
for index, packet in enumerate(finished):
    if packet == [[2]]:
        save_index = index + 1
    if packet == [[6]]:
        print_green('decoder key', save_index * (index + 1))


# wrong: 45

# too low: 396
# too high: 5742



# # https://adventofcode.com/2022

# from helpers import * 

# import pathlib

# filepath = pathlib.Path(__file__)

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')



# def in_right_order(first, second, level=0):
#     if type(first) == int and type(second) == int:
#         print(f'{" " * (level * 4)}- Compare {first} vs {second}')
#         if first > second:
#             print_red(f'{" " * ((level + 1) * 4)}- Right side is smaller, so inputs are not in the right order')
#             return False
#         elif first < second:
#             print_green(f'{" " * ((level + 1) * 4)}- Left side is smaller, so inputs are in the right order')
#             return True
#         return None

#     print(f'{" " * (level * 4)}- Compare {first} vs {second}')
    

#     if type(first) != type(second):
#         print(f'{" " * (level * 4)}- Mixed types; converting and retry comparison')
#         if type(first) == int:
#             return in_right_order([first], second, level)
#         else:
#             return in_right_order(first, [second], level)
    
#     while len(first) and len(second):
#         ele1, ele2 = first.pop(0), second.pop(0)
#         result = in_right_order(ele1, ele2, level+1)
#         if result == None:
#             continue
#         return result

#     if len(second) == 0 and len(first) == 0:
#         print_cyan(f'{" " * (level * 4)}- Same time, idk what to do')
#         return None
#     if len(second) == 0:
#         print_red(f'{" " * ((level + 1) * 4)}- Right side ran out of items, so inputs are not in the right order')
#         return False
#     if len(first) == 0:
#         print_green(f'{" " * ((level + 1) * 4)}- Left side ran out of items, so inputs are in the right order')
#         return True
#     print('NEVER GET HERE')
#     exit()


# # def in_right_order(first, second, level=0):
# #     # print('looking at first:', first, 'and second:', second)

# #     if len(second) == 0 and len(first) == 0:
# #         print_cyan(f'{" " * (level * 4)}- Same time, idk what to do')
# #         return True
# #     if len(second) == 0:
# #         print_red(f'{" " * (level * 4)}- Right side ran out of items, so inputs are not in the right order')
# #         return False
# #     if len(first) == 0:
# #         print_green(f'{" " * (level * 4)}- Left side ran out of items, so inputs are in the right order')
# #         return True

# #     if type(first[0]) != type(second[0]):
# #         # print('deeper', type(first[0]), type(second[0]))
# #         if type(first[0]) == int:
# #             return in_right_order([[first[0]] + first[1:]], second, level+1)
# #         else:
# #             # print('huh', [[second[0]]] + second[1:])
# #             return in_right_order(first, [[second[0]]] + second[1:], level+1)

# #     elif type(first[0]) == int and type(second[0]) == int:
# #         print(f'{" " * (level * 4)}- Compare {first[0]} vs {second[0]}')
# #         if first[0] == second[0]:
# #             return in_right_order(first[1:], second[1:], level)

# #         if first[0] > second[0]:
# #             return False
# #         # return in_right_order(first[1:], second)
# #         return True


# #     elif type(first[0]) == list and type(second[0]) == list:
# #         print(f'{" " * (level * 4)}- Compare {first} vs {second}')
# #         if not in_right_order(first[0], second[0], level+1):
# #             return False
# #         return in_right_order(first[1:], second[1:], level+1)



# right_order_indicies = 0
# with open(data_file) as f:
#     index = 0
#     while first := f.readline().strip():
#         second, blank_line = f.readline().strip(), f.readline()

#         index += 1

#         print(f'\n== Pair {index} ==')
#         # if index != 2:
#         #     continue

#         first, second = eval(first), eval(second)
#         if in_right_order(first, second):
#             # print_blue(f'Correct! index {index}')
#             right_order_indicies += index
#         else:
#             pass
#             # print_red(f'WRONG ORDER: index {index}')




# print_blue(f'sum of those indicies: {right_order_indicies}')





# # wrong: 45

# # too low: 396
# # too high: 5742