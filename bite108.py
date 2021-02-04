from collections import namedtuple

BeltStats = namedtuple('BeltStats', 'score ninjas')

ninja_belts = {'yellow': BeltStats(50, 11),
               'orange': BeltStats(100, 7),
               'green': BeltStats(175, 1),
               'blue': BeltStats(250, 5)}

more_belts = dict(brown=BeltStats(400, 2),
                  black=BeltStats(600, 5))
ninja_belts_updated = {**ninja_belts, **more_belts}

total = 0
for value in ninja_belts_updated.values():
    total += value[0]*value[1]
print(total)
total = 0
for belt in ninja_belts_updated.values():
    print(belt)
    total += belt.score * belt.ninjas
print(total)