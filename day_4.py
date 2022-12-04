#region: imports
#endregion: imports
#region: additional functions
def find_full_overlap(pair):
    if int(pair[0][0]) <= int(pair[1][0]) and int(pair[0][1]) >= int(pair[1][1]):
        return 1
    elif int(pair[1][0]) <= int(pair[0][0]) and int(pair[1][1]) >= int(pair[0][1]):
        return 1
    return 0

def find_overlap(pair):
    if int(pair[0][0]) <= int(pair[1][0]) and int(pair[0][1]) >= int(pair[1][0]):
        return 1
    elif int(pair[1][0]) <= int(pair[0][0]) and int(pair[1][1]) >= int(pair[0][0]):
        return 1
    return 0

#endregion: addtional functions
#region: load input
pairs = []
for l in open('4').readlines():
    tmp = l.split(',')
    tmp2 = [a.split('-') for a in tmp]
    pairs.append(tmp2)

#endregion: input loaded

#region: part 1
print(sum(find_full_overlap(pair) for pair in pairs))
#endregion: part 1
#region: part 2
print(sum(find_overlap(pair) for pair in pairs))
#endregion: part 2