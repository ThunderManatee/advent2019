from aocd import get_data
import copy
data = get_data(day=6)

def find_children(dtn, sat, occ):
    doi = 0
    i = 0
    dtr = copy.copy(dtn)
    while True:
        cur = dtr.pop(i)
        if cur[0] == sat:
            doi += find_children(dtn, cur[1], occ+1) + occ

        if len(dtr) == 0:
            return doi


dtn = [(d[:3], d[4:]) for d in data.split('\n')]
p1 = find_children(dtn, 'COM', 1)
print(p1)
