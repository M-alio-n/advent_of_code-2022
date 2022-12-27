#region: imports
import time
import numpy  as np
#endregion: imports
#region: additional functions
start_time = time.time()
def test_ways(storms,start,goal,minute):
    movs = [(0,1),(1,0),(0,-1),(-1,0),(0,0)]
    pos_s = set([start])
    while True:
        minute += 1
        storms = mov_storms(storms)
        storm_pos = det_storm_pos(storms)
        next_pos = set()
        for pos in pos_s:
            for new_pos in [(pos[0]+mov[0], pos[1]+mov[1]) for mov in movs]:
                if not new_pos in storm_pos and not new_pos in warps and  0 <= new_pos[0] <= line_idx:
                    next_pos.add(new_pos)
                    if new_pos == goal:
                        return (minute,storms)
        pos_s = next_pos



def mov_storms(old_storms):
    storms = set()
    for storm in old_storms:
        if not (storm[0]+storm[2], storm[1]+storm[3]) in warps:
            storms.add((storm[0]+storm[2], storm[1]+storm[3], storm[2], storm[3]))
        else:
            storms.add((warps[(storm[0]+storm[2],storm[1]+storm[3])][0], warps[(storm[0]+storm[2],storm[1]+storm[3])][1], storm[2], storm[3]))
    return storms

def det_storm_pos(storms):
    pos = set()
    for storm in storms:
        pos.add((storm[0],storm[1]))
    return pos
#endregion: addtional functions
#region: load input
storms = set()
warps = {}
for line_idx,line in enumerate(open('24').read().split('\n')):
    if line_idx == 0 or line[0:2] == '##':
        continue
    for char_idx,char in enumerate(line):
        if char_idx > 0 and char == '#':
            warps[(line_idx, char_idx)] = (line_idx, 1)
            warps[(line_idx, 0)] = (line_idx, char_idx-1)
        elif char == '>':
            storms.add((line_idx,char_idx,0,1))
        elif char == 'v':
            storms.add((line_idx,char_idx,1,0))
        elif char == '<':
            storms.add((line_idx,char_idx,0,-1))
        elif char == '^':
            storms.add((line_idx,char_idx,-1,0))
for char_idx in range(char_idx+1):
    warps[(0,char_idx)] = (line_idx-1, char_idx)
    warps[(line_idx,char_idx)] = (1, char_idx)
start = (0,1)
goal = (line_idx,char_idx-1)
del warps[start]
del warps[goal]
#endregion: input loaded
#region: part 1
minute, storms = test_ways(storms,start,goal,0)
print(f'Solution 1: {minute}')
part1 = time.time()
#endregion: part 1
#region: part 2
minute, storms = test_ways(storms,goal,start,minute)
minute, storms = test_ways(storms,start,goal,minute)
print(f'Solution 2: {minute}')
part2 = time.time()
print(f'Total time: {part2-start_time}, part 1 time: {part1-start_time}, part 2 time: {part2-part1}')
#endregion: part 2