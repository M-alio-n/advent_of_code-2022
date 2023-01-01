#region: imports
import heapq
import time

import numpy as np
import matplotlib.pyplot as plt
#endregion: imports
#region: additional functions
start_time = time.time()
def A_star(start,goal,blocks):
    movs = [(0,1),(1,0),(0,-1),(-1,0)]

    open_dict = {start:[0,None]}
    open_heap = [(0,start, None)]
    heapq.heapify(open_heap)
    closed_dict = {}
    
    while len(open_heap) > 0:
        check_point = heapq.heappop(open_heap)
        check_coords = check_point[1]
        del open_dict[check_coords]
        closed_dict[check_coords] = [check_point[0], check_point[2]]

        for child_coords in [(check_coords[0]+mov[0],check_coords[1]+mov[1]) for mov in movs]:
            if disallowed_step(child_coords,blocks,check_coords):
                # step is not allowed
                continue
            elif not child_coords in open_dict and not child_coords in closed_dict:
                # add the child to the open list
                heapq.heappush(open_heap, (priority(child_coords, check_coords, goal, closed_dict), child_coords, check_coords))
                open_dict[child_coords] = [priority(child_coords, check_coords,goal, closed_dict),check_coords]
            elif child_coords in open_dict and priority(child_coords, check_coords,goal, closed_dict) < open_dict[child_coords][0]:
                # update the existing entry (new priority, parent and distance)
                heapq.heappush(open_heap, (priority(child_coords, check_coords,goal, closed_dict),child_coords, check_coords))
                for idx,elem in enumerate(open_heap):
                    if elem[1] == child_coords:
                        del open_heap[idx]
                        break
                open_dict[child_coords] = [priority(child_coords, check_coords,goal, closed_dict), check_coords]
        if goal in closed_dict:
            return closed_dict
    
    # no solution found
    return {}

def disallowed_step(new_coordinates,blocks,parent_coords):
    global field_size
    if new_coordinates[0] < 0 or new_coordinates[1] < 0:
        # step out of the field
        return True
    elif new_coordinates[0] > field_size[0]-1 or new_coordinates[1] > field_size[1]-1:
        #step out of the field
        return True
    elif ord(blocks[new_coordinates[0]][new_coordinates[1]])-ord(blocks[parent_coords[0]][parent_coords[1]]) > 1:
        # step too steep
        return True
    else:
        return False

def priority(p1,parent,goal,closed_dict):
    return closed_dict[parent][0]+1

def man_dist(p1,p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

def trace_path(goal, closed):
    path = [goal]
    while closed[path[-1]][1]:
        path.append(closed[path[-1]][1])
    path.reverse()
    return path
#endregion: addtional functions
#region: load input
map = []
for line in open('12').readlines():
    map.append(list(line.strip()))

for idx1 in range(len(map)):
    if 'S' in map[idx1] or 'E' in map[idx1]:
        for idx2 in range(len(map[idx1])):
            if map[idx1][idx2] == 'S':
                start = (idx1,idx2)
            elif map[idx1][idx2] == 'E':
                end = (idx1,idx2)
            try:
                if type(start) is tuple and type(end) is tuple:
                    break
            except:
                continue

map[end[0]][end[1]] = 'z'
map[start[0]][start[1]] = 'a'

field_size = (len(map), len(map[0]))
#endregion: input loaded
#region: part 1
closed = A_star(start,end,map)
print(closed[end][0])

path = trace_path(end, closed)
np_map = np.zeros((len(map),len(map[0])))
for idx1 in range(len(map)):
    for idx2 in range(len(map[idx1])):
        np_map[idx1,idx2] = ord(map[idx1][idx2])-97
for coord in path:
    np_map[coord[0],coord[1]] = ord('z')-96
plt.imshow(np_map)
plt.show()

#endregion: part 1
#region: part 2
shortest_path = 1000
for idx1 in range(len(map)):
    for idx2 in range(len(map[idx1])):
        if map[idx1][idx2] == 'a':
            closed = A_star((idx1,idx2),end,map)
            if len(closed) > 0:
                if closed[end][0] < shortest_path:
                    shortest_path = closed[end][0]
print(shortest_path)
print(time.time()-start_time)
#endregion: part 2