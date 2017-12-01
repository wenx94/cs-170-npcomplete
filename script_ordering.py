import os

staffDirIn = "./inputs/inputs_staff/"
staffDirOut = "./outputs/outputs_staff/"
In20 = "./inputs/inputs20/"
Out20 = "./outputs/outputs20/"
In35 = "./inputs/inputs35/"
Out35 = "./outputs/outputs35/"
In50 = "./inputs/inputs50/"
Out50 = "./outputs/outputs50/"

# Executes wizard_ordering.py for a series of input files
# Input file locations must be relative to wizard_ordering.py as described above
# Comment out and edit ranges as necessary

# For Input 20s
for i in range(10):
	inputFile = In20 + "input20_" + str(i) + ".in"
	outputFile = Out20 + "input20_" + str(i) + ".out"
	os.system("python wizard_ordering.py {0} {1}".format(inputFile, outputFile))

# For Input 35s
for i in range(10):
	inputFile = In35 + "input35_" + str(i) + ".in"
	outputFile = Out35 + "input35_" + str(i) + ".out"
	os.system("python wizard_ordering.py {0} {1}".format(inputFile, outputFile))

# For Input 50s
for i in range(10):
	inputFile = In50 + "input50_" + str(i) + ".in"
	outputFile = Out50 + "input50_" + str(i) + ".out"
	os.system("python wizard_ordering.py {0} {1}".format(inputFile, outputFile))

# For Staff Inputs
for i in range(3, 21):
	j = i * 20
	inputFile = staffDirIn + "staff_" + str(j) + ".in"
	outputFile = staffDirOut + "staff_" + str(j) + ".out"
	os.system("python wizard_ordering.py {0} {1}".format(inputFile, outputFile))
