#region: imports
import time
#endregion: imports
#region: additional functions
start_time = time.time()
def move(pos,instruction,part):
    global view_idx
    views = [(0,1),(1,0),(0,-1),(-1,0)]
    view_idx = 0
    final = 0
    while len(instruction) > 0:
        # get the next movement and crop the instruction
        if instruction.find('R') != -1 or instruction.find('L') != -1:
            str_idx = min([found for found in [instruction.find('R'), instruction.find('L')] if found > -1])
            steps = int(instruction[0:str_idx])
            rotate = instruction[str_idx]
            instruction = instruction[str_idx+1:]
        else:
            steps = int(instruction)
            instruction = ''
            final = 1
        # make individual steps
        for _ in range(steps):
            test_pos = (pos[0]+views[view_idx][0],pos[1]+views[view_idx][1])
            # check if the next position leads to a warp
            if part == 2:
                # three special cases, where it matters from which side you approach a field
                if test_pos == (99,49):
                    if pos == (100,49):
                        test_pos = (99,50)
                    elif pos == (99,50):
                        test_pos = (100,49)
                elif test_pos == (150,50):
                    if pos == (149,50):
                        test_pos = (150,49)
                    elif pos == (150,49):
                        test_pos = (149,50)
                elif test_pos == (50,100):
                    if pos == (49,100):
                        test_pos = (50,99)
                    elif pos == (50,99):
                        test_pos = (49,100)
                elif test_pos in warps:
                    test_pos = warps[test_pos]
            else:
                if test_pos in warps:
                    test_pos = warps[test_pos]
            # test if the next position is a rock, if yes stop the movement
            if test_pos in rocks:
                break
            # check if the side of the cube was switched and adjust the facing (in part 2)
            if part == 2:
                view_idx = find_face(find_side(pos),find_side(test_pos))
            pos = test_pos
        # rotate if it was not the last step
        if not final:
            if rotate == 'R':
                view_idx = (view_idx+1)%4
            elif rotate == 'L':
                view_idx = (view_idx-1)%4
    return (pos[0],pos[1],view_idx)
    
def find_side(pos):
    if 0 <= pos[0] <= 49 and 50 <= pos[1] <= 99:
        return 1
    elif 50 <= pos[0] <= 99 and 50 <= pos[1] <= 99:
        return 2
    elif 100 <= pos[0] <= 149 and 50 <= pos[1] <= 99:
        return 6
    elif 150 <= pos[0] <= 199 and 0 <= pos[1] <= 49:
        return 5
    elif 100 <= pos[0] <= 149 and 0 <= pos[1] <= 49:
        return 3
    elif 0 <= pos[0] <= 49 and 100 <= pos[1] <= 149:
        return 4

def find_face(old, new):
    global view_idx
    if old == new:
        return view_idx
    indexes = {(1,2): 1,
        (1,3): 0,
        (1,4): 0,
        (1,5): 0,
        (2,1): 3,
        (2,3): 1,
        (2,4): 3,
        (2,6): 1,
        (3,1): 0,
        (3,2): 0,
        (3,5): 1,
        (3,6): 0,
        (4,1): 2,
        (4,2): 2,
        (4,5): 3,
        (4,6): 2,
        (5,1): 1,
        (5,3): 3,
        (5,4): 1,
        (5,6): 3,
        (6,2): 3,
        (6,3): 2,
        (6,4): 2,
        (6,5): 2}
    return indexes[(old,new)]
#endregion: addtional functions
#region: load input
input = open('22').read().split('\n')
# create a ' ' padded field of strings
field = []
max = 0
for line in input:
    if line.find('R') != -1:
        instruction = line
    else:
        field.append(' '+line+' ')
        if len(field[-1]) > max:
            max = len(field[-1])
del field[-1]
field.append(''.join([' ' for _ in range(len(field[0]))]))
field.insert(0,''.join([' ' for _ in range(len(field[0]))]))
for idx,line in enumerate(field):
    if len(line) < max:
        field[idx] = line+''.join([' ' for _ in range(max-len(line))])
# field created
# now scan for rocks and warps by line
rocks = set()
warps = {}
start = []
for line_idx,line in enumerate(field):
    outside = 1
    for column_idx,char in enumerate(line):
        if outside and char != ' ':
            outside = 0
            tmp = (line_idx-1,column_idx-2)
        elif outside == 0 and char == ' ':
            outside = 1
            warps[tmp] = (line_idx-1,column_idx-2)
            warps[(line_idx-1,column_idx-1)] = (tmp[0], tmp[1]+1)
        if char == '#':
            rocks.add((line_idx-1,column_idx-1))
        if len(start) == 0 and char == '.':
            start = (line_idx-1,column_idx-1)
# now scan for warps by column
for column_idx in range(len(field[0])):
    outside = 1
    for line_idx in range(len(field)):
        char = field[line_idx][column_idx]
        if outside and char != ' ':
            outside = 0
            tmp = (line_idx-2,column_idx-1)
        elif outside == 0 and char == ' ':
            outside = 1
            warps[tmp] = (line_idx-2,column_idx-1)
            warps[(line_idx-1,column_idx-1)] = (tmp[0]+1, tmp[1])
#endregion: input loaded
#region: part 1
pos = (start[0], start[1])
pos = move(pos,instruction,1)
print((pos[0]+1)*1000+(pos[1]+1)*4+pos[2])
part1 = time.time()
#endregion: part 1
#region: part 2
# adjust the warps manually, specifically for MY input shape ([[,1,2],[,3,],[4,5,],[6,,]])
warps={}
for ind in range(50,100):
    warps[(ind,100)] = (49,ind+50)
    warps[(50,ind+50)] = (ind,99)
for ind in range(50):
    warps[(ind,150)] = (149-ind,99)
    warps[(149-ind,100)] = (ind,149)
for ind in range(100,150):
    warps[(-1,ind)] = (199,ind-100)
    warps[(200,ind-100)] = (0,ind)
for ind in range(50,100):
    warps[(150,ind)] = (100+ind,49)
    warps[(100+ind,50)] = (149,ind)
for ind in range(50,100):
    warps[(ind,49)] = (100,ind-50)
    warps[(99,ind-50)] = (ind,50)
for ind in range(50):
    warps[(ind,49)] = (149-ind,0)
    warps[(149-ind,-1)] = (ind,50)
for ind in range(50,100):
    warps[(-1,ind)] = (ind+100,0)
    warps[(ind+100,-1)] = (0,ind)
pos = (start[0], start[1])
pos = move(pos,instruction,2)
print((pos[0]+1)*1000+(pos[1]+1)*4+pos[2])
part2 = time.time()
print(f'Total time: {part2-start_time}, part 1 time: {part1-start_time}, part 2 time: {part2-part1}')
#endregion: part 2