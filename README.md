# Wizardry Party README #
#### Xintong (Robert) Wen & James Scott Reese 
#### UC Berkeley CS 170 - Fall 2017

The two necessary files for ordering calculation are in the main directory: `wizard_ordering.py` and `output_validator.py`.
All associated input files are in the directory `./inputs`

`wizard_ordering.py` solves the constraints using an LP solver and calls `output_validator.py` at the end to check number of constraints satisfied.

The following command should be run for wizard_ordering:  
`$ python wizard_ordering.py <input file> <output file>`

So for example, to run the solver on `./inputs/inputs20/input20_0.in` and write the output to `./outputs/outputs20/output20_0.out` use the following command:  
`$ python wizard_ordering.py ./inputs/inputs20/input20_0.in ./outputs/outputs20/output20_0.out`

To run the solver on all inputs, we have a file `script_ordering.py` which can be run as follows:  
`$ python script_ordering.py`  

Range values can be edited inside `script_ordering.py` to only run the solver of a certain series of desired inputs. More instructions are commented inside.

The output files we have in `./outputs/` are the results of running the solver on the respective input with the same basename as instructed. There is an exception for the inputs with 20 wizards because we switched from using the CBC LP Solver to the Gurobi Solver for inputs with 35 wizards or larger.
