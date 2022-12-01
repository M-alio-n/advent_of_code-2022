#region: imports
import numpy as np
#endregion: imported
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
print(f'One elf has {int(np.max(stash_sums))} calories, very nutritious!')
#endregion: part 1
#region: part 2
sorted_sums = np.sort(stash_sums)
print(f'The three most heavily packed elfs combine to {int(np.sum(sorted_sums[-3:]))} calories!')
#endregion: part 2

#region: just for fun
def vstack_fill(arr1, arr2, fill=0):
    # if any array is empty
    if arr1.size == 0:
        return arr2
    elif arr2.size == 0:
        return arr1
    # reshape 1D arrays
    if arr1.ndim == 1:
        arr1 = np.array([arr1])
    if arr2.ndim == 1:
        arr2 = np.array([arr2])
    # zero filling of not matching entries
    if np.shape(arr1)[1] > np.shape(arr2)[1]:
        res_array = np.vstack((arr1,np.pad(arr2,((0,0),(0,np.shape(arr1)[1]-np.shape(arr2)[1])), 'constant', constant_values=(fill))))
    elif np.shape(arr2)[1] > np.shape(arr1)[1]:
        res_array = np.vstack((np.pad(arr1,((0,0),(0,np.shape(arr2)[1]-np.shape(arr1)[1])), 'constant', constant_values=(fill)),arr2))
    else:
        # dimensions are fine
        res_array = np.vstack((arr1,arr2))
    return res_array


file = open('day_1_inpt.txt', 'r')
stash_sums = np.array([])
elfs = np.array([])
food = np.array([])
for count, line in enumerate(file.readlines()):
    if line == '\n':
        elfs = vstack_fill(elfs,food)
        food = np.array([])
    else:
        food = np.append(food,np.double(line.strip()))
elfs = vstack_fill(elfs,food)
print(f'One elf has {int(np.max(np.sum(elfs,axis=1)))} calories, very nutritious!')
print(f'The three most heavily packed elfs combine to {int(np.sum(np.sort(np.sum(elfs,axis=1))[-3:]))} calories!')
#endregion: just for fun