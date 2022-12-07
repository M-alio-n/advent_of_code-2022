#region: imports
#endregion: imports
#region: additional functions
def dir_size(dir,system):
    size_val = system[dir][0]
    for dirs in system[dir][1][0]:
        size_val += dir_size(dirs,system)
    return size_val

#endregion: addtional functions
#region: load input
input = open('7').read().split('\n')
#endregion: input loaded
#region: part 1
system={'dir /':[0,[[],[]]]}
file_sizes = {}
curr_dir = ''
contentflag = 0
for line in input:
    if line[0:4] == '$ cd':
        contentflag = 0
        # we have to cd
        if line[5::] == '/':
            # go to main dir
            curr_dir = 'dir /'
        elif line[5::] == '..':
            # go down one level
            for dir in system:
                if curr_dir in system[dir][1][0]:
                    curr_dir = dir
        else:
            for dir in system[curr_dir][1][0]:
                if dir.strip() == 'dir '+ line[5::]:
                    curr_dir = dir
                    break
    elif line[0:4] == '$ ls':
        contentflag = 1
        continue
    elif contentflag == 1:
        if line[0:3] == 'dir':
            while line in system:
                # dir exists
                line = line + ' '
            system[line] = [0,[[],[]]]
            system[curr_dir][1][0].append(line)
        else:
            system[curr_dir][0] += int(line.split()[0])
            system[curr_dir][1][1].append(line)

solution = 0
for dirs in system:
    if dir_size(dirs,system) <= 100000:
        solution += dir_size(dirs,system)
print(solution)
#endregion: part 1
#region: part 2
free = 70000000 - dir_size('dir /',system)
requ = 30000000 - free
sol = 30000000
for dirs in system:
    if sol > dir_size(dirs,system) >= requ:
        sol = dir_size(dirs,system)
print(sol)
#endregion: part 2