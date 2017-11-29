import argparse
import os

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

def solve(num_wizards, num_constraints, wizards, constraints, filename):
    base = os.path.basename(filename)

    filenameLP = os.path.splitext(base)[0] + "_LP.py"

    with open(filenameLP, "w") as f:
        # setting up LP script
        f.write("from pulp import *\n\n")
        f.write("prob = LpProblem(\"wiz\", LpMaximize)\n\n")

        f.write("smallC = 0.05\n")
        f.write("bigM = {0}\n".format(2* num_wizards))
        f.write("wizzies = set()\n")
        # wizard variables
        for wiz in wizards:
            f.write("{0} = LpVariable(\"{0}\", 1, {1}, cat = \"Integer\")\n".format(wiz, num_wizards))
            f.write("wizzies.add(\"{0}\")\n".format(wiz))

        # objective: max0 (no maximization or min, just want to see if a solution exists)
        f.write("\nprob += 0\n\n")

        # turn wiz constraints into LP constraints
        for i in range(num_constraints):
            constraint = constraints[i]
            x_1 = constraint[2]
            x_2 = constraint[0]
            x_3 = constraint[1]

            # x1 must be outside the age bounds of x2, x3
            # e.g. constraint = x_2 x_3 x_1

#           # binary helper for constrained ordering
            z_1 = "z{0}_1".format(i)
            f.write("{0} = LpVariable(\"{0}\", cat=\"Binary\")\n".format(z_1))

            # z1 => x1 > x2 and x1 > x3
            # !z1 => x < x2 and x1 < x3
            f.write("prob += {0} + smallC <= {1} + bigM * {2}\n".format(x_1, x_2, z_1))
            f.write("prob += {0} + smallC <= {1} + bigM * {2}\n".format(x_1, x_3, z_1))
            f.write("prob += {0} >= smallC + {1} - (1 - {2}) * bigM\n".format(x_1, x_2, z_1))
            f.write("prob += {0} >= smallC + {1} - (1 - {2}) * bigM\n".format(x_1, x_3, z_1))

        f.write("\n")
        f.write("GLPK().solve(prob)\n")
        f.write("ages = {}\n")
        f.write("for v in prob.variables():\n")
        f.write("\tif v.name in wizzies:\n")
        f.write("\t\tprint(v.name, \"=\", v.varValue)\n")
        f.write("\t\tages[v.name] = v.varValue\n")
        f.write("sorted_ages = sorted(ages.items(), key = lambda x: x[1])\n")
        f.write("relative_mapping = {}\n")
        f.write("for i in range(len(sorted_ages)):\n")
        f.write("\trelative_mapping[sorted_ages[i][0]] = i\n")


    return None

def num_satisfied_constraints(constraints, num_constraints):

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

# python wizard_ordering.py ./inputs/inputs20/inputs20_0.in ./outputs/outputs20/outputs20_0.out
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Constraint Solver.")
    parser.add_argument("input_file", type=str, help = "___.in")
    parser.add_argument("output_file", type=str, help = "___.out")
    args = parser.parse_args()

    num_wizards, num_constraints, wizards, constraints = read_input(args.input_file)
    solution = solve(num_wizards, num_constraints, wizards, constraints, args.input_file)
    print(num_satisfied_constraints(constraints, num_constraints))
    # write_output(args.output_file, solution)

