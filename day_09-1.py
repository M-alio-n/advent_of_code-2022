#region: imports
import numpy as np
import time
import copy
start = time.time()
#endregion: imports
#region: additional functions
def mov_head(head,instruction):
    if instruction == 'R':
        head = (head[0],head[1]+1)
    elif instruction == 'L':
        head = (head[0],head[1]-1)
    elif instruction == 'D':
        head = (head[0]-1,head[1])
    elif instruction == 'U':
        head = (head[0]+1,head[1])
    return head

def follow(head,tail):
    if any([abs(head[idx]-tail[idx])==2 for idx in range(2)]) and any([abs(head[idx]-tail[idx])==1 for idx in range(2)]):
        tail = (tail[0]+1*np.sign(head[0]-tail[0]),tail[1]+1*np.sign(head[1]-tail[1]))
    elif abs(head[0]-tail[0])==2:
        tail = (int(tail[0]+((head[0]-tail[0])/2)), tail[1])
    elif abs(head[1]-tail[1])==2:
        tail = (tail[0],int(tail[1]+((head[1]-tail[1])/2)))
    return tail

def move_rope(rope_len,input):
    positions = [(0,0)]*rope_len
    visited = {positions[-1]}
    for line in input:
        for _ in range(int(line.split(' ')[1])):
            positions[0] = mov_head(positions[0],line.split(' ')[0])
            for idx in range(1,rope_len):
                tmp = follow(positions[idx-1],positions[idx])
                if tmp == positions[idx]:
                    break
                positions[idx] = tmp
            visited.add(positions[-1])
    return len(visited)
#endregion: addtional functions
#region: load input
input = open('09').read().split('\n')
#endregion: input loaded
#region: part 1
print(move_rope(2,input))
#endregion: part 1
#region: part 2
print(move_rope(10,input))
#endregion: part 2
print(time.time()-start)