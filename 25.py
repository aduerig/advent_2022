# https://adventofcode.com/2022

from helpers import * 

import pathlib

filepath = pathlib.Path(__file__)

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


snafus = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()
        snafus.append(list(line))


convert = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2,
}


to_more_dec = []
for snafu in snafus:
    building = []
    for c in snafu:
        building.append(convert[c])
    to_more_dec.append(building)


def snafu_to_decimal(snafu):
    dec_num = 0
    curr_base = 1
    for i in reversed(range(len(snafu))):
        dec_num += snafu[i] * curr_base
        curr_base *= 5
    return dec_num

convert_to_snaf = {
    4: '1-',
    3: '1=',
    2: '2',
    1: '1',
    0: '0',
}
convert_to_snaf_func = lambda x: convert_to_snaf[x]
def decimal_to_snafu(decimal):
    snafu = []
    while decimal > 0:
        # decimal % 5
        snafu.append(decimal % 5)
        decimal //= 5
    return ''.join(map(convert_to_snaf_func, reversed(snafu)))

# print(f'{1}: {decimal_to_snafu(1)}')
# print(f'{2}: {decimal_to_snafu(2)}')
# print(f'{3}: {decimal_to_snafu(3)}')
# print(f'{4}: {decimal_to_snafu(4)}')
# print(f'{5}: {decimal_to_snafu(5)}')
# print(f'{6}: {decimal_to_snafu(6)}')
# print(f'{7}: {decimal_to_snafu(7)}')
# print(f'{8}: {decimal_to_snafu(8)}')
# print(f'{9}: {decimal_to_snafu(9)}')
# print(f'{10}: {decimal_to_snafu(10)}')
# print(f'{11}: {decimal_to_snafu(11)}')
# print(f'{12}: {decimal_to_snafu(12)}')
# print(f'{13}: {decimal_to_snafu(13)}')
# print(f'{14}: {decimal_to_snafu(14)}')
# print(f'{15}: {decimal_to_snafu(15)}')
# print(f'{16}: {decimal_to_snafu(16)}')
# print(f'{17}: {decimal_to_snafu(17)}')
# exit()

decimal = sum(map(snafu_to_decimal, to_more_dec))
print_green(decimal)


to_try = [
    2,
    0,
    -1,
    1,
    -1,
    1,
    1,
    -2,
    -2,
    0,
    -1,
    -2,
    0,
    1,
    1,
    2,
    -1,
    2,
    2,
    2,
]


convert2 = {
    2: '2',
    1: '1',
    0: '0',
    -1: '-',
    -2: '=',
}

build = ''
for c in to_try:
    build += convert2[c]
print(build) # -22=2-=00211=---2000

print(f'{snafu_to_decimal(to_try):,}')
print(f'{37512839082437:,}')
# print(f'{pow(5, 19):,}')
# exit()

if snafu_to_decimal(to_try) == 37512839082437:
    print_green('done')
elif snafu_to_decimal(to_try) > 37512839082437:
    print_red(f'too big')
else:
    print_yellow(f'too small')

# 37512839082437