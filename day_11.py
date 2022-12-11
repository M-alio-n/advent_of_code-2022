#region: imports
import math
import numpy as np
import primefac
#endregion: imports
#region: additional functions
class monkey:
    def __init__(self, items, fun, divisor, targets) -> None:
        self.items = items  # list of items in possession
        self.fun = fun  # operation function as string
        self.divisor = divisor # the divisor that decides which target to throw to
        self.targets = targets  # tuple of targets at throw
        self.inspections = 0    # number of completed inspections

    def turn(self):
        for item in self.items:
            # the worying inspection and the relief thereafter
            old = item
            item = math.floor(eval(self.fun)/3)
            self.inspections += 1
            if item % self.divisor == 0:
                monkeys[self.targets[0]].items.append(item)
            else:
                monkeys[self.targets[1]].items.append(item)
        self.items = []


class prime_monkey:
    def __init__(self, items, fun, divisor, targets) -> None:
        self.items = [[item%div for div in divisors] for item in items]  # list of items in possession
        self.fun = fun  # operation function as string
        self.divisor = divisor # the divisor that decides which target to throw to
        self.targets = targets  # tuple of targets at throw
        self.inspections = 0    # number of completed inspections

    def turn(self):
        for item in self.items:
            if self.fun.find('+') == -1:
                if self.fun == 'old * old':
                    item = [(item[count]*item[count])%div for count,div in enumerate(divisors)]
                else:
                    item = [(item[count]*int(self.fun.split(' * ')[1]))%div for count,div in enumerate(divisors)]
            else:
                # addition
                item = [(item[count]+int(self.fun.split(' + ')[1]))%div for count,div in enumerate(divisors)]
            self.inspections += 1
            if item[divisors.index(self.divisor)] == 0:
                prime_monkeys[self.targets[0]].items.append(item)
            else:
                prime_monkeys[self.targets[1]].items.append(item)
        self.items = []

#endregion: addtional functions
#region: load input
input = open('11').read().split('\n')
monkeys = []
divisors = []
for line in input:
    if line.startswith('  Starting items: '):
        starting_items = [int(item) for item in line.strip().split(': ')[1].split(', ')]
    elif line.startswith('  Operation: new = '):
        operation = line.split('= ')[1]
    elif line.startswith('  Test:'):
        divisor = int(line.split('by')[1])
        divisors.append(int(line.split('by')[1]))
    elif line.startswith('    If true:'):
        target1 = int(line.split('monkey')[1])
    elif line.startswith('    If false:'):
        target2 = int(line.split('monkey')[1])
    elif line.startswith('Monkey') and not line.startswith('Monkey 0:'):
        monkeys.append(monkey(starting_items,operation,divisor,(target1,target2)))
monkeys.append(monkey(starting_items,operation,divisor,(target1,target2)))
prime_monkeys = [prime_monkey(mon.items,mon.fun, mon.divisor, mon.targets) for mon in monkeys]
#endregion: input loaded
#region: part 1
for round in range(20):
    for curr_monkey in monkeys:
        curr_monkey.turn()
inspections = sorted([mon.inspections for mon in monkeys])
print(inspections[-1]*inspections[-2])
#endregion: part 1
#region: part 2

# All "divisible by" numbers are prime
# All "old * " numbers are prime

for round in range(10000):
    for count,curr_monkey in enumerate(prime_monkeys):
        curr_monkey.turn()

inspections = sorted([mon.inspections for mon in prime_monkeys])
print(inspections[-1]*inspections[-2])
#endregion: part 2