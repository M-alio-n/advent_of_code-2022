from copy import deepcopy as dc
import time
#region: additional functions
start = time.time()
def play_the_game(time):
    global robot_configs, max_geodes
    # each game is a tuple of two tuples ((robots),(resources)) and is stored in a set
    new_games = set([((1,0,0,0),(0,0,0,0))])
    # keep track of the time
    clock = 1
    # run until time == 23, in the final round, no more robots need to be build, they won't get ready
    while clock < time:
        current_games = dc(new_games)
        new_games = set()
        for game in current_games:
            for robo_idx,price in enumerate(prices):
                if all([game[1][idx] >= price[idx] for idx in range(4)]):

                    # purchase is allowed
                    res_game = (tuple([game[0][idx] if idx != robo_idx else game[0][idx]+1 for idx in range(4)]),
                        tuple([game[1][idx]-price[idx]+game[0][idx] for idx in range(4)]))
                    if not res_game[0] in robot_configs or clock == robot_configs[res_game[0]]:
                        robot_configs[res_game[0]] = clock
                        new_games.add(res_game)
                        if res_game[1][3] > max_geodes:
                            max_geodes = res_game[1][3]
            res_game = (game[0],tuple([game[0][idx]+game[1][idx] for idx in range(4)]))
            new_games.add(res_game)
            if res_game[1][3] > max_geodes:
                max_geodes = res_game[1][3]
        print(f'After minute {clock}, there are {len(new_games)} games and a total of {len(robot_configs)} robot configurations were realized.')
        clock += 1
    # the last time step is only increasing the resources, robots won't get ready
    for game in new_games:
        res_game = (game[0],tuple([game[0][idx]+game[1][idx] for idx in range(4)]))
        if res_game[1][3] > max_geodes:
            max_geodes = res_game[1][3]
    return


def add_tuple(tup1, tup2):
    return tuple([tup1[idx]+tup2[idx] for idx in range(len(tup1))])
#endregion: additional functions
#region: load input
input = open('19').read().split('\n')
#endregion: input loaded
#region: part 1
levels = []
for blueprint in input:
    # All costs are noted as list of lists with prices in the order of [ore, clay, obsidian, geodes]
    prices = ((int(blueprint.split('costs ')[1].split(' ')[0]),0,0,0), (int(blueprint.split('costs ')[2].split(' ')[0]),0,0,0),
            (int(blueprint.split('costs ')[3].split(' ')[0]),int(blueprint.split('costs ')[3].split(' ')[3]),0,0),(int(blueprint.split('costs ')[4].split(' ')[0]),0,int(blueprint.split('costs ')[4].split(' ')[3]),0))
    # keep track of the highest scored geodes
    max_geodes = 0
    # keep track of the realized robots configurations
    robot_configs = {}
    play_the_game(24)
    levels.append(max_geodes)
print(f'Solution for part 1: {sum([level*(count+1) for count,level in enumerate(levels)])}')

part1 = time.time()
print(f'{part1-start}')
print()
#endregion: part 1
#region: part 2
solution = 1
for blueprint in input[0:3]:
    # All costs are noted as list of lists with prices in the order of [ore, clay, obsidian, geodes]
    prices = ((int(blueprint.split('costs ')[1].split(' ')[0]),0,0,0), (int(blueprint.split('costs ')[2].split(' ')[0]),0,0,0),
            (int(blueprint.split('costs ')[3].split(' ')[0]),int(blueprint.split('costs ')[3].split(' ')[3]),0,0),(int(blueprint.split('costs ')[4].split(' ')[0]),0,int(blueprint.split('costs ')[4].split(' ')[3]),0))
    # keep track of the highest scored geodes
    max_geodes = 0
    # keep track of the realized robots configurations
    robot_configs = {}
    play_the_game(32)
    solution *= max_geodes
print(f'Solution for part 1: {solution}')
print(f'{time.time()-part1}')
#endregion: part 2