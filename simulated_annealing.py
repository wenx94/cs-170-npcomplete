import random
import math
import time

# Randomization Idea: http://katrinaeg.com/simulated-annealing.html

def swap_opt(wizards, mapping):
    wiz1 = random.choice(wizards)
    wiz2 = random.choice(wizards)
    wiz1_prev_index = mapping[wiz1]
    wiz2_prev_index = mapping[wiz2]
    mapping[wiz2] = wiz1_prev_index
    mapping[wiz1] = wiz2_prev_index
    return wiz1, wiz2

def cost_opt(mapping, constraints):
    failed = 0
    for c in constraints:
        wiz_a = mapping[c[0]]
        wiz_b = mapping[c[1]]
        wiz_mid = mapping[c[2]]
        if (wiz_a < wiz_mid < wiz_b) or (wiz_b < wiz_mid < wiz_a):
            failed += 1
    return failed

def acceptance_probability(old_cost, new_cost, T):
    if new_cost < old_cost:
        return 1.0
    else:
        return math.exp((old_cost - new_cost) / T)

def anneal_opt(wizards, constraints):
    random.shuffle(wizards)
    tempSet = set(wizards)
    # maps wiz order to reduce indexing runtime costs
    mapping = {k: v for v, k in enumerate(tempSet)}
    old_cost = cost_opt(mapping, constraints)
    T = 1.0
    T_min = 0.0001
    alpha = 0.94 # increase to improve probability of satisfying all constraints
    while T > T_min:
        i = 0
        while i < 7000: # increase to improve probability of satisfying all constraints
            wiz1, wiz2 = swap_opt(wizards, mapping)
            new_cost = cost_opt(mapping, constraints)
            if new_cost == 0:
                print("Found!")
                return mapping
            ap = acceptance_probability(old_cost, new_cost, T)
            if ap > random.random():
                old_cost = new_cost
            else:
                # revert back to pre-swap ordering
                temp = mapping[wiz1]
                mapping[wiz1] = mapping[wiz2]
                mapping[wiz2] = temp
            i += 1
        T = T * alpha
    return mapping

def solve_opt(wizards, constraints, filename):
    start = time.time()
    mapping = anneal_opt(wizards, constraints)
    solution = sorted(mapping.keys(), key=lambda x: mapping[x])
    write_output(filename, solution)
    print("Time taken: {0}".format(time.time() - start))

def write_output(filename, solution):
    with open(filename, "w") as f:
        for wizard in solution:
            f.write("{0} ".format(wizard))
