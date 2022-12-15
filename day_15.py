#region: imports
import time
#endregion: imports
#region: additional functions
start = time.time()
def manhattan_dist(sens,beac):
    return abs(sens[0]-beac[0])+abs(sens[1]-beac[1])

def find_max_range(sensors,loi):
    covered = set([])
    for count,sensor in enumerate(sensors):
        walk_up = 0
        walk_down = 0
        while manhattan_dist(sensor,(sensor[0]+walk_up,loi)) <= sensor[2] or manhattan_dist(sensor,(sensor[0]+walk_down,loi)) <= sensor[2]:
            if manhattan_dist(sensor,(sensor[0]+walk_up,loi)) <= sensor[2]:
                covered.add((sensor[0]+walk_up,loi))
                walk_up += 1
            if manhattan_dist(sensor,(sensor[0]+walk_down,loi)) <= sensor[2]:
                covered.add((sensor[0]+walk_down,loi))
                walk_down -= 1
    return covered

def iscovered(sensors,point):
    for sensor in sensors:
        if manhattan_dist(sensor,point) <= sensor[2]:
            return True
    return False

#endregion: addtional functions
#region: load input
input = open('15').read().split('\n')
sensors = []
beacons = []
for line in input:
    tmp = ((int(line.split('=')[1].split(',')[0]),int(line.split('=')[2].split(':')[0])))
    beacons.append((int(line.split('=')[3].split(',')[0]),int(line.split('=')[4])))
    sensors.append((tmp[0],tmp[1],manhattan_dist(tmp,beacons[-1])))
#endregion: input loaded
#region: part 1
line_of_interest = 2000000
beacons_in_line = sum([list(set(beacons))[idx][1]==line_of_interest for idx in range(len(list(set(beacons))))])
sensors_in_line = sum([list(set(sensors))[idx][1]==line_of_interest for idx in range(len(list(set(sensors))))])

covered_fields = find_max_range(sensors,line_of_interest)
for beacon in beacons:
    if beacon in covered_fields:
        covered_fields.remove(beacon)
print(len(covered_fields))
part1 = time.time()
#endregion: part 1
#region: part 2
searchspace = 4000000

flag = 0

for count,sensor in enumerate(sensors):
    print(f'Checked {count} out of {len(sensors)}')
    # from right to top
    idx0 = sensor[0]+sensor[2]+1
    idx1 = sensor[1]
    while True:
        idx1 -= 1
        if idx0 <= searchspace and idx0 >= 0 and idx1 <= searchspace and idx1 >= 0:
            if not iscovered(sensors,(idx0,idx1)):
                print(idx0*4000000+idx1)
                flag = 1
                break
        idx0 -= 1
        if idx0 <= searchspace and idx0 >= 0 and idx1 <= searchspace and idx1 >= 0:
            if not iscovered(sensors,(idx0,idx1)):
                print(idx0*4000000+idx1)
                flag = 1
                break
        if idx0 < sensor[0]:
            break
    if flag == 1:
        break
        



part2 = time.time()
print(f'Total time: {part2-start}, part 1 time: {part1-start}, part 2 time: {part2-part1}')
#endregion: part 2