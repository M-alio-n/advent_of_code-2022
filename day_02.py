#region: imports
#endregion: imported
#region: additional functions    
#endregion: addtional functions
#region: load input
file = open('02', 'r')
games = []
for line in file.readlines():
    games.append(line.strip())
#endregion: input loaded
#region: part 1
#scores
scores = {
    'A X': 1+3,
    'A Y': 2+6,
    'A Z': 3+0,
    'B X': 1+0,
    'B Y': 2+3,
    'B Z': 3+6,
    'C X': 1+6,
    'C Y': 2+0,
    'C Z': 3+3,
}
score_p1 = 0
for game in games:
    score_p1 += scores[game]
print(f'The final score is {score_p1}, not bad!')
#endregion: part 1
#region: part 2
#pairs
pairs = {
    'A X': 'A Z',
    'A Y': 'A X',
    'A Z': 'A Y',
    'B X': 'B X',
    'B Y': 'B Y',
    'B Z': 'B Z',
    'C X': 'C Y',
    'C Y': 'C Z',
    'C Z': 'C X',
}
score_p2 = 0
for game in games:
    score_p2 += scores[pairs[game]]
if score_p2 < score_p1:
    print(f'The final score is {score_p2}, still fine!')
else:
    print(f'The final score is {score_p2}, even better!')
#endregion: part 2