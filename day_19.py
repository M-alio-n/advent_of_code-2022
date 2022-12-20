#region: imports
import time
import numpy as np
import copy
#endregion: imports
#region: additional functions
start = time.time()
def play_the_game(resources,robots):
    cutoff = 2
    tmp_games = [[resources,robots]] # every game is a list of [resources, robots]
    max_geodes = 0
    time = 1
    while time <= 24:
        cutoff_flag = 0
        games = []
        for game in tmp_games:
            # do some action(s)
            list = possible_actions(*game)
            for new_game in list:
                # get the new resources
                new_game[0] = new_game[0] + game[1]
                # get the new robots
                new_robos = np.array([0,0,0,0])
                for count,robot in enumerate(prices):
                    new_robos[count] = new_game[2].count(robot)
                new_game[1] = new_game[1] + new_robos
                ### Lets clean a little
                # once two of the cheap robots could have been built, kick out all games that did not build a single robot
                if 24-time == prices['ObR'][1]:
                    if new_game[1][1] > 0:
                        games.append(new_game[0:2])
                elif 24-time == prices['GeR'][2]:
                    if new_game[1][2] > 0:
                        games.append(new_game[0:2])
                else:
                    games.append(new_game[0:2])
                
                if new_game[0][3] > max_geodes:
                    max_geodes = new_game[0][3]
        if cutoff_flag == 1:
            cutoff += 1
        tmp_games = games
        print(len(tmp_games))
        time += 1

    return max_geodes

def possible_actions(resources,robots):
    action_lists = [[resources,robots,[]]] # each entry is a list of [remaining ressources, original robots, open geodes, new robots]
    final_action_lists = [[resources,robots,[]]]
    # Can we build robots?
    change_flag = 1
    while change_flag:
        change_flag = 0
        tmp_action_list = []
        for action in action_lists:
            for robot in prices:
                if all(resources >= prices[robot]+price_of_list(action[2])):
                    # we have enough resources to additionally buy this type of robot
                    tmp = copy.deepcopy(action)
                    tmp[0] -= price_of_list([robot])
                    tmp[2].append(robot)
                    tmp_action_list.append(tmp)
                    final_action_lists.append(tmp)
                    change_flag = 1
        action_lists = tmp_action_list
    return final_action_lists
    
def price_of_list(list):
    price = np.array([0,0,0,0])
    for item in list:
        price += prices[item]
    return price
#endregion: addtional functions
#region: load input
input = open('19t').read().split('\n')
#endregion: input loaded
#region: part 1
levels = []
for blueprint in input:
    # All costs are noted as array of [ore, clay, obsidian, geodes]
    prices = {
            'OrR': np.array([int(blueprint.split('costs ')[1].split(' ')[0]),0,0,0]),
            'ClR': np.array([int(blueprint.split('costs ')[2].split(' ')[0]),0,0,0]),
            'ObR': np.array([int(blueprint.split('costs ')[3].split(' ')[0]),int(blueprint.split('costs ')[3].split(' ')[3]),0,0]),
            'GeR': np.array([int(blueprint.split('costs ')[4].split(' ')[0]),0,int(blueprint.split('costs ')[4].split(' ')[3]),0])
        }
    # an array of the robots in order [OrR, ClR, ObR, GeR]
    robots = np.array([1,0,0,0])
    resources = np.array([0,0,0,0])
    levels.append(play_the_game(resources,robots))
print(f'Solution for part 1: {sum([level*(count+1) for count,level in enumerate(levels)])}')

part1 = time.time()
print(f'{part1-start}')
#endregion: part 1
#region: part 2
part2 = time.time()
print(f'Total time: {part2-start}, part 1 time: {part1-start}, part 2 time: {part2-part1}')
#endregion: part 2