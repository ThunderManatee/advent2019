from aocd import get_data
import copy
from itertools import permutations
data = get_data(day=7)

def get_thrust(ini, pm, d):
    i = 0
    retcode = None
    prev = 0
    o1 = lambda: dn[dn[i+1]] if p1 else dn[i+1]
    o2 = lambda: dn[dn[i+2]] if p2 else dn[i+2]
    for a in pm:
        dn = copy.copy(d)
        print(a, prev)
        fl = False
        while True:
            instr = str(dn[i]).zfill(4)
            oc = instr[2:]
            p2, p1 = [v == '0' for v in instr[:2]]
            if oc == '99':
                prev = retcode
                break

            if oc == '01':
                dn[dn[i+3]] = o1() + o2()
                i += 4
            elif oc == '02':
                dn[dn[i+3]] = o1() * o2()
                i += 4
            elif oc == '03':
                if fl == False:
                    dn[dn[i+1]] = a
                    fl = True
                else:
                    dn[dn[i+1]] = prev
                i += 2
            elif oc == '04':
                print(o1())
                retcode = o1()
                i += 2
            elif oc == '05':
                i = o2() if o1() else i + 3
            elif oc == '06':
                i = o2() if not o1() else i + 3
            elif oc == '07':
                dn[dn[i+3]] = 1 if o1() < o2() else 0
                i += 4
            elif oc == '08':
                dn[dn[i+3]] = 1 if o1() == o2() else 0
                i += 4
    return prev

datap = [int(d) for d in data.split(',')]
datan = copy.copy(datap)
thr= []
for p in permutations(range(0,5)):
    thr.append(get_thrust(0, p, datan))
print(thr)