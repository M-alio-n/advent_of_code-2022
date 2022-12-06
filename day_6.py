#region: imports
#endregion: imports
#region: additional functions
def find_packet(inpt):
    for idx in range(4,len(inpt)):
        if len(set(inpt[idx-4:idx])) == 4:
            return idx
    return False
def find_message(inpt):
    for idx in range(14,len(inpt)):
        if len(set(inpt[idx-14:idx])) == 14:
            return idx
    return False
#endregion: addtional functions
#region: load input
input = open('6').read()
#endregion: input loaded
#region: part 1
print(find_packet(input))
#endregion: part 1
#region: part 2
print(find_message(input))
#endregion: part 2