import argparse
import os
import output_validator

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

def solve(num_wizards, num_constraints, wizards, constraints, filename, outfile):
    base = os.path.basename(filename)

    filenameLP = os.path.splitext(base)[0] + "_LP.py"
    # filenameLPout = os.path.splitext(base)[0] + "_LP.out"

    with open(filenameLP, "w") as f:
        # setting up LP script
        f.write("import time\n")
        f.write("from pulp import *\n\n")
        f.write("prob = LpProblem(\"wiz\", LpMaximize)\n\n")

        f.write("start = time.time()\n")
        f.write("smallC = 0.05\n")
        f.write("bigM = {0}\n".format(5 + num_wizards))
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
            f.write("prob += {0} >= smallC + {1} - (1 - {2}) * bigM\n\n".format(x_1, x_3, z_1))

        f.write("\n")
        f.write("GLPK().solve(prob)\n")
        f.write("ages = {}\n")
        f.write("for v in prob.variables():\n")
        f.write("\tif v.name in wizzies:\n")
        f.write("\t\tprint(v.name, \"=\", v.varValue)\n")
        f.write("\t\tages[v.name] = v.varValue\n")
        f.write("print(\"Time taken: {0}\".format((time.time() - start) * 1000))\n")
        f.write("sorted_ages = sorted(ages.items(), key = lambda x: x[1])\n")
        f.write("with open(\"{0}\", \"w\") as f:\n".format(outfile))
        f.write("\tfor i in range({0}):\n".format(num_wizards))
        f.write("\t\tf.write(\"{0} \".format(sorted_ages[i][0]))\n")
        # f.write("relative_mapping = {}\n")
        # f.write("for i in range(len(sorted_ages)):\n")
        # f.write("\trelative_mapping[sorted_ages[i][0]] = i\n")
    os.system("python {0}".format(filenameLP))



# def num_satisfied_constraints(constraints, num_constraints):
#     wizard_indices = {'Neal': 0, 'Conner': 1, 'Janette': 2, 'Amari': 3, 'Carla': 4, 'Curt': 5, 'Chase': 6, 'Ayesha': 7, 'Gene': 8, 'Dominick': 9, 'Joni': 10, 'Pam': 11, 'Wesley': 12, 'Mckenna': 13, 'Lianne': 14, 'Skylar': 15, 'Ruben': 16, 'Paris': 17, 'Daragh': 18, 'Oisin': 19}
#
#     num_satisfied = 0
#
#     for i in range(num_constraints):
#         constraint = constraints[i]
#         left_index = min(wizard_indices[constraint[0]], wizard_indices[constraint[1]])
#         right_index = max(wizard_indices[constraint[0]], wizard_indices[constraint[1]])
#         wiz_index = wizard_indices[constraint[2]]
#
#         if (wiz_index < left_index) or (wiz_index > right_index):
#             num_satisfied += 1
#
#     return num_satisfied

# def write_output(filename, solution):
#     with open(filename, "w") as f:
#         for wizard in solution:
#             f.write("{0} ".format(wizard))

# python wizard_ordering.py ./inputs/inputs20/input20_1.in ./outputs/outputs20/output20_1.out
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Constraint Solver.")
    parser.add_argument("input_file", type=str, help = "___.in")
    parser.add_argument("output_file", type=str, help = "___.out")
    args = parser.parse_args()

    num_wizards, num_constraints, wizards, constraints = read_input(args.input_file)
    solve(num_wizards, num_constraints, wizards, constraints, args.input_file, args.output_file)
    constraints_satisfied, num_constraints, constraints_failed = output_validator.processInput(args.input_file, args.output_file)
    print("You satisfied {}/{} constraints. List of failed constraints: {}".format(constraints_satisfied, num_constraints, constraints_failed))
    # print(num_satisfied_constraints(constraints, num_constraints))
    # write_output(args.output_file, solution)

