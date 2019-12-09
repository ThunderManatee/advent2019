from aocd import get_data
import copy
data = [int(d) for d in get_data(day=8)]

def count_numbers(data):
    start = 0
    end = 150
    max_counts = [150, 150, 150]
    while True:
        counts = [0, 0, 0]
        for i in range(start,end):
            if data[i] == 0:
                counts[0] += 1
            elif data[i] == 1:
                counts[1] += 1
            elif data[i] == 2:
                counts[2] += 1
        if counts[0] < max_counts[0]:
            max_counts = counts
        if end == len(data):
            break
        start +=150
        end += 150
    return max_counts[1]*max_counts[2]

def construct_img(data):
    dn = copy.copy(data)
    master = [[2 for i in range(25)] for j in range(6)]
    while True:
        for v in range(6):
            for h in range(25):
                p = dn.pop(0)
                if  master[v][h] == 2:
                    master[v][h] = p
        if len(dn) == 0:
            break
    return master

print(f'P1: {count_numbers(data)}')
img = construct_img(data)
print(img)
for i in img:
    for j in range(25):
        print(i[j], end='')
    print('\n')
