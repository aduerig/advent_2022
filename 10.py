# https://adventofcode.com/2022

from helpers import * 

import pathlib

filepath = pathlib.Path(__file__)

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


reg = 1
summed_signal_strengths = 0
cycle = 1
def should_draw(cycle):
    pinging = ((cycle - 1) % 40) + 1
    print(pinging, reg)
    if pinging in [reg, reg + 1, reg + 2]:
        return True
    return False


cycle_arr = []
def do_cycle(cycle):
    if should_draw(cycle):
        cycle_arr.append('#')
    else:
        cycle_arr.append('.')


with open(data_file) as f:
    for index, line in enumerate(f.readlines()):
        line = line.strip()


        # if cycle > 0 and (cycle + 20) % 40 == 0:
        #     print_cyan(f'cycle: {cycle}, reg: {reg}, signal_strength: {cycle * reg}')
        #     summed_signal_strengths += cycle * reg


        if line == 'noop':
            do_cycle(cycle)
            cycle += 1
        else:
            do_cycle(cycle)
            cycle += 1
            do_cycle(cycle)

            _, num = line.split()
            num = int(num)
            reg += num
            cycle += 1

        # print_blue(f'cycle: {cycle}, reg: {reg}')

            # if cycle > 0 and (cycle + 20) % 40 == 0:
            #     print_cyan(f'cycle: {cycle}, reg: {reg}, signal_strength: {cycle * reg}')
            #     summed_signal_strengths += cycle * reg
        # if cycle > 10:
        #     for i in range(6):
        #         # print(i*40)
        #         print(''.join(cycle_arr[(i*40):(i*40)+40]))

            # exit()

for i in range(6):
    # print(i*40)
    print(''.join(cycle_arr[(i*40):(i*40)+40]))
# print(cycle)



# # https://adventofcode.com/2022

# from helpers import * 

# import pathlib

# filepath = pathlib.Path(__file__)

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# reg = 1
# summed_signal_strengths = 0
# cycle = 1
# with open(data_file) as f:
#     for index, line in enumerate(f.readlines()):
#         line = line.strip()


#         cycle += 1
#         if cycle > 0 and (cycle + 20) % 40 == 0:
#             print_cyan(f'cycle: {cycle}, reg: {reg}, signal_strength: {cycle * reg}')
#             summed_signal_strengths += cycle * reg


#         if line != 'noop':
#             cycle += 1
#             _, num = line.split()
#             num = int(num)

#             reg += num
#         # print_blue(f'cycle: {cycle}, reg: {reg}')

#             if cycle > 0 and (cycle + 20) % 40 == 0:
#                 print_cyan(f'cycle: {cycle}, reg: {reg}, signal_strength: {cycle * reg}')
#                 summed_signal_strengths += cycle * reg



# print_green(f'summed signal_strengths: {summed_signal_strengths}')