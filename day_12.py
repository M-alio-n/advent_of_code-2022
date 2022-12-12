#region: imports
import copy
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
#endregion: imports
#region: additional functions
def backstep(inpt,count,part2 = False):
    if distances[start[0]][start[1]] != -1:
        # a solution was found
        if distances[start[0]][start[1]] <= count:
            #the found solution is faster or as fast
            return
    if part2:
        if shortest_way <= count:
            #the found solution is faster or as fast
            return
    steps=[(inpt[0],inpt[1]+1),(inpt[0],inpt[1]-1),(inpt[0]-1,inpt[1]),(inpt[0]+1,inpt[1])]

    for step in steps:
        if 0 > step[0] or step[0] >= len(map) or 0 > step[1] or step[1] >= len(map[1]):
            continue
        if ord(map[step[0]][step[1]]) - ord(map[inpt[0]][inpt[1]]) >= -1:
            #allowed step
            if distances[step[0]][step[1]] == -1 or distances[step[0]][step[1]] > count:
                distances[step[0]][step[1]] = count
                #[print(''.join(str(distances[idx]))) for idx in range(len(map))]
                backstep(step,count+1,part2)



#endregion: addtional functions
#region: load input
map = []
for line in open('12').readlines():
    map.append(list(line.strip()))
distances = []
for _ in range(len(map)):
    distances.append([-1]*len(map[0]))

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
# numbermap = []
# for idx1 in range(len(map)):
#     numbermap.append([ord(map[idx1][idx2])-ord('a') for idx2 in range(len(map[idx1]))])
# numbermap = np.array(numbermap)
# imgplot = plt.imshow(numbermap)
# plt.show()

distances[end[0]][end[1]] = 0
backup_dist = copy.deepcopy(distances)
#endregion: input loaded
#region: part 1
backstep(end,1)
print(distances[start[0]][start[1]])
#endregion: part 1
#region: part 2
dists = []
not_visited = []
for idx1 in range(len(map)):
    for idx2 in range(len(map)):
        if map[idx1][idx2] == 'a':
            if distances[idx1][idx2] > -1:
                dists.append(distances[idx1][idx2])
            else:
                not_visited.append((idx1,idx2))
###### WORKING BUT SLOW SOLUTION
shortest_way = min(dists)
for count,start in enumerate(not_visited):
    distances = copy.deepcopy(backup_dist)
    backstep(end,1,True)
    print(f'Checked {count} of {len(not_visited)}')
    if shortest_way >= distances[start[0]][start[1]] and distances[start[0]][start[1]] > -1:
        shortest_way = distances[start[0]][start[1]]
        short = (start[0],start[1])
print(shortest_way)
#endregion: part 2