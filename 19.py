# https://adventofcode.com/2022


import pathlib
import time

from helpers import * 

filepath = pathlib.Path(__file__)

data_file = filepath.parent.joinpath(filepath.stem + '.dat')


plans = []
with open(data_file) as f:
    for line in f.readlines():
        line = line.strip()

        index_part, rest = line.split(':')
        index = int(index_part.split(' ')[1].strip())
        rest = rest.strip().split('. ')
        # regex for number
        import re
        ore_robot = (int(re.findall(r'\d+', rest[0])[0]), 0, 0)
        clay_robot = (int(re.findall(r'\d+', rest[1])[0]), 0, 0)
        
        finding = re.findall(r'\d+', rest[2])
        obsidian_robot = (int(finding[0]), int(finding[1]), 0)

        finding = re.findall(r'\d+', rest[3])
        geode_robot = (int(finding[0]), 0, int(finding[1]))

        plans.append((ore_robot, clay_robot, obsidian_robot, geode_robot, index))

max_costs = [-float('inf'), -float('inf'), -float('inf'), -float('inf')]



class State:
    def __init__(self, minutes_left=32):        
        self.minutes_left = minutes_left
        
        self.ore = 0
        self.clay = 0
        self.obsidian = 0
        self.geode = 0

        self.robots = [
            1,
            0,
            0,
            0,
        ]


    def copy_state(self):
        newy = State()

        newy.ore = self.ore
        newy.clay = self.clay
        newy.obsidian = self.obsidian
        newy.geode = self.geode

        newy.robots = list(self.robots)
        return newy


    def __repr__(self):
        return f'{self.minutes_left=}, {self.ore=}, {self.clay=}, {self.obsidian=}, {self.geode=}, {self.robots=}'



def add_correct(state, robot_to_buy):
    if robot_to_buy == 1:
        state.ore_robot += 1
    elif robot_to_buy == 2:
        state.clay_robot += 1
    elif robot_to_buy == 3:
        state.obsidian_robot += 1
    elif robot_to_buy == 4:
        state.geode_robot += 1


def get_max_cost(plan, index):
    return max(map(lambda x: x[index], plan[:-1]))


all_max_geodes = []
start_time = time.time()
nodes = 0
for plan in plans:
    plan_start_time = time.time()
    ore_robot, clay_robot, obsidian_robot, geode_robot, plan_num = plan
    max_ore_cost = get_max_cost(plan, 0)
    max_clay_cost = get_max_cost(plan, 1)
    max_obsidian_cost = get_max_cost(plan, 2)
    max_costs = [max_ore_cost, max_clay_cost, max_obsidian_cost]

    print_blue(f'Plan {plan_num}: {ore_robot=}, {clay_robot=}, {obsidian_robot=}, {geode_robot=}, {max_costs=}')
    
    queue = [State()]
    max_geodes = 0
    while queue:
        curr_state = queue.pop()        
        nodes += 1

        if curr_state.minutes_left == 0:
            continue

        # if random.randint(1, 500000) == 2:
        #     print(f'plan {plan_num}/{len(plans)}, {nodes / (time.time() - start_time):,.0f} nps, {len(queue)=}, {curr_state.minutes_left=}, {curr_state.ore=}, {curr_state.clay=}, {curr_state.obsidian=}, {curr_state.geode=}, {max_geodes=}, {nodes=:,}, {curr_state.robots=}')
        #     print(list(map(lambda x: x.depth, queue)))

        # do nothing till end
        if curr_state.robots[3]:
            geodes_left_to_collect = curr_state.robots[3] * curr_state.minutes_left
            max_geodes = max(max_geodes, curr_state.geode + geodes_left_to_collect)


        for robot_to_buy in (0, 1, 2, 3):
            if robot_to_buy < 3:
                if max_costs[robot_to_buy] <= curr_state.robots[robot_to_buy]:
                    continue
            ore_cost, clay_cost, obsidian_cost = plan[robot_to_buy]

            if ore_cost and not curr_state.robots[0]:
                continue

            if clay_cost and not curr_state.robots[1]:
                continue

            if obsidian_cost and not curr_state.robots[2]:
                continue

            def get_needed_minutes(cost, have, robots):
                needed = cost - have
                
                whole_num = needed // robots
                if needed % robots:
                    whole_num += 1
                return whole_num

            ore_minutes, clay_minutes, obsidian_minutes = 1, 1, 1
            if ore_cost and curr_state.ore < ore_cost:
                ore_minutes += get_needed_minutes(ore_cost, curr_state.ore, curr_state.robots[0])
            if clay_cost and curr_state.clay < clay_cost:
                clay_minutes += get_needed_minutes(clay_cost, curr_state.clay, curr_state.robots[1])
            if obsidian_cost and curr_state.obsidian < obsidian_cost:
                obsidian_minutes += get_needed_minutes(obsidian_cost, curr_state.obsidian, curr_state.robots[2])

            minutes_needed = max(ore_minutes, clay_minutes, obsidian_minutes)

            if curr_state.minutes_left - minutes_needed < 0:
                continue

            # print(f'{minutes_needed=}, {ore_minutes=}, {clay_minutes=}, {obsidian_minutes=}, {curr_state.ore=}, {curr_state.clay=}, {curr_state.obsidian=}, {curr_state.geode=}, {curr_state.robots=}, {ore_cost=}, {clay_cost=}, {obsidian_cost=}, {robot_to_buy=}')


            new_state = curr_state.copy_state()
            new_state.minutes_left = curr_state.minutes_left - minutes_needed

            new_state.ore += (new_state.robots[0] * minutes_needed)
            new_state.clay += (new_state.robots[1] * minutes_needed)
            new_state.obsidian += (new_state.robots[2] * minutes_needed)
            new_state.geode += (new_state.robots[3] * minutes_needed)

            new_state.ore -= ore_cost
            new_state.clay -= clay_cost
            new_state.obsidian -= obsidian_cost

            new_state.robots[robot_to_buy] += 1

            max_geodes = max(max_geodes, new_state.geode)
            queue.append(new_state)

    all_max_geodes.append(max_geodes)
    print_green(f'Plan {plan_num}, {max_geodes=}, {time.time() - plan_start_time:.2f} seconds')

