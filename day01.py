from aocd import get_data
data = get_data(day=1)
dn = [int(d) for d in data.split()]

def fuel_calc(weight):
    currentFuel = weight//3-2
    if currentFuel > 0:
        currentFuel += fuel_calc(currentFuel)
    else:
        currentFuel = 0
    return currentFuel

p1 = sum(d//3-2 for d in dn)
print(p1)

p2 = sum(fuel_calc(x) for x in dn)
print(p2)