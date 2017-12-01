import random
import math
import copy
import time

def swap(wizards):
    neighbor = copy.deepcopy(wizards)
    index1 = random.randint(0, len(wizards) - 1)
    index2 = random.randint(0, len(wizards) - 1)
    neighbor[index1], neighbor[index2] = neighbor[index2], neighbor[index1]
    return neighbor

def cost(wizards, constraints):
    failed = 0
    for c in constraints:
        wiz1 = wizards.index(c[0])
        wiz2 = wizards.index(c[1])
        lowerBound = min(wiz1, wiz2)
        upperBound = max(wiz1, wiz2)
        if (lowerBound < wizards.index(c[2]) < upperBound):
            failed += 1
    return failed

def acceptance_probability(old_cost, new_cost, T):
    if new_cost < old_cost:
        return 1.0
    else:
        return math.exp((old_cost - new_cost) / T)


    # 
    # output_ordering_set = set(output_ordering)
    # output_ordering_map = {k: v for v, k in enumerate(output_ordering)}
def anneal(wizards, constraints):
    random.shuffle(wizards)
    curr = wizards
    old_cost = cost(curr, constraints)
    T = 1.0
    T_min = 0.0001
    alpha = 0.90
    while T > T_min:
        i = 0
        while i < 2000:
            neighbor = swap(curr)
            new_cost = cost(neighbor, constraints)
            if new_cost == 0:
                print("Found!")
                return neighbor
            ap = acceptance_probability(old_cost, new_cost, T)
            if ap > random.random():
                curr = neighbor
                old_cost = new_cost
            i += 1
        T = T * alpha
    return curr


def solve(wizards, constraints, filename):
    start = time.time()
    solution = anneal(wizards, constraints)
    write_output(filename, solution)
    print("Time taken: {0}".format(time.time() - start))


def write_output(filename, solution):
    with open(filename, "w") as f:
        for wizard in solution:
            f.write("{0} ".format(wizard))
