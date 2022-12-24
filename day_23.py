#region: imports
import time
#endregion: imports
#region: additional functions
start = time.time()
def move_elfs(elfs,cycle):
    change_flag = 0
    propositions = []
    for elf in elfs:
        # list with the directions
        directions = [[(elf[0]-1,elf[1]-1),(elf[0]-1,elf[1]),(elf[0]-1,elf[1]+1)],#north
            [(elf[0]+1,elf[1]-1),(elf[0]+1,elf[1]),(elf[0]+1,elf[1]+1)],#south
            [(elf[0]-1,elf[1]-1),(elf[0],elf[1]-1),(elf[0]+1,elf[1]-1)],#west
            [(elf[0]-1,elf[1]+1),(elf[0],elf[1]+1),(elf[0]+1,elf[1]+1)]]#east

        if not any([direction in elfs for direction_list in directions for direction in direction_list]):
            # No elf in adjacent spots
            propositions.append(elf)
            continue
        else:
            flag = 1
            for dir_cycler in range(cycle,cycle+4):
                dir_idx = dir_cycler%4
                if not any([direction in elfs for direction in directions[dir_idx]]):
                    propositions.append(directions[dir_idx][1])
                    flag = 0
                    break
            if flag == 1:
                propositions.append(elf)
    for idx,prop in enumerate(propositions):
        if propositions.count(prop) > 1:
            continue
        else:
            if not elfs[idx] == prop:
                elfs[idx] = prop
                change_flag = 1
    return (elfs,change_flag)

def count_soil(elfs):
    min0 = 100000
    max0 = 0
    min1 = 100000
    max1 = 0
    for elf in elfs:
        if elf[0] > max0:
            max0 = elf[0]
        if elf[0] < min0:
            min0 = elf[0]
        if elf[1] > max1:
            max1 = elf[1]
        if elf[1] < min1:
            min1 = elf[1]
    return (max0-min0+1)*(max1-min1+1) - len(elfs)
#endregion: addtional functions
#region: load input
elfs = []
for count,line in enumerate(open('23')):
    if count == 0:
        [elfs.append((count,idx)) for idx,char in enumerate(line.strip()) if char == '#']
    else:
        [elfs.append((count,idx)) for idx,char in enumerate(line.strip()) if char == '#']
#endregion: input loaded
#region: part 1 & part 2
round = 0
change_flag = 1
while change_flag:
    elfs, change_flag = move_elfs(elfs,round)
    print(f'Round {round}')
    #print_field(elfs)
    round += 1
    if round == 10:
        sol1 = count_soil(elfs)
        print(f'Solution for part 1: {sol1}')
        part1 = time.time()
sol2 = round
print(f'Solution for part 2: {sol2}')
part2 = time.time()
print(f'Total time: {part2-start}, part 1 time: {part1-start}, part 2 time: {part2-part1}')
#endregion: part 1 & part 2