print_cyan(f'{time.time() - start_time:.2f} seconds')

print(all_max_geodes)
multed = all_max_geodes[0] * all_max_geodes[1]
print_blue('all 2', multed)


print_blue('all 3', multed * all_max_geodes[2])

















# import pathlib
# import time

# from helpers import * 

# filepath = pathlib.Path(__file__)

# data_file = filepath.parent.joinpath(filepath.stem + '.dat')

# # Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.

# plans = []
# with open(data_file) as f:
#     for line in f.readlines():
#         line = line.strip()

#         index_part, rest = line.split(':')
#         index = int(index_part.split(' ')[1].strip())
#         rest = rest.strip().split('. ')
#         # regex for number
#         import re
#         ore_robot = (int(re.findall(r'\d+', rest[0])[0]), 0, 0)
#         clay_robot = (int(re.findall(r'\d+', rest[1])[0]), 0, 0)
        
#         finding = re.findall(r'\d+', rest[2])
#         obsidian_robot = (int(finding[0]), int(finding[1]), 0)

#         finding = re.findall(r'\d+', rest[3])
#         geode_robot = (int(finding[0]), 0, int(finding[1]))

#         plans.append((ore_robot, clay_robot, obsidian_robot, geode_robot, index))

# max_costs = [-float('inf'), -float('inf'), -float('inf'), -float('inf')]



# class State:
#     def __init__(self, plan, minutes_left=24):
#         self.plan = plan
        
#         self.minutes_left = minutes_left
        
#         self.depth = 0

#         self.ore = 0
#         self.clay = 0
#         self.obsidian = 0
#         self.geode = 0

#         self.robots = [
#             1,
#             0,
#             0,
#             0,
#         ]


#     def copy_state(self):
#         newy = State(self.plan)

#         newy.ore = self.ore
#         newy.clay = self.clay
#         newy.obsidian = self.obsidian
#         newy.geode = self.geode

#         newy.depth = self.depth + 1

#         newy.robots = list(self.robots)
#         return newy


#     def __repr__(self):
#         return f'{self.minutes_left=}, {self.ore=}, {self.clay=}, {self.obsidian=}, {self.geode=}, {self.robots=}'



# def add_correct(state, robot_to_buy):
#     if robot_to_buy == 1:
#         state.ore_robot += 1
#     elif robot_to_buy == 2:
#         state.clay_robot += 1
#     elif robot_to_buy == 3:
#         state.obsidian_robot += 1
#     elif robot_to_buy == 4:
#         state.geode_robot += 1


# def get_max_cost(plan, index):
#     return max(map(lambda x: x[index], plan[:-1]))


