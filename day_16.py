#region: imports
import time
import numpy as np
import functools
#endregion: imports
#region: additional functions
start = time.time()
def comparisson(a, b):
    if a[2] > b[2]:
        return 1
    elif a[2] < b[2]:
        return -1
    else:
        return 0

def fastest_way(origin,goal):
    ways = [[origin]]
    for way in ways:
        for next in valves[way[-1]][0]:
            if next in way:
                continue
            ways.append(way+[next])
        for way_2 in ways:
            if way_2[-1] == goal:
                return way_2

def expand_ways(ways,goal):
    for way in ways:
        for next in valves[way[-1]][0]:
            if next in way:
                continue
            ways.append(way+[next])
        for way_2 in ways:
            if way_2[-1] == goal:
                return way_2

def determine_value(actionlist):
    worth = 0
    for count,action in enumerate(actionlist):
        if action.startswith('open'):
            worth += (30-(count)) * valves[action[-2::]][1]
    return worth

def best_combination(time_limit):
    # the tuples descirbe: order of the opening, time it takes, value
    tmp_combinations = [([0],1,0)]
    max_value = 0
    combinations = []
    change_flag = 1
    while change_flag:
        combinations = []
        change_flag = 0
        for combination in tmp_combinations:
            combination_changed_flag = 0
            for idx,next in enumerate(useful_valves):
                if not idx in combination[0]:
                    if combination[1]+1+distances[combination[0][-1],idx] < time_limit:
                        # If this valve was not yet visited and the resulting time is below the time limit add it to the list
                        combinations.append((combination[0]+[idx], combination[1]+1+distances[combination[0][-1],idx], combination[2]+useful_capacities[idx]*(time_limit-(combination[1]+distances[combination[0][-1],idx]))))
                        change_flag = 1
                        combination_changed_flag = 1
                        if combinations[-1][2] > max_value:
                            max_value = combinations[-1][2]
        if change_flag:
            tmp_combinations = combinations
    return max_value

def all_combinations(time_limit):
    # the tuples descirbe: order of the opening, time it takes, value
    tmp_combinations = [([0],1,0)]
    final_combinations = tmp_combinations
    combinations = []
    change_flag = 1
    while change_flag:
        combinations = []
        change_flag = 0
        for combination in tmp_combinations:
            combination_changed_flag = 0
            for idx,next in enumerate(useful_valves):
                if not idx in combination[0]:
                    if combination[1]+1+distances[combination[0][-1],idx] < time_limit:
                        # If this valve was not yet visited and the resulting time is below the time limit add it to the list
                        combinations.append((combination[0]+[idx], combination[1]+1+distances[combination[0][-1],idx], combination[2]+useful_capacities[idx]*(time_limit-(combination[1]+distances[combination[0][-1],idx]))))
                        change_flag = 1
                        combination_changed_flag = 1
            if combination_changed_flag == 0:
                # There are no longer combinations building on this, but it may be the best, keep it!
                combinations.append(combination)
        if change_flag:
            tmp_combinations = combinations
            final_combinations = final_combinations+combinations
    max_value = 0
    for combination in tmp_combinations:
        if combination[2] > max_value:
            max_value = combination[2]
    return (max_value,final_combinations)

#endregion: addtional functions
#region: load input
input = open('16').read().split('\n')
valves = {}
useful_valves = ['AA']
useful_capacities = [0]
for line in input:
    valves[line[6:8]] = ([line.split(', ')[0][-2::]] +line.split(', ')[1::], int(line.split(';')[0].split('=')[1]))
    if int(line.split(';')[0].split('=')[1]) > 0:
        useful_valves.append(line[6:8])
        useful_capacities.append(int(line.split(';')[0].split('=')[1]))
#endregion: input loaded
#region: part 1
distances = np.zeros((len(useful_valves),len(useful_valves)),dtype=int)
for count,valve in enumerate(useful_valves):
    for count_2,valve_2 in enumerate(useful_valves):
        if valve == valve_2:
            continue
        distances[count,count_2] = len(fastest_way(valve,valve_2))-1

best_value = best_combination(30)
print(f'Solution for part 1: {best_value}')
part1 = time.time()
#endregion: part 1
#region: part 2
'''This solution does not work for the testinput, because best_combination only returns
combinations that utilize the complete time that is available. For the optimal solution
of the testinput both, the elephant and I, would just work 11 minutes of the 26.
I might include these cases, though it will increase the already long runtime...
'''
_, combinations = all_combinations(26)

combinations = sorted(combinations, key=functools.cmp_to_key(comparisson),reverse=True)
best_val = 0
first_hit_flag = 0
for count,comb_1 in enumerate(combinations):
    if first_hit_flag:
        if comb_1[2] < best_val/2:
            # once we have one correct hit, we don't need to go further down than to the half of this value
            break
    for comb_2 in combinations[count+1::]:
        if not any([valve in comb_2[0] for valve in comb_1[0][1::]]):
            # legal hit!
            if comb_2[2]+comb_1[2] > best_val:
                best_val = comb_2[2]+comb_1[2]
                first_hit_flag = 1
            if first_hit_flag:
                if comb_2[2] < best_val/2:
                    # once we have one correct hit, we don't need to go further down than to the half of this value
                    break
part2 = time.time()
print(f'Solution for part 2: {best_val}')
print(f'Total time: {part2-start}, part 1 time: {part1-start}, part 2 time: {part2-part1}')
#endregion: part 2