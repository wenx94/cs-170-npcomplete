from pulp import *

prob = LpProblem("wiz", LpMaximize)

smallC = 0.005
bigM = 40
wizzies = set()
Daragh = LpVariable("Daragh", 1, 20)
wizzies.add("Daragh")
Conner = LpVariable("Conner", 1, 20)
wizzies.add("Conner")
Chase = LpVariable("Chase", 1, 20)
wizzies.add("Chase")
Oisin = LpVariable("Oisin", 1, 20)
wizzies.add("Oisin")
Dominick = LpVariable("Dominick", 1, 20)
wizzies.add("Dominick")
Neal = LpVariable("Neal", 1, 20)
wizzies.add("Neal")
Skylar = LpVariable("Skylar", 1, 20)
wizzies.add("Skylar")
Ayesha = LpVariable("Ayesha", 1, 20)
wizzies.add("Ayesha")
Paris = LpVariable("Paris", 1, 20)
wizzies.add("Paris")
Carla = LpVariable("Carla", 1, 20)
wizzies.add("Carla")
Mckenna = LpVariable("Mckenna", 1, 20)
wizzies.add("Mckenna")
Wesley = LpVariable("Wesley", 1, 20)
wizzies.add("Wesley")
Curt = LpVariable("Curt", 1, 20)
wizzies.add("Curt")
Lianne = LpVariable("Lianne", 1, 20)
wizzies.add("Lianne")
Amari = LpVariable("Amari", 1, 20)
wizzies.add("Amari")
Ruben = LpVariable("Ruben", 1, 20)
wizzies.add("Ruben")
Pam = LpVariable("Pam", 1, 20)
wizzies.add("Pam")
Gene = LpVariable("Gene", 1, 20)
wizzies.add("Gene")
Janette = LpVariable("Janette", 1, 20)
wizzies.add("Janette")
Joni = LpVariable("Joni", 1, 20)
wizzies.add("Joni")

prob += 0

z0_1 = LpVariable("z0_1", cat="Binary")
z0_2 = LpVariable("z0_2", cat="Binary")
prob += Oisin + smallC <= Janette + bigM * z0_1
prob += Oisin + smallC <= Daragh + bigM * z0_2
prob += z0_1 == z0_2

z1_1 = LpVariable("z1_1", cat="Binary")
z1_2 = LpVariable("z1_2", cat="Binary")
prob += Wesley + smallC <= Ruben + bigM * z1_1
prob += Wesley + smallC <= Paris + bigM * z1_2
prob += z1_1 == z1_2

z2_1 = LpVariable("z2_1", cat="Binary")
z2_2 = LpVariable("z2_2", cat="Binary")
prob += Oisin + smallC <= Dominick + bigM * z2_1
prob += Oisin + smallC <= Daragh + bigM * z2_2
prob += z2_1 == z2_2

z3_1 = LpVariable("z3_1", cat="Binary")
z3_2 = LpVariable("z3_2", cat="Binary")
prob += Neal + smallC <= Gene + bigM * z3_1
prob += Neal + smallC <= Janette + bigM * z3_2
prob += z3_1 == z3_2

z4_1 = LpVariable("z4_1", cat="Binary")
z4_2 = LpVariable("z4_2", cat="Binary")
prob += Skylar + smallC <= Paris + bigM * z4_1
prob += Skylar + smallC <= Ruben + bigM * z4_2
prob += z4_1 == z4_2

z5_1 = LpVariable("z5_1", cat="Binary")
z5_2 = LpVariable("z5_2", cat="Binary")
prob += Ruben + smallC <= Oisin + bigM * z5_1
prob += Ruben + smallC <= Daragh + bigM * z5_2
prob += z5_1 == z5_2

z6_1 = LpVariable("z6_1", cat="Binary")
z6_2 = LpVariable("z6_2", cat="Binary")
prob += Mckenna + smallC <= Carla + bigM * z6_1
prob += Mckenna + smallC <= Conner + bigM * z6_2
prob += z6_1 == z6_2

z7_1 = LpVariable("z7_1", cat="Binary")
z7_2 = LpVariable("z7_2", cat="Binary")
prob += Oisin + smallC <= Curt + bigM * z7_1
prob += Oisin + smallC <= Mckenna + bigM * z7_2
prob += z7_1 == z7_2

z8_1 = LpVariable("z8_1", cat="Binary")
z8_2 = LpVariable("z8_2", cat="Binary")
prob += Curt + smallC <= Ruben + bigM * z8_1
prob += Curt + smallC <= Oisin + bigM * z8_2
prob += z8_1 == z8_2

z9_1 = LpVariable("z9_1", cat="Binary")
z9_2 = LpVariable("z9_2", cat="Binary")
prob += Skylar + smallC <= Gene + bigM * z9_1
prob += Skylar + smallC <= Lianne + bigM * z9_2
prob += z9_1 == z9_2

z10_1 = LpVariable("z10_1", cat="Binary")
z10_2 = LpVariable("z10_2", cat="Binary")
prob += Janette + smallC <= Conner + bigM * z10_1
prob += Janette + smallC <= Neal + bigM * z10_2
prob += z10_1 == z10_2

z11_1 = LpVariable("z11_1", cat="Binary")
z11_2 = LpVariable("z11_2", cat="Binary")
prob += Wesley + smallC <= Daragh + bigM * z11_1
prob += Wesley + smallC <= Paris + bigM * z11_2
prob += z11_1 == z11_2

z12_1 = LpVariable("z12_1", cat="Binary")
z12_2 = LpVariable("z12_2", cat="Binary")
prob += Paris + smallC <= Oisin + bigM * z12_1
prob += Paris + smallC <= Daragh + bigM * z12_2
prob += z12_1 == z12_2

z13_1 = LpVariable("z13_1", cat="Binary")
z13_2 = LpVariable("z13_2", cat="Binary")
prob += Conner + smallC <= Daragh + bigM * z13_1
prob += Conner + smallC <= Oisin + bigM * z13_2
prob += z13_1 == z13_2

z14_1 = LpVariable("z14_1", cat="Binary")
z14_2 = LpVariable("z14_2", cat="Binary")
prob += Mckenna + smallC <= Neal + bigM * z14_1
prob += Mckenna + smallC <= Dominick + bigM * z14_2
prob += z14_1 == z14_2

z15_1 = LpVariable("z15_1", cat="Binary")
z15_2 = LpVariable("z15_2", cat="Binary")
prob += Joni + smallC <= Amari + bigM * z15_1
prob += Joni + smallC <= Neal + bigM * z15_2
prob += z15_1 == z15_2

z16_1 = LpVariable("z16_1", cat="Binary")
z16_2 = LpVariable("z16_2", cat="Binary")
prob += Ruben + smallC <= Daragh + bigM * z16_1
prob += Ruben + smallC <= Oisin + bigM * z16_2
prob += z16_1 == z16_2

z17_1 = LpVariable("z17_1", cat="Binary")
z17_2 = LpVariable("z17_2", cat="Binary")
prob += Pam + smallC <= Skylar + bigM * z17_1
prob += Pam + smallC <= Wesley + bigM * z17_2
prob += z17_1 == z17_2

z18_1 = LpVariable("z18_1", cat="Binary")
z18_2 = LpVariable("z18_2", cat="Binary")
prob += Ayesha + smallC <= Janette + bigM * z18_1
prob += Ayesha + smallC <= Chase + bigM * z18_2
prob += z18_1 == z18_2

z19_1 = LpVariable("z19_1", cat="Binary")
z19_2 = LpVariable("z19_2", cat="Binary")
prob += Pam + smallC <= Paris + bigM * z19_1
prob += Pam + smallC <= Wesley + bigM * z19_2
prob += z19_1 == z19_2

z20_1 = LpVariable("z20_1", cat="Binary")
z20_2 = LpVariable("z20_2", cat="Binary")
prob += Neal + smallC <= Conner + bigM * z20_1
prob += Neal + smallC <= Mckenna + bigM * z20_2
prob += z20_1 == z20_2

z21_1 = LpVariable("z21_1", cat="Binary")
z21_2 = LpVariable("z21_2", cat="Binary")
prob += Wesley + smallC <= Skylar + bigM * z21_1
prob += Wesley + smallC <= Lianne + bigM * z21_2
prob += z21_1 == z21_2

z22_1 = LpVariable("z22_1", cat="Binary")
z22_2 = LpVariable("z22_2", cat="Binary")
prob += Daragh + smallC <= Gene + bigM * z22_1
prob += Daragh + smallC <= Curt + bigM * z22_2
prob += z22_1 == z22_2

z23_1 = LpVariable("z23_1", cat="Binary")
z23_2 = LpVariable("z23_2", cat="Binary")
prob += Conner + smallC <= Janette + bigM * z23_1
prob += Conner + smallC <= Pam + bigM * z23_2
prob += z23_1 == z23_2

z24_1 = LpVariable("z24_1", cat="Binary")
z24_2 = LpVariable("z24_2", cat="Binary")
prob += Paris + smallC <= Daragh + bigM * z24_1
prob += Paris + smallC <= Oisin + bigM * z24_2
prob += z24_1 == z24_2

z25_1 = LpVariable("z25_1", cat="Binary")
z25_2 = LpVariable("z25_2", cat="Binary")
prob += Amari + smallC <= Conner + bigM * z25_1
prob += Amari + smallC <= Neal + bigM * z25_2
prob += z25_1 == z25_2

z26_1 = LpVariable("z26_1", cat="Binary")
z26_2 = LpVariable("z26_2", cat="Binary")
prob += Amari + smallC <= Neal + bigM * z26_1
prob += Amari + smallC <= Conner + bigM * z26_2
prob += z26_1 == z26_2

z27_1 = LpVariable("z27_1", cat="Binary")
z27_2 = LpVariable("z27_2", cat="Binary")
prob += Mckenna + smallC <= Oisin + bigM * z27_1
prob += Mckenna + smallC <= Ruben + bigM * z27_2
prob += z27_1 == z27_2

z28_1 = LpVariable("z28_1", cat="Binary")
z28_2 = LpVariable("z28_2", cat="Binary")
prob += Amari + smallC <= Neal + bigM * z28_1
prob += Amari + smallC <= Conner + bigM * z28_2
prob += z28_1 == z28_2

z29_1 = LpVariable("z29_1", cat="Binary")
z29_2 = LpVariable("z29_2", cat="Binary")
prob += Oisin + smallC <= Dominick + bigM * z29_1
prob += Oisin + smallC <= Ruben + bigM * z29_2
prob += z29_1 == z29_2

z30_1 = LpVariable("z30_1", cat="Binary")
z30_2 = LpVariable("z30_2", cat="Binary")
prob += Janette + smallC <= Curt + bigM * z30_1
prob += Janette + smallC <= Skylar + bigM * z30_2
prob += z30_1 == z30_2

z31_1 = LpVariable("z31_1", cat="Binary")
z31_2 = LpVariable("z31_2", cat="Binary")
prob += Wesley + smallC <= Lianne + bigM * z31_1
prob += Wesley + smallC <= Ruben + bigM * z31_2
prob += z31_1 == z31_2

z32_1 = LpVariable("z32_1", cat="Binary")
z32_2 = LpVariable("z32_2", cat="Binary")
prob += Curt + smallC <= Gene + bigM * z32_1
prob += Curt + smallC <= Ayesha + bigM * z32_2
prob += z32_1 == z32_2

z33_1 = LpVariable("z33_1", cat="Binary")
z33_2 = LpVariable("z33_2", cat="Binary")
prob += Oisin + smallC <= Joni + bigM * z33_1
prob += Oisin + smallC <= Paris + bigM * z33_2
prob += z33_1 == z33_2

z34_1 = LpVariable("z34_1", cat="Binary")
z34_2 = LpVariable("z34_2", cat="Binary")
prob += Amari + smallC <= Joni + bigM * z34_1
prob += Amari + smallC <= Pam + bigM * z34_2
prob += z34_1 == z34_2

z35_1 = LpVariable("z35_1", cat="Binary")
z35_2 = LpVariable("z35_2", cat="Binary")
prob += Conner + smallC <= Lianne + bigM * z35_1
prob += Conner + smallC <= Janette + bigM * z35_2
prob += z35_1 == z35_2

z36_1 = LpVariable("z36_1", cat="Binary")
z36_2 = LpVariable("z36_2", cat="Binary")
prob += Skylar + smallC <= Ruben + bigM * z36_1
prob += Skylar + smallC <= Daragh + bigM * z36_2
prob += z36_1 == z36_2

z37_1 = LpVariable("z37_1", cat="Binary")
z37_2 = LpVariable("z37_2", cat="Binary")
prob += Paris + smallC <= Neal + bigM * z37_1
prob += Paris + smallC <= Gene + bigM * z37_2
prob += z37_1 == z37_2

z38_1 = LpVariable("z38_1", cat="Binary")
z38_2 = LpVariable("z38_2", cat="Binary")
prob += Daragh + smallC <= Neal + bigM * z38_1
prob += Daragh + smallC <= Pam + bigM * z38_2
prob += z38_1 == z38_2

z39_1 = LpVariable("z39_1", cat="Binary")
z39_2 = LpVariable("z39_2", cat="Binary")
prob += Skylar + smallC <= Oisin + bigM * z39_1
prob += Skylar + smallC <= Daragh + bigM * z39_2
prob += z39_1 == z39_2

z40_1 = LpVariable("z40_1", cat="Binary")
z40_2 = LpVariable("z40_2", cat="Binary")
prob += Janette + smallC <= Neal + bigM * z40_1
prob += Janette + smallC <= Conner + bigM * z40_2
prob += z40_1 == z40_2

z41_1 = LpVariable("z41_1", cat="Binary")
z41_2 = LpVariable("z41_2", cat="Binary")
prob += Curt + smallC <= Amari + bigM * z41_1
prob += Curt + smallC <= Neal + bigM * z41_2
prob += z41_1 == z41_2

z42_1 = LpVariable("z42_1", cat="Binary")
z42_2 = LpVariable("z42_2", cat="Binary")
prob += Skylar + smallC <= Lianne + bigM * z42_1
prob += Skylar + smallC <= Chase + bigM * z42_2
prob += z42_1 == z42_2

z43_1 = LpVariable("z43_1", cat="Binary")
z43_2 = LpVariable("z43_2", cat="Binary")
prob += Ayesha + smallC <= Amari + bigM * z43_1
prob += Ayesha + smallC <= Neal + bigM * z43_2
prob += z43_1 == z43_2

z44_1 = LpVariable("z44_1", cat="Binary")
z44_2 = LpVariable("z44_2", cat="Binary")
prob += Conner + smallC <= Curt + bigM * z44_1
prob += Conner + smallC <= Wesley + bigM * z44_2
prob += z44_1 == z44_2

z45_1 = LpVariable("z45_1", cat="Binary")
z45_2 = LpVariable("z45_2", cat="Binary")
prob += Janette + smallC <= Neal + bigM * z45_1
prob += Janette + smallC <= Conner + bigM * z45_2
prob += z45_1 == z45_2

z46_1 = LpVariable("z46_1", cat="Binary")
z46_2 = LpVariable("z46_2", cat="Binary")
prob += Oisin + smallC <= Lianne + bigM * z46_1
prob += Oisin + smallC <= Conner + bigM * z46_2
prob += z46_1 == z46_2

z47_1 = LpVariable("z47_1", cat="Binary")
z47_2 = LpVariable("z47_2", cat="Binary")
prob += Mckenna + smallC <= Chase + bigM * z47_1
prob += Mckenna + smallC <= Joni + bigM * z47_2
prob += z47_1 == z47_2

z48_1 = LpVariable("z48_1", cat="Binary")
z48_2 = LpVariable("z48_2", cat="Binary")
prob += Curt + smallC <= Neal + bigM * z48_1
prob += Curt + smallC <= Janette + bigM * z48_2
prob += z48_1 == z48_2

z49_1 = LpVariable("z49_1", cat="Binary")
z49_2 = LpVariable("z49_2", cat="Binary")
prob += Lianne + smallC <= Oisin + bigM * z49_1
prob += Lianne + smallC <= Ruben + bigM * z49_2
prob += z49_1 == z49_2

z50_1 = LpVariable("z50_1", cat="Binary")
z50_2 = LpVariable("z50_2", cat="Binary")
prob += Wesley + smallC <= Oisin + bigM * z50_1
prob += Wesley + smallC <= Paris + bigM * z50_2
prob += z50_1 == z50_2

z51_1 = LpVariable("z51_1", cat="Binary")
z51_2 = LpVariable("z51_2", cat="Binary")
prob += Conner + smallC <= Joni + bigM * z51_1
prob += Conner + smallC <= Carla + bigM * z51_2
prob += z51_1 == z51_2

z52_1 = LpVariable("z52_1", cat="Binary")
z52_2 = LpVariable("z52_2", cat="Binary")
prob += Skylar + smallC <= Lianne + bigM * z52_1
prob += Skylar + smallC <= Conner + bigM * z52_2
prob += z52_1 == z52_2

z53_1 = LpVariable("z53_1", cat="Binary")
z53_2 = LpVariable("z53_2", cat="Binary")
prob += Lianne + smallC <= Oisin + bigM * z53_1
prob += Lianne + smallC <= Skylar + bigM * z53_2
prob += z53_1 == z53_2

z54_1 = LpVariable("z54_1", cat="Binary")
z54_2 = LpVariable("z54_2", cat="Binary")
prob += Paris + smallC <= Oisin + bigM * z54_1
prob += Paris + smallC <= Daragh + bigM * z54_2
prob += z54_1 == z54_2

z55_1 = LpVariable("z55_1", cat="Binary")
z55_2 = LpVariable("z55_2", cat="Binary")
prob += Lianne + smallC <= Gene + bigM * z55_1
prob += Lianne + smallC <= Carla + bigM * z55_2
prob += z55_1 == z55_2

z56_1 = LpVariable("z56_1", cat="Binary")
z56_2 = LpVariable("z56_2", cat="Binary")
prob += Neal + smallC <= Amari + bigM * z56_1
prob += Neal + smallC <= Ruben + bigM * z56_2
prob += z56_1 == z56_2

