#region: imports
import time
import numpy as np
#endregion: imports
#region: additional functions
start = time.time()

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
    max_value = 0
    for combination in tmp_combinations:
        if combination[2] > max_value:
            max_value = combination[2]
    return (max_value,tmp_combinations)

#endregion: addtional functions
#region: load input
input = open('16t').read().split('\n')
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

best_value, combinations = best_combination(30)
print(f'Solution for part 1: {best_value}')
part1 = time.time()
#endregion: part 1
#region: part 2

'''This solution does not work for the testinput, because best_combination only returns
combinations that utilize the complete time that is available. For the optimal solution
of the testinput both, the elephant and I, would just work 11 minutes of the 26.
I might include these cases, though it will increase the already long runtime...
'''
part2 = time.time()
_, combinations = best_combination(26)
best_value = 0
for count1, combination_1 in enumerate(combinations):
    print(f'Checked {count1} of {len(combinations)} current solution: {best_value}')
    for count2,combination_2 in enumerate(combinations):
        if not any([valve in combination_2[0] for valve in combination_1[0][1::]]):
            if combination_1[2]+combination_2[2]> best_value:
                best_value = combination_1[2]+combination_2[2]
print(f'Solution for part 2: {best_value}')
print(f'Total time: {part2-start}, part 1 time: {part1-start}, part 2 time: {part2-part1}')
#endregion: part 2