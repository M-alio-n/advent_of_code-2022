#region: imports
#endregion: imports
#region: additional functions
def gen_sprite(X):
    sprite = ['#' if idx==X or idx==X-1 or idx==X+1 else '.' for idx in range(40)]
    return sprite
#endregion: addtional functions
#region: load input
input = open('10').read().split('\n')
#endregion: input loaded
#region: part 1
X = 1
cycle = 1
strength_idx = 20
steps = {'noop':1,'addx':2}
sum_strength = 0
for line in input:
    if cycle+steps[line.split(' ')[0]] > strength_idx:
        print(f'Current strength in cycle {strength_idx}: {strength_idx*X}')
        sum_strength += strength_idx*X
        strength_idx += 40
    cycle += steps[line.split(' ')[0]]
    if line.startswith('addx'):
        X += int(line.split(' ')[1])
print(f'Total sum of strengths in the relevant cycles: {sum_strength}')
#endregion: part 1
#region: part 2
change_x = 0
curr_line = 0
next_line = 0
add_x = 0
X = 1
display = []
sprite = gen_sprite(X)
for cycle in range(240):
    if cycle == change_x:
        X += add_x
        sprite = gen_sprite(X)
    if next_line == cycle:
        if input[curr_line].startswith('addx'):
            next_line += 2
            change_x = cycle+2
            add_x = int(input[curr_line].split(' ')[1])
        else:
            next_line += 1
        curr_line += 1
    display.append(sprite[cycle%40])
for lines in range(6):
    print(''.join(display[lines*40:(lines+1)*40]))
#endregion: part 2