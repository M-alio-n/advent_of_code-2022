#region: imports
import time
import numpy as np
#endregion: imports
#region: additional functions
start = time.time()
def isneighbour(a,b):
    idxs = [0,1,2]
    for idx in range(0,3):
        if a[idxs[idx]] == b[idxs[idx]] and a[idxs[idx-1]] == b[idxs[idx-1]] and (a[idxs[idx-2]] == b[idxs[idx-2]]+1 or a[idxs[idx-2]] == b[idxs[idx-2]]-1):
            return True
    return False

def extrude_shell(shells):
    global surface_count
    shells.append(set())
    for position in shells[-2]:
        for move in [[0,0,1],[0,1,0],[1,0,0]]:
            for sign in [-1,1]:
                new_position = np.array(position)+sign*np.array(move)
                if any(new_position < 0) or any(new_position > np.array([max0+1,max1+1,max2+1])):
                    # We are leaving the area of interest
                    continue
                elif full_grid[tuple(new_position)] == 1:
                    # We have moved into the lava body
                    surface_count += 1
                elif full_grid[tuple(new_position)] == 0:
                    # A new air cube that can be reached
                    full_grid[tuple(new_position)] = 2
                    shells[-1].add(tuple(new_position))
                elif full_grid[tuple(new_position)] == 2:
                    # A position already covered
                    continue
                else:
                    # This should not happen
                    print('Argh, what now?!')

    if len(shells[-1]) == 0:
        return
    else:
        extrude_shell(shells)
    return
#endregion: addtional functions
#region: load input
input = open('18').read().split('\n')
positions = []
max0 = 0
max1 = 0
max2 = 0
for line in input:
    #increase each index by 1 for part 2
    positions.append(tuple([int(val)+1 for val in line.split(',')]))
    if positions[-1][0] > max0:
        max0 = positions[-1][0]
    if positions[-1][1] > max1:
        max1 = positions[-1][1]
    if positions[-1][2] > max2:
        max2 = positions[-1][2]
#endregion: input loaded
#region: part 1
total_faces = 6*len(positions)
for count, cube in enumerate(positions):
    for cube_2 in positions[count+1::]:
        if isneighbour(cube, cube_2):
            total_faces -= 2
print(total_faces)
part1 = time.time()
#endregion: part 1
#region: part 2
full_grid = np.zeros((max0+2,max1+2,max2+2),dtype=int)
for position in positions:
    full_grid[position] = 1
# manually create the first shell (stupid)
shells = []
shells.append(set())
for idx0 in [0,max0+1]:
    for idx1 in range(max1+2):
        for idx2 in range(max2+2):
            shells[0].add((idx0,idx1,idx2))
            full_grid[(idx0,idx1,idx2)] = 2
for idx1 in [0,max1+1]:
    for idx0 in range(max0+2):
        for idx2 in range(max2+2):
            shells[0].add((idx0,idx1,idx2))
            full_grid[(idx0,idx1,idx2)] = 2
for idx2 in [0,max2+1]:
    for idx0 in range(max0+2):
        for idx1 in range(max1+2):
            shells[0].add((idx0,idx1,idx2))
            full_grid[(idx0,idx1,idx2)] = 2
surface_count = 0
extrude_shell(shells)
print(surface_count)
part2 = time.time()
print(f'Total time: {part2-start}, part 1 time: {part1-start}, part 2 time: {part2-part1}')
#endregion: part 2