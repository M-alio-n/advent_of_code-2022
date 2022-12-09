#region: imports
#endregion: imports
#region: additional functions
def prio(item):
    if item.isupper():
        prio = ord(item)-38
    else:
        prio = ord(item)-96
    return prio

def find_common_prio(rucksack):
    common = list(set(rucksack[0:len(rucksack)//2]).intersection(set(rucksack[len(rucksack)//2::])))[0]
    return prio(common)

def find_group_prio(groupsack):
    common = list(set.intersection(*[set(r) for r in groupsack]))[0]
    return prio(common)
#endregion: addtional functions
#region: load input
rucksacks = open('03', 'r').read().split()
#endregion: input loaded

#region: part 1
print(f'The sum of mispacked priorities is {sum(find_common_prio(r) for r in rucksacks)}.')
#endregion: part 1
#region: part 2
print(f'The sum of group badge priorities is {sum(find_group_prio(rucksacks[idx*3:idx*3+3]) for idx in range(0,len(rucksacks)//3))}.')
#endregion: part 2