z57_1 = LpVariable("z57_1", cat="Binary")
z57_2 = LpVariable("z57_2", cat="Binary")
prob += Ruben + smallC <= Chase + bigM * z57_1
prob += Ruben + smallC <= Ayesha + bigM * z57_2
prob += z57_1 == z57_2

z58_1 = LpVariable("z58_1", cat="Binary")
z58_2 = LpVariable("z58_2", cat="Binary")
prob += Ayesha + smallC <= Pam + bigM * z58_1
prob += Ayesha + smallC <= Mckenna + bigM * z58_2
prob += z58_1 == z58_2

z59_1 = LpVariable("z59_1", cat="Binary")
z59_2 = LpVariable("z59_2", cat="Binary")
prob += Neal + smallC <= Oisin + bigM * z59_1
prob += Neal + smallC <= Amari + bigM * z59_2
prob += z59_1 == z59_2

z60_1 = LpVariable("z60_1", cat="Binary")
z60_2 = LpVariable("z60_2", cat="Binary")
prob += Lianne + smallC <= Paris + bigM * z60_1
prob += Lianne + smallC <= Daragh + bigM * z60_2
prob += z60_1 == z60_2

z61_1 = LpVariable("z61_1", cat="Binary")
z61_2 = LpVariable("z61_2", cat="Binary")
prob += Paris + smallC <= Neal + bigM * z61_1
prob += Paris + smallC <= Carla + bigM * z61_2
prob += z61_1 == z61_2

z62_1 = LpVariable("z62_1", cat="Binary")
z62_2 = LpVariable("z62_2", cat="Binary")
prob += Lianne + smallC <= Paris + bigM * z62_1
prob += Lianne + smallC <= Daragh + bigM * z62_2
prob += z62_1 == z62_2

z63_1 = LpVariable("z63_1", cat="Binary")
z63_2 = LpVariable("z63_2", cat="Binary")
prob += Joni + smallC <= Chase + bigM * z63_1
prob += Joni + smallC <= Conner + bigM * z63_2
prob += z63_1 == z63_2

z64_1 = LpVariable("z64_1", cat="Binary")
z64_2 = LpVariable("z64_2", cat="Binary")
prob += Ruben + smallC <= Dominick + bigM * z64_1
prob += Ruben + smallC <= Mckenna + bigM * z64_2
prob += z64_1 == z64_2

z65_1 = LpVariable("z65_1", cat="Binary")
z65_2 = LpVariable("z65_2", cat="Binary")
prob += Lianne + smallC <= Pam + bigM * z65_1
prob += Lianne + smallC <= Janette + bigM * z65_2
prob += z65_1 == z65_2

z66_1 = LpVariable("z66_1", cat="Binary")
z66_2 = LpVariable("z66_2", cat="Binary")
prob += Pam + smallC <= Oisin + bigM * z66_1
prob += Pam + smallC <= Paris + bigM * z66_2
prob += z66_1 == z66_2

z67_1 = LpVariable("z67_1", cat="Binary")
z67_2 = LpVariable("z67_2", cat="Binary")
prob += Skylar + smallC <= Paris + bigM * z67_1
prob += Skylar + smallC <= Daragh + bigM * z67_2
prob += z67_1 == z67_2

z68_1 = LpVariable("z68_1", cat="Binary")
z68_2 = LpVariable("z68_2", cat="Binary")
prob += Oisin + smallC <= Paris + bigM * z68_1
prob += Oisin + smallC <= Gene + bigM * z68_2
prob += z68_1 == z68_2

z69_1 = LpVariable("z69_1", cat="Binary")
z69_2 = LpVariable("z69_2", cat="Binary")
prob += Skylar + smallC <= Daragh + bigM * z69_1
prob += Skylar + smallC <= Ruben + bigM * z69_2
prob += z69_1 == z69_2

z70_1 = LpVariable("z70_1", cat="Binary")
z70_2 = LpVariable("z70_2", cat="Binary")
prob += Wesley + smallC <= Mckenna + bigM * z70_1
prob += Wesley + smallC <= Oisin + bigM * z70_2
prob += z70_1 == z70_2

z71_1 = LpVariable("z71_1", cat="Binary")
z71_2 = LpVariable("z71_2", cat="Binary")
prob += Ruben + smallC <= Paris + bigM * z71_1
prob += Ruben + smallC <= Oisin + bigM * z71_2
prob += z71_1 == z71_2

z72_1 = LpVariable("z72_1", cat="Binary")
z72_2 = LpVariable("z72_2", cat="Binary")
prob += Joni + smallC <= Amari + bigM * z72_1
prob += Joni + smallC <= Janette + bigM * z72_2
prob += z72_1 == z72_2

z73_1 = LpVariable("z73_1", cat="Binary")
z73_2 = LpVariable("z73_2", cat="Binary")
prob += Conner + smallC <= Ruben + bigM * z73_1
prob += Conner + smallC <= Gene + bigM * z73_2
prob += z73_1 == z73_2

z74_1 = LpVariable("z74_1", cat="Binary")
z74_2 = LpVariable("z74_2", cat="Binary")
prob += Amari + smallC <= Paris + bigM * z74_1
prob += Amari + smallC <= Lianne + bigM * z74_2
prob += z74_1 == z74_2

z75_1 = LpVariable("z75_1", cat="Binary")
z75_2 = LpVariable("z75_2", cat="Binary")
prob += Conner + smallC <= Janette + bigM * z75_1
prob += Conner + smallC <= Gene + bigM * z75_2
prob += z75_1 == z75_2

z76_1 = LpVariable("z76_1", cat="Binary")
z76_2 = LpVariable("z76_2", cat="Binary")
prob += Janette + smallC <= Conner + bigM * z76_1
prob += Janette + smallC <= Neal + bigM * z76_2
prob += z76_1 == z76_2

z77_1 = LpVariable("z77_1", cat="Binary")
z77_2 = LpVariable("z77_2", cat="Binary")
prob += Oisin + smallC <= Paris + bigM * z77_1
prob += Oisin + smallC <= Carla + bigM * z77_2
prob += z77_1 == z77_2

z78_1 = LpVariable("z78_1", cat="Binary")
z78_2 = LpVariable("z78_2", cat="Binary")
prob += Neal + smallC <= Lianne + bigM * z78_1
prob += Neal + smallC <= Daragh + bigM * z78_2
prob += z78_1 == z78_2

z79_1 = LpVariable("z79_1", cat="Binary")
z79_2 = LpVariable("z79_2", cat="Binary")
prob += Amari + smallC <= Janette + bigM * z79_1
prob += Amari + smallC <= Neal + bigM * z79_2
prob += z79_1 == z79_2

z80_1 = LpVariable("z80_1", cat="Binary")
z80_2 = LpVariable("z80_2", cat="Binary")
prob += Curt + smallC <= Joni + bigM * z80_1
prob += Curt + smallC <= Lianne + bigM * z80_2
prob += z80_1 == z80_2

z81_1 = LpVariable("z81_1", cat="Binary")
z81_2 = LpVariable("z81_2", cat="Binary")
prob += Lianne + smallC <= Ruben + bigM * z81_1
prob += Lianne + smallC <= Daragh + bigM * z81_2
prob += z81_1 == z81_2

z82_1 = LpVariable("z82_1", cat="Binary")
z82_2 = LpVariable("z82_2", cat="Binary")
prob += Janette + smallC <= Joni + bigM * z82_1
prob += Janette + smallC <= Paris + bigM * z82_2
prob += z82_1 == z82_2

z83_1 = LpVariable("z83_1", cat="Binary")
z83_2 = LpVariable("z83_2", cat="Binary")
prob += Mckenna + smallC <= Joni + bigM * z83_1
prob += Mckenna + smallC <= Janette + bigM * z83_2
prob += z83_1 == z83_2

z84_1 = LpVariable("z84_1", cat="Binary")
z84_2 = LpVariable("z84_2", cat="Binary")
prob += Neal + smallC <= Gene + bigM * z84_1
prob += Neal + smallC <= Paris + bigM * z84_2
prob += z84_1 == z84_2

z85_1 = LpVariable("z85_1", cat="Binary")
z85_2 = LpVariable("z85_2", cat="Binary")
prob += Pam + smallC <= Joni + bigM * z85_1
prob += Pam + smallC <= Curt + bigM * z85_2
prob += z85_1 == z85_2

z86_1 = LpVariable("z86_1", cat="Binary")
z86_2 = LpVariable("z86_2", cat="Binary")
prob += Daragh + smallC <= Lianne + bigM * z86_1
prob += Daragh + smallC <= Ayesha + bigM * z86_2
prob += z86_1 == z86_2

z87_1 = LpVariable("z87_1", cat="Binary")
z87_2 = LpVariable("z87_2", cat="Binary")
prob += Curt + smallC <= Janette + bigM * z87_1
prob += Curt + smallC <= Amari + bigM * z87_2
prob += z87_1 == z87_2

z88_1 = LpVariable("z88_1", cat="Binary")
z88_2 = LpVariable("z88_2", cat="Binary")
prob += Ayesha + smallC <= Janette + bigM * z88_1
prob += Ayesha + smallC <= Chase + bigM * z88_2
prob += z88_1 == z88_2

z89_1 = LpVariable("z89_1", cat="Binary")
z89_2 = LpVariable("z89_2", cat="Binary")
prob += Amari + smallC <= Conner + bigM * z89_1
prob += Amari + smallC <= Neal + bigM * z89_2
prob += z89_1 == z89_2

z90_1 = LpVariable("z90_1", cat="Binary")
z90_2 = LpVariable("z90_2", cat="Binary")
prob += Amari + smallC <= Neal + bigM * z90_1
prob += Amari + smallC <= Janette + bigM * z90_2
prob += z90_1 == z90_2

z91_1 = LpVariable("z91_1", cat="Binary")
z91_2 = LpVariable("z91_2", cat="Binary")
prob += Mckenna + smallC <= Skylar + bigM * z91_1
prob += Mckenna + smallC <= Oisin + bigM * z91_2
prob += z91_1 == z91_2

z92_1 = LpVariable("z92_1", cat="Binary")
z92_2 = LpVariable("z92_2", cat="Binary")
prob += Ayesha + smallC <= Oisin + bigM * z92_1
prob += Ayesha + smallC <= Paris + bigM * z92_2
prob += z92_1 == z92_2

z93_1 = LpVariable("z93_1", cat="Binary")
z93_2 = LpVariable("z93_2", cat="Binary")
prob += Paris + smallC <= Ruben + bigM * z93_1
prob += Paris + smallC <= Skylar + bigM * z93_2
prob += z93_1 == z93_2

z94_1 = LpVariable("z94_1", cat="Binary")
z94_2 = LpVariable("z94_2", cat="Binary")
prob += Mckenna + smallC <= Lianne + bigM * z94_1
prob += Mckenna + smallC <= Ruben + bigM * z94_2
prob += z94_1 == z94_2

z95_1 = LpVariable("z95_1", cat="Binary")
z95_2 = LpVariable("z95_2", cat="Binary")
prob += Mckenna + smallC <= Joni + bigM * z95_1
prob += Mckenna + smallC <= Pam + bigM * z95_2
prob += z95_1 == z95_2

z96_1 = LpVariable("z96_1", cat="Binary")
z96_2 = LpVariable("z96_2", cat="Binary")
prob += Oisin + smallC <= Dominick + bigM * z96_1
prob += Oisin + smallC <= Amari + bigM * z96_2
prob += z96_1 == z96_2

z97_1 = LpVariable("z97_1", cat="Binary")
z97_2 = LpVariable("z97_2", cat="Binary")
prob += Daragh + smallC <= Pam + bigM * z97_1
prob += Daragh + smallC <= Gene + bigM * z97_2
prob += z97_1 == z97_2

z98_1 = LpVariable("z98_1", cat="Binary")
z98_2 = LpVariable("z98_2", cat="Binary")
prob += Ruben + smallC <= Oisin + bigM * z98_1
prob += Ruben + smallC <= Daragh + bigM * z98_2
prob += z98_1 == z98_2

z99_1 = LpVariable("z99_1", cat="Binary")
z99_2 = LpVariable("z99_2", cat="Binary")
prob += Amari + smallC <= Chase + bigM * z99_1
prob += Amari + smallC <= Pam + bigM * z99_2
prob += z99_1 == z99_2

z100_1 = LpVariable("z100_1", cat="Binary")
z100_2 = LpVariable("z100_2", cat="Binary")
prob += Joni + smallC <= Paris + bigM * z100_1
prob += Joni + smallC <= Wesley + bigM * z100_2
prob += z100_1 == z100_2

z101_1 = LpVariable("z101_1", cat="Binary")
z101_2 = LpVariable("z101_2", cat="Binary")
prob += Ayesha + smallC <= Wesley + bigM * z101_1
prob += Ayesha + smallC <= Oisin + bigM * z101_2
prob += z101_1 == z101_2

z102_1 = LpVariable("z102_1", cat="Binary")
z102_2 = LpVariable("z102_2", cat="Binary")
prob += Skylar + smallC <= Lianne + bigM * z102_1
prob += Skylar + smallC <= Wesley + bigM * z102_2
prob += z102_1 == z102_2

z103_1 = LpVariable("z103_1", cat="Binary")
z103_2 = LpVariable("z103_2", cat="Binary")
prob += Paris + smallC <= Oisin + bigM * z103_1
prob += Paris + smallC <= Daragh + bigM * z103_2
prob += z103_1 == z103_2

z104_1 = LpVariable("z104_1", cat="Binary")
z104_2 = LpVariable("z104_2", cat="Binary")
prob += Conner + smallC <= Lianne + bigM * z104_1
prob += Conner + smallC <= Daragh + bigM * z104_2
prob += z104_1 == z104_2

z105_1 = LpVariable("z105_1", cat="Binary")
z105_2 = LpVariable("z105_2", cat="Binary")
prob += Neal + smallC <= Mckenna + bigM * z105_1
prob += Neal + smallC <= Janette + bigM * z105_2
prob += z105_1 == z105_2

z106_1 = LpVariable("z106_1", cat="Binary")
z106_2 = LpVariable("z106_2", cat="Binary")
prob += Ayesha + smallC <= Neal + bigM * z106_1
prob += Ayesha + smallC <= Amari + bigM * z106_2
prob += z106_1 == z106_2

z107_1 = LpVariable("z107_1", cat="Binary")
z107_2 = LpVariable("z107_2", cat="Binary")
prob += Skylar + smallC <= Conner + bigM * z107_1
prob += Skylar + smallC <= Mckenna + bigM * z107_2
prob += z107_1 == z107_2

z108_1 = LpVariable("z108_1", cat="Binary")
z108_2 = LpVariable("z108_2", cat="Binary")
prob += Amari + smallC <= Janette + bigM * z108_1
prob += Amari + smallC <= Neal + bigM * z108_2
prob += z108_1 == z108_2

z109_1 = LpVariable("z109_1", cat="Binary")
z109_2 = LpVariable("z109_2", cat="Binary")
prob += Paris + smallC <= Oisin + bigM * z109_1
prob += Paris + smallC <= Daragh + bigM * z109_2
prob += z109_1 == z109_2

z110_1 = LpVariable("z110_1", cat="Binary")
z110_2 = LpVariable("z110_2", cat="Binary")
prob += Janette + smallC <= Daragh + bigM * z110_1
prob += Janette + smallC <= Lianne + bigM * z110_2
prob += z110_1 == z110_2

z111_1 = LpVariable("z111_1", cat="Binary")
z111_2 = LpVariable("z111_2", cat="Binary")
prob += Ayesha + smallC <= Amari + bigM * z111_1
prob += Ayesha + smallC <= Curt + bigM * z111_2
prob += z111_1 == z111_2

z112_1 = LpVariable("z112_1", cat="Binary")
z112_2 = LpVariable("z112_2", cat="Binary")
prob += Skylar + smallC <= Paris + bigM * z112_1
prob += Skylar + smallC <= Daragh + bigM * z112_2
prob += z112_1 == z112_2

z113_1 = LpVariable("z113_1", cat="Binary")
z113_2 = LpVariable("z113_2", cat="Binary")
prob += Amari + smallC <= Lianne + bigM * z113_1
prob += Amari + smallC <= Gene + bigM * z113_2
prob += z113_1 == z113_2

z114_1 = LpVariable("z114_1", cat="Binary")
z114_2 = LpVariable("z114_2", cat="Binary")
prob += Mckenna + smallC <= Conner + bigM * z114_1
prob += Mckenna + smallC <= Dominick + bigM * z114_2
prob += z114_1 == z114_2

z115_1 = LpVariable("z115_1", cat="Binary")
z115_2 = LpVariable("z115_2", cat="Binary")
prob += Amari + smallC <= Skylar + bigM * z115_1
prob += Amari + smallC <= Curt + bigM * z115_2
prob += z115_1 == z115_2

z116_1 = LpVariable("z116_1", cat="Binary")
z116_2 = LpVariable("z116_2", cat="Binary")
prob += Ayesha + smallC <= Paris + bigM * z116_1
prob += Ayesha + smallC <= Wesley + bigM * z116_2
prob += z116_1 == z116_2

z117_1 = LpVariable("z117_1", cat="Binary")
z117_2 = LpVariable("z117_2", cat="Binary")
prob += Oisin + smallC <= Neal + bigM * z117_1
prob += Oisin + smallC <= Wesley + bigM * z117_2
prob += z117_1 == z117_2

z118_1 = LpVariable("z118_1", cat="Binary")
z118_2 = LpVariable("z118_2", cat="Binary")
prob += Mckenna + smallC <= Lianne + bigM * z118_1
prob += Mckenna + smallC <= Skylar + bigM * z118_2
prob += z118_1 == z118_2

z119_1 = LpVariable("z119_1", cat="Binary")
z119_2 = LpVariable("z119_2", cat="Binary")
prob += Janette + smallC <= Mckenna + bigM * z119_1
prob += Janette + smallC <= Ayesha + bigM * z119_2
prob += z119_1 == z119_2