# total_quality_level = 0
# start_time = time.time()
# nodes = 0
# for plan in plans:
#     ore_robot, clay_robot, obsidian_robot, geode_robot, plan_num = plan
#     max_ore_cost = get_max_cost(plan, 0)
#     max_clay_cost = get_max_cost(plan, 1)
#     max_obsidian_cost = get_max_cost(plan, 2)
#     max_costs = [max_ore_cost, max_clay_cost, max_obsidian_cost]

#     print_blue(f'Plan {plan_num}: {ore_robot=}, {clay_robot=}, {obsidian_robot=}, {geode_robot=}, {max_costs=}')
    
#     queue = [State(plan=plan)]
#     max_geodes = 0
#     while queue:
#         curr_state = queue.pop()        
#         nodes += 1

#         if curr_state.minutes_left == 0:
#             continue

#         # if random.randint(1, 500000) == 2:
#         #     print(f'plan {plan_num}/{len(plans)}, {nodes / (time.time() - start_time):,.0f} nps, {len(queue)=}, {curr_state.minutes_left=}, {curr_state.ore=}, {curr_state.clay=}, {curr_state.obsidian=}, {curr_state.geode=}, {max_geodes=}, {nodes=:,}, {curr_state.robots=}')
#         #     print(list(map(lambda x: x.depth, queue)))

#         # do nothing till end
#         if curr_state.robots[3]:
#             geodes_left_to_collect = curr_state.robots[3] * curr_state.minutes_left
#             max_geodes = max(max_geodes, curr_state.geode + geodes_left_to_collect)


#         for robot_to_buy in (0, 1, 2, 3):
#             if robot_to_buy < 3:
#                 if max_costs[robot_to_buy] <= curr_state.robots[robot_to_buy]:
#                     continue
#             ore_cost, clay_cost, obsidian_cost = curr_state.plan[robot_to_buy]

#             if ore_cost and not curr_state.robots[0]:
#                 continue

#             if clay_cost and not curr_state.robots[1]:
#                 continue

#             if obsidian_cost and not curr_state.robots[2]:
#                 continue

#             def get_needed_minutes(cost, have, robots):
#                 counter = 1
#                 while True:
#                     if robots * counter >= (cost - have):
#                         return counter
#                     counter += 1

#                 # needed_material = cost - have
#                 # remainder = needed_material % robots
#                 # minutes_needed = (needed_material + remainder) // robots
#                 print(f'{minutes_needed=}, {cost=}, {have=}, {robots=}')
#                 # if minutes_needed < 0:
#                 #     print(f'{minutes_needed=}, {cost=}, {have=}, {robots=}')
#                 #     exit()
#                 return max(minutes_needed, 0)

#             ore_minutes, clay_minutes, obsidian_minutes = 1, 1, 1
#             if ore_cost and curr_state.ore < ore_cost:
#                 ore_minutes += get_needed_minutes(ore_cost, curr_state.ore, curr_state.robots[0])
#             if clay_cost and curr_state.clay < clay_cost:
#                 clay_minutes += get_needed_minutes(clay_cost, curr_state.clay, curr_state.robots[1])
#             if obsidian_cost and curr_state.obsidian < obsidian_cost:
#                 obsidian_minutes += get_needed_minutes(obsidian_cost, curr_state.obsidian, curr_state.robots[2])

#             minutes_needed = max(ore_minutes, clay_minutes, obsidian_minutes)

#             if curr_state.minutes_left - minutes_needed < 0:
#                 continue

#             # print(f'{minutes_needed=}, {ore_minutes=}, {clay_minutes=}, {obsidian_minutes=}, {curr_state.ore=}, {curr_state.clay=}, {curr_state.obsidian=}, {curr_state.geode=}, {curr_state.robots=}, {ore_cost=}, {clay_cost=}, {obsidian_cost=}, {robot_to_buy=}')


#             new_state = curr_state.copy_state()
#             new_state.minutes_left = curr_state.minutes_left - minutes_needed

#             new_state.ore += (new_state.robots[0] * minutes_needed)
#             new_state.clay += (new_state.robots[1] * minutes_needed)
#             new_state.obsidian += (new_state.robots[2] * minutes_needed)
#             new_state.geode += (new_state.robots[3] * minutes_needed)

#             new_state.ore -= ore_cost
#             new_state.clay -= clay_cost
#             new_state.obsidian -= obsidian_cost

#             new_state.robots[robot_to_buy] += 1

#             max_geodes = max(max_geodes, new_state.geode)
#             queue.append(new_state)

#     quality_level = plan_num * max_geodes
#     total_quality_level += quality_level
#     print_green(f'Plan {plan_num}, {max_geodes=}, Quality level: {quality_level}')
# print_blue(f'{total_quality_level=}')



















