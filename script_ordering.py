import os

testDirIn = "./inputs/inputs_staff/"
testDirOut = "./outputs/outputs_staff/"

# wizard_ordering.main(testIn, testOut)
# os.system("python wizard_ordering.py {0} {1}".format(testIn, testOut))

for i in range(3, 21):
	j = i * 20
	inputFile = testDirIn + "staff_" + str(j) + ".in"
	print("Input File: {0}".format(inputFile))

	outputFile = testDirOut + "staff_" + str(j) + ".out"
	print("Output File: {0}".format(outputFile))

	os.system("python wizard_ordering.py {0} {1}".format(inputFile, outputFile))