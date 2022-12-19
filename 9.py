# https://adventofcode.com/2022

from helpers import * 

import pathlib

filepath = pathlib.Path(__file__)

data_file = filepath.parent.joinpath(filepath.stem + '.dat')



head = [0, 0]
body = []
for i in range(9):
    body.append([0, 0])


direction_map = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1),
}

seen = set([(0, 0)])
with open(data_file) as f:
    for index, line in enumerate(f.readlines()):
        # if index == 3:
        #     exit()
        line = line.strip()
        og_direction, count = line.split()
        direction, count = direction_map[og_direction], int(count)

        for _ in range(count):
            print(f'moving {_} {direction}')
            head[0] += direction[0]
            head[1] += direction[1]
            
            last = head
            ahead_moved = direction

            for i in range(len(body)):
                part = body[i]

                dist = pow(pow(last[0] - part[0], 2) + pow(last[1] - part[1], 2), 0.5)
                # print('dist', dist)
                if dist < 1.5:
                    # print('skipping')
                    break

                before = list(part)
                

                if part[0] == last[0] and part[1] == last[1] + 2:
                    part[1] -= 1
                elif part[0] == last[0] and part[1] == last[1] - 2:
                    part[1] += 1
                elif part[1] == last[1] and part[0] == last[0] + 2:
                    part[0] -= 1
                elif part[1] == last[1] and part[0] == last[0] - 2:
                    part[0] += 1
                elif ahead_moved[0] != 0 and ahead_moved[1] != 0:
                    part[0] += ahead_moved[0]
                    part[1] += ahead_moved[1]
                elif ahead_moved[0] != 0:
                    part[0] += ahead_moved[0]
                    if part[1] != last[1]:
                        part[1] += int((int(last[1] > part[1]) * 2) - 1)
                else:
                    part[1] += ahead_moved[1]
                    if part[0] != last[0]:
                        part[0] += int((int(last[0] > part[0]) * 2) - 1)

                # print(f'direction from {i - 1}, ahead_moved: {ahead_moved}')
                # print_cyan(head, body)

                ahead_moved = [part[0] - before[0], part[1] - before[1]]
                last = part
                seen.add(tuple(body[-1]))
            seen.add(tuple(body[-1]))


        print(f'AFTER {og_direction}{count}')
        for j in range(15, -15, -1):
            row = []
            for i in range(-15, 15):
                if i == head[0] and j == head[1]:
                    row.append('H')
                    continue
                for idx2, (i2, j2) in enumerate(body):
                    if i == i2 and j == j2:
                        row.append(str(idx2 + 1))
                        break
                else:
                    if i == 0 and j == 0:
                        row.append('s')
                    else:
                        row.append('.')
            print(''.join(row))

        # print_blue('head', head)
        # print_cyan('tail', body[-1])
        # print_cyan('body', body[0])


print_green('tail visited', len(seen))









# # https://adventofcode.com/2022

# from helpers import * 

# import pathlib

# filepath = pathlib.Path(__file__)

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')



# head = [0, 0]
# tail = [0, 0]


# direction_map = {
#     'R': (1, 0),
#     'L': (-1, 0),
#     'U': (0, 1),
#     'D': (0, -1),
# }

# seen = set([(0, 0)])
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()
#         direction, count = line.split()
#         direction, count = direction_map[direction], int(count)

#         for _ in range(count):
#             head[0] += direction[0]
#             head[1] += direction[1]
            
#             dist = pow(pow(head[0] - tail[0], 2) + pow(head[1] - tail[1], 2), 0.5)
#             print_blue('dist', dist)
#             if dist < 1.5:
#                 print('skipping')
#                 continue

#             if direction[0] != 0:
#                 tail[0] += direction[0]
#                 if tail[1] != head[1]:
#                     tail[1] += int((int(head[1] > tail[1]) * 2) - 1)
#             else:
#                 tail[1] += direction[1]
#                 if tail[0] != head[0]:
#                     tail[0] += int((int(head[0] > tail[0]) * 2) - 1)
#             seen.add(tuple(tail))
#             print(tail)

# print_green('tail visited', len(seen))




