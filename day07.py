from aocd import get_data
import copy
from itertools import permutations
data = get_data(day=7)

def tpop(t):
    l = list(t)
    del l[0]
    return tuple(l)

def get_thrust(pm, d):
    a = 0
    retcode = 0
    da = [copy.copy(d)]*5
    ic = [pm[i] for i in range(len(pm))]
    rp = [0]*5
    o1 = lambda: dn[dn[i+1]] if p1 else dn[i+1]
    o2 = lambda: dn[dn[i+2]] if p2 else dn[i+2]
    fl = False
    while True:
        dn = da[a]
        i = rp[a]
        while True:
            instr = str(dn[i]).zfill(4)
            oc = instr[2:]
            p2, p1 = [v == '0' for v in instr[:2]]
            if oc == '99':
                return retcode

            if oc == '01':
                dn[dn[i+3]] = o1() + o2()
                i += 4
            elif oc == '02':
                dn[dn[i+3]] = o1() * o2()
                i += 4
            elif oc == '03':
                dn[dn[i+1]] = ic[a]
                ic[a] = retcode
                i += 2
            elif oc == '04':
                retcode = o1()
                i += 2
                rp[a] = i
                da[a] = dn
                if a == 4:
                    a = 0
                else:
                    a += 1
                ic[a] = retcode
                break
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

datap = [int(d) for d in data.split(',')]
datan = copy.copy(datap)
thr= []
for p in permutations(range(5,10)):
    thr.append(get_thrust(p, datan))
print(max(thr))