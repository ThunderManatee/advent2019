from aocd import get_data
from itertools import product
import copy
data = get_data(day=2)

def get_output(noun, verb, d):
    d[1] = noun
    d[2] = verb
    iterange = iter(range(len(d)))

    for i in iterange:
        if d[i] == 99:
            return d[0]

        if d[i] == 1:
            d[d[i+3]] = d[d[i+1]] + d[d[i+2]]
        elif d[i] == 2:
            d[d[i+3]] = d[d[i+1]] * d[d[i+2]]

        [next(iterange) for i in range(3)]

datap = [int(d) for d in data.split(',')]
datan = copy.copy(datap)
p1 = get_output(12, 2, datan)
print(f'Part 1: {p1}')

for noun, verb in product(range(100),repeat=2):
    datan = copy.copy(datap)
    p2q = get_output(noun, verb, datan)
    if p2q == 19690720:
        p2h = 100 * noun + verb
        print(f'Part 2: {p2h}')
        break
