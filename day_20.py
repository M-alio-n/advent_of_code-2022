#region: imports
import time
import math
#endregion: imports
#region: additional functions
start = time.time()
def find_curr_idx(idx):
    for count,item in enumerate(list):
        if item[1] == idx:
            return count

def move_item(curr_idx):
    mov_by = list[curr_idx][0]
    item = list.pop(curr_idx)
    if curr_idx+mov_by == 0:
        list.append(item)
    elif curr_idx+mov_by > len(list):
        list.insert((curr_idx+mov_by)%len(list),item)
    elif curr_idx+mov_by < 0:
        list.insert((curr_idx+mov_by)%len(list),item)
    else:
        list.insert(curr_idx+mov_by,item)

def find_coords():
    for count,item in enumerate(list):
        if item[0] == 0:
            break
    
    coords = [list[(count+1000*(multi+1))%len(list)][0] for multi in range(3)]
    print(f'Solution for part 1: {sum(coords)}')
    return

def print_list():
    print([item[0] for item in list])
    return
#endregion: addtional functions
#region: load input
file = '20'
input = open(file).read().split('\n')
list = []
maxi = 0
for count,line in enumerate(input):
    list.append((int(line),count))
    if int(line) > maxi:
        maxi = int(line)
#endregion: input loaded
#region: part 1
for idx in range(len(list)):
    curr_idx = find_curr_idx(idx)
    move_item(curr_idx)
find_coords()
part1 = time.time()
#endregion: part 1
#region: part 
input = open(file).read().split('\n')
list = []
maxi = 0
for count,line in enumerate(input):
    list.append((int(int(line)*811589153),count))
    if int(line) > maxi:
        maxi = int(line)

for _ in range(10):
    for idx in range(len(list)):
        curr_idx = find_curr_idx(idx)
        move_item(curr_idx)
find_coords()

part2 = time.time()
print(f'Total time: {part2-start}, part 1 time: {part1-start}, part 2 time: {part2-part1}')
#endregion: part 2