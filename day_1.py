#region: imports
import numpy as np
#endregion: imports
#region: additional functions    
#endregion: addtional functions
#region: load input
file = open('day_1_inpt.txt', 'r')
stash_sums = np.array([])
food = np.array([])
for count, line in enumerate(file.readlines()):
    if line == '\n':
        stash_sums = np.append(stash_sums,np.sum(food))
        food = np.array([])
    else:
        food = np.append(food,np.double(line.strip()))
stash_sums = np.append(stash_sums,np.sum(food))

#endregion: input loaded
#region: part 1
print(np.max(stash_sums))
#endregion: part 1
#region: part 2
sorted_sums = np.sort(stash_sums)
print(np.sum(sorted_sums[-3:]))
#endregion: part 2