# https://adventofcode.com/2022

from helpers import * 

import pathlib

import sys
sys.set_int_max_str_digits(10000000)

filepath = pathlib.Path(__file__)

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


class Item:
    def __init__(self, worry):
        self.worry = worry
        self.next_item = {}

    def __repr__(self):
        return f'{self.worry}'

monkies = []
by_all = 1
with open(data_file) as f:
    # for index, line in enumerate(f.readlines()):
    #     line = line.strip()
    while f.readline():
        starting_worry_levels = list(map(int, f.readline().strip().replace('Starting items: ', '').split(',')))
        op = f.readline().strip().replace('Operation: new = ', '')
        test = int(f.readline().strip().replace('Test: divisible by ', ''))
        if_true = f.readline().strip().replace('If true: throw to monkey ', '')
        if_false = f.readline().strip().replace('If false: throw to monkey ', '')
        f.readline()
        
        by_all *= test

        monkies.append({
            'items': list(map(lambda x: Item(x), starting_worry_levels)),
            'op': op,
            'test': test,
            'if_true': if_true,
            'if_false': if_false,
        })

for index, monkey in enumerate(monkies):
    print(monkey['items'])



active = [0] * len(monkies)
for the_round in range(10000):
    print(f'=== round {the_round} ===')
    for index, monkey in enumerate(monkies):
        for item in monkey['items']:
            # if item.worry % monkey['test'] in item.next_item:
                # item.worry = (item.worry % monkey['test']) + monkey['test']
                # item.worry = item.next_item[item.worry % monkey['test']]


            before_worry_level = item.worry
            next_worry_level = eval(monkey['op'].replace('old', str(item.worry)))
            
            next_worry_level %= by_all


            item.worry = next_worry_level
            if item.worry % monkey['test'] == 0:
                next_monkey = int(monkey['if_true'])
            else:
                next_monkey = int(monkey['if_false'])

            # item.next_item[before_worry_level % monkey['test']] = before_worry_level

            monkies[next_monkey]['items'].append(item)

            active[index] += 1        
        monkey['items'] = []

for index, monkey in enumerate(monkies):
    print('items', monkey['items'], 'inspected:', active[index])
    


active.sort()

print_blue(active[-1], active[-2])
print_green('monkey buisness:', active[-1] * active[-2])

# 2713310158 too low




# https://adventofcode.com/2022

# from helpers import * 

# import pathlib

# filepath = pathlib.Path(__file__)

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# monkies = []
# with open(data_file) as f:
#     # for index, line in enumerate(f.readlines()):
#     #     line = line.strip()
#     while f.readline():
#         start = list(map(int, f.readline().strip().replace('Starting items: ', '').split(',')))
#         op = f.readline().strip().replace('Operation: new = ', '')
#         test = int(f.readline().strip().replace('Test: divisible by ', ''))
#         if_true = f.readline().strip().replace('If true: throw to monkey ', '')
#         if_false = f.readline().strip().replace('If false: throw to monkey ', '')
#         f.readline()

#         monkies.append({
#             'items': start,
#             'op': op,
#             'test': test,
#             'if_true': if_true,
#             'if_false': if_false,
#         })

# for index, monkey in enumerate(monkies):
#     print(monkey['items'])


# active = [0] * len(monkies)
# for the_round in range(20):
#     print(f'=== round {the_round} ===')
#     for index, monkey in enumerate(monkies):
#         for worry_level_item in monkey['items']:
#             worry_level_item = eval(monkey['op'].replace('old', str(worry_level_item)))
#             # worry_level_item //= 3

#             # if index == 3:
#             #     worry_level_item %= monkey['test']

#             if worry_level_item % monkey['test'] == 0:
#                 next_monkey = int(monkey['if_true'])
#             else:
#                 next_monkey = int(monkey['if_false'])
#             monkies[next_monkey]['items'].append(worry_level_item)

#             active[index] += 1        
#         monkey['items'] = []

# for index, monkey in enumerate(monkies):
#     print(monkey['items'], 'inspected:', active[index])

# active.sort()

# print_blue(active[-1], active[-2])
# print_green('monkey buisness:', active[-1] * active[-2])


# # https://adventofcode.com/2022

# from helpers import * 

# import pathlib

# filepath = pathlib.Path(__file__)

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')


# monkies = []
# with open(data_file) as f:
#     # for index, line in enumerate(f.readlines()):
#     #     line = line.strip()
#     while f.readline():
#         start = list(map(int, f.readline().strip().replace('Starting items: ', '').split(',')))
#         op = f.readline().strip().replace('Operation: new = ', '')
#         test = int(f.readline().strip().replace('Test: divisible by ', ''))
#         if_true = f.readline().strip().replace('If true: throw to monkey ', '')
#         if_false = f.readline().strip().replace('If false: throw to monkey ', '')
#         f.readline()

#         monkies.append({
#             'items': start,
#             'op': op,
#             'test': test,
#             'if_true': if_true,
#             'if_false': if_false,
#         })

# for index, monkey in enumerate(monkies):
#     print(monkey['items'])


# active = [0] * len(monkies)
# for the_round in range(20):
#     print(f'=== round {the_round} ===')
#     for index, monkey in enumerate(monkies):
#         for worry_level_item in monkey['items']:
#             worry_level_item = eval(monkey['op'].replace('old', str(worry_level_item)))
#             worry_level_item //= 3
#             if worry_level_item % monkey['test'] == 0:
#                 monkies[int(monkey['if_true'])]['items'].append(worry_level_item)
#             else:
#                 # print('worry_level_item', worry_level_item)
#                 monkies[int(monkey['if_false'])]['items'].append(worry_level_item)
#             active[index] += 1        
#         monkey['items'] = []

# for index, monkey in enumerate(monkies):
#     print(monkey['items'])


# active.sort()

# print_blue(active[-1], active[-2])
# print_green('monkey buisness:', active[-1] * active[-2])