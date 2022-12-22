#region: imports
import time
#endregion: imports
#region: additional functions
start = time.time()
def equation_solver(string,val):
    counter = 1
    while string != 'X' and string != '(X)':
        string=string[1:len(string)-1]
        if string[0] == '(':
            # next operation is at the end
            next = max([string.rfind('*'),string.rfind('/'),string.rfind('+'),string.rfind('-')])
            if string[next] == '*':
                val = val /int(string[next+1::])
            elif string[next] == '/':
                val = val *int(string[next+1::])
            elif string[next] == '-':
                val = val +int(string[next+1::])
            elif string[next] == '+':
                val = val -int(string[next+1::])
            string = string[0:next]
        else:
            # next operation in front
            next = min([val for val in [string.find('*'),string.find('/'),string.find('+'),string.find('-')] if val > -1])
            if string[next] == '*':
                val = val /int(string[0:next])
            elif string[next] == '/':
                val = int(string[0:next])/val
            elif string[next] == '-':
                val = -(val -int(string[0:next]))
            elif string[next] == '+':
                val = val -int(string[0:next])
            string = string[next+1::]
            counter += 1
    return val

#endregion: addtional functions
#region: load input
input = open('21').read().split('\n')
monkeys = {}
for line in input:
    if len(line.split(' ')) == 2:
        monkeys[line.split(':')[0]] = int(line.split(' ')[1])
    else:
        monkeys[line.split(':')[0]] = line.split(' ')[1:4]
#endregion: input loaded
#region: part 1
while type(monkeys['root']) == type(list()):
    for monkey in monkeys:
        if type(monkeys[monkey]) == type(list()):
            if type(monkeys[monkeys[monkey][0]]) == type(int()) and type(monkeys[monkeys[monkey][2]]) == type(int()):
                if monkeys[monkey][1] == '+':
                    monkeys[monkey] = int(monkeys[monkeys[monkey][0]] + monkeys[monkeys[monkey][2]])
                elif monkeys[monkey][1] == '*':
                    monkeys[monkey] = int(monkeys[monkeys[monkey][0]] * monkeys[monkeys[monkey][2]])
                elif monkeys[monkey][1] == '-':
                    monkeys[monkey] = int(monkeys[monkeys[monkey][0]] - monkeys[monkeys[monkey][2]])
                elif monkeys[monkey][1] == '/':
                    monkeys[monkey] = int(monkeys[monkeys[monkey][0]] / monkeys[monkeys[monkey][2]])
print(monkeys['root'])
part1 = time.time()
#endregion: part 1
#region: part 2
for line in input:
    if len(line.split(' ')) == 2:
        monkeys[line.split(':')[0]] = int(line.split(' ')[1])
    else:
        monkeys[line.split(':')[0]] = line.split(' ')[1:4]
monkeys['root'][1] = '='
monkeys['humn'] = 'X'

change_flag = 1
while change_flag:
    change_flag = 0
    for monkey in monkeys:
        if monkey == 'humn':
            continue
        if type(monkeys[monkey]) == type(list()):
            if type(monkeys[monkeys[monkey][0]]) == type(int()) and type(monkeys[monkeys[monkey][2]]) == type(int()):
                if monkeys[monkey][1] == '+':
                    monkeys[monkey] = int(monkeys[monkeys[monkey][0]] + monkeys[monkeys[monkey][2]])
                    change_flag = 1
                elif monkeys[monkey][1] == '*':
                    monkeys[monkey] = int(monkeys[monkeys[monkey][0]] * monkeys[monkeys[monkey][2]])
                    change_flag = 1
                elif monkeys[monkey][1] == '-':
                    monkeys[monkey] = int(monkeys[monkeys[monkey][0]] - monkeys[monkeys[monkey][2]])
                    change_flag = 1
                elif monkeys[monkey][1] == '/':
                    monkeys[monkey] = int(monkeys[monkeys[monkey][0]] / monkeys[monkeys[monkey][2]])
                    change_flag = 1


string = ''.join(monkeys['root'][0]+'='+monkeys['root'][2])
changeflag = 1
while changeflag:
    changeflag = 0
    for monkey in monkeys:
        if string.find(monkey) != -1:
            if type(monkeys[monkey]) == type(int()):
                string=string.replace(monkey,str(monkeys[monkey]))
            else:
                string=string.replace(monkey,'('+''.join(monkeys[monkey])+')')
            changeflag = 1
print(string)
print(equation_solver(string.split('=')[0],int(string.split('=')[1])))
part2 = time.time()
print(f'Total time: {part2-start}, part 1 time: {part1-start}, part 2 time: {part2-part1}')
#endregion: part 2