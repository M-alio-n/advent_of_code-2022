#region: imports
import numpy as np
#endregion: imports
#region: additional functions
#endregion: addtional functions
#region: load input
file = open('08')
visibility = np.array([])
for count,line in enumerate(file.readlines()):
    if count > 0:
        trees = np.vstack((trees, np.array([int(a) for a in line.strip()])))
    else:
        trees = np.array([int(a) for a in line.strip()])
visibility = np.zeros_like(trees)
#endregion: input loaded
#region: part 1
for ind1 in range(np.shape(trees)[0]):
    curr_max = -1
    for ind2 in range(np.shape(trees)[1]):
        if trees[ind1,ind2] > curr_max:
            curr_max = trees[ind1,ind2]
            visibility[ind1,ind2] = 1
for ind2 in range(np.shape(trees)[0]):
    curr_max = -1
    for ind1 in range(np.shape(trees)[1]):
        if trees[ind1,ind2] > curr_max:
            curr_max = trees[ind1,ind2]
            visibility[ind1,ind2] = 1
for ind1 in range(np.shape(trees)[0]-1,-1,-1):
    curr_max = -1
    for ind2 in range(np.shape(trees)[1]-1,-1,-1):
        if trees[ind1,ind2] > curr_max:
            curr_max = trees[ind1,ind2]
            visibility[ind1,ind2] = 1
for ind2 in range(np.shape(trees)[0]-1,0,-1):
    curr_max = -1
    for ind1 in range(np.shape(trees)[1]-1,-1,-1):
        if trees[ind1,ind2] > curr_max:
            curr_max = trees[ind1,ind2]
            visibility[ind1,ind2] = 1
print(np.sum(visibility))
#endregion: part 1
#region: part 2
highest_score = 0
for tree_idx1 in range(np.shape(trees)[0]):
    for tree_idx2 in range(np.shape(trees)[1]):
        range1 = 0
        for look_idx1 in range(tree_idx1-1,-1,-1):
            range1 += 1
            if trees[tree_idx1][tree_idx2] <= trees[look_idx1][tree_idx2]:
                break
        range2 = 0
        for look_idx1 in range(tree_idx1+1,np.shape(trees)[0]):
            range2 += 1
            if trees[tree_idx1][tree_idx2] <= trees[look_idx1][tree_idx2]:
                break
        range3 = 0
        for look_idx2 in range(tree_idx2+1,np.shape(trees)[1]):
            range3 += 1
            if trees[tree_idx1][tree_idx2] <= trees[tree_idx1][look_idx2]:
                break
        range4 = 0
        for look_idx2 in range(tree_idx2-1,-1,-1):
            range4 += 1
            if trees[tree_idx1][tree_idx2] <= trees[tree_idx1][look_idx2]:
                break
        if range1*range2*range3*range4 > highest_score:
            highest_score = range1*range2*range3*range4
print(highest_score)
#endregion: part 2