z120_1 = LpVariable("z120_1", cat="Binary")
z120_2 = LpVariable("z120_2", cat="Binary")
prob += Mckenna + smallC <= Oisin + bigM * z120_1
prob += Mckenna + smallC <= Skylar + bigM * z120_2
prob += z120_1 == z120_2

z121_1 = LpVariable("z121_1", cat="Binary")
z121_2 = LpVariable("z121_2", cat="Binary")
prob += Pam + smallC <= Mckenna + bigM * z121_1
prob += Pam + smallC <= Wesley + bigM * z121_2
prob += z121_1 == z121_2

z122_1 = LpVariable("z122_1", cat="Binary")
z122_2 = LpVariable("z122_2", cat="Binary")
prob += Neal + smallC <= Skylar + bigM * z122_1
prob += Neal + smallC <= Conner + bigM * z122_2
prob += z122_1 == z122_2

z123_1 = LpVariable("z123_1", cat="Binary")
z123_2 = LpVariable("z123_2", cat="Binary")
prob += Ayesha + smallC <= Carla + bigM * z123_1
prob += Ayesha + smallC <= Chase + bigM * z123_2
prob += z123_1 == z123_2

z124_1 = LpVariable("z124_1", cat="Binary")
z124_2 = LpVariable("z124_2", cat="Binary")
prob += Pam + smallC <= Ruben + bigM * z124_1
prob += Pam + smallC <= Lianne + bigM * z124_2
prob += z124_1 == z124_2

z125_1 = LpVariable("z125_1", cat="Binary")
z125_2 = LpVariable("z125_2", cat="Binary")
prob += Conner + smallC <= Janette + bigM * z125_1
prob += Conner + smallC <= Curt + bigM * z125_2
prob += z125_1 == z125_2

z126_1 = LpVariable("z126_1", cat="Binary")
z126_2 = LpVariable("z126_2", cat="Binary")
prob += Pam + smallC <= Paris + bigM * z126_1
prob += Pam + smallC <= Wesley + bigM * z126_2
prob += z126_1 == z126_2

z127_1 = LpVariable("z127_1", cat="Binary")
z127_2 = LpVariable("z127_2", cat="Binary")
prob += Pam + smallC <= Oisin + bigM * z127_1
prob += Pam + smallC <= Paris + bigM * z127_2
prob += z127_1 == z127_2

z128_1 = LpVariable("z128_1", cat="Binary")
z128_2 = LpVariable("z128_2", cat="Binary")
prob += Neal + smallC <= Conner + bigM * z128_1
prob += Neal + smallC <= Curt + bigM * z128_2
prob += z128_1 == z128_2

z129_1 = LpVariable("z129_1", cat="Binary")
z129_2 = LpVariable("z129_2", cat="Binary")
prob += Lianne + smallC <= Oisin + bigM * z129_1
prob += Lianne + smallC <= Ruben + bigM * z129_2
prob += z129_1 == z129_2

z130_1 = LpVariable("z130_1", cat="Binary")
z130_2 = LpVariable("z130_2", cat="Binary")
prob += Janette + smallC <= Dominick + bigM * z130_1
prob += Janette + smallC <= Daragh + bigM * z130_2
prob += z130_1 == z130_2

z131_1 = LpVariable("z131_1", cat="Binary")
z131_2 = LpVariable("z131_2", cat="Binary")
prob += Amari + smallC <= Conner + bigM * z131_1
prob += Amari + smallC <= Neal + bigM * z131_2
prob += z131_1 == z131_2

z132_1 = LpVariable("z132_1", cat="Binary")
z132_2 = LpVariable("z132_2", cat="Binary")
prob += Mckenna + smallC <= Dominick + bigM * z132_1
prob += Mckenna + smallC <= Joni + bigM * z132_2
prob += z132_1 == z132_2

z133_1 = LpVariable("z133_1", cat="Binary")
z133_2 = LpVariable("z133_2", cat="Binary")
prob += Neal + smallC <= Dominick + bigM * z133_1
prob += Neal + smallC <= Chase + bigM * z133_2
prob += z133_1 == z133_2

z134_1 = LpVariable("z134_1", cat="Binary")
z134_2 = LpVariable("z134_2", cat="Binary")
prob += Wesley + smallC <= Daragh + bigM * z134_1
prob += Wesley + smallC <= Oisin + bigM * z134_2
prob += z134_1 == z134_2

z135_1 = LpVariable("z135_1", cat="Binary")
z135_2 = LpVariable("z135_2", cat="Binary")
prob += Janette + smallC <= Conner + bigM * z135_1
prob += Janette + smallC <= Neal + bigM * z135_2
prob += z135_1 == z135_2

z136_1 = LpVariable("z136_1", cat="Binary")
z136_2 = LpVariable("z136_2", cat="Binary")
prob += Lianne + smallC <= Skylar + bigM * z136_1
prob += Lianne + smallC <= Paris + bigM * z136_2
prob += z136_1 == z136_2

z137_1 = LpVariable("z137_1", cat="Binary")
z137_2 = LpVariable("z137_2", cat="Binary")
prob += Ruben + smallC <= Janette + bigM * z137_1
prob += Ruben + smallC <= Gene + bigM * z137_2
prob += z137_1 == z137_2

z138_1 = LpVariable("z138_1", cat="Binary")
z138_2 = LpVariable("z138_2", cat="Binary")
prob += Joni + smallC <= Carla + bigM * z138_1
prob += Joni + smallC <= Amari + bigM * z138_2
prob += z138_1 == z138_2

z139_1 = LpVariable("z139_1", cat="Binary")
z139_2 = LpVariable("z139_2", cat="Binary")
prob += Oisin + smallC <= Dominick + bigM * z139_1
prob += Oisin + smallC <= Skylar + bigM * z139_2
prob += z139_1 == z139_2

z140_1 = LpVariable("z140_1", cat="Binary")
z140_2 = LpVariable("z140_2", cat="Binary")
prob += Mckenna + smallC <= Dominick + bigM * z140_1
prob += Mckenna + smallC <= Chase + bigM * z140_2
prob += z140_1 == z140_2

z141_1 = LpVariable("z141_1", cat="Binary")
z141_2 = LpVariable("z141_2", cat="Binary")
prob += Janette + smallC <= Conner + bigM * z141_1
prob += Janette + smallC <= Neal + bigM * z141_2
prob += z141_1 == z141_2

z142_1 = LpVariable("z142_1", cat="Binary")
z142_2 = LpVariable("z142_2", cat="Binary")
prob += Daragh + smallC <= Wesley + bigM * z142_1
prob += Daragh + smallC <= Neal + bigM * z142_2
prob += z142_1 == z142_2

z143_1 = LpVariable("z143_1", cat="Binary")
z143_2 = LpVariable("z143_2", cat="Binary")
prob += Curt + smallC <= Wesley + bigM * z143_1
prob += Curt + smallC <= Lianne + bigM * z143_2
prob += z143_1 == z143_2

z144_1 = LpVariable("z144_1", cat="Binary")
z144_2 = LpVariable("z144_2", cat="Binary")
prob += Amari + smallC <= Janette + bigM * z144_1
prob += Amari + smallC <= Neal + bigM * z144_2
prob += z144_1 == z144_2

z145_1 = LpVariable("z145_1", cat="Binary")
z145_2 = LpVariable("z145_2", cat="Binary")
prob += Oisin + smallC <= Chase + bigM * z145_1
prob += Oisin + smallC <= Conner + bigM * z145_2
prob += z145_1 == z145_2

z146_1 = LpVariable("z146_1", cat="Binary")
z146_2 = LpVariable("z146_2", cat="Binary")
prob += Pam + smallC <= Paris + bigM * z146_1
prob += Pam + smallC <= Skylar + bigM * z146_2
prob += z146_1 == z146_2

z147_1 = LpVariable("z147_1", cat="Binary")
z147_2 = LpVariable("z147_2", cat="Binary")
prob += Janette + smallC <= Joni + bigM * z147_1
prob += Janette + smallC <= Amari + bigM * z147_2
prob += z147_1 == z147_2

z148_1 = LpVariable("z148_1", cat="Binary")
z148_2 = LpVariable("z148_2", cat="Binary")
prob += Ruben + smallC <= Amari + bigM * z148_1
prob += Ruben + smallC <= Ayesha + bigM * z148_2
prob += z148_1 == z148_2

z149_1 = LpVariable("z149_1", cat="Binary")
z149_2 = LpVariable("z149_2", cat="Binary")
prob += Conner + smallC <= Curt + bigM * z149_1
prob += Conner + smallC <= Chase + bigM * z149_2
prob += z149_1 == z149_2

z150_1 = LpVariable("z150_1", cat="Binary")
z150_2 = LpVariable("z150_2", cat="Binary")
prob += Joni + smallC <= Amari + bigM * z150_1
prob += Joni + smallC <= Curt + bigM * z150_2
prob += z150_1 == z150_2

z151_1 = LpVariable("z151_1", cat="Binary")
z151_2 = LpVariable("z151_2", cat="Binary")
prob += Lianne + smallC <= Pam + bigM * z151_1
prob += Lianne + smallC <= Carla + bigM * z151_2
prob += z151_1 == z151_2

z152_1 = LpVariable("z152_1", cat="Binary")
z152_2 = LpVariable("z152_2", cat="Binary")
prob += Paris + smallC <= Oisin + bigM * z152_1
prob += Paris + smallC <= Daragh + bigM * z152_2
prob += z152_1 == z152_2

z153_1 = LpVariable("z153_1", cat="Binary")
z153_2 = LpVariable("z153_2", cat="Binary")
prob += Wesley + smallC <= Ruben + bigM * z153_1
prob += Wesley + smallC <= Mckenna + bigM * z153_2
prob += z153_1 == z153_2

z154_1 = LpVariable("z154_1", cat="Binary")
z154_2 = LpVariable("z154_2", cat="Binary")
prob += Lianne + smallC <= Carla + bigM * z154_1
prob += Lianne + smallC <= Chase + bigM * z154_2
prob += z154_1 == z154_2

z155_1 = LpVariable("z155_1", cat="Binary")
z155_2 = LpVariable("z155_2", cat="Binary")
prob += Curt + smallC <= Conner + bigM * z155_1
prob += Curt + smallC <= Janette + bigM * z155_2
prob += z155_1 == z155_2

z156_1 = LpVariable("z156_1", cat="Binary")
z156_2 = LpVariable("z156_2", cat="Binary")
prob += Pam + smallC <= Carla + bigM * z156_1
prob += Pam + smallC <= Chase + bigM * z156_2
prob += z156_1 == z156_2

z157_1 = LpVariable("z157_1", cat="Binary")
z157_2 = LpVariable("z157_2", cat="Binary")
prob += Conner + smallC <= Daragh + bigM * z157_1
prob += Conner + smallC <= Ayesha + bigM * z157_2
prob += z157_1 == z157_2

z158_1 = LpVariable("z158_1", cat="Binary")
z158_2 = LpVariable("z158_2", cat="Binary")
prob += Pam + smallC <= Lianne + bigM * z158_1
prob += Pam + smallC <= Daragh + bigM * z158_2
prob += z158_1 == z158_2

z159_1 = LpVariable("z159_1", cat="Binary")
z159_2 = LpVariable("z159_2", cat="Binary")
prob += Curt + smallC <= Amari + bigM * z159_1
prob += Curt + smallC <= Neal + bigM * z159_2
prob += z159_1 == z159_2

z160_1 = LpVariable("z160_1", cat="Binary")
z160_2 = LpVariable("z160_2", cat="Binary")
prob += Oisin + smallC <= Carla + bigM * z160_1
prob += Oisin + smallC <= Gene + bigM * z160_2
prob += z160_1 == z160_2

z161_1 = LpVariable("z161_1", cat="Binary")
z161_2 = LpVariable("z161_2", cat="Binary")
prob += Neal + smallC <= Gene + bigM * z161_1
prob += Neal + smallC <= Lianne + bigM * z161_2
prob += z161_1 == z161_2

z162_1 = LpVariable("z162_1", cat="Binary")
z162_2 = LpVariable("z162_2", cat="Binary")
prob += Janette + smallC <= Neal + bigM * z162_1
prob += Janette + smallC <= Conner + bigM * z162_2
prob += z162_1 == z162_2

z163_1 = LpVariable("z163_1", cat="Binary")
z163_2 = LpVariable("z163_2", cat="Binary")
prob += Lianne + smallC <= Skylar + bigM * z163_1
prob += Lianne + smallC <= Ruben + bigM * z163_2
prob += z163_1 == z163_2

z164_1 = LpVariable("z164_1", cat="Binary")
z164_2 = LpVariable("z164_2", cat="Binary")
prob += Curt + smallC <= Oisin + bigM * z164_1
prob += Curt + smallC <= Ayesha + bigM * z164_2
prob += z164_1 == z164_2

z165_1 = LpVariable("z165_1", cat="Binary")
z165_2 = LpVariable("z165_2", cat="Binary")
prob += Janette + smallC <= Skylar + bigM * z165_1
prob += Janette + smallC <= Daragh + bigM * z165_2
prob += z165_1 == z165_2

z166_1 = LpVariable("z166_1", cat="Binary")
z166_2 = LpVariable("z166_2", cat="Binary")
prob += Paris + smallC <= Conner + bigM * z166_1
prob += Paris + smallC <= Curt + bigM * z166_2
prob += z166_1 == z166_2

z167_1 = LpVariable("z167_1", cat="Binary")
z167_2 = LpVariable("z167_2", cat="Binary")
prob += Mckenna + smallC <= Paris + bigM * z167_1
prob += Mckenna + smallC <= Daragh + bigM * z167_2
prob += z167_1 == z167_2

z168_1 = LpVariable("z168_1", cat="Binary")
z168_2 = LpVariable("z168_2", cat="Binary")
prob += Ruben + smallC <= Daragh + bigM * z168_1
prob += Ruben + smallC <= Oisin + bigM * z168_2
prob += z168_1 == z168_2

z169_1 = LpVariable("z169_1", cat="Binary")
z169_2 = LpVariable("z169_2", cat="Binary")
prob += Daragh + smallC <= Ayesha + bigM * z169_1
prob += Daragh + smallC <= Paris + bigM * z169_2
prob += z169_1 == z169_2

z170_1 = LpVariable("z170_1", cat="Binary")
z170_2 = LpVariable("z170_2", cat="Binary")
prob += Skylar + smallC <= Mckenna + bigM * z170_1
prob += Skylar + smallC <= Lianne + bigM * z170_2
prob += z170_1 == z170_2

z171_1 = LpVariable("z171_1", cat="Binary")
z171_2 = LpVariable("z171_2", cat="Binary")
prob += Conner + smallC <= Chase + bigM * z171_1
prob += Conner + smallC <= Skylar + bigM * z171_2
prob += z171_1 == z171_2

z172_1 = LpVariable("z172_1", cat="Binary")
z172_2 = LpVariable("z172_2", cat="Binary")
prob += Ruben + smallC <= Paris + bigM * z172_1
prob += Ruben + smallC <= Oisin + bigM * z172_2
prob += z172_1 == z172_2

z173_1 = LpVariable("z173_1", cat="Binary")
z173_2 = LpVariable("z173_2", cat="Binary")
prob += Pam + smallC <= Daragh + bigM * z173_1
prob += Pam + smallC <= Ruben + bigM * z173_2
prob += z173_1 == z173_2

z174_1 = LpVariable("z174_1", cat="Binary")
z174_2 = LpVariable("z174_2", cat="Binary")
prob += Curt + smallC <= Chase + bigM * z174_1
prob += Curt + smallC <= Daragh + bigM * z174_2
prob += z174_1 == z174_2

z175_1 = LpVariable("z175_1", cat="Binary")
z175_2 = LpVariable("z175_2", cat="Binary")
prob += Wesley + smallC <= Joni + bigM * z175_1
prob += Wesley + smallC <= Pam + bigM * z175_2
prob += z175_1 == z175_2

z176_1 = LpVariable("z176_1", cat="Binary")
z176_2 = LpVariable("z176_2", cat="Binary")
prob += Ayesha + smallC <= Chase + bigM * z176_1
prob += Ayesha + smallC <= Curt + bigM * z176_2
prob += z176_1 == z176_2

z177_1 = LpVariable("z177_1", cat="Binary")
z177_2 = LpVariable("z177_2", cat="Binary")
prob += Conner + smallC <= Carla + bigM * z177_1
prob += Conner + smallC <= Wesley + bigM * z177_2
prob += z177_1 == z177_2

z178_1 = LpVariable("z178_1", cat="Binary")
z178_2 = LpVariable("z178_2", cat="Binary")
prob += Paris + smallC <= Daragh + bigM * z178_1
prob += Paris + smallC <= Oisin + bigM * z178_2
prob += z178_1 == z178_2

z179_1 = LpVariable("z179_1", cat="Binary")
z179_2 = LpVariable("z179_2", cat="Binary")
prob += Ayesha + smallC <= Neal + bigM * z179_1
prob += Ayesha + smallC <= Carla + bigM * z179_2
prob += z179_1 == z179_2

z180_1 = LpVariable("z180_1", cat="Binary")
z180_2 = LpVariable("z180_2", cat="Binary")
prob += Pam + smallC <= Chase + bigM * z180_1
prob += Pam + smallC <= Ayesha + bigM * z180_2
prob += z180_1 == z180_2

z181_1 = LpVariable("z181_1", cat="Binary")
z181_2 = LpVariable("z181_2", cat="Binary")
prob += Mckenna + smallC <= Janette + bigM * z181_1
prob += Mckenna + smallC <= Ayesha + bigM * z181_2
prob += z181_1 == z181_2

z182_1 = LpVariable("z182_1", cat="Binary")
z182_2 = LpVariable("z182_2", cat="Binary")
prob += Oisin + smallC <= Curt + bigM * z182_1
prob += Oisin + smallC <= Wesley + bigM * z182_2
prob += z182_1 == z182_2

z183_1 = LpVariable("z183_1", cat="Binary")
z183_2 = LpVariable("z183_2", cat="Binary")
prob += Conner + smallC <= Janette + bigM * z183_1
prob += Conner + smallC <= Daragh + bigM * z183_2
prob += z183_1 == z183_2

