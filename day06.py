from aocd import get_data
import copy
data = get_data(day=6)

def find_children(dn, orb, corbs):
    doi = 0
    i = 0
    dr = copy.copy(dn)
    while True:
        cur = dr.pop(i)
        if cur[0] == orb:
            doi += find_children(dn, cur[1], corbs+1) + corbs

        if len(dr) == 0:
            return doi


dn = [(d[:3], d[4:]) for d in data.split('\n')]
p1 = find_children(dn, 'COM', 1)
print(p1)
