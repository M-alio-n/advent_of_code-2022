#region: imports
import copy
#endregion: imports
#region: additional functions
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
    if flag == -1:
        #start sorting pairs for second part
        tmp = copy.deepcopy(packets[(idx*2)+1])
        packets[idx*2+1] = copy.deepcopy(packets[(idx*2)])
        packets[idx*2] = copy.deepcopy(tmp)
print(result)
#endregion: part 1
#region: part 2
div_pack_1 = [[2]]
div_pack_2 = [[6]]
packets = [div_pack_1] + packets
packets = [div_pack_2] + packets

something_changed = 1
while something_changed:
    something_changed = 0
    for idx in range(len(packets)-1):
        flag = compare(packets[idx],packets[idx+1])
        if flag == -1:
            tmp = copy.deepcopy(packets[idx+1])
            packets[idx+1] = copy.deepcopy(packets[idx])
            packets[idx] = copy.deepcopy(tmp)
            something_changed = 1
            break

result = 1
for count,packet in enumerate(packets):
    if packet == div_pack_1:
        result *= count+1
    elif packet == div_pack_2:
        result *= count+1
print(result)
#endregion: part 2