z184_1 = LpVariable("z184_1", cat="Binary")
z184_2 = LpVariable("z184_2", cat="Binary")
prob += Ayesha + smallC <= Oisin + bigM * z184_1
prob += Ayesha + smallC <= Daragh + bigM * z184_2
prob += z184_1 == z184_2

z185_1 = LpVariable("z185_1", cat="Binary")
z185_2 = LpVariable("z185_2", cat="Binary")
prob += Ruben + smallC <= Paris + bigM * z185_1
prob += Ruben + smallC <= Oisin + bigM * z185_2
prob += z185_1 == z185_2

z186_1 = LpVariable("z186_1", cat="Binary")
z186_2 = LpVariable("z186_2", cat="Binary")
prob += Daragh + smallC <= Carla + bigM * z186_1
prob += Daragh + smallC <= Curt + bigM * z186_2
prob += z186_1 == z186_2

z187_1 = LpVariable("z187_1", cat="Binary")
z187_2 = LpVariable("z187_2", cat="Binary")
prob += Lianne + smallC <= Paris + bigM * z187_1
prob += Lianne + smallC <= Skylar + bigM * z187_2
prob += z187_1 == z187_2

z188_1 = LpVariable("z188_1", cat="Binary")
z188_2 = LpVariable("z188_2", cat="Binary")
prob += Joni + smallC <= Ayesha + bigM * z188_1
prob += Joni + smallC <= Chase + bigM * z188_2
prob += z188_1 == z188_2

z189_1 = LpVariable("z189_1", cat="Binary")
z189_2 = LpVariable("z189_2", cat="Binary")
prob += Neal + smallC <= Conner + bigM * z189_1
prob += Neal + smallC <= Chase + bigM * z189_2
prob += z189_1 == z189_2

z190_1 = LpVariable("z190_1", cat="Binary")
z190_2 = LpVariable("z190_2", cat="Binary")
prob += Janette + smallC <= Amari + bigM * z190_1
prob += Janette + smallC <= Lianne + bigM * z190_2
prob += z190_1 == z190_2

z191_1 = LpVariable("z191_1", cat="Binary")
z191_2 = LpVariable("z191_2", cat="Binary")
prob += Neal + smallC <= Janette + bigM * z191_1
prob += Neal + smallC <= Chase + bigM * z191_2
prob += z191_1 == z191_2

z192_1 = LpVariable("z192_1", cat="Binary")
z192_2 = LpVariable("z192_2", cat="Binary")
prob += Daragh + smallC <= Joni + bigM * z192_1
prob += Daragh + smallC <= Carla + bigM * z192_2
prob += z192_1 == z192_2

z193_1 = LpVariable("z193_1", cat="Binary")
z193_2 = LpVariable("z193_2", cat="Binary")
prob += Amari + smallC <= Neal + bigM * z193_1
prob += Amari + smallC <= Conner + bigM * z193_2
prob += z193_1 == z193_2

z194_1 = LpVariable("z194_1", cat="Binary")
z194_2 = LpVariable("z194_2", cat="Binary")
prob += Joni + smallC <= Mckenna + bigM * z194_1
prob += Joni + smallC <= Daragh + bigM * z194_2
prob += z194_1 == z194_2

z195_1 = LpVariable("z195_1", cat="Binary")
z195_2 = LpVariable("z195_2", cat="Binary")
prob += Skylar + smallC <= Paris + bigM * z195_1
prob += Skylar + smallC <= Ruben + bigM * z195_2
prob += z195_1 == z195_2

z196_1 = LpVariable("z196_1", cat="Binary")
z196_2 = LpVariable("z196_2", cat="Binary")
prob += Ruben + smallC <= Joni + bigM * z196_1
prob += Ruben + smallC <= Amari + bigM * z196_2
prob += z196_1 == z196_2

z197_1 = LpVariable("z197_1", cat="Binary")
z197_2 = LpVariable("z197_2", cat="Binary")
prob += Neal + smallC <= Chase + bigM * z197_1
prob += Neal + smallC <= Oisin + bigM * z197_2
prob += z197_1 == z197_2

z198_1 = LpVariable("z198_1", cat="Binary")
z198_2 = LpVariable("z198_2", cat="Binary")
prob += Ruben + smallC <= Curt + bigM * z198_1
prob += Ruben + smallC <= Janette + bigM * z198_2
prob += z198_1 == z198_2

z199_1 = LpVariable("z199_1", cat="Binary")
z199_2 = LpVariable("z199_2", cat="Binary")
prob += Skylar + smallC <= Oisin + bigM * z199_1
prob += Skylar + smallC <= Ruben + bigM * z199_2
prob += z199_1 == z199_2

z200_1 = LpVariable("z200_1", cat="Binary")
z200_2 = LpVariable("z200_2", cat="Binary")
prob += Paris + smallC <= Chase + bigM * z200_1
prob += Paris + smallC <= Wesley + bigM * z200_2
prob += z200_1 == z200_2

z201_1 = LpVariable("z201_1", cat="Binary")
z201_2 = LpVariable("z201_2", cat="Binary")
prob += Paris + smallC <= Daragh + bigM * z201_1
prob += Paris + smallC <= Oisin + bigM * z201_2
prob += z201_1 == z201_2

z202_1 = LpVariable("z202_1", cat="Binary")
z202_2 = LpVariable("z202_2", cat="Binary")
prob += Joni + smallC <= Gene + bigM * z202_1
prob += Joni + smallC <= Ayesha + bigM * z202_2
prob += z202_1 == z202_2

z203_1 = LpVariable("z203_1", cat="Binary")
z203_2 = LpVariable("z203_2", cat="Binary")
prob += Curt + smallC <= Neal + bigM * z203_1
prob += Curt + smallC <= Janette + bigM * z203_2
prob += z203_1 == z203_2

z204_1 = LpVariable("z204_1", cat="Binary")
z204_2 = LpVariable("z204_2", cat="Binary")
prob += Ayesha + smallC <= Joni + bigM * z204_1
prob += Ayesha + smallC <= Oisin + bigM * z204_2
prob += z204_1 == z204_2

z205_1 = LpVariable("z205_1", cat="Binary")
z205_2 = LpVariable("z205_2", cat="Binary")
prob += Oisin + smallC <= Joni + bigM * z205_1
prob += Oisin + smallC <= Ayesha + bigM * z205_2
prob += z205_1 == z205_2

z206_1 = LpVariable("z206_1", cat="Binary")
z206_2 = LpVariable("z206_2", cat="Binary")
prob += Janette + smallC <= Oisin + bigM * z206_1
prob += Janette + smallC <= Chase + bigM * z206_2
prob += z206_1 == z206_2

z207_1 = LpVariable("z207_1", cat="Binary")
z207_2 = LpVariable("z207_2", cat="Binary")
prob += Janette + smallC <= Neal + bigM * z207_1
prob += Janette + smallC <= Conner + bigM * z207_2
prob += z207_1 == z207_2

z208_1 = LpVariable("z208_1", cat="Binary")
z208_2 = LpVariable("z208_2", cat="Binary")
prob += Pam + smallC <= Skylar + bigM * z208_1
prob += Pam + smallC <= Daragh + bigM * z208_2
prob += z208_1 == z208_2

z209_1 = LpVariable("z209_1", cat="Binary")
z209_2 = LpVariable("z209_2", cat="Binary")
prob += Oisin + smallC <= Skylar + bigM * z209_1
prob += Oisin + smallC <= Paris + bigM * z209_2
prob += z209_1 == z209_2

z210_1 = LpVariable("z210_1", cat="Binary")
z210_2 = LpVariable("z210_2", cat="Binary")
prob += Joni + smallC <= Pam + bigM * z210_1
prob += Joni + smallC <= Daragh + bigM * z210_2
prob += z210_1 == z210_2

z211_1 = LpVariable("z211_1", cat="Binary")
z211_2 = LpVariable("z211_2", cat="Binary")
prob += Wesley + smallC <= Lianne + bigM * z211_1
prob += Wesley + smallC <= Oisin + bigM * z211_2
prob += z211_1 == z211_2

z212_1 = LpVariable("z212_1", cat="Binary")
z212_2 = LpVariable("z212_2", cat="Binary")
prob += Paris + smallC <= Oisin + bigM * z212_1
prob += Paris + smallC <= Daragh + bigM * z212_2
prob += z212_1 == z212_2

z213_1 = LpVariable("z213_1", cat="Binary")
z213_2 = LpVariable("z213_2", cat="Binary")
prob += Wesley + smallC <= Mckenna + bigM * z213_1
prob += Wesley + smallC <= Lianne + bigM * z213_2
prob += z213_1 == z213_2

z214_1 = LpVariable("z214_1", cat="Binary")
z214_2 = LpVariable("z214_2", cat="Binary")
prob += Joni + smallC <= Daragh + bigM * z214_1
prob += Joni + smallC <= Lianne + bigM * z214_2
prob += z214_1 == z214_2

z215_1 = LpVariable("z215_1", cat="Binary")
z215_2 = LpVariable("z215_2", cat="Binary")
prob += Neal + smallC <= Mckenna + bigM * z215_1
prob += Neal + smallC <= Ruben + bigM * z215_2
prob += z215_1 == z215_2

z216_1 = LpVariable("z216_1", cat="Binary")
z216_2 = LpVariable("z216_2", cat="Binary")
prob += Pam + smallC <= Carla + bigM * z216_1
prob += Pam + smallC <= Gene + bigM * z216_2
prob += z216_1 == z216_2

z217_1 = LpVariable("z217_1", cat="Binary")
z217_2 = LpVariable("z217_2", cat="Binary")
prob += Neal + smallC <= Dominick + bigM * z217_1
prob += Neal + smallC <= Lianne + bigM * z217_2
prob += z217_1 == z217_2

z218_1 = LpVariable("z218_1", cat="Binary")
z218_2 = LpVariable("z218_2", cat="Binary")
prob += Skylar + smallC <= Lianne + bigM * z218_1
prob += Skylar + smallC <= Gene + bigM * z218_2
prob += z218_1 == z218_2

z219_1 = LpVariable("z219_1", cat="Binary")
z219_2 = LpVariable("z219_2", cat="Binary")
prob += Ayesha + smallC <= Paris + bigM * z219_1
prob += Ayesha + smallC <= Daragh + bigM * z219_2
prob += z219_1 == z219_2

z220_1 = LpVariable("z220_1", cat="Binary")
z220_2 = LpVariable("z220_2", cat="Binary")
prob += Janette + smallC <= Neal + bigM * z220_1
prob += Janette + smallC <= Conner + bigM * z220_2
prob += z220_1 == z220_2

z221_1 = LpVariable("z221_1", cat="Binary")
z221_2 = LpVariable("z221_2", cat="Binary")
prob += Lianne + smallC <= Daragh + bigM * z221_1
prob += Lianne + smallC <= Skylar + bigM * z221_2
prob += z221_1 == z221_2

z222_1 = LpVariable("z222_1", cat="Binary")
z222_2 = LpVariable("z222_2", cat="Binary")
prob += Amari + smallC <= Lianne + bigM * z222_1
prob += Amari + smallC <= Joni + bigM * z222_2
prob += z222_1 == z222_2

z223_1 = LpVariable("z223_1", cat="Binary")
z223_2 = LpVariable("z223_2", cat="Binary")
prob += Pam + smallC <= Ruben + bigM * z223_1
prob += Pam + smallC <= Mckenna + bigM * z223_2
prob += z223_1 == z223_2

z224_1 = LpVariable("z224_1", cat="Binary")
z224_2 = LpVariable("z224_2", cat="Binary")
prob += Lianne + smallC <= Skylar + bigM * z224_1
prob += Lianne + smallC <= Ruben + bigM * z224_2
prob += z224_1 == z224_2

z225_1 = LpVariable("z225_1", cat="Binary")
z225_2 = LpVariable("z225_2", cat="Binary")
prob += Pam + smallC <= Chase + bigM * z225_1
prob += Pam + smallC <= Janette + bigM * z225_2
prob += z225_1 == z225_2

z226_1 = LpVariable("z226_1", cat="Binary")
z226_2 = LpVariable("z226_2", cat="Binary")
prob += Skylar + smallC <= Curt + bigM * z226_1
prob += Skylar + smallC <= Pam + bigM * z226_2
prob += z226_1 == z226_2

z227_1 = LpVariable("z227_1", cat="Binary")
z227_2 = LpVariable("z227_2", cat="Binary")
prob += Pam + smallC <= Ayesha + bigM * z227_1
prob += Pam + smallC <= Curt + bigM * z227_2
prob += z227_1 == z227_2

z228_1 = LpVariable("z228_1", cat="Binary")
z228_2 = LpVariable("z228_2", cat="Binary")
prob += Lianne + smallC <= Oisin + bigM * z228_1
prob += Lianne + smallC <= Ruben + bigM * z228_2
prob += z228_1 == z228_2

z229_1 = LpVariable("z229_1", cat="Binary")
z229_2 = LpVariable("z229_2", cat="Binary")
prob += Oisin + smallC <= Pam + bigM * z229_1
prob += Oisin + smallC <= Dominick + bigM * z229_2
prob += z229_1 == z229_2

z230_1 = LpVariable("z230_1", cat="Binary")
z230_2 = LpVariable("z230_2", cat="Binary")
prob += Skylar + smallC <= Dominick + bigM * z230_1
prob += Skylar + smallC <= Joni + bigM * z230_2
prob += z230_1 == z230_2

z231_1 = LpVariable("z231_1", cat="Binary")
z231_2 = LpVariable("z231_2", cat="Binary")
prob += Paris + smallC <= Dominick + bigM * z231_1
prob += Paris + smallC <= Neal + bigM * z231_2
prob += z231_1 == z231_2

z232_1 = LpVariable("z232_1", cat="Binary")
z232_2 = LpVariable("z232_2", cat="Binary")
prob += Mckenna + smallC <= Curt + bigM * z232_1
prob += Mckenna + smallC <= Neal + bigM * z232_2
prob += z232_1 == z232_2

z233_1 = LpVariable("z233_1", cat="Binary")
z233_2 = LpVariable("z233_2", cat="Binary")
prob += Joni + smallC <= Neal + bigM * z233_1
prob += Joni + smallC <= Dominick + bigM * z233_2
prob += z233_1 == z233_2

z234_1 = LpVariable("z234_1", cat="Binary")
z234_2 = LpVariable("z234_2", cat="Binary")
prob += Skylar + smallC <= Daragh + bigM * z234_1
prob += Skylar + smallC <= Oisin + bigM * z234_2
prob += z234_1 == z234_2

z235_1 = LpVariable("z235_1", cat="Binary")
z235_2 = LpVariable("z235_2", cat="Binary")
prob += Lianne + smallC <= Ayesha + bigM * z235_1
prob += Lianne + smallC <= Chase + bigM * z235_2
prob += z235_1 == z235_2

z236_1 = LpVariable("z236_1", cat="Binary")
z236_2 = LpVariable("z236_2", cat="Binary")
prob += Neal + smallC <= Janette + bigM * z236_1
prob += Neal + smallC <= Lianne + bigM * z236_2
prob += z236_1 == z236_2

z237_1 = LpVariable("z237_1", cat="Binary")
z237_2 = LpVariable("z237_2", cat="Binary")
prob += Amari + smallC <= Mckenna + bigM * z237_1
prob += Amari + smallC <= Dominick + bigM * z237_2
prob += z237_1 == z237_2

z238_1 = LpVariable("z238_1", cat="Binary")
z238_2 = LpVariable("z238_2", cat="Binary")
prob += Wesley + smallC <= Mckenna + bigM * z238_1
prob += Wesley + smallC <= Skylar + bigM * z238_2
prob += z238_1 == z238_2

z239_1 = LpVariable("z239_1", cat="Binary")
z239_2 = LpVariable("z239_2", cat="Binary")
prob += Lianne + smallC <= Dominick + bigM * z239_1
prob += Lianne + smallC <= Mckenna + bigM * z239_2
prob += z239_1 == z239_2

z240_1 = LpVariable("z240_1", cat="Binary")
z240_2 = LpVariable("z240_2", cat="Binary")
prob += Oisin + smallC <= Ayesha + bigM * z240_1
prob += Oisin + smallC <= Daragh + bigM * z240_2
prob += z240_1 == z240_2

z241_1 = LpVariable("z241_1", cat="Binary")
z241_2 = LpVariable("z241_2", cat="Binary")
prob += Ayesha + smallC <= Paris + bigM * z241_1
prob += Ayesha + smallC <= Daragh + bigM * z241_2
prob += z241_1 == z241_2

z242_1 = LpVariable("z242_1", cat="Binary")
z242_2 = LpVariable("z242_2", cat="Binary")
prob += Joni + smallC <= Conner + bigM * z242_1
prob += Joni + smallC <= Amari + bigM * z242_2
prob += z242_1 == z242_2

z243_1 = LpVariable("z243_1", cat="Binary")
z243_2 = LpVariable("z243_2", cat="Binary")
prob += Daragh + smallC <= Pam + bigM * z243_1
prob += Daragh + smallC <= Carla + bigM * z243_2
prob += z243_1 == z243_2

z244_1 = LpVariable("z244_1", cat="Binary")
z244_2 = LpVariable("z244_2", cat="Binary")
prob += Conner + smallC <= Pam + bigM * z244_1
prob += Conner + smallC <= Daragh + bigM * z244_2
prob += z244_1 == z244_2

z245_1 = LpVariable("z245_1", cat="Binary")
z245_2 = LpVariable("z245_2", cat="Binary")
prob += Janette + smallC <= Curt + bigM * z245_1
prob += Janette + smallC <= Gene + bigM * z245_2
prob += z245_1 == z245_2

z246_1 = LpVariable("z246_1", cat="Binary")
z246_2 = LpVariable("z246_2", cat="Binary")
prob += Neal + smallC <= Skylar + bigM * z246_1
prob += Neal + smallC <= Chase + bigM * z246_2
prob += z246_1 == z246_2

