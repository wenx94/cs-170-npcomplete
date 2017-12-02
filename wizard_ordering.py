import argparse
import os
import output_validator
import simulated_annealing

staffMin = 160

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

    # used simulated annealing optimization algorithm to solve staff inputs
    if num_wizards >= staffMin:
        simulated_annealing.solve_opt(wizards, constraints, outfile)
    else:
        base = os.path.basename(filename)
        filenameLP = os.path.splitext(base)[0] + "_LP.py"

        # for smaller input sizes, reduce to ILP

        with open(filenameLP, "w") as f:
            # setting up LP script
            f.write("import time\n")
            f.write("from pulp import *\n\n")
            f.write("prob = LpProblem(\"wiz\", LpMaximize)\n\n")

            f.write("start = time.time()\n")
            f.write("smallC = 1\n")
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
            # f.write("GLPK().solve(prob)\n")
            f.write("prob.solve(pulp.GUROBI_CMD())\n")
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

        os.system("python {0}".format(filenameLP))
        os.remove(filenameLP)


# python wizard_ordering.py ./inputs/inputs20/input20_0.in ./outputs/outputs20/output20_0.out
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Constraint Solver.")
    parser.add_argument("input_file", type=str, help = "___.in")
    parser.add_argument("output_file", type=str, help = "___.out")
    args = parser.parse_args()

    num_wizards, num_constraints, wizards, constraints = read_input(args.input_file)
    solve(num_wizards, num_constraints, wizards, constraints, args.input_file, args.output_file)
    constraints_satisfied, num_constraints, constraints_failed = output_validator.processInput(args.input_file, args.output_file)
    print("You satisfied {}/{} constraints. List of failed constraints: {}".format(constraints_satisfied, num_constraints, constraints_failed))

