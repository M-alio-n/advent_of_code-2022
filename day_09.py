#region: imports
import numpy as np
#endregion: imports
#region: additional functions
def mov_head(head,instruction):
    if instruction == 'R':
        head += np.array([0, 1])
    elif instruction == 'L':
        head += np.array([0, -1])
    elif instruction == 'D':
        head += np.array([-1, 0])
    elif instruction == 'U':
        head += np.array([1, 0])
    return head

def follow(head,tail):
    if any(abs(head-tail)==2) and any(abs(head-tail)==1):
        tail += np.ones((2,),dtype=int)*np.sign(head-tail)
    elif any(abs(head-tail)==2):
        tail += ((head-tail)/2).astype('int')
    return tail
#endregion: addtional functions
#region: load input
input = open('09').read().split('\n')
#endregion: input loaded
#region: part 1
positions = np.zeros((2,2),dtype=int)
visited = {str(positions[::,-1])}
for line in input:
    for _ in range(int(line.split(' ')[1])):
        positions[::,0] = mov_head(positions[::,0],line.split(' ')[0])
        for idx in range(1,np.shape(positions)[1]):
            positions[::,idx] = follow(positions[::,idx-1],positions[::,idx])
        visited.add(str(positions[::,-1]))
print(len(visited))
#endregion: part 1
#region: part 2
positions = np.zeros((2,10),dtype=int)
visited = {str(positions[::,-1])}
for line in input:
    for _ in range(int(line.split(' ')[1])):
        positions[::,0] = mov_head(positions[::,0],line.split(' ')[0])
        for idx in range(1,np.shape(positions)[1]):
            positions[::,idx] = follow(positions[::,idx-1],positions[::,idx])
        visited.add(str(positions[::,-1]))
print(len(visited))
#endregion: part 2