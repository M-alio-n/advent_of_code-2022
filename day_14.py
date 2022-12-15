#region: imports
import time
import numpy as np
import copy
#endregion: imports
#region: additional functions
start = time.time()

def create_field(input):
    idx0 = [500]
    idx1 = [0]
    for line in input:
        for fields in line.split(' -> '):
            idx0.append(int(fields.split(',')[0]))
            idx1.append(int(fields.split(',')[1]))
    max_x = max(idx0)
    min_x = min(idx0)
    max_y = max(idx1)
    min_y = min(idx1)
    # prepare the field with two additional columns and one additional row
    row = np.array([['.']*(max_x-min_x+3)])
    field = copy.deepcopy(row)
    for _ in range(max_y-min_y+2):
        field = np.vstack((field,row))
    mod_x = -min_x+1
    field[0,500+mod_x] = '+'
    # paint the rocks
    for line in input:
        for count,fields in enumerate(line.split(' -> ')[:-1]):
            idx0_1 = int(fields.split(',')[0])+mod_x
            idx0_0 = int(fields.split(',')[1])
            idx1_1 = int((line.split(' -> ')[count+1]).split(',')[0])+mod_x
            idx1_0 = int((line.split(' -> ')[count+1]).split(',')[1])
            field[min([idx0_0,idx1_0]):max([idx0_0,idx1_0])+1,min([idx0_1,idx1_1]):max([idx0_1,idx1_1])+1] = '#'
    return (field,mod_x)

def print_field(field):
    for line in field:
        print(''.join(line))
    return

def sand_1(field):
    sand_count = 0
    while np.all(field[-1,:]=='.'):
        sand_count += 1
        sand_0 = 0
        sand_1 = 500+mod_x
        while field[sand_0,sand_1] != 'o':
            if field[sand_0+1,sand_1]=='.':
                sand_0 += 1
            elif field[sand_0+1,sand_1-1]=='.':
                sand_0 += 1
                sand_1 -= 1
            elif field[sand_0+1,sand_1+1]=='.':
                sand_0 += 1
                sand_1 += 1
            else:
                field[sand_0,sand_1] = 'o'
            if sand_0 == np.shape(field)[0]-1:
                #print_field(field)
                print(sand_count-1)
                return (field,sand_count)
    return (field,sand_count)

def sand_2(field,sand_count):
    column = np.transpose(np.array([['.']*np.shape(field)[0]]))
    column[-1,0] = '#'
    loc_mod_x=mod_x
    while field[0,500+loc_mod_x] == '+':
        sand_count += 1
        sand_0 = 0
        sand_1 = 500+loc_mod_x
        while field[sand_0,sand_1] != 'o':
            if sand_1+1 == np.shape(field)[1]:
                field = np.hstack((field,column))
            elif sand_1-1 < 0:
                field = np.hstack((column,field))
                loc_mod_x += 1
                sand_1 = sand_1+1
            if field[sand_0+1,sand_1]=='.':
                sand_0 += 1
            elif field[sand_0+1,sand_1-1]=='.':
                sand_0 += 1
                sand_1 -= 1
            elif field[sand_0+1,sand_1+1]=='.':
                sand_0 += 1
                sand_1 += 1
            else:
                field[sand_0,sand_1] = 'o'
        if field[0,500+mod_x] == 'o':
            print(sand_count-1)
            return field
    #print_field(field)
    print(sand_count-1)
    return field

#endregion: addtional functions
#region: load input
input = open('14').read().split('\n')
field,mod_x = create_field(input)
#endregion: input loaded
#region: part 1
field,sand_count = sand_1(field)
part1 = time.time()
#endregion: part 1
#region: part 2
field[-1,:] = '#'
field = sand_2(field,sand_count)
part2 = time.time()
print(f'Total time: {part2-start}, part 1 time: {part1-start}, part 2 time: {part2-part1}')
#endregion: part 2