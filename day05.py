from aocd import get_data
import copy
data = get_data(day=5)

def get_output(inp, d):
    i = 0
    retcode = None
    o1 = lambda: d[d[i+1]] if p1 else d[i+1]
    o2 = lambda: d[d[i+2]] if p2 else d[i+2]

    while True:
        instr = str(d[i]).zfill(4)
        oc = instr[2:]
        p2, p1 = [v == '0' for v in instr[:2]]
        if oc == '99':
            return retcode

        if oc == '01':
            d[d[i+3]] = o1() + o2()
            i += 4
        elif oc == '02':
            d[d[i+3]] = o1() * o2()
            i += 4
        elif oc == '03':
            d[d[i+1]] = inp
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
            d[d[i+3]] = 1 if o1() < o2() else 0
            i += 4
        elif oc == '08':
            d[d[i+3]] = 1 if o1() == o2() else 0
            i += 4

datap = [int(d) for d in data.split(',')]
datan = copy.copy(datap)
p1 = get_output(1, datan)
print(f'Part 1: {p1}')
d = copy.copy(datap)
p2 = get_output(5, d)
print(f"Part 2: {p2}")