#region: imports
import time
import numpy  as np
#endregion: imports
#region: additional functions
start = time.time()
def SNAFU2dec(string):
    val = 0
    for exp,char in enumerate(string[::-1]):
        if char == '=':
            val += -2*5**exp
        elif char == '-':
            val += -5**exp
        else:
            val += int(char)*5**exp
    return val

def dec2SNAFU(val):
    digs = ['2','1','0','-','=']
    digits = 1
    while True:
        if val > sum([2*5**exp for exp in range(digits)]):
            digits += 1
        else:
            break
    string = ''.join(['=' for _ in range(digits)])

    for digit in range(digits):
        for dig in digs:
            if SNAFU2dec(string[0:digit]+dig+string[digit+1::]) == val:
                return string[0:digit]+dig+string[digit+1::]
            if SNAFU2dec(string[0:digit]+dig+string[digit+1::]) < val:
                string = string[0:digit]+dig+string[digit+1::]
                break
    return string
#endregion: addtional functions
#region: load input
input = open('25').read().split('\n')
#endregion: input loaded
#region: part 1
print(dec2SNAFU(sum([SNAFU2dec(string) for string in input])))
part1 = time.time()
print(f'Total time: {part1-start}')
#endregion: part 1