z247_1 = LpVariable("z247_1", cat="Binary")
z247_2 = LpVariable("z247_2", cat="Binary")
prob += Wesley + smallC <= Ruben + bigM * z247_1
prob += Wesley + smallC <= Mckenna + bigM * z247_2
prob += z247_1 == z247_2

z248_1 = LpVariable("z248_1", cat="Binary")
z248_2 = LpVariable("z248_2", cat="Binary")
prob += Pam + smallC <= Janette + bigM * z248_1
prob += Pam + smallC <= Dominick + bigM * z248_2
prob += z248_1 == z248_2

z249_1 = LpVariable("z249_1", cat="Binary")
z249_2 = LpVariable("z249_2", cat="Binary")
prob += Paris + smallC <= Mckenna + bigM * z249_1
prob += Paris + smallC <= Skylar + bigM * z249_2
prob += z249_1 == z249_2

z250_1 = LpVariable("z250_1", cat="Binary")
z250_2 = LpVariable("z250_2", cat="Binary")
prob += Paris + smallC <= Skylar + bigM * z250_1
prob += Paris + smallC <= Neal + bigM * z250_2
prob += z250_1 == z250_2

z251_1 = LpVariable("z251_1", cat="Binary")
z251_2 = LpVariable("z251_2", cat="Binary")
prob += Wesley + smallC <= Curt + bigM * z251_1
prob += Wesley + smallC <= Janette + bigM * z251_2
prob += z251_1 == z251_2

z252_1 = LpVariable("z252_1", cat="Binary")
z252_2 = LpVariable("z252_2", cat="Binary")
prob += Skylar + smallC <= Daragh + bigM * z252_1
prob += Skylar + smallC <= Ruben + bigM * z252_2
prob += z252_1 == z252_2

z253_1 = LpVariable("z253_1", cat="Binary")
z253_2 = LpVariable("z253_2", cat="Binary")
prob += Curt + smallC <= Conner + bigM * z253_1
prob += Curt + smallC <= Neal + bigM * z253_2
prob += z253_1 == z253_2

z254_1 = LpVariable("z254_1", cat="Binary")
z254_2 = LpVariable("z254_2", cat="Binary")
prob += Curt + smallC <= Neal + bigM * z254_1
prob += Curt + smallC <= Amari + bigM * z254_2
prob += z254_1 == z254_2

z255_1 = LpVariable("z255_1", cat="Binary")
z255_2 = LpVariable("z255_2", cat="Binary")
prob += Ruben + smallC <= Lianne + bigM * z255_1
prob += Ruben + smallC <= Skylar + bigM * z255_2
prob += z255_1 == z255_2

z256_1 = LpVariable("z256_1", cat="Binary")
z256_2 = LpVariable("z256_2", cat="Binary")
prob += Joni + smallC <= Carla + bigM * z256_1
prob += Joni + smallC <= Gene + bigM * z256_2
prob += z256_1 == z256_2

z257_1 = LpVariable("z257_1", cat="Binary")
z257_2 = LpVariable("z257_2", cat="Binary")
prob += Ruben + smallC <= Mckenna + bigM * z257_1
prob += Ruben + smallC <= Janette + bigM * z257_2
prob += z257_1 == z257_2

z258_1 = LpVariable("z258_1", cat="Binary")
z258_2 = LpVariable("z258_2", cat="Binary")
prob += Ayesha + smallC <= Pam + bigM * z258_1
prob += Ayesha + smallC <= Dominick + bigM * z258_2
prob += z258_1 == z258_2

z259_1 = LpVariable("z259_1", cat="Binary")
z259_2 = LpVariable("z259_2", cat="Binary")
prob += Skylar + smallC <= Oisin + bigM * z259_1
prob += Skylar + smallC <= Paris + bigM * z259_2
prob += z259_1 == z259_2

z260_1 = LpVariable("z260_1", cat="Binary")
z260_2 = LpVariable("z260_2", cat="Binary")
prob += Oisin + smallC <= Curt + bigM * z260_1
prob += Oisin + smallC <= Daragh + bigM * z260_2
prob += z260_1 == z260_2

z261_1 = LpVariable("z261_1", cat="Binary")
z261_2 = LpVariable("z261_2", cat="Binary")
prob += Oisin + smallC <= Paris + bigM * z261_1
prob += Oisin + smallC <= Pam + bigM * z261_2
prob += z261_1 == z261_2

z262_1 = LpVariable("z262_1", cat="Binary")
z262_2 = LpVariable("z262_2", cat="Binary")
prob += Mckenna + smallC <= Ayesha + bigM * z262_1
prob += Mckenna + smallC <= Amari + bigM * z262_2
prob += z262_1 == z262_2

z263_1 = LpVariable("z263_1", cat="Binary")
z263_2 = LpVariable("z263_2", cat="Binary")
prob += Lianne + smallC <= Daragh + bigM * z263_1
prob += Lianne + smallC <= Paris + bigM * z263_2
prob += z263_1 == z263_2

z264_1 = LpVariable("z264_1", cat="Binary")
z264_2 = LpVariable("z264_2", cat="Binary")
prob += Ayesha + smallC <= Paris + bigM * z264_1
prob += Ayesha + smallC <= Lianne + bigM * z264_2
prob += z264_1 == z264_2

z265_1 = LpVariable("z265_1", cat="Binary")
z265_2 = LpVariable("z265_2", cat="Binary")
prob += Neal + smallC <= Curt + bigM * z265_1
prob += Neal + smallC <= Carla + bigM * z265_2
prob += z265_1 == z265_2

z266_1 = LpVariable("z266_1", cat="Binary")
z266_2 = LpVariable("z266_2", cat="Binary")
prob += Mckenna + smallC <= Ruben + bigM * z266_1
prob += Mckenna + smallC <= Skylar + bigM * z266_2
prob += z266_1 == z266_2

z267_1 = LpVariable("z267_1", cat="Binary")
z267_2 = LpVariable("z267_2", cat="Binary")
prob += Daragh + smallC <= Dominick + bigM * z267_1
prob += Daragh + smallC <= Janette + bigM * z267_2
prob += z267_1 == z267_2

z268_1 = LpVariable("z268_1", cat="Binary")
z268_2 = LpVariable("z268_2", cat="Binary")
prob += Wesley + smallC <= Chase + bigM * z268_1
prob += Wesley + smallC <= Dominick + bigM * z268_2
prob += z268_1 == z268_2

z269_1 = LpVariable("z269_1", cat="Binary")
z269_2 = LpVariable("z269_2", cat="Binary")
prob += Neal + smallC <= Daragh + bigM * z269_1
prob += Neal + smallC <= Paris + bigM * z269_2
prob += z269_1 == z269_2

z270_1 = LpVariable("z270_1", cat="Binary")
z270_2 = LpVariable("z270_2", cat="Binary")
prob += Ayesha + smallC <= Gene + bigM * z270_1
prob += Ayesha + smallC <= Mckenna + bigM * z270_2
prob += z270_1 == z270_2

z271_1 = LpVariable("z271_1", cat="Binary")
z271_2 = LpVariable("z271_2", cat="Binary")
prob += Mckenna + smallC <= Amari + bigM * z271_1
prob += Mckenna + smallC <= Gene + bigM * z271_2
prob += z271_1 == z271_2

z272_1 = LpVariable("z272_1", cat="Binary")
z272_2 = LpVariable("z272_2", cat="Binary")
prob += Conner + smallC <= Ruben + bigM * z272_1
prob += Conner + smallC <= Chase + bigM * z272_2
prob += z272_1 == z272_2

z273_1 = LpVariable("z273_1", cat="Binary")
z273_2 = LpVariable("z273_2", cat="Binary")
prob += Conner + smallC <= Skylar + bigM * z273_1
prob += Conner + smallC <= Paris + bigM * z273_2
prob += z273_1 == z273_2

z274_1 = LpVariable("z274_1", cat="Binary")
z274_2 = LpVariable("z274_2", cat="Binary")
prob += Paris + smallC <= Curt + bigM * z274_1
prob += Paris + smallC <= Carla + bigM * z274_2
prob += z274_1 == z274_2

z275_1 = LpVariable("z275_1", cat="Binary")
z275_2 = LpVariable("z275_2", cat="Binary")
prob += Ayesha + smallC <= Amari + bigM * z275_1
prob += Ayesha + smallC <= Janette + bigM * z275_2
prob += z275_1 == z275_2

z276_1 = LpVariable("z276_1", cat="Binary")
z276_2 = LpVariable("z276_2", cat="Binary")
prob += Curt + smallC <= Conner + bigM * z276_1
prob += Curt + smallC <= Amari + bigM * z276_2
prob += z276_1 == z276_2

z277_1 = LpVariable("z277_1", cat="Binary")
z277_2 = LpVariable("z277_2", cat="Binary")
prob += Pam + smallC <= Ayesha + bigM * z277_1
prob += Pam + smallC <= Dominick + bigM * z277_2
prob += z277_1 == z277_2

z278_1 = LpVariable("z278_1", cat="Binary")
z278_2 = LpVariable("z278_2", cat="Binary")
prob += Curt + smallC <= Gene + bigM * z278_1
prob += Curt + smallC <= Ayesha + bigM * z278_2
prob += z278_1 == z278_2

z279_1 = LpVariable("z279_1", cat="Binary")
z279_2 = LpVariable("z279_2", cat="Binary")
prob += Conner + smallC <= Curt + bigM * z279_1
prob += Conner + smallC <= Wesley + bigM * z279_2
prob += z279_1 == z279_2

z280_1 = LpVariable("z280_1", cat="Binary")
z280_2 = LpVariable("z280_2", cat="Binary")
prob += Joni + smallC <= Amari + bigM * z280_1
prob += Joni + smallC <= Neal + bigM * z280_2
prob += z280_1 == z280_2

z281_1 = LpVariable("z281_1", cat="Binary")
z281_2 = LpVariable("z281_2", cat="Binary")
prob += Lianne + smallC <= Paris + bigM * z281_1
prob += Lianne + smallC <= Oisin + bigM * z281_2
prob += z281_1 == z281_2

z282_1 = LpVariable("z282_1", cat="Binary")
z282_2 = LpVariable("z282_2", cat="Binary")
prob += Skylar + smallC <= Ruben + bigM * z282_1
prob += Skylar + smallC <= Daragh + bigM * z282_2
prob += z282_1 == z282_2

z283_1 = LpVariable("z283_1", cat="Binary")
z283_2 = LpVariable("z283_2", cat="Binary")
prob += Amari + smallC <= Conner + bigM * z283_1
prob += Amari + smallC <= Janette + bigM * z283_2
prob += z283_1 == z283_2

z284_1 = LpVariable("z284_1", cat="Binary")
z284_2 = LpVariable("z284_2", cat="Binary")
prob += Pam + smallC <= Conner + bigM * z284_1
prob += Pam + smallC <= Ayesha + bigM * z284_2
prob += z284_1 == z284_2

z285_1 = LpVariable("z285_1", cat="Binary")
z285_2 = LpVariable("z285_2", cat="Binary")
prob += Ruben + smallC <= Daragh + bigM * z285_1
prob += Ruben + smallC <= Paris + bigM * z285_2
prob += z285_1 == z285_2

z286_1 = LpVariable("z286_1", cat="Binary")
z286_2 = LpVariable("z286_2", cat="Binary")
prob += Lianne + smallC <= Pam + bigM * z286_1
prob += Lianne + smallC <= Ayesha + bigM * z286_2
prob += z286_1 == z286_2

z287_1 = LpVariable("z287_1", cat="Binary")
z287_2 = LpVariable("z287_2", cat="Binary")
prob += Skylar + smallC <= Carla + bigM * z287_1
prob += Skylar + smallC <= Conner + bigM * z287_2
prob += z287_1 == z287_2

z288_1 = LpVariable("z288_1", cat="Binary")
z288_2 = LpVariable("z288_2", cat="Binary")
prob += Joni + smallC <= Curt + bigM * z288_1
prob += Joni + smallC <= Amari + bigM * z288_2
prob += z288_1 == z288_2

z289_1 = LpVariable("z289_1", cat="Binary")
z289_2 = LpVariable("z289_2", cat="Binary")
prob += Ayesha + smallC <= Paris + bigM * z289_1
prob += Ayesha + smallC <= Joni + bigM * z289_2
prob += z289_1 == z289_2

z290_1 = LpVariable("z290_1", cat="Binary")
z290_2 = LpVariable("z290_2", cat="Binary")
prob += Paris + smallC <= Daragh + bigM * z290_1
prob += Paris + smallC <= Oisin + bigM * z290_2
prob += z290_1 == z290_2

z291_1 = LpVariable("z291_1", cat="Binary")
z291_2 = LpVariable("z291_2", cat="Binary")
prob += Ayesha + smallC <= Mckenna + bigM * z291_1
prob += Ayesha + smallC <= Joni + bigM * z291_2
prob += z291_1 == z291_2

z292_1 = LpVariable("z292_1", cat="Binary")
z292_2 = LpVariable("z292_2", cat="Binary")
prob += Ayesha + smallC <= Amari + bigM * z292_1
prob += Ayesha + smallC <= Carla + bigM * z292_2
prob += z292_1 == z292_2

z293_1 = LpVariable("z293_1", cat="Binary")
z293_2 = LpVariable("z293_2", cat="Binary")
prob += Skylar + smallC <= Oisin + bigM * z293_1
prob += Skylar + smallC <= Daragh + bigM * z293_2
prob += z293_1 == z293_2

z294_1 = LpVariable("z294_1", cat="Binary")
z294_2 = LpVariable("z294_2", cat="Binary")
prob += Joni + smallC <= Pam + bigM * z294_1
prob += Joni + smallC <= Mckenna + bigM * z294_2
prob += z294_1 == z294_2

z295_1 = LpVariable("z295_1", cat="Binary")
z295_2 = LpVariable("z295_2", cat="Binary")
prob += Wesley + smallC <= Daragh + bigM * z295_1
prob += Wesley + smallC <= Lianne + bigM * z295_2
prob += z295_1 == z295_2

z296_1 = LpVariable("z296_1", cat="Binary")
z296_2 = LpVariable("z296_2", cat="Binary")
prob += Curt + smallC <= Janette + bigM * z296_1
prob += Curt + smallC <= Conner + bigM * z296_2
prob += z296_1 == z296_2

z297_1 = LpVariable("z297_1", cat="Binary")
z297_2 = LpVariable("z297_2", cat="Binary")
prob += Ayesha + smallC <= Neal + bigM * z297_1
prob += Ayesha + smallC <= Carla + bigM * z297_2
prob += z297_1 == z297_2

z298_1 = LpVariable("z298_1", cat="Binary")
z298_2 = LpVariable("z298_2", cat="Binary")
prob += Curt + smallC <= Conner + bigM * z298_1
prob += Curt + smallC <= Amari + bigM * z298_2
prob += z298_1 == z298_2

z299_1 = LpVariable("z299_1", cat="Binary")
z299_2 = LpVariable("z299_2", cat="Binary")
prob += Lianne + smallC <= Janette + bigM * z299_1
prob += Lianne + smallC <= Joni + bigM * z299_2
prob += z299_1 == z299_2

z300_1 = LpVariable("z300_1", cat="Binary")
z300_2 = LpVariable("z300_2", cat="Binary")
prob += Oisin + smallC <= Chase + bigM * z300_1
prob += Oisin + smallC <= Wesley + bigM * z300_2
prob += z300_1 == z300_2

z301_1 = LpVariable("z301_1", cat="Binary")
z301_2 = LpVariable("z301_2", cat="Binary")
prob += Daragh + smallC <= Mckenna + bigM * z301_1
prob += Daragh + smallC <= Chase + bigM * z301_2
prob += z301_1 == z301_2

z302_1 = LpVariable("z302_1", cat="Binary")
z302_2 = LpVariable("z302_2", cat="Binary")
prob += Oisin + smallC <= Conner + bigM * z302_1
prob += Oisin + smallC <= Ruben + bigM * z302_2
prob += z302_1 == z302_2

z303_1 = LpVariable("z303_1", cat="Binary")
z303_2 = LpVariable("z303_2", cat="Binary")
prob += Curt + smallC <= Conner + bigM * z303_1
prob += Curt + smallC <= Neal + bigM * z303_2
prob += z303_1 == z303_2

z304_1 = LpVariable("z304_1", cat="Binary")
z304_2 = LpVariable("z304_2", cat="Binary")
prob += Ruben + smallC <= Oisin + bigM * z304_1
prob += Ruben + smallC <= Paris + bigM * z304_2
prob += z304_1 == z304_2

z305_1 = LpVariable("z305_1", cat="Binary")
z305_2 = LpVariable("z305_2", cat="Binary")
prob += Curt + smallC <= Conner + bigM * z305_1
prob += Curt + smallC <= Janette + bigM * z305_2
prob += z305_1 == z305_2

z306_1 = LpVariable("z306_1", cat="Binary")
z306_2 = LpVariable("z306_2", cat="Binary")
prob += Amari + smallC <= Skylar + bigM * z306_1
prob += Amari + smallC <= Carla + bigM * z306_2
prob += z306_1 == z306_2

z307_1 = LpVariable("z307_1", cat="Binary")
z307_2 = LpVariable("z307_2", cat="Binary")
prob += Paris + smallC <= Daragh + bigM * z307_1
prob += Paris + smallC <= Oisin + bigM * z307_2
prob += z307_1 == z307_2

z308_1 = LpVariable("z308_1", cat="Binary")
z308_2 = LpVariable("z308_2", cat="Binary")
prob += Daragh + smallC <= Janette + bigM * z308_1
prob += Daragh + smallC <= Ruben + bigM * z308_2
prob += z308_1 == z308_2

z309_1 = LpVariable("z309_1", cat="Binary")
z309_2 = LpVariable("z309_2", cat="Binary")
prob += Pam + smallC <= Paris + bigM * z309_1
prob += Pam + smallC <= Oisin + bigM * z309_2
prob += z309_1 == z309_2

