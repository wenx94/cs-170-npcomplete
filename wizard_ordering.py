import argparse
import time
import random

RUNTIME = 600 #seconds

def read_input(filename):
    with open(filename) as f:
        num_wizards = int(f.readline())
        num_constraints = int(f.readline())
        constraints = []
        wizards = set()
        for _ in range(num_constraints):
            c = f.readline().split()
            constraints.append(c)
            for w in c:
                wizards.add(w)
                
    wizards = list(wizards)
    return num_wizards, num_constraints, wizards, constraints

def solve(num_wizards, num_constraints, wizards, constraints):
    start_time = time.time()
    end_time = start_time + RUNTIME
    maximum_satisfied = 0
    best_list = []

    while start_time < end_time:
        random.shuffle(wizards)
        wizard_indices = {}

        for i in range(num_wizards):
            wizard_indices[wizards[i]] = i

        satisfied = num_satisfied_constraints(wizard_indices, constraints, num_constraints)

        if satisfied == num_constraints:
            print("Number of Constraints Satisfied: " + str(satisfied))
            return wizards
        elif satisfied > maximum_satisfied:
            maximum_satisfied = satisfied
            best_list = wizards[:]

        start_time = time.time()

    #optimize best_list
    print("Number of Constraints Satisfied: " + str(maximum_satisfied))
    return best_list

def num_satisfied_constraints(wizard_indices, constraints, num_constraints):
    num_satisfied = 0

    for i in range(num_constraints):
        constraint = constraints[i]
        left_index = min(wizard_indices[constraint[0]], wizard_indices[constraint[1]])
        right_index = max(wizard_indices[constraint[0]], wizard_indices[constraint[1]])
        wiz_index = wizard_indices[constraint[2]]

        if (wiz_index < left_index) or (wiz_index > right_index):
            num_satisfied += 1

    return num_satisfied

def write_output(filename, solution):
    with open(filename, "w") as f:
        for wizard in solution:
            f.write("{0} ".format(wizard))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Constraint Solver.")
    parser.add_argument("input_file", type=str, help = "___.in")
    parser.add_argument("output_file", type=str, help = "___.out")
    args = parser.parse_args()

    num_wizards, num_constraints, wizards, constraints = read_input(args.input_file)
    solution = solve(num_wizards, num_constraints, wizards, constraints)
    write_output(args.output_file, solution)

