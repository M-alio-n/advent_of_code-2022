#region: imports
import time
#endregion: imports
#region: additional functions
start = time.time()
def compare(left,right):
    #flag: -1 wrong, 0 undecided, 1 right order
    flag = 0
    if type(left) == type(list()) and type(right) == type(list()):
        #both inputs are lists
        idx = 0
        while flag == 0:
            if idx == len(left) and idx == len(right):
                flag = 0
                break
            elif idx == len(left):
                flag = 1
                break
            elif idx == len(right):
                flag = -1
                break
            flag = compare(left[idx],right[idx])
            idx += 1
    elif type(left) == type(int()) and type(right) == type(int()):
        #both inputs are integers
        if left < right:
            flag = 1
        elif left > right:
            flag = -1
        else:
            flag = 0
    else:
        #mixed inputs
        if type(left) == type(int()) and type(right) == type(list()):
            flag = compare([left],right)
        elif type(left) == type(list()) and type(right) == type(int()):
            flag = compare(left,[right])
    return flag
#endregion: addtional functions
#region: load input
input = open('13').read().split('\n\n')
packets = []
for pair in input:
    for packet in pair.split('\n'):
        packets.append(eval(packet))
#endregion: input loaded
#region: part 1

result = 0
for idx in range(int(len(packets)/2)):
    flag = compare(packets[idx*2],packets[(idx*2)+1])
    if flag == 1:
        result += idx+1
print(f'solution 1: {result}')
part1 = time.time()
#endregion: part 1
#region: part 2
div_pack_1 = [[2]]
div_pack_2 = [[6]]

# how many are smaller than div_pack_1
pos_1 = 1 # +1 because of zero-indexing
for idx in range(len(packets)):
    flag = compare(div_pack_1,packets[idx])
    if flag == -1:
        pos_1 += 1
# how many are smaller than div_pack_2
pos_2 = 2 # +2 because of zero-indexing and div_pack_1
for idx in range(len(packets)):
    flag = compare(div_pack_2,packets[idx])
    if flag == -1:
        pos_2 += 1
print(f'solution 2: {pos_1*pos_2}')
part2 = time.time()
print(f'Total time: {part2-start}, part 1 time: {part1-start}, part 2 time: {part2-part1}')
#endregion: part 2