import os

testDirIn = "./inputs/inputs50/"
testDirOut = "./outputs/outputs50/"

# wizard_ordering.main(testIn, testOut)
# os.system("python wizard_ordering.py {0} {1}".format(testIn, testOut))

for i in range(3, 10):
	inputFile = testDirIn + "input50_" + str(i) + ".in"
	print("Input File: {0}".format(inputFile))

	outputFile = testDirOut + "output50_" + str(i) + ".out"
	print("Output File: {0}".format(outputFile))

	os.system("python wizard_ordering.py {0} {1}".format(inputFile, outputFile))