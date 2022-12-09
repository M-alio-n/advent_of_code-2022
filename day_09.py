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

def move_rope(rope_len,input):
    positions = np.zeros((2,rope_len),dtype=int)
    visited = {str(positions[:,-1])}
    for line in input:
        for _ in range(int(line.split(' ')[1])):
            positions[:,0] = mov_head(positions[:,0],line.split(' ')[0])
            for idx in range(1,rope_len):
                ## IT DOES NOT WORK WITH THIS BREAK CONDITION....WHY DOES IT RETURN TRUE?!
                #if np.array_equal(follow(positions[:,idx-1],positions[:,idx]),positions[:,idx]):
                #    break
                positions[:,idx] = follow(positions[:,idx-1],positions[:,idx])
            visited.add(str(positions[:,-1]))
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