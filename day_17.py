#region: imports
import time
import numpy as np
#endregion: imports
#region: additional functions
start = time.time()
def move_rock(loi,chamber):
    global blast_idx, highest_rock
    while True:
        # chamber[loi] = 1
        # print_chamber(chamber)
        # chamber[loi] = 0
        # blast
        if blast_order[blast_idx] == '>':
            loi = (loi[0],loi[1]-1)
            if any(loi[1] < 0):
                # if crashing into corner or rock revert
                loi = (loi[0],loi[1]+1)
            elif any(chamber[loi]== 1):
                # if crashing into corner or rock revert
                loi = (loi[0],loi[1]+1)
        elif blast_order[blast_idx] == '<':
            loi = (loi[0],loi[1]+1)
            if any(loi[1] > 6):
                # if crashing into corner or rock revert
                loi = (loi[0],loi[1]-1)
            elif any(chamber[loi]== 1):
                # if crashing into corner or rock revert
                loi = (loi[0],loi[1]-1)
        blast_idx = (blast_idx+1)%len(blast_order)
        # drop one layer
        loi = (loi[0]-1,loi[1])
        if any(loi[0] < 0):
            # we hit rock bottom revert the drop and manifest the rock
            loi = (loi[0]+1,loi[1])
            chamber[loi] = 1
            break
        elif any(chamber[loi]== 1):
            # we hit a rock revert the drop and manifest the rock
            loi = (loi[0]+1,loi[1])
            chamber[loi] = 1
            break
    # determine highest rock
    for idx in range(np.shape(chamber)[0]-1,-1,-1):
        if any(chamber[idx,:] == 1):
            highest_rock = idx+1
            break
    return chamber

def spawn_rock(chamber,number_of_rocks,number_of_rocks_2):
    flag1 = 0
    flag2 = 0
    global rock_count, pattern_tracker, blast_idx
    while any([not flag1, not flag2]):
        # determine the rock_idx
        rock_idx = (rock_count-1)%5
        # spawn the rock
        if rock_idx == 0:
            idx_0 = highest_rock+3
            idx_1 = 1
            loi = (np.array([idx_0,idx_0,idx_0,idx_0]),np.array([idx_1,idx_1+1,idx_1+2,idx_1+3]))
        elif rock_idx == 1:
            idx_0 = highest_rock+3
            idx_1 = 1
            loi = (np.array([idx_0+2,idx_0+1,idx_0+1,idx_0+1,idx_0]),np.array([idx_1+2,idx_1+1,idx_1+2,idx_1+3,idx_1+2]))
        elif rock_idx == 2:
            idx_0 = highest_rock+3
            idx_1 = 2
            loi = (np.array([idx_0,idx_0,idx_0,idx_0+1,idx_0+2]),np.array([idx_1+2,idx_1+1,idx_1,idx_1,idx_1]))
        elif rock_idx == 3:
            idx_0 = highest_rock+4
            idx_1 = 4
            loi = (np.array([idx_0+2,idx_0+1,idx_0,idx_0-1]),np.array([idx_1,idx_1,idx_1,idx_1]))
        elif rock_idx == 4:
            idx_0 = highest_rock+2
            idx_1 = 3
            loi = (np.array([idx_0+2,idx_0+1,idx_0+2,idx_0+1]),np.array([idx_1,idx_1+1,idx_1+1,idx_1]))
        # if necesary increase chamber height
        if any(loi[0] >= np.shape(chamber)[0]):
            chamber = np.vstack((chamber,np.zeros((max(loi[0])-np.shape(chamber)[0]+1,7),dtype=int)))
        chamber = move_rock(loi,chamber)
        if rock_count == number_of_rocks:
            print(f'Solution for part 1: {highest_rock}')
            flag1 = 1
        
        if (rock_idx, blast_idx) in pattern_tracker and not flag2 == 1:
            pattern_tracker[(rock_idx, blast_idx)][0].append(highest_rock)
            pattern_tracker[(rock_idx, blast_idx)][1].append(rock_count)
            if len(pattern_tracker[(rock_idx, blast_idx)][0]) >= 3 and len(set(np.diff(pattern_tracker[(rock_idx, blast_idx)][0]))) == 1 and len(set(np.diff(pattern_tracker[(rock_idx, blast_idx)][1]))) == 1 and (number_of_rocks_2-rock_count)%np.diff(pattern_tracker[(rock_idx, blast_idx)][1])[0] == 0:
                flag2 = 1
                print(f'Solution for part 2: {int(highest_rock+np.diff(pattern_tracker[(rock_idx, blast_idx)][0])[0]*(number_of_rocks_2-rock_count)/np.diff(pattern_tracker[(rock_idx, blast_idx)][1])[0])}')
        else:
            pattern_tracker[(rock_idx, blast_idx)] = ([highest_rock],[rock_count])
        rock_count += 1
    return chamber

def print_chamber(chamber):
    print(np.fliplr(np.flipud(chamber)))
    return
#endregion: addtional functions
#region: load input
blast_order = open('17').read()
#endregion: input loaded
#region: part 1
pattern_tracker = {}
chamber = np.zeros((0,7),dtype=int)
highest_rock = 0
rock_count = 1
blast_idx = 0
chamber = spawn_rock(chamber, 2022, 1000000000000)
#endregion: part 1
#region: part 2
part2 = time.time()
print(f'Total time: {part2-start}')
#endregion: part 2
