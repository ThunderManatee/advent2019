from aocd import get_data
import copy
data = get_data(day=6)

nums = []
def find_children(dtn, sat, occ, find):
    doi = 0
    dtr = copy.copy(dtn)
    while True:
        global nums
        cur = dtr.pop(0)
        if cur[0] == sat and cur[1] == find:
            nums.append(occ)

        if cur[0] == sat:
            doi += find_children(dtn, cur[1], occ+1, find) + occ
        
        if len(dtr) == 0:
            return doi

def back_it_up(dtn, lnum, snum, ln, sn):
    tsnum = snum
    tlnum = lnum
    tn1 = ln
    tn2 = sn
    while True:
        for i in range(len(dtn)):
            if dtn[i][1] == tn1:
                tn1 = dtn[i][0]
                break
        if tsnum == tlnum:
            for i in range(len(dtn)):
                if dtn[i][1] == tn2:
                    tn2 = dtn[i][0]
                    break
            tsnum -= 1
        tlnum -= 1
        if tn1 == tn2:
            return tsnum


dtn = [(d[:3], d[4:]) for d in data.split('\n')]
p1 = find_children(dtn, 'COM', 1, 'dsasdads')
p2a, p2b = find_children(dtn, 'COM', 1, 'YOU'), find_children(dtn, 'COM', 1, 'SAN')
p2c = back_it_up(dtn, nums[0], nums[1], 'YOU', 'SAN')
print(p1)
p2 = nums[0] + nums[1] - 2 - p2c*2
print(p2)