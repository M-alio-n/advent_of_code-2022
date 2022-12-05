#region: imports
import copy
#endregion: imports
#region: additional functions
def move_crates(instruction,stacks):
    for _ in range(instruction[0]):
        stacks[instruction[2]-1].append(stacks[instruction[1]-1].pop())
    return stacks

def move_crates_2(instruction,stacks):
    tmp_stack = []
    for _ in range(instruction[0]):
        tmp_stack.append(stacks[instruction[1]-1].pop())
    tmp_stack.reverse()
    stacks[instruction[2]-1]+=tmp_stack
    return stacks

#endregion: addtional functions
#region: load input
stacks = []
moves = []
count = 1
for l in open('5').readlines():
    if l != '\n' and count >= 1 :
        crates = list(l)[1::4]
        if count == 1:
            for _ in range(len(crates)):
                stacks.append([])
        for idx,crate in enumerate(crates):
            stacks[idx].append(crate)
        count += 1
    elif l == '\n':
        count = -1
        for idx in range(len(stacks)):
            stacks[idx].pop()
            stacks[idx] = list((''.join(stacks[idx])).strip())
            stacks[idx].reverse()
    else:
        moves.append([int(char) for char in l.split(' ')[1::2]])

#endregion: input loaded

#region: part 1
stacks_1 = copy.deepcopy(stacks)
for move in moves:
    stacks_1 = move_crates(move,stacks_1)
print(''.join([stack.pop() for stack in stacks_1]))
#endregion: part 1
#region: part 2
for move in moves:
    stacks = move_crates_2(move,stacks)
print(''.join([stack.pop() for stack in stacks]))
#endregion: part 2