z310_1 = LpVariable("z310_1", cat="Binary")
z310_2 = LpVariable("z310_2", cat="Binary")
prob += Daragh + smallC <= Dominick + bigM * z310_1
prob += Daragh + smallC <= Ayesha + bigM * z310_2
prob += z310_1 == z310_2

z311_1 = LpVariable("z311_1", cat="Binary")
z311_2 = LpVariable("z311_2", cat="Binary")
prob += Wesley + smallC <= Mckenna + bigM * z311_1
prob += Wesley + smallC <= Oisin + bigM * z311_2
prob += z311_1 == z311_2

z312_1 = LpVariable("z312_1", cat="Binary")
z312_2 = LpVariable("z312_2", cat="Binary")
prob += Wesley + smallC <= Amari + bigM * z312_1
prob += Wesley + smallC <= Chase + bigM * z312_2
prob += z312_1 == z312_2

z313_1 = LpVariable("z313_1", cat="Binary")
z313_2 = LpVariable("z313_2", cat="Binary")
prob += Wesley + smallC <= Daragh + bigM * z313_1
prob += Wesley + smallC <= Oisin + bigM * z313_2
prob += z313_1 == z313_2

z314_1 = LpVariable("z314_1", cat="Binary")
z314_2 = LpVariable("z314_2", cat="Binary")
prob += Lianne + smallC <= Neal + bigM * z314_1
prob += Lianne + smallC <= Amari + bigM * z314_2
prob += z314_1 == z314_2

z315_1 = LpVariable("z315_1", cat="Binary")
z315_2 = LpVariable("z315_2", cat="Binary")
prob += Pam + smallC <= Ayesha + bigM * z315_1
prob += Pam + smallC <= Conner + bigM * z315_2
prob += z315_1 == z315_2

z316_1 = LpVariable("z316_1", cat="Binary")
z316_2 = LpVariable("z316_2", cat="Binary")
prob += Paris + smallC <= Daragh + bigM * z316_1
prob += Paris + smallC <= Oisin + bigM * z316_2
prob += z316_1 == z316_2

z317_1 = LpVariable("z317_1", cat="Binary")
z317_2 = LpVariable("z317_2", cat="Binary")
prob += Conner + smallC <= Janette + bigM * z317_1
prob += Conner + smallC <= Carla + bigM * z317_2
prob += z317_1 == z317_2

z318_1 = LpVariable("z318_1", cat="Binary")
z318_2 = LpVariable("z318_2", cat="Binary")
prob += Skylar + smallC <= Daragh + bigM * z318_1
prob += Skylar + smallC <= Ruben + bigM * z318_2
prob += z318_1 == z318_2

z319_1 = LpVariable("z319_1", cat="Binary")
z319_2 = LpVariable("z319_2", cat="Binary")
prob += Neal + smallC <= Pam + bigM * z319_1
prob += Neal + smallC <= Ruben + bigM * z319_2
prob += z319_1 == z319_2

z320_1 = LpVariable("z320_1", cat="Binary")
z320_2 = LpVariable("z320_2", cat="Binary")
prob += Curt + smallC <= Dominick + bigM * z320_1
prob += Curt + smallC <= Joni + bigM * z320_2
prob += z320_1 == z320_2

z321_1 = LpVariable("z321_1", cat="Binary")
z321_2 = LpVariable("z321_2", cat="Binary")
prob += Ayesha + smallC <= Amari + bigM * z321_1
prob += Ayesha + smallC <= Conner + bigM * z321_2
prob += z321_1 == z321_2

z322_1 = LpVariable("z322_1", cat="Binary")
z322_2 = LpVariable("z322_2", cat="Binary")
prob += Neal + smallC <= Gene + bigM * z322_1
prob += Neal + smallC <= Lianne + bigM * z322_2
prob += z322_1 == z322_2

z323_1 = LpVariable("z323_1", cat="Binary")
z323_2 = LpVariable("z323_2", cat="Binary")
prob += Mckenna + smallC <= Wesley + bigM * z323_1
prob += Mckenna + smallC <= Neal + bigM * z323_2
prob += z323_1 == z323_2

z324_1 = LpVariable("z324_1", cat="Binary")
z324_2 = LpVariable("z324_2", cat="Binary")
prob += Skylar + smallC <= Daragh + bigM * z324_1
prob += Skylar + smallC <= Oisin + bigM * z324_2
prob += z324_1 == z324_2

z325_1 = LpVariable("z325_1", cat="Binary")
z325_2 = LpVariable("z325_2", cat="Binary")
prob += Conner + smallC <= Chase + bigM * z325_1
prob += Conner + smallC <= Ruben + bigM * z325_2
prob += z325_1 == z325_2

z326_1 = LpVariable("z326_1", cat="Binary")
z326_2 = LpVariable("z326_2", cat="Binary")
prob += Lianne + smallC <= Oisin + bigM * z326_1
prob += Lianne + smallC <= Paris + bigM * z326_2
prob += z326_1 == z326_2

z327_1 = LpVariable("z327_1", cat="Binary")
z327_2 = LpVariable("z327_2", cat="Binary")
prob += Daragh + smallC <= Joni + bigM * z327_1
prob += Daragh + smallC <= Dominick + bigM * z327_2
prob += z327_1 == z327_2

z328_1 = LpVariable("z328_1", cat="Binary")
z328_2 = LpVariable("z328_2", cat="Binary")
prob += Ayesha + smallC <= Ruben + bigM * z328_1
prob += Ayesha + smallC <= Gene + bigM * z328_2
prob += z328_1 == z328_2

z329_1 = LpVariable("z329_1", cat="Binary")
z329_2 = LpVariable("z329_2", cat="Binary")
prob += Wesley + smallC <= Gene + bigM * z329_1
prob += Wesley + smallC <= Chase + bigM * z329_2
prob += z329_1 == z329_2

z330_1 = LpVariable("z330_1", cat="Binary")
z330_2 = LpVariable("z330_2", cat="Binary")
prob += Curt + smallC <= Joni + bigM * z330_1
prob += Curt + smallC <= Wesley + bigM * z330_2
prob += z330_1 == z330_2

z331_1 = LpVariable("z331_1", cat="Binary")
z331_2 = LpVariable("z331_2", cat="Binary")
prob += Skylar + smallC <= Oisin + bigM * z331_1
prob += Skylar + smallC <= Daragh + bigM * z331_2
prob += z331_1 == z331_2

z332_1 = LpVariable("z332_1", cat="Binary")
z332_2 = LpVariable("z332_2", cat="Binary")
prob += Conner + smallC <= Mckenna + bigM * z332_1
prob += Conner + smallC <= Dominick + bigM * z332_2
prob += z332_1 == z332_2

z333_1 = LpVariable("z333_1", cat="Binary")
z333_2 = LpVariable("z333_2", cat="Binary")
prob += Wesley + smallC <= Pam + bigM * z333_1
prob += Wesley + smallC <= Neal + bigM * z333_2
prob += z333_1 == z333_2

z334_1 = LpVariable("z334_1", cat="Binary")
z334_2 = LpVariable("z334_2", cat="Binary")
prob += Mckenna + smallC <= Chase + bigM * z334_1
prob += Mckenna + smallC <= Pam + bigM * z334_2
prob += z334_1 == z334_2

z335_1 = LpVariable("z335_1", cat="Binary")
z335_2 = LpVariable("z335_2", cat="Binary")
prob += Lianne + smallC <= Mckenna + bigM * z335_1
prob += Lianne + smallC <= Conner + bigM * z335_2
prob += z335_1 == z335_2

z336_1 = LpVariable("z336_1", cat="Binary")
z336_2 = LpVariable("z336_2", cat="Binary")
prob += Skylar + smallC <= Chase + bigM * z336_1
prob += Skylar + smallC <= Pam + bigM * z336_2
prob += z336_1 == z336_2

z337_1 = LpVariable("z337_1", cat="Binary")
z337_2 = LpVariable("z337_2", cat="Binary")
prob += Pam + smallC <= Oisin + bigM * z337_1
prob += Pam + smallC <= Daragh + bigM * z337_2
prob += z337_1 == z337_2

z338_1 = LpVariable("z338_1", cat="Binary")
z338_2 = LpVariable("z338_2", cat="Binary")
prob += Ruben + smallC <= Curt + bigM * z338_1
prob += Ruben + smallC <= Chase + bigM * z338_2
prob += z338_1 == z338_2

z339_1 = LpVariable("z339_1", cat="Binary")
z339_2 = LpVariable("z339_2", cat="Binary")
prob += Skylar + smallC <= Pam + bigM * z339_1
prob += Skylar + smallC <= Amari + bigM * z339_2
prob += z339_1 == z339_2

z340_1 = LpVariable("z340_1", cat="Binary")
z340_2 = LpVariable("z340_2", cat="Binary")
prob += Amari + smallC <= Chase + bigM * z340_1
prob += Amari + smallC <= Skylar + bigM * z340_2
prob += z340_1 == z340_2

z341_1 = LpVariable("z341_1", cat="Binary")
z341_2 = LpVariable("z341_2", cat="Binary")
prob += Oisin + smallC <= Curt + bigM * z341_1
prob += Oisin + smallC <= Conner + bigM * z341_2
prob += z341_1 == z341_2

z342_1 = LpVariable("z342_1", cat="Binary")
z342_2 = LpVariable("z342_2", cat="Binary")
prob += Mckenna + smallC <= Amari + bigM * z342_1
prob += Mckenna + smallC <= Janette + bigM * z342_2
prob += z342_1 == z342_2

z343_1 = LpVariable("z343_1", cat="Binary")
z343_2 = LpVariable("z343_2", cat="Binary")
prob += Daragh + smallC <= Pam + bigM * z343_1
prob += Daragh + smallC <= Conner + bigM * z343_2
prob += z343_1 == z343_2

z344_1 = LpVariable("z344_1", cat="Binary")
z344_2 = LpVariable("z344_2", cat="Binary")
prob += Daragh + smallC <= Wesley + bigM * z344_1
prob += Daragh + smallC <= Ayesha + bigM * z344_2
prob += z344_1 == z344_2

z345_1 = LpVariable("z345_1", cat="Binary")
z345_2 = LpVariable("z345_2", cat="Binary")
prob += Mckenna + smallC <= Chase + bigM * z345_1
prob += Mckenna + smallC <= Dominick + bigM * z345_2
prob += z345_1 == z345_2

z346_1 = LpVariable("z346_1", cat="Binary")
z346_2 = LpVariable("z346_2", cat="Binary")
prob += Mckenna + smallC <= Amari + bigM * z346_1
prob += Mckenna + smallC <= Conner + bigM * z346_2
prob += z346_1 == z346_2

z347_1 = LpVariable("z347_1", cat="Binary")
z347_2 = LpVariable("z347_2", cat="Binary")
prob += Janette + smallC <= Amari + bigM * z347_1
prob += Janette + smallC <= Ayesha + bigM * z347_2
prob += z347_1 == z347_2

z348_1 = LpVariable("z348_1", cat="Binary")
z348_2 = LpVariable("z348_2", cat="Binary")
prob += Lianne + smallC <= Amari + bigM * z348_1
prob += Lianne + smallC <= Mckenna + bigM * z348_2
prob += z348_1 == z348_2

z349_1 = LpVariable("z349_1", cat="Binary")
z349_2 = LpVariable("z349_2", cat="Binary")
prob += Amari + smallC <= Conner + bigM * z349_1
prob += Amari + smallC <= Janette + bigM * z349_2
prob += z349_1 == z349_2

z350_1 = LpVariable("z350_1", cat="Binary")
z350_2 = LpVariable("z350_2", cat="Binary")
prob += Conner + smallC <= Gene + bigM * z350_1
prob += Conner + smallC <= Daragh + bigM * z350_2
prob += z350_1 == z350_2

z351_1 = LpVariable("z351_1", cat="Binary")
z351_2 = LpVariable("z351_2", cat="Binary")
prob += Paris + smallC <= Daragh + bigM * z351_1
prob += Paris + smallC <= Oisin + bigM * z351_2
prob += z351_1 == z351_2

z352_1 = LpVariable("z352_1", cat="Binary")
z352_2 = LpVariable("z352_2", cat="Binary")
prob += Pam + smallC <= Chase + bigM * z352_1
prob += Pam + smallC <= Neal + bigM * z352_2
prob += z352_1 == z352_2

z353_1 = LpVariable("z353_1", cat="Binary")
z353_2 = LpVariable("z353_2", cat="Binary")
prob += Ruben + smallC <= Paris + bigM * z353_1
prob += Ruben + smallC <= Daragh + bigM * z353_2
prob += z353_1 == z353_2

z354_1 = LpVariable("z354_1", cat="Binary")
z354_2 = LpVariable("z354_2", cat="Binary")
prob += Daragh + smallC <= Paris + bigM * z354_1
prob += Daragh + smallC <= Conner + bigM * z354_2
prob += z354_1 == z354_2

z355_1 = LpVariable("z355_1", cat="Binary")
z355_2 = LpVariable("z355_2", cat="Binary")
prob += Joni + smallC <= Janette + bigM * z355_1
prob += Joni + smallC <= Curt + bigM * z355_2
prob += z355_1 == z355_2

z356_1 = LpVariable("z356_1", cat="Binary")
z356_2 = LpVariable("z356_2", cat="Binary")
prob += Mckenna + smallC <= Ruben + bigM * z356_1
prob += Mckenna + smallC <= Daragh + bigM * z356_2
prob += z356_1 == z356_2

z357_1 = LpVariable("z357_1", cat="Binary")
z357_2 = LpVariable("z357_2", cat="Binary")
prob += Skylar + smallC <= Wesley + bigM * z357_1
prob += Skylar + smallC <= Mckenna + bigM * z357_2
prob += z357_1 == z357_2

z358_1 = LpVariable("z358_1", cat="Binary")
z358_2 = LpVariable("z358_2", cat="Binary")
prob += Joni + smallC <= Paris + bigM * z358_1
prob += Joni + smallC <= Ruben + bigM * z358_2
prob += z358_1 == z358_2

z359_1 = LpVariable("z359_1", cat="Binary")
z359_2 = LpVariable("z359_2", cat="Binary")
prob += Oisin + smallC <= Paris + bigM * z359_1
prob += Oisin + smallC <= Dominick + bigM * z359_2
prob += z359_1 == z359_2

z360_1 = LpVariable("z360_1", cat="Binary")
z360_2 = LpVariable("z360_2", cat="Binary")
prob += Oisin + smallC <= Neal + bigM * z360_1
prob += Oisin + smallC <= Wesley + bigM * z360_2
prob += z360_1 == z360_2

z361_1 = LpVariable("z361_1", cat="Binary")
z361_2 = LpVariable("z361_2", cat="Binary")
prob += Ruben + smallC <= Ayesha + bigM * z361_1
prob += Ruben + smallC <= Janette + bigM * z361_2
prob += z361_1 == z361_2

z362_1 = LpVariable("z362_1", cat="Binary")
z362_2 = LpVariable("z362_2", cat="Binary")
prob += Oisin + smallC <= Paris + bigM * z362_1
prob += Oisin + smallC <= Lianne + bigM * z362_2
prob += z362_1 == z362_2

z363_1 = LpVariable("z363_1", cat="Binary")
z363_2 = LpVariable("z363_2", cat="Binary")
prob += Ruben + smallC <= Mckenna + bigM * z363_1
prob += Ruben + smallC <= Janette + bigM * z363_2
prob += z363_1 == z363_2

z364_1 = LpVariable("z364_1", cat="Binary")
z364_2 = LpVariable("z364_2", cat="Binary")
prob += Oisin + smallC <= Wesley + bigM * z364_1
prob += Oisin + smallC <= Skylar + bigM * z364_2
prob += z364_1 == z364_2

z365_1 = LpVariable("z365_1", cat="Binary")
z365_2 = LpVariable("z365_2", cat="Binary")
prob += Curt + smallC <= Ayesha + bigM * z365_1
prob += Curt + smallC <= Paris + bigM * z365_2
prob += z365_1 == z365_2

z366_1 = LpVariable("z366_1", cat="Binary")
z366_2 = LpVariable("z366_2", cat="Binary")
prob += Neal + smallC <= Daragh + bigM * z366_1
prob += Neal + smallC <= Carla + bigM * z366_2
prob += z366_1 == z366_2

z367_1 = LpVariable("z367_1", cat="Binary")
z367_2 = LpVariable("z367_2", cat="Binary")
prob += Wesley + smallC <= Neal + bigM * z367_1
prob += Wesley + smallC <= Curt + bigM * z367_2
prob += z367_1 == z367_2

z368_1 = LpVariable("z368_1", cat="Binary")
z368_2 = LpVariable("z368_2", cat="Binary")
prob += Ayesha + smallC <= Carla + bigM * z368_1
prob += Ayesha + smallC <= Chase + bigM * z368_2
prob += z368_1 == z368_2

z369_1 = LpVariable("z369_1", cat="Binary")
z369_2 = LpVariable("z369_2", cat="Binary")
prob += Oisin + smallC <= Dominick + bigM * z369_1
prob += Oisin + smallC <= Chase + bigM * z369_2
prob += z369_1 == z369_2

z370_1 = LpVariable("z370_1", cat="Binary")
z370_2 = LpVariable("z370_2", cat="Binary")
prob += Joni + smallC <= Chase + bigM * z370_1
prob += Joni + smallC <= Gene + bigM * z370_2
prob += z370_1 == z370_2

z371_1 = LpVariable("z371_1", cat="Binary")
z371_2 = LpVariable("z371_2", cat="Binary")
prob += Pam + smallC <= Ruben + bigM * z371_1
prob += Pam + smallC <= Oisin + bigM * z371_2
prob += z371_1 == z371_2

z372_1 = LpVariable("z372_1", cat="Binary")
z372_2 = LpVariable("z372_2", cat="Binary")
prob += Daragh + smallC <= Ayesha + bigM * z372_1
prob += Daragh + smallC <= Pam + bigM * z372_2
prob += z372_1 == z372_2

z373_1 = LpVariable("z373_1", cat="Binary")
z373_2 = LpVariable("z373_2", cat="Binary")
prob += Ruben + smallC <= Daragh + bigM * z373_1
prob += Ruben + smallC <= Paris + bigM * z373_2
prob += z373_1 == z373_2

z374_1 = LpVariable("z374_1", cat="Binary")
z374_2 = LpVariable("z374_2", cat="Binary")
prob += Joni + smallC <= Dominick + bigM * z374_1
prob += Joni + smallC <= Amari + bigM * z374_2
prob += z374_1 == z374_2

z375_1 = LpVariable("z375_1", cat="Binary")
z375_2 = LpVariable("z375_2", cat="Binary")
prob += Paris + smallC <= Oisin + bigM * z375_1
prob += Paris + smallC <= Daragh + bigM * z375_2
prob += z375_1 == z375_2

z376_1 = LpVariable("z376_1", cat="Binary")
z376_2 = LpVariable("z376_2", cat="Binary")
prob += Conner + smallC <= Dominick + bigM * z376_1
prob += Conner + smallC <= Paris + bigM * z376_2
prob += z376_1 == z376_2

z377_1 = LpVariable("z377_1", cat="Binary")
z377_2 = LpVariable("z377_2", cat="Binary")
prob += Lianne + smallC <= Gene + bigM * z377_1
prob += Lianne + smallC <= Conner + bigM * z377_2
prob += z377_1 == z377_2

z378_1 = LpVariable("z378_1", cat="Binary")
z378_2 = LpVariable("z378_2", cat="Binary")
prob += Daragh + smallC <= Carla + bigM * z378_1
prob += Daragh + smallC <= Skylar + bigM * z378_2
prob += z378_1 == z378_2

z379_1 = LpVariable("z379_1", cat="Binary")
z379_2 = LpVariable("z379_2", cat="Binary")
prob += Lianne + smallC <= Pam + bigM * z379_1
prob += Lianne + smallC <= Janette + bigM * z379_2
prob += z379_1 == z379_2

z380_1 = LpVariable("z380_1", cat="Binary")
z380_2 = LpVariable("z380_2", cat="Binary")
prob += Lianne + smallC <= Joni + bigM * z380_1
prob += Lianne + smallC <= Gene + bigM * z380_2
prob += z380_1 == z380_2

z381_1 = LpVariable("z381_1", cat="Binary")
z381_2 = LpVariable("z381_2", cat="Binary")
prob += Conner + smallC <= Lianne + bigM * z381_1
prob += Conner + smallC <= Ruben + bigM * z381_2
prob += z381_1 == z381_2

z382_1 = LpVariable("z382_1", cat="Binary")
z382_2 = LpVariable("z382_2", cat="Binary")
prob += Mckenna + smallC <= Lianne + bigM * z382_1
prob += Mckenna + smallC <= Skylar + bigM * z382_2
prob += z382_1 == z382_2

z383_1 = LpVariable("z383_1", cat="Binary")
z383_2 = LpVariable("z383_2", cat="Binary")
prob += Oisin + smallC <= Conner + bigM * z383_1
prob += Oisin + smallC <= Ruben + bigM * z383_2
prob += z383_1 == z383_2

z384_1 = LpVariable("z384_1", cat="Binary")
z384_2 = LpVariable("z384_2", cat="Binary")
prob += Paris + smallC <= Oisin + bigM * z384_1
prob += Paris + smallC <= Daragh + bigM * z384_2
prob += z384_1 == z384_2

z385_1 = LpVariable("z385_1", cat="Binary")
z385_2 = LpVariable("z385_2", cat="Binary")
prob += Wesley + smallC <= Mckenna + bigM * z385_1
prob += Wesley + smallC <= Skylar + bigM * z385_2
prob += z385_1 == z385_2

z386_1 = LpVariable("z386_1", cat="Binary")
z386_2 = LpVariable("z386_2", cat="Binary")
prob += Pam + smallC <= Skylar + bigM * z386_1
prob += Pam + smallC <= Ruben + bigM * z386_2
prob += z386_1 == z386_2

z387_1 = LpVariable("z387_1", cat="Binary")
z387_2 = LpVariable("z387_2", cat="Binary")
prob += Wesley + smallC <= Skylar + bigM * z387_1
prob += Wesley + smallC <= Mckenna + bigM * z387_2
prob += z387_1 == z387_2

z388_1 = LpVariable("z388_1", cat="Binary")
z388_2 = LpVariable("z388_2", cat="Binary")
prob += Wesley + smallC <= Lianne + bigM * z388_1
prob += Wesley + smallC <= Skylar + bigM * z388_2
prob += z388_1 == z388_2

z389_1 = LpVariable("z389_1", cat="Binary")
z389_2 = LpVariable("z389_2", cat="Binary")
prob += Janette + smallC <= Ruben + bigM * z389_1
prob += Janette + smallC <= Pam + bigM * z389_2
prob += z389_1 == z389_2

z390_1 = LpVariable("z390_1", cat="Binary")
z390_2 = LpVariable("z390_2", cat="Binary")
prob += Janette + smallC <= Daragh + bigM * z390_1
prob += Janette + smallC <= Chase + bigM * z390_2
prob += z390_1 == z390_2

z391_1 = LpVariable("z391_1", cat="Binary")
z391_2 = LpVariable("z391_2", cat="Binary")
prob += Paris + smallC <= Oisin + bigM * z391_1
prob += Paris + smallC <= Daragh + bigM * z391_2
prob += z391_1 == z391_2

z392_1 = LpVariable("z392_1", cat="Binary")
z392_2 = LpVariable("z392_2", cat="Binary")
prob += Skylar + smallC <= Ruben + bigM * z392_1
prob += Skylar + smallC <= Daragh + bigM * z392_2
prob += z392_1 == z392_2

z393_1 = LpVariable("z393_1", cat="Binary")
z393_2 = LpVariable("z393_2", cat="Binary")
prob += Lianne + smallC <= Carla + bigM * z393_1
prob += Lianne + smallC <= Mckenna + bigM * z393_2
prob += z393_1 == z393_2

z394_1 = LpVariable("z394_1", cat="Binary")
z394_2 = LpVariable("z394_2", cat="Binary")
prob += Pam + smallC <= Wesley + bigM * z394_1
prob += Pam + smallC <= Lianne + bigM * z394_2
prob += z394_1 == z394_2

z395_1 = LpVariable("z395_1", cat="Binary")
z395_2 = LpVariable("z395_2", cat="Binary")
prob += Ruben + smallC <= Paris + bigM * z395_1
prob += Ruben + smallC <= Daragh + bigM * z395_2
prob += z395_1 == z395_2

z396_1 = LpVariable("z396_1", cat="Binary")
z396_2 = LpVariable("z396_2", cat="Binary")
prob += Daragh + smallC <= Neal + bigM * z396_1
prob += Daragh + smallC <= Gene + bigM * z396_2
prob += z396_1 == z396_2

z397_1 = LpVariable("z397_1", cat="Binary")
z397_2 = LpVariable("z397_2", cat="Binary")
prob += Mckenna + smallC <= Chase + bigM * z397_1
prob += Mckenna + smallC <= Joni + bigM * z397_2
prob += z397_1 == z397_2

z398_1 = LpVariable("z398_1", cat="Binary")
z398_2 = LpVariable("z398_2", cat="Binary")
prob += Neal + smallC <= Carla + bigM * z398_1
prob += Neal + smallC <= Gene + bigM * z398_2
prob += z398_1 == z398_2

z399_1 = LpVariable("z399_1", cat="Binary")
z399_2 = LpVariable("z399_2", cat="Binary")
prob += Oisin + smallC <= Janette + bigM * z399_1
prob += Oisin + smallC <= Ruben + bigM * z399_2
prob += z399_1 == z399_2

z400_1 = LpVariable("z400_1", cat="Binary")
z400_2 = LpVariable("z400_2", cat="Binary")
prob += Skylar + smallC <= Paris + bigM * z400_1
prob += Skylar + smallC <= Daragh + bigM * z400_2
prob += z400_1 == z400_2

z401_1 = LpVariable("z401_1", cat="Binary")
z401_2 = LpVariable("z401_2", cat="Binary")
prob += Wesley + smallC <= Neal + bigM * z401_1
prob += Wesley + smallC <= Gene + bigM * z401_2
prob += z401_1 == z401_2

z402_1 = LpVariable("z402_1", cat="Binary")
z402_2 = LpVariable("z402_2", cat="Binary")
prob += Ayesha + smallC <= Lianne + bigM * z402_1
prob += Ayesha + smallC <= Ruben + bigM * z402_2
prob += z402_1 == z402_2

z403_1 = LpVariable("z403_1", cat="Binary")
z403_2 = LpVariable("z403_2", cat="Binary")
prob += Ayesha + smallC <= Curt + bigM * z403_1
prob += Ayesha + smallC <= Chase + bigM * z403_2
prob += z403_1 == z403_2

z404_1 = LpVariable("z404_1", cat="Binary")
z404_2 = LpVariable("z404_2", cat="Binary")
prob += Janette + smallC <= Conner + bigM * z404_1
prob += Janette + smallC <= Neal + bigM * z404_2
prob += z404_1 == z404_2

z405_1 = LpVariable("z405_1", cat="Binary")
z405_2 = LpVariable("z405_2", cat="Binary")
prob += Neal + smallC <= Ayesha + bigM * z405_1
prob += Neal + smallC <= Oisin + bigM * z405_2
prob += z405_1 == z405_2

z406_1 = LpVariable("z406_1", cat="Binary")
z406_2 = LpVariable("z406_2", cat="Binary")
prob += Oisin + smallC <= Skylar + bigM * z406_1
prob += Oisin + smallC <= Chase + bigM * z406_2
prob += z406_1 == z406_2

z407_1 = LpVariable("z407_1", cat="Binary")
z407_2 = LpVariable("z407_2", cat="Binary")
prob += Oisin + smallC <= Gene + bigM * z407_1
prob += Oisin + smallC <= Chase + bigM * z407_2
prob += z407_1 == z407_2

z408_1 = LpVariable("z408_1", cat="Binary")
z408_2 = LpVariable("z408_2", cat="Binary")
prob += Ruben + smallC <= Daragh + bigM * z408_1
prob += Ruben + smallC <= Oisin + bigM * z408_2
prob += z408_1 == z408_2

z409_1 = LpVariable("z409_1", cat="Binary")
z409_2 = LpVariable("z409_2", cat="Binary")
prob += Conner + smallC <= Ayesha + bigM * z409_1
prob += Conner + smallC <= Dominick + bigM * z409_2
prob += z409_1 == z409_2

z410_1 = LpVariable("z410_1", cat="Binary")
z410_2 = LpVariable("z410_2", cat="Binary")
prob += Daragh + smallC <= Gene + bigM * z410_1
prob += Daragh + smallC <= Mckenna + bigM * z410_2
prob += z410_1 == z410_2

z411_1 = LpVariable("z411_1", cat="Binary")
z411_2 = LpVariable("z411_2", cat="Binary")
prob += Daragh + smallC <= Mckenna + bigM * z411_1
prob += Daragh + smallC <= Dominick + bigM * z411_2
prob += z411_1 == z411_2

z412_1 = LpVariable("z412_1", cat="Binary")
z412_2 = LpVariable("z412_2", cat="Binary")
prob += Oisin + smallC <= Skylar + bigM * z412_1
prob += Oisin + smallC <= Gene + bigM * z412_2
prob += z412_1 == z412_2

z413_1 = LpVariable("z413_1", cat="Binary")
z413_2 = LpVariable("z413_2", cat="Binary")
prob += Neal + smallC <= Daragh + bigM * z413_1
prob += Neal + smallC <= Paris + bigM * z413_2
prob += z413_1 == z413_2

z414_1 = LpVariable("z414_1", cat="Binary")
z414_2 = LpVariable("z414_2", cat="Binary")
prob += Daragh + smallC <= Dominick + bigM * z414_1
prob += Daragh + smallC <= Chase + bigM * z414_2
prob += z414_1 == z414_2

z415_1 = LpVariable("z415_1", cat="Binary")
z415_2 = LpVariable("z415_2", cat="Binary")
prob += Conner + smallC <= Curt + bigM * z415_1
prob += Conner + smallC <= Ayesha + bigM * z415_2
prob += z415_1 == z415_2

z416_1 = LpVariable("z416_1", cat="Binary")
z416_2 = LpVariable("z416_2", cat="Binary")
prob += Curt + smallC <= Gene + bigM * z416_1
prob += Curt + smallC <= Pam + bigM * z416_2
prob += z416_1 == z416_2

z417_1 = LpVariable("z417_1", cat="Binary")
z417_2 = LpVariable("z417_2", cat="Binary")
prob += Wesley + smallC <= Chase + bigM * z417_1
prob += Wesley + smallC <= Conner + bigM * z417_2
prob += z417_1 == z417_2

z418_1 = LpVariable("z418_1", cat="Binary")
z418_2 = LpVariable("z418_2", cat="Binary")
prob += Amari + smallC <= Mckenna + bigM * z418_1
prob += Amari + smallC <= Joni + bigM * z418_2
prob += z418_1 == z418_2

z419_1 = LpVariable("z419_1", cat="Binary")
z419_2 = LpVariable("z419_2", cat="Binary")
prob += Pam + smallC <= Oisin + bigM * z419_1
prob += Pam + smallC <= Paris + bigM * z419_2
prob += z419_1 == z419_2

z420_1 = LpVariable("z420_1", cat="Binary")
z420_2 = LpVariable("z420_2", cat="Binary")
prob += Neal + smallC <= Curt + bigM * z420_1
prob += Neal + smallC <= Amari + bigM * z420_2
prob += z420_1 == z420_2

z421_1 = LpVariable("z421_1", cat="Binary")
z421_2 = LpVariable("z421_2", cat="Binary")
prob += Mckenna + smallC <= Daragh + bigM * z421_1
prob += Mckenna + smallC <= Ruben + bigM * z421_2
prob += z421_1 == z421_2

z422_1 = LpVariable("z422_1", cat="Binary")
z422_2 = LpVariable("z422_2", cat="Binary")
prob += Pam + smallC <= Gene + bigM * z422_1
prob += Pam + smallC <= Neal + bigM * z422_2
prob += z422_1 == z422_2

z423_1 = LpVariable("z423_1", cat="Binary")
z423_2 = LpVariable("z423_2", cat="Binary")
prob += Paris + smallC <= Mckenna + bigM * z423_1
prob += Paris + smallC <= Joni + bigM * z423_2
prob += z423_1 == z423_2

z424_1 = LpVariable("z424_1", cat="Binary")
z424_2 = LpVariable("z424_2", cat="Binary")
prob += Joni + smallC <= Janette + bigM * z424_1
prob += Joni + smallC <= Carla + bigM * z424_2
prob += z424_1 == z424_2

z425_1 = LpVariable("z425_1", cat="Binary")
z425_2 = LpVariable("z425_2", cat="Binary")
prob += Conner + smallC <= Wesley + bigM * z425_1
prob += Conner + smallC <= Oisin + bigM * z425_2
prob += z425_1 == z425_2

z426_1 = LpVariable("z426_1", cat="Binary")
z426_2 = LpVariable("z426_2", cat="Binary")
prob += Conner + smallC <= Joni + bigM * z426_1
prob += Conner + smallC <= Daragh + bigM * z426_2
prob += z426_1 == z426_2

z427_1 = LpVariable("z427_1", cat="Binary")
z427_2 = LpVariable("z427_2", cat="Binary")
prob += Amari + smallC <= Conner + bigM * z427_1
prob += Amari + smallC <= Janette + bigM * z427_2
prob += z427_1 == z427_2

z428_1 = LpVariable("z428_1", cat="Binary")
z428_2 = LpVariable("z428_2", cat="Binary")
prob += Paris + smallC <= Daragh + bigM * z428_1
prob += Paris + smallC <= Oisin + bigM * z428_2
prob += z428_1 == z428_2

z429_1 = LpVariable("z429_1", cat="Binary")
z429_2 = LpVariable("z429_2", cat="Binary")
prob += Paris + smallC <= Oisin + bigM * z429_1
prob += Paris + smallC <= Daragh + bigM * z429_2
prob += z429_1 == z429_2

z430_1 = LpVariable("z430_1", cat="Binary")
z430_2 = LpVariable("z430_2", cat="Binary")
prob += Ruben + smallC <= Carla + bigM * z430_1
prob += Ruben + smallC <= Neal + bigM * z430_2
prob += z430_1 == z430_2

z431_1 = LpVariable("z431_1", cat="Binary")
z431_2 = LpVariable("z431_2", cat="Binary")
prob += Oisin + smallC <= Curt + bigM * z431_1
prob += Oisin + smallC <= Conner + bigM * z431_2
prob += z431_1 == z431_2

z432_1 = LpVariable("z432_1", cat="Binary")
z432_2 = LpVariable("z432_2", cat="Binary")
prob += Daragh + smallC <= Joni + bigM * z432_1
prob += Daragh + smallC <= Skylar + bigM * z432_2
prob += z432_1 == z432_2

z433_1 = LpVariable("z433_1", cat="Binary")
z433_2 = LpVariable("z433_2", cat="Binary")
prob += Curt + smallC <= Amari + bigM * z433_1
prob += Curt + smallC <= Conner + bigM * z433_2
prob += z433_1 == z433_2

z434_1 = LpVariable("z434_1", cat="Binary")
z434_2 = LpVariable("z434_2", cat="Binary")
prob += Daragh + smallC <= Wesley + bigM * z434_1
prob += Daragh + smallC <= Conner + bigM * z434_2
prob += z434_1 == z434_2

z435_1 = LpVariable("z435_1", cat="Binary")
z435_2 = LpVariable("z435_2", cat="Binary")
prob += Conner + smallC <= Pam + bigM * z435_1
prob += Conner + smallC <= Amari + bigM * z435_2
prob += z435_1 == z435_2

z436_1 = LpVariable("z436_1", cat="Binary")
z436_2 = LpVariable("z436_2", cat="Binary")
prob += Daragh + smallC <= Carla + bigM * z436_1
prob += Daragh + smallC <= Chase + bigM * z436_2
prob += z436_1 == z436_2

z437_1 = LpVariable("z437_1", cat="Binary")
z437_2 = LpVariable("z437_2", cat="Binary")
prob += Paris + smallC <= Carla + bigM * z437_1
prob += Paris + smallC <= Lianne + bigM * z437_2
prob += z437_1 == z437_2

z438_1 = LpVariable("z438_1", cat="Binary")
z438_2 = LpVariable("z438_2", cat="Binary")
prob += Amari + smallC <= Neal + bigM * z438_1
prob += Amari + smallC <= Conner + bigM * z438_2
prob += z438_1 == z438_2

z439_1 = LpVariable("z439_1", cat="Binary")
z439_2 = LpVariable("z439_2", cat="Binary")
prob += Oisin + smallC <= Carla + bigM * z439_1
prob += Oisin + smallC <= Joni + bigM * z439_2
prob += z439_1 == z439_2

z440_1 = LpVariable("z440_1", cat="Binary")
z440_2 = LpVariable("z440_2", cat="Binary")
prob += Neal + smallC <= Amari + bigM * z440_1
prob += Neal + smallC <= Lianne + bigM * z440_2
prob += z440_1 == z440_2

z441_1 = LpVariable("z441_1", cat="Binary")
z441_2 = LpVariable("z441_2", cat="Binary")
prob += Skylar + smallC <= Daragh + bigM * z441_1
prob += Skylar + smallC <= Oisin + bigM * z441_2
prob += z441_1 == z441_2

z442_1 = LpVariable("z442_1", cat="Binary")
z442_2 = LpVariable("z442_2", cat="Binary")
prob += Ayesha + smallC <= Skylar + bigM * z442_1
prob += Ayesha + smallC <= Paris + bigM * z442_2
prob += z442_1 == z442_2

z443_1 = LpVariable("z443_1", cat="Binary")
z443_2 = LpVariable("z443_2", cat="Binary")
prob += Paris + smallC <= Daragh + bigM * z443_1
prob += Paris + smallC <= Oisin + bigM * z443_2
prob += z443_1 == z443_2

z444_1 = LpVariable("z444_1", cat="Binary")
z444_2 = LpVariable("z444_2", cat="Binary")
prob += Ayesha + smallC <= Conner + bigM * z444_1
prob += Ayesha + smallC <= Amari + bigM * z444_2
prob += z444_1 == z444_2

z445_1 = LpVariable("z445_1", cat="Binary")
z445_2 = LpVariable("z445_2", cat="Binary")
prob += Mckenna + smallC <= Oisin + bigM * z445_1
prob += Mckenna + smallC <= Lianne + bigM * z445_2
prob += z445_1 == z445_2

z446_1 = LpVariable("z446_1", cat="Binary")
z446_2 = LpVariable("z446_2", cat="Binary")
prob += Lianne + smallC <= Oisin + bigM * z446_1
prob += Lianne + smallC <= Paris + bigM * z446_2
prob += z446_1 == z446_2

z447_1 = LpVariable("z447_1", cat="Binary")
z447_2 = LpVariable("z447_2", cat="Binary")
prob += Lianne + smallC <= Paris + bigM * z447_1
prob += Lianne + smallC <= Ruben + bigM * z447_2
prob += z447_1 == z447_2

z448_1 = LpVariable("z448_1", cat="Binary")
z448_2 = LpVariable("z448_2", cat="Binary")
prob += Curt + smallC <= Oisin + bigM * z448_1
prob += Curt + smallC <= Pam + bigM * z448_2
prob += z448_1 == z448_2

z449_1 = LpVariable("z449_1", cat="Binary")
z449_2 = LpVariable("z449_2", cat="Binary")
prob += Curt + smallC <= Janette + bigM * z449_1
prob += Curt + smallC <= Neal + bigM * z449_2
prob += z449_1 == z449_2

z450_1 = LpVariable("z450_1", cat="Binary")
z450_2 = LpVariable("z450_2", cat="Binary")
prob += Skylar + smallC <= Neal + bigM * z450_1
prob += Skylar + smallC <= Joni + bigM * z450_2
prob += z450_1 == z450_2

z451_1 = LpVariable("z451_1", cat="Binary")
z451_2 = LpVariable("z451_2", cat="Binary")
prob += Conner + smallC <= Curt + bigM * z451_1
prob += Conner + smallC <= Chase + bigM * z451_2
prob += z451_1 == z451_2

z452_1 = LpVariable("z452_1", cat="Binary")
z452_2 = LpVariable("z452_2", cat="Binary")
prob += Curt + smallC <= Conner + bigM * z452_1
prob += Curt + smallC <= Janette + bigM * z452_2
prob += z452_1 == z452_2

z453_1 = LpVariable("z453_1", cat="Binary")
z453_2 = LpVariable("z453_2", cat="Binary")
prob += Skylar + smallC <= Dominick + bigM * z453_1
prob += Skylar + smallC <= Ayesha + bigM * z453_2
prob += z453_1 == z453_2

z454_1 = LpVariable("z454_1", cat="Binary")
z454_2 = LpVariable("z454_2", cat="Binary")
prob += Wesley + smallC <= Skylar + bigM * z454_1
prob += Wesley + smallC <= Mckenna + bigM * z454_2
prob += z454_1 == z454_2

z455_1 = LpVariable("z455_1", cat="Binary")
z455_2 = LpVariable("z455_2", cat="Binary")
prob += Paris + smallC <= Oisin + bigM * z455_1
prob += Paris + smallC <= Daragh + bigM * z455_2
prob += z455_1 == z455_2

z456_1 = LpVariable("z456_1", cat="Binary")
z456_2 = LpVariable("z456_2", cat="Binary")
prob += Amari + smallC <= Skylar + bigM * z456_1
prob += Amari + smallC <= Ayesha + bigM * z456_2
prob += z456_1 == z456_2

z457_1 = LpVariable("z457_1", cat="Binary")
z457_2 = LpVariable("z457_2", cat="Binary")
prob += Wesley + smallC <= Neal + bigM * z457_1
prob += Wesley + smallC <= Janette + bigM * z457_2
prob += z457_1 == z457_2

z458_1 = LpVariable("z458_1", cat="Binary")
z458_2 = LpVariable("z458_2", cat="Binary")
prob += Daragh + smallC <= Joni + bigM * z458_1
prob += Daragh + smallC <= Amari + bigM * z458_2
prob += z458_1 == z458_2

z459_1 = LpVariable("z459_1", cat="Binary")
z459_2 = LpVariable("z459_2", cat="Binary")
prob += Ruben + smallC <= Oisin + bigM * z459_1
prob += Ruben + smallC <= Paris + bigM * z459_2
prob += z459_1 == z459_2

z460_1 = LpVariable("z460_1", cat="Binary")
z460_2 = LpVariable("z460_2", cat="Binary")
prob += Joni + smallC <= Chase + bigM * z460_1
prob += Joni + smallC <= Carla + bigM * z460_2
prob += z460_1 == z460_2

z461_1 = LpVariable("z461_1", cat="Binary")
z461_2 = LpVariable("z461_2", cat="Binary")
prob += Joni + smallC <= Dominick + bigM * z461_1
prob += Joni + smallC <= Amari + bigM * z461_2
prob += z461_1 == z461_2

z462_1 = LpVariable("z462_1", cat="Binary")
z462_2 = LpVariable("z462_2", cat="Binary")
prob += Ruben + smallC <= Amari + bigM * z462_1
prob += Ruben + smallC <= Carla + bigM * z462_2
prob += z462_1 == z462_2

z463_1 = LpVariable("z463_1", cat="Binary")
z463_2 = LpVariable("z463_2", cat="Binary")
prob += Paris + smallC <= Ruben + bigM * z463_1
prob += Paris + smallC <= Ayesha + bigM * z463_2
prob += z463_1 == z463_2

z464_1 = LpVariable("z464_1", cat="Binary")
z464_2 = LpVariable("z464_2", cat="Binary")
prob += Conner + smallC <= Dominick + bigM * z464_1
prob += Conner + smallC <= Curt + bigM * z464_2
prob += z464_1 == z464_2

z465_1 = LpVariable("z465_1", cat="Binary")
z465_2 = LpVariable("z465_2", cat="Binary")
prob += Ruben + smallC <= Skylar + bigM * z465_1
prob += Ruben + smallC <= Wesley + bigM * z465_2
prob += z465_1 == z465_2

z466_1 = LpVariable("z466_1", cat="Binary")
z466_2 = LpVariable("z466_2", cat="Binary")
prob += Oisin + smallC <= Daragh + bigM * z466_1
prob += Oisin + smallC <= Lianne + bigM * z466_2
prob += z466_1 == z466_2

z467_1 = LpVariable("z467_1", cat="Binary")
z467_2 = LpVariable("z467_2", cat="Binary")
prob += Curt + smallC <= Mckenna + bigM * z467_1
prob += Curt + smallC <= Daragh + bigM * z467_2
prob += z467_1 == z467_2

z468_1 = LpVariable("z468_1", cat="Binary")
z468_2 = LpVariable("z468_2", cat="Binary")
prob += Paris + smallC <= Daragh + bigM * z468_1
prob += Paris + smallC <= Oisin + bigM * z468_2
prob += z468_1 == z468_2

z469_1 = LpVariable("z469_1", cat="Binary")
z469_2 = LpVariable("z469_2", cat="Binary")
prob += Curt + smallC <= Amari + bigM * z469_1
prob += Curt + smallC <= Janette + bigM * z469_2
prob += z469_1 == z469_2

z470_1 = LpVariable("z470_1", cat="Binary")
z470_2 = LpVariable("z470_2", cat="Binary")
prob += Ayesha + smallC <= Paris + bigM * z470_1
prob += Ayesha + smallC <= Dominick + bigM * z470_2
prob += z470_1 == z470_2

z471_1 = LpVariable("z471_1", cat="Binary")
z471_2 = LpVariable("z471_2", cat="Binary")
prob += Amari + smallC <= Chase + bigM * z471_1
prob += Amari + smallC <= Curt + bigM * z471_2
prob += z471_1 == z471_2

z472_1 = LpVariable("z472_1", cat="Binary")
z472_2 = LpVariable("z472_2", cat="Binary")
prob += Janette + smallC <= Conner + bigM * z472_1
prob += Janette + smallC <= Neal + bigM * z472_2
prob += z472_1 == z472_2

z473_1 = LpVariable("z473_1", cat="Binary")
z473_2 = LpVariable("z473_2", cat="Binary")
prob += Janette + smallC <= Curt + bigM * z473_1
prob += Janette + smallC <= Lianne + bigM * z473_2
prob += z473_1 == z473_2

z474_1 = LpVariable("z474_1", cat="Binary")
z474_2 = LpVariable("z474_2", cat="Binary")
prob += Neal + smallC <= Pam + bigM * z474_1
prob += Neal + smallC <= Janette + bigM * z474_2
prob += z474_1 == z474_2

z475_1 = LpVariable("z475_1", cat="Binary")
z475_2 = LpVariable("z475_2", cat="Binary")
prob += Amari + smallC <= Janette + bigM * z475_1
prob += Amari + smallC <= Neal + bigM * z475_2
prob += z475_1 == z475_2

z476_1 = LpVariable("z476_1", cat="Binary")
z476_2 = LpVariable("z476_2", cat="Binary")
prob += Mckenna + smallC <= Ayesha + bigM * z476_1
prob += Mckenna + smallC <= Carla + bigM * z476_2
prob += z476_1 == z476_2

z477_1 = LpVariable("z477_1", cat="Binary")
z477_2 = LpVariable("z477_2", cat="Binary")
prob += Ayesha + smallC <= Mckenna + bigM * z477_1
prob += Ayesha + smallC <= Gene + bigM * z477_2
prob += z477_1 == z477_2

z478_1 = LpVariable("z478_1", cat="Binary")
z478_2 = LpVariable("z478_2", cat="Binary")
prob += Pam + smallC <= Joni + bigM * z478_1
prob += Pam + smallC <= Chase + bigM * z478_2
prob += z478_1 == z478_2

z479_1 = LpVariable("z479_1", cat="Binary")
z479_2 = LpVariable("z479_2", cat="Binary")
prob += Paris + smallC <= Ruben + bigM * z479_1
prob += Paris + smallC <= Conner + bigM * z479_2
prob += z479_1 == z479_2

z480_1 = LpVariable("z480_1", cat="Binary")
z480_2 = LpVariable("z480_2", cat="Binary")
prob += Ruben + smallC <= Neal + bigM * z480_1
prob += Ruben + smallC <= Gene + bigM * z480_2
prob += z480_1 == z480_2

z481_1 = LpVariable("z481_1", cat="Binary")
z481_2 = LpVariable("z481_2", cat="Binary")
prob += Janette + smallC <= Conner + bigM * z481_1
prob += Janette + smallC <= Neal + bigM * z481_2
prob += z481_1 == z481_2

z482_1 = LpVariable("z482_1", cat="Binary")
z482_2 = LpVariable("z482_2", cat="Binary")
prob += Mckenna + smallC <= Paris + bigM * z482_1
prob += Mckenna + smallC <= Skylar + bigM * z482_2
prob += z482_1 == z482_2

z483_1 = LpVariable("z483_1", cat="Binary")
z483_2 = LpVariable("z483_2", cat="Binary")
prob += Lianne + smallC <= Daragh + bigM * z483_1
prob += Lianne + smallC <= Skylar + bigM * z483_2
prob += z483_1 == z483_2

z484_1 = LpVariable("z484_1", cat="Binary")
z484_2 = LpVariable("z484_2", cat="Binary")
prob += Joni + smallC <= Neal + bigM * z484_1
prob += Joni + smallC <= Ayesha + bigM * z484_2
prob += z484_1 == z484_2

z485_1 = LpVariable("z485_1", cat="Binary")
z485_2 = LpVariable("z485_2", cat="Binary")
prob += Mckenna + smallC <= Neal + bigM * z485_1
prob += Mckenna + smallC <= Dominick + bigM * z485_2
prob += z485_1 == z485_2

z486_1 = LpVariable("z486_1", cat="Binary")
z486_2 = LpVariable("z486_2", cat="Binary")
prob += Skylar + smallC <= Oisin + bigM * z486_1
prob += Skylar + smallC <= Paris + bigM * z486_2
prob += z486_1 == z486_2

z487_1 = LpVariable("z487_1", cat="Binary")
z487_2 = LpVariable("z487_2", cat="Binary")
prob += Conner + smallC <= Mckenna + bigM * z487_1
prob += Conner + smallC <= Ruben + bigM * z487_2
prob += z487_1 == z487_2

z488_1 = LpVariable("z488_1", cat="Binary")
z488_2 = LpVariable("z488_2", cat="Binary")
prob += Oisin + smallC <= Wesley + bigM * z488_1
prob += Oisin + smallC <= Paris + bigM * z488_2
prob += z488_1 == z488_2

z489_1 = LpVariable("z489_1", cat="Binary")
z489_2 = LpVariable("z489_2", cat="Binary")
prob += Curt + smallC <= Janette + bigM * z489_1
prob += Curt + smallC <= Conner + bigM * z489_2
prob += z489_1 == z489_2

z490_1 = LpVariable("z490_1", cat="Binary")
z490_2 = LpVariable("z490_2", cat="Binary")
prob += Amari + smallC <= Neal + bigM * z490_1
prob += Amari + smallC <= Janette + bigM * z490_2
prob += z490_1 == z490_2

z491_1 = LpVariable("z491_1", cat="Binary")
z491_2 = LpVariable("z491_2", cat="Binary")
prob += Daragh + smallC <= Gene + bigM * z491_1
prob += Daragh + smallC <= Mckenna + bigM * z491_2
prob += z491_1 == z491_2

z492_1 = LpVariable("z492_1", cat="Binary")
z492_2 = LpVariable("z492_2", cat="Binary")
prob += Daragh + smallC <= Ruben + bigM * z492_1
prob += Daragh + smallC <= Skylar + bigM * z492_2
prob += z492_1 == z492_2

z493_1 = LpVariable("z493_1", cat="Binary")
z493_2 = LpVariable("z493_2", cat="Binary")
prob += Joni + smallC <= Ruben + bigM * z493_1
prob += Joni + smallC <= Lianne + bigM * z493_2
prob += z493_1 == z493_2

z494_1 = LpVariable("z494_1", cat="Binary")
z494_2 = LpVariable("z494_2", cat="Binary")
prob += Conner + smallC <= Janette + bigM * z494_1
prob += Conner + smallC <= Gene + bigM * z494_2
prob += z494_1 == z494_2

z495_1 = LpVariable("z495_1", cat="Binary")
z495_2 = LpVariable("z495_2", cat="Binary")
prob += Wesley + smallC <= Amari + bigM * z495_1
prob += Wesley + smallC <= Conner + bigM * z495_2
prob += z495_1 == z495_2

z496_1 = LpVariable("z496_1", cat="Binary")
z496_2 = LpVariable("z496_2", cat="Binary")
prob += Joni + smallC <= Gene + bigM * z496_1
prob += Joni + smallC <= Curt + bigM * z496_2
prob += z496_1 == z496_2

z497_1 = LpVariable("z497_1", cat="Binary")
z497_2 = LpVariable("z497_2", cat="Binary")
prob += Paris + smallC <= Conner + bigM * z497_1
prob += Paris + smallC <= Lianne + bigM * z497_2
prob += z497_1 == z497_2

z498_1 = LpVariable("z498_1", cat="Binary")
z498_2 = LpVariable("z498_2", cat="Binary")
prob += Ayesha + smallC <= Neal + bigM * z498_1
prob += Ayesha + smallC <= Conner + bigM * z498_2
prob += z498_1 == z498_2

z499_1 = LpVariable("z499_1", cat="Binary")
z499_2 = LpVariable("z499_2", cat="Binary")
prob += Daragh + smallC <= Neal + bigM * z499_1
prob += Daragh + smallC <= Amari + bigM * z499_2
prob += z499_1 == z499_2


GLPK().solve(prob)
ages = {}

for v in prob.variables():
	if v.name in wizzies:
		print(v.name, "=", v.varValue)
		ages[v.name] = v.varValue
