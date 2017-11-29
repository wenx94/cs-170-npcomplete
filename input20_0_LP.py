from pulp import *

prob = LpProblem("wiz", LpMaximize)

smallC = 0.05
bigM = 40
wizzies = set()
Curt = LpVariable("Curt", 1, 20, cat = "Integer")
wizzies.add("Curt")
Ruben = LpVariable("Ruben", 1, 20, cat = "Integer")
wizzies.add("Ruben")
Paris = LpVariable("Paris", 1, 20, cat = "Integer")
wizzies.add("Paris")
Chase = LpVariable("Chase", 1, 20, cat = "Integer")
wizzies.add("Chase")
Neal = LpVariable("Neal", 1, 20, cat = "Integer")
wizzies.add("Neal")
Carla = LpVariable("Carla", 1, 20, cat = "Integer")
wizzies.add("Carla")
Lianne = LpVariable("Lianne", 1, 20, cat = "Integer")
wizzies.add("Lianne")
Wesley = LpVariable("Wesley", 1, 20, cat = "Integer")
wizzies.add("Wesley")
Skylar = LpVariable("Skylar", 1, 20, cat = "Integer")
wizzies.add("Skylar")
Ayesha = LpVariable("Ayesha", 1, 20, cat = "Integer")
wizzies.add("Ayesha")
Dominick = LpVariable("Dominick", 1, 20, cat = "Integer")
wizzies.add("Dominick")
Conner = LpVariable("Conner", 1, 20, cat = "Integer")
wizzies.add("Conner")
Oisin = LpVariable("Oisin", 1, 20, cat = "Integer")
wizzies.add("Oisin")
Daragh = LpVariable("Daragh", 1, 20, cat = "Integer")
wizzies.add("Daragh")
Mckenna = LpVariable("Mckenna", 1, 20, cat = "Integer")
wizzies.add("Mckenna")
Gene = LpVariable("Gene", 1, 20, cat = "Integer")
wizzies.add("Gene")
Pam = LpVariable("Pam", 1, 20, cat = "Integer")
wizzies.add("Pam")
Joni = LpVariable("Joni", 1, 20, cat = "Integer")
wizzies.add("Joni")
Janette = LpVariable("Janette", 1, 20, cat = "Integer")
wizzies.add("Janette")
Amari = LpVariable("Amari", 1, 20, cat = "Integer")
wizzies.add("Amari")

prob += 0

z0_1 = LpVariable("z0_1", cat="Binary")
prob += Oisin + smallC <= Janette + bigM * z0_1
prob += Oisin + smallC <= Daragh + bigM * z0_1
prob += Oisin >= smallC + Janette - (1 - z0_1) * bigM
prob += Oisin >= smallC + Daragh - (1 - z0_1) * bigM
z1_1 = LpVariable("z1_1", cat="Binary")
prob += Wesley + smallC <= Ruben + bigM * z1_1
prob += Wesley + smallC <= Paris + bigM * z1_1
prob += Wesley >= smallC + Ruben - (1 - z1_1) * bigM
prob += Wesley >= smallC + Paris - (1 - z1_1) * bigM
z2_1 = LpVariable("z2_1", cat="Binary")
prob += Oisin + smallC <= Dominick + bigM * z2_1
prob += Oisin + smallC <= Daragh + bigM * z2_1
prob += Oisin >= smallC + Dominick - (1 - z2_1) * bigM
prob += Oisin >= smallC + Daragh - (1 - z2_1) * bigM
z3_1 = LpVariable("z3_1", cat="Binary")
prob += Neal + smallC <= Gene + bigM * z3_1
prob += Neal + smallC <= Janette + bigM * z3_1
prob += Neal >= smallC + Gene - (1 - z3_1) * bigM
prob += Neal >= smallC + Janette - (1 - z3_1) * bigM
z4_1 = LpVariable("z4_1", cat="Binary")
prob += Skylar + smallC <= Paris + bigM * z4_1
prob += Skylar + smallC <= Ruben + bigM * z4_1
prob += Skylar >= smallC + Paris - (1 - z4_1) * bigM
prob += Skylar >= smallC + Ruben - (1 - z4_1) * bigM
z5_1 = LpVariable("z5_1", cat="Binary")
prob += Ruben + smallC <= Oisin + bigM * z5_1
prob += Ruben + smallC <= Daragh + bigM * z5_1
prob += Ruben >= smallC + Oisin - (1 - z5_1) * bigM
prob += Ruben >= smallC + Daragh - (1 - z5_1) * bigM
z6_1 = LpVariable("z6_1", cat="Binary")
prob += Mckenna + smallC <= Carla + bigM * z6_1
prob += Mckenna + smallC <= Conner + bigM * z6_1
prob += Mckenna >= smallC + Carla - (1 - z6_1) * bigM
prob += Mckenna >= smallC + Conner - (1 - z6_1) * bigM
z7_1 = LpVariable("z7_1", cat="Binary")
prob += Oisin + smallC <= Curt + bigM * z7_1
prob += Oisin + smallC <= Mckenna + bigM * z7_1
prob += Oisin >= smallC + Curt - (1 - z7_1) * bigM
prob += Oisin >= smallC + Mckenna - (1 - z7_1) * bigM
z8_1 = LpVariable("z8_1", cat="Binary")
prob += Curt + smallC <= Ruben + bigM * z8_1
prob += Curt + smallC <= Oisin + bigM * z8_1
prob += Curt >= smallC + Ruben - (1 - z8_1) * bigM
prob += Curt >= smallC + Oisin - (1 - z8_1) * bigM
z9_1 = LpVariable("z9_1", cat="Binary")
prob += Skylar + smallC <= Gene + bigM * z9_1
prob += Skylar + smallC <= Lianne + bigM * z9_1
prob += Skylar >= smallC + Gene - (1 - z9_1) * bigM
prob += Skylar >= smallC + Lianne - (1 - z9_1) * bigM
z10_1 = LpVariable("z10_1", cat="Binary")
prob += Janette + smallC <= Conner + bigM * z10_1
prob += Janette + smallC <= Neal + bigM * z10_1
prob += Janette >= smallC + Conner - (1 - z10_1) * bigM
prob += Janette >= smallC + Neal - (1 - z10_1) * bigM
z11_1 = LpVariable("z11_1", cat="Binary")
prob += Wesley + smallC <= Daragh + bigM * z11_1
prob += Wesley + smallC <= Paris + bigM * z11_1
prob += Wesley >= smallC + Daragh - (1 - z11_1) * bigM
prob += Wesley >= smallC + Paris - (1 - z11_1) * bigM
z12_1 = LpVariable("z12_1", cat="Binary")
prob += Paris + smallC <= Oisin + bigM * z12_1
prob += Paris + smallC <= Daragh + bigM * z12_1
prob += Paris >= smallC + Oisin - (1 - z12_1) * bigM
prob += Paris >= smallC + Daragh - (1 - z12_1) * bigM
z13_1 = LpVariable("z13_1", cat="Binary")
prob += Conner + smallC <= Daragh + bigM * z13_1
prob += Conner + smallC <= Oisin + bigM * z13_1
prob += Conner >= smallC + Daragh - (1 - z13_1) * bigM
prob += Conner >= smallC + Oisin - (1 - z13_1) * bigM
z14_1 = LpVariable("z14_1", cat="Binary")
prob += Mckenna + smallC <= Neal + bigM * z14_1
prob += Mckenna + smallC <= Dominick + bigM * z14_1
prob += Mckenna >= smallC + Neal - (1 - z14_1) * bigM
prob += Mckenna >= smallC + Dominick - (1 - z14_1) * bigM
z15_1 = LpVariable("z15_1", cat="Binary")
prob += Joni + smallC <= Amari + bigM * z15_1
prob += Joni + smallC <= Neal + bigM * z15_1
prob += Joni >= smallC + Amari - (1 - z15_1) * bigM
prob += Joni >= smallC + Neal - (1 - z15_1) * bigM
z16_1 = LpVariable("z16_1", cat="Binary")
prob += Ruben + smallC <= Daragh + bigM * z16_1
prob += Ruben + smallC <= Oisin + bigM * z16_1
prob += Ruben >= smallC + Daragh - (1 - z16_1) * bigM
prob += Ruben >= smallC + Oisin - (1 - z16_1) * bigM
z17_1 = LpVariable("z17_1", cat="Binary")
prob += Pam + smallC <= Skylar + bigM * z17_1
prob += Pam + smallC <= Wesley + bigM * z17_1
prob += Pam >= smallC + Skylar - (1 - z17_1) * bigM
prob += Pam >= smallC + Wesley - (1 - z17_1) * bigM
z18_1 = LpVariable("z18_1", cat="Binary")
prob += Ayesha + smallC <= Janette + bigM * z18_1
prob += Ayesha + smallC <= Chase + bigM * z18_1
prob += Ayesha >= smallC + Janette - (1 - z18_1) * bigM
prob += Ayesha >= smallC + Chase - (1 - z18_1) * bigM
z19_1 = LpVariable("z19_1", cat="Binary")
prob += Pam + smallC <= Paris + bigM * z19_1
prob += Pam + smallC <= Wesley + bigM * z19_1
prob += Pam >= smallC + Paris - (1 - z19_1) * bigM
prob += Pam >= smallC + Wesley - (1 - z19_1) * bigM
z20_1 = LpVariable("z20_1", cat="Binary")
prob += Neal + smallC <= Conner + bigM * z20_1
prob += Neal + smallC <= Mckenna + bigM * z20_1
prob += Neal >= smallC + Conner - (1 - z20_1) * bigM
prob += Neal >= smallC + Mckenna - (1 - z20_1) * bigM
z21_1 = LpVariable("z21_1", cat="Binary")
prob += Wesley + smallC <= Skylar + bigM * z21_1
prob += Wesley + smallC <= Lianne + bigM * z21_1
prob += Wesley >= smallC + Skylar - (1 - z21_1) * bigM
prob += Wesley >= smallC + Lianne - (1 - z21_1) * bigM
z22_1 = LpVariable("z22_1", cat="Binary")
prob += Daragh + smallC <= Gene + bigM * z22_1
prob += Daragh + smallC <= Curt + bigM * z22_1
prob += Daragh >= smallC + Gene - (1 - z22_1) * bigM
prob += Daragh >= smallC + Curt - (1 - z22_1) * bigM
z23_1 = LpVariable("z23_1", cat="Binary")
prob += Conner + smallC <= Janette + bigM * z23_1
prob += Conner + smallC <= Pam + bigM * z23_1
prob += Conner >= smallC + Janette - (1 - z23_1) * bigM
prob += Conner >= smallC + Pam - (1 - z23_1) * bigM
z24_1 = LpVariable("z24_1", cat="Binary")
prob += Paris + smallC <= Daragh + bigM * z24_1
prob += Paris + smallC <= Oisin + bigM * z24_1
prob += Paris >= smallC + Daragh - (1 - z24_1) * bigM
prob += Paris >= smallC + Oisin - (1 - z24_1) * bigM
z25_1 = LpVariable("z25_1", cat="Binary")
prob += Amari + smallC <= Conner + bigM * z25_1
prob += Amari + smallC <= Neal + bigM * z25_1
prob += Amari >= smallC + Conner - (1 - z25_1) * bigM
prob += Amari >= smallC + Neal - (1 - z25_1) * bigM
z26_1 = LpVariable("z26_1", cat="Binary")
prob += Amari + smallC <= Neal + bigM * z26_1
prob += Amari + smallC <= Conner + bigM * z26_1
prob += Amari >= smallC + Neal - (1 - z26_1) * bigM
prob += Amari >= smallC + Conner - (1 - z26_1) * bigM
z27_1 = LpVariable("z27_1", cat="Binary")
prob += Mckenna + smallC <= Oisin + bigM * z27_1
prob += Mckenna + smallC <= Ruben + bigM * z27_1
prob += Mckenna >= smallC + Oisin - (1 - z27_1) * bigM
prob += Mckenna >= smallC + Ruben - (1 - z27_1) * bigM
z28_1 = LpVariable("z28_1", cat="Binary")
prob += Amari + smallC <= Neal + bigM * z28_1
prob += Amari + smallC <= Conner + bigM * z28_1
prob += Amari >= smallC + Neal - (1 - z28_1) * bigM
prob += Amari >= smallC + Conner - (1 - z28_1) * bigM
z29_1 = LpVariable("z29_1", cat="Binary")
prob += Oisin + smallC <= Dominick + bigM * z29_1
prob += Oisin + smallC <= Ruben + bigM * z29_1
prob += Oisin >= smallC + Dominick - (1 - z29_1) * bigM
prob += Oisin >= smallC + Ruben - (1 - z29_1) * bigM
z30_1 = LpVariable("z30_1", cat="Binary")
prob += Janette + smallC <= Curt + bigM * z30_1
prob += Janette + smallC <= Skylar + bigM * z30_1
prob += Janette >= smallC + Curt - (1 - z30_1) * bigM
prob += Janette >= smallC + Skylar - (1 - z30_1) * bigM
z31_1 = LpVariable("z31_1", cat="Binary")
prob += Wesley + smallC <= Lianne + bigM * z31_1
prob += Wesley + smallC <= Ruben + bigM * z31_1
prob += Wesley >= smallC + Lianne - (1 - z31_1) * bigM
prob += Wesley >= smallC + Ruben - (1 - z31_1) * bigM
z32_1 = LpVariable("z32_1", cat="Binary")
prob += Curt + smallC <= Gene + bigM * z32_1
prob += Curt + smallC <= Ayesha + bigM * z32_1
prob += Curt >= smallC + Gene - (1 - z32_1) * bigM
prob += Curt >= smallC + Ayesha - (1 - z32_1) * bigM
z33_1 = LpVariable("z33_1", cat="Binary")
prob += Oisin + smallC <= Joni + bigM * z33_1
prob += Oisin + smallC <= Paris + bigM * z33_1
prob += Oisin >= smallC + Joni - (1 - z33_1) * bigM
prob += Oisin >= smallC + Paris - (1 - z33_1) * bigM
z34_1 = LpVariable("z34_1", cat="Binary")
prob += Amari + smallC <= Joni + bigM * z34_1
prob += Amari + smallC <= Pam + bigM * z34_1
prob += Amari >= smallC + Joni - (1 - z34_1) * bigM
prob += Amari >= smallC + Pam - (1 - z34_1) * bigM
z35_1 = LpVariable("z35_1", cat="Binary")
prob += Conner + smallC <= Lianne + bigM * z35_1
prob += Conner + smallC <= Janette + bigM * z35_1
prob += Conner >= smallC + Lianne - (1 - z35_1) * bigM
prob += Conner >= smallC + Janette - (1 - z35_1) * bigM
z36_1 = LpVariable("z36_1", cat="Binary")
prob += Skylar + smallC <= Ruben + bigM * z36_1
prob += Skylar + smallC <= Daragh + bigM * z36_1
prob += Skylar >= smallC + Ruben - (1 - z36_1) * bigM
prob += Skylar >= smallC + Daragh - (1 - z36_1) * bigM
z37_1 = LpVariable("z37_1", cat="Binary")
prob += Paris + smallC <= Neal + bigM * z37_1
prob += Paris + smallC <= Gene + bigM * z37_1
prob += Paris >= smallC + Neal - (1 - z37_1) * bigM
prob += Paris >= smallC + Gene - (1 - z37_1) * bigM
z38_1 = LpVariable("z38_1", cat="Binary")
prob += Daragh + smallC <= Neal + bigM * z38_1
prob += Daragh + smallC <= Pam + bigM * z38_1
prob += Daragh >= smallC + Neal - (1 - z38_1) * bigM
prob += Daragh >= smallC + Pam - (1 - z38_1) * bigM
z39_1 = LpVariable("z39_1", cat="Binary")
prob += Skylar + smallC <= Oisin + bigM * z39_1
prob += Skylar + smallC <= Daragh + bigM * z39_1
prob += Skylar >= smallC + Oisin - (1 - z39_1) * bigM
prob += Skylar >= smallC + Daragh - (1 - z39_1) * bigM
z40_1 = LpVariable("z40_1", cat="Binary")
prob += Janette + smallC <= Neal + bigM * z40_1
prob += Janette + smallC <= Conner + bigM * z40_1
prob += Janette >= smallC + Neal - (1 - z40_1) * bigM
prob += Janette >= smallC + Conner - (1 - z40_1) * bigM
z41_1 = LpVariable("z41_1", cat="Binary")
prob += Curt + smallC <= Amari + bigM * z41_1
prob += Curt + smallC <= Neal + bigM * z41_1
prob += Curt >= smallC + Amari - (1 - z41_1) * bigM
prob += Curt >= smallC + Neal - (1 - z41_1) * bigM
z42_1 = LpVariable("z42_1", cat="Binary")
prob += Skylar + smallC <= Lianne + bigM * z42_1
prob += Skylar + smallC <= Chase + bigM * z42_1
prob += Skylar >= smallC + Lianne - (1 - z42_1) * bigM
prob += Skylar >= smallC + Chase - (1 - z42_1) * bigM
z43_1 = LpVariable("z43_1", cat="Binary")
prob += Ayesha + smallC <= Amari + bigM * z43_1
prob += Ayesha + smallC <= Neal + bigM * z43_1
prob += Ayesha >= smallC + Amari - (1 - z43_1) * bigM
prob += Ayesha >= smallC + Neal - (1 - z43_1) * bigM
z44_1 = LpVariable("z44_1", cat="Binary")
prob += Conner + smallC <= Curt + bigM * z44_1
prob += Conner + smallC <= Wesley + bigM * z44_1
prob += Conner >= smallC + Curt - (1 - z44_1) * bigM
prob += Conner >= smallC + Wesley - (1 - z44_1) * bigM
z45_1 = LpVariable("z45_1", cat="Binary")
prob += Janette + smallC <= Neal + bigM * z45_1
prob += Janette + smallC <= Conner + bigM * z45_1
prob += Janette >= smallC + Neal - (1 - z45_1) * bigM
prob += Janette >= smallC + Conner - (1 - z45_1) * bigM
z46_1 = LpVariable("z46_1", cat="Binary")
prob += Oisin + smallC <= Lianne + bigM * z46_1
prob += Oisin + smallC <= Conner + bigM * z46_1
prob += Oisin >= smallC + Lianne - (1 - z46_1) * bigM
prob += Oisin >= smallC + Conner - (1 - z46_1) * bigM
z47_1 = LpVariable("z47_1", cat="Binary")
prob += Mckenna + smallC <= Chase + bigM * z47_1
prob += Mckenna + smallC <= Joni + bigM * z47_1
prob += Mckenna >= smallC + Chase - (1 - z47_1) * bigM
prob += Mckenna >= smallC + Joni - (1 - z47_1) * bigM
z48_1 = LpVariable("z48_1", cat="Binary")
prob += Curt + smallC <= Neal + bigM * z48_1
prob += Curt + smallC <= Janette + bigM * z48_1
prob += Curt >= smallC + Neal - (1 - z48_1) * bigM
prob += Curt >= smallC + Janette - (1 - z48_1) * bigM
z49_1 = LpVariable("z49_1", cat="Binary")
prob += Lianne + smallC <= Oisin + bigM * z49_1
prob += Lianne + smallC <= Ruben + bigM * z49_1
prob += Lianne >= smallC + Oisin - (1 - z49_1) * bigM
prob += Lianne >= smallC + Ruben - (1 - z49_1) * bigM
z50_1 = LpVariable("z50_1", cat="Binary")
prob += Wesley + smallC <= Oisin + bigM * z50_1
prob += Wesley + smallC <= Paris + bigM * z50_1
prob += Wesley >= smallC + Oisin - (1 - z50_1) * bigM
prob += Wesley >= smallC + Paris - (1 - z50_1) * bigM
z51_1 = LpVariable("z51_1", cat="Binary")
prob += Conner + smallC <= Joni + bigM * z51_1
prob += Conner + smallC <= Carla + bigM * z51_1
prob += Conner >= smallC + Joni - (1 - z51_1) * bigM
prob += Conner >= smallC + Carla - (1 - z51_1) * bigM
z52_1 = LpVariable("z52_1", cat="Binary")
prob += Skylar + smallC <= Lianne + bigM * z52_1
prob += Skylar + smallC <= Conner + bigM * z52_1
prob += Skylar >= smallC + Lianne - (1 - z52_1) * bigM
prob += Skylar >= smallC + Conner - (1 - z52_1) * bigM
z53_1 = LpVariable("z53_1", cat="Binary")
prob += Lianne + smallC <= Oisin + bigM * z53_1
prob += Lianne + smallC <= Skylar + bigM * z53_1
prob += Lianne >= smallC + Oisin - (1 - z53_1) * bigM
prob += Lianne >= smallC + Skylar - (1 - z53_1) * bigM
z54_1 = LpVariable("z54_1", cat="Binary")
prob += Paris + smallC <= Oisin + bigM * z54_1
prob += Paris + smallC <= Daragh + bigM * z54_1
prob += Paris >= smallC + Oisin - (1 - z54_1) * bigM
prob += Paris >= smallC + Daragh - (1 - z54_1) * bigM
z55_1 = LpVariable("z55_1", cat="Binary")
prob += Lianne + smallC <= Gene + bigM * z55_1
prob += Lianne + smallC <= Carla + bigM * z55_1
prob += Lianne >= smallC + Gene - (1 - z55_1) * bigM
prob += Lianne >= smallC + Carla - (1 - z55_1) * bigM
z56_1 = LpVariable("z56_1", cat="Binary")
prob += Neal + smallC <= Amari + bigM * z56_1
prob += Neal + smallC <= Ruben + bigM * z56_1
prob += Neal >= smallC + Amari - (1 - z56_1) * bigM
prob += Neal >= smallC + Ruben - (1 - z56_1) * bigM
z57_1 = LpVariable("z57_1", cat="Binary")
prob += Ruben + smallC <= Chase + bigM * z57_1
prob += Ruben + smallC <= Ayesha + bigM * z57_1
prob += Ruben >= smallC + Chase - (1 - z57_1) * bigM
prob += Ruben >= smallC + Ayesha - (1 - z57_1) * bigM
z58_1 = LpVariable("z58_1", cat="Binary")
prob += Ayesha + smallC <= Pam + bigM * z58_1
prob += Ayesha + smallC <= Mckenna + bigM * z58_1
prob += Ayesha >= smallC + Pam - (1 - z58_1) * bigM
prob += Ayesha >= smallC + Mckenna - (1 - z58_1) * bigM
z59_1 = LpVariable("z59_1", cat="Binary")
prob += Neal + smallC <= Oisin + bigM * z59_1
prob += Neal + smallC <= Amari + bigM * z59_1
prob += Neal >= smallC + Oisin - (1 - z59_1) * bigM
prob += Neal >= smallC + Amari - (1 - z59_1) * bigM
z60_1 = LpVariable("z60_1", cat="Binary")
prob += Lianne + smallC <= Paris + bigM * z60_1
prob += Lianne + smallC <= Daragh + bigM * z60_1
prob += Lianne >= smallC + Paris - (1 - z60_1) * bigM
prob += Lianne >= smallC + Daragh - (1 - z60_1) * bigM
z61_1 = LpVariable("z61_1", cat="Binary")
prob += Paris + smallC <= Neal + bigM * z61_1
prob += Paris + smallC <= Carla + bigM * z61_1
prob += Paris >= smallC + Neal - (1 - z61_1) * bigM
prob += Paris >= smallC + Carla - (1 - z61_1) * bigM
z62_1 = LpVariable("z62_1", cat="Binary")
prob += Lianne + smallC <= Paris + bigM * z62_1
prob += Lianne + smallC <= Daragh + bigM * z62_1
prob += Lianne >= smallC + Paris - (1 - z62_1) * bigM
prob += Lianne >= smallC + Daragh - (1 - z62_1) * bigM
z63_1 = LpVariable("z63_1", cat="Binary")
prob += Joni + smallC <= Chase + bigM * z63_1
prob += Joni + smallC <= Conner + bigM * z63_1
prob += Joni >= smallC + Chase - (1 - z63_1) * bigM
prob += Joni >= smallC + Conner - (1 - z63_1) * bigM
z64_1 = LpVariable("z64_1", cat="Binary")
prob += Ruben + smallC <= Dominick + bigM * z64_1
prob += Ruben + smallC <= Mckenna + bigM * z64_1
prob += Ruben >= smallC + Dominick - (1 - z64_1) * bigM
prob += Ruben >= smallC + Mckenna - (1 - z64_1) * bigM
z65_1 = LpVariable("z65_1", cat="Binary")
prob += Lianne + smallC <= Pam + bigM * z65_1
prob += Lianne + smallC <= Janette + bigM * z65_1
prob += Lianne >= smallC + Pam - (1 - z65_1) * bigM
prob += Lianne >= smallC + Janette - (1 - z65_1) * bigM
z66_1 = LpVariable("z66_1", cat="Binary")
prob += Pam + smallC <= Oisin + bigM * z66_1
prob += Pam + smallC <= Paris + bigM * z66_1
prob += Pam >= smallC + Oisin - (1 - z66_1) * bigM
prob += Pam >= smallC + Paris - (1 - z66_1) * bigM
z67_1 = LpVariable("z67_1", cat="Binary")
prob += Skylar + smallC <= Paris + bigM * z67_1
prob += Skylar + smallC <= Daragh + bigM * z67_1
prob += Skylar >= smallC + Paris - (1 - z67_1) * bigM
prob += Skylar >= smallC + Daragh - (1 - z67_1) * bigM
z68_1 = LpVariable("z68_1", cat="Binary")
prob += Oisin + smallC <= Paris + bigM * z68_1
prob += Oisin + smallC <= Gene + bigM * z68_1
prob += Oisin >= smallC + Paris - (1 - z68_1) * bigM
prob += Oisin >= smallC + Gene - (1 - z68_1) * bigM
z69_1 = LpVariable("z69_1", cat="Binary")
prob += Skylar + smallC <= Daragh + bigM * z69_1
prob += Skylar + smallC <= Ruben + bigM * z69_1
prob += Skylar >= smallC + Daragh - (1 - z69_1) * bigM
prob += Skylar >= smallC + Ruben - (1 - z69_1) * bigM
z70_1 = LpVariable("z70_1", cat="Binary")
prob += Wesley + smallC <= Mckenna + bigM * z70_1
prob += Wesley + smallC <= Oisin + bigM * z70_1
prob += Wesley >= smallC + Mckenna - (1 - z70_1) * bigM
prob += Wesley >= smallC + Oisin - (1 - z70_1) * bigM
z71_1 = LpVariable("z71_1", cat="Binary")
prob += Ruben + smallC <= Paris + bigM * z71_1
prob += Ruben + smallC <= Oisin + bigM * z71_1
prob += Ruben >= smallC + Paris - (1 - z71_1) * bigM
prob += Ruben >= smallC + Oisin - (1 - z71_1) * bigM
z72_1 = LpVariable("z72_1", cat="Binary")
prob += Joni + smallC <= Amari + bigM * z72_1
prob += Joni + smallC <= Janette + bigM * z72_1
prob += Joni >= smallC + Amari - (1 - z72_1) * bigM
prob += Joni >= smallC + Janette - (1 - z72_1) * bigM
z73_1 = LpVariable("z73_1", cat="Binary")
prob += Conner + smallC <= Ruben + bigM * z73_1
prob += Conner + smallC <= Gene + bigM * z73_1
prob += Conner >= smallC + Ruben - (1 - z73_1) * bigM
prob += Conner >= smallC + Gene - (1 - z73_1) * bigM
z74_1 = LpVariable("z74_1", cat="Binary")
prob += Amari + smallC <= Paris + bigM * z74_1
prob += Amari + smallC <= Lianne + bigM * z74_1
prob += Amari >= smallC + Paris - (1 - z74_1) * bigM
prob += Amari >= smallC + Lianne - (1 - z74_1) * bigM
z75_1 = LpVariable("z75_1", cat="Binary")
prob += Conner + smallC <= Janette + bigM * z75_1
prob += Conner + smallC <= Gene + bigM * z75_1
prob += Conner >= smallC + Janette - (1 - z75_1) * bigM
prob += Conner >= smallC + Gene - (1 - z75_1) * bigM
z76_1 = LpVariable("z76_1", cat="Binary")
prob += Janette + smallC <= Conner + bigM * z76_1
prob += Janette + smallC <= Neal + bigM * z76_1
prob += Janette >= smallC + Conner - (1 - z76_1) * bigM
prob += Janette >= smallC + Neal - (1 - z76_1) * bigM
z77_1 = LpVariable("z77_1", cat="Binary")
prob += Oisin + smallC <= Paris + bigM * z77_1
prob += Oisin + smallC <= Carla + bigM * z77_1
prob += Oisin >= smallC + Paris - (1 - z77_1) * bigM
prob += Oisin >= smallC + Carla - (1 - z77_1) * bigM
z78_1 = LpVariable("z78_1", cat="Binary")
prob += Neal + smallC <= Lianne + bigM * z78_1
prob += Neal + smallC <= Daragh + bigM * z78_1
prob += Neal >= smallC + Lianne - (1 - z78_1) * bigM
prob += Neal >= smallC + Daragh - (1 - z78_1) * bigM
z79_1 = LpVariable("z79_1", cat="Binary")
prob += Amari + smallC <= Janette + bigM * z79_1
prob += Amari + smallC <= Neal + bigM * z79_1
prob += Amari >= smallC + Janette - (1 - z79_1) * bigM
prob += Amari >= smallC + Neal - (1 - z79_1) * bigM
z80_1 = LpVariable("z80_1", cat="Binary")
prob += Curt + smallC <= Joni + bigM * z80_1
prob += Curt + smallC <= Lianne + bigM * z80_1
prob += Curt >= smallC + Joni - (1 - z80_1) * bigM
prob += Curt >= smallC + Lianne - (1 - z80_1) * bigM
z81_1 = LpVariable("z81_1", cat="Binary")
prob += Lianne + smallC <= Ruben + bigM * z81_1
prob += Lianne + smallC <= Daragh + bigM * z81_1
prob += Lianne >= smallC + Ruben - (1 - z81_1) * bigM
prob += Lianne >= smallC + Daragh - (1 - z81_1) * bigM
z82_1 = LpVariable("z82_1", cat="Binary")
prob += Janette + smallC <= Joni + bigM * z82_1
prob += Janette + smallC <= Paris + bigM * z82_1
prob += Janette >= smallC + Joni - (1 - z82_1) * bigM
prob += Janette >= smallC + Paris - (1 - z82_1) * bigM
z83_1 = LpVariable("z83_1", cat="Binary")
prob += Mckenna + smallC <= Joni + bigM * z83_1
prob += Mckenna + smallC <= Janette + bigM * z83_1
prob += Mckenna >= smallC + Joni - (1 - z83_1) * bigM
prob += Mckenna >= smallC + Janette - (1 - z83_1) * bigM
z84_1 = LpVariable("z84_1", cat="Binary")
prob += Neal + smallC <= Gene + bigM * z84_1
prob += Neal + smallC <= Paris + bigM * z84_1
prob += Neal >= smallC + Gene - (1 - z84_1) * bigM
prob += Neal >= smallC + Paris - (1 - z84_1) * bigM
z85_1 = LpVariable("z85_1", cat="Binary")
prob += Pam + smallC <= Joni + bigM * z85_1
prob += Pam + smallC <= Curt + bigM * z85_1
prob += Pam >= smallC + Joni - (1 - z85_1) * bigM
prob += Pam >= smallC + Curt - (1 - z85_1) * bigM
z86_1 = LpVariable("z86_1", cat="Binary")
prob += Daragh + smallC <= Lianne + bigM * z86_1
prob += Daragh + smallC <= Ayesha + bigM * z86_1
prob += Daragh >= smallC + Lianne - (1 - z86_1) * bigM
prob += Daragh >= smallC + Ayesha - (1 - z86_1) * bigM
z87_1 = LpVariable("z87_1", cat="Binary")
prob += Curt + smallC <= Janette + bigM * z87_1
prob += Curt + smallC <= Amari + bigM * z87_1
prob += Curt >= smallC + Janette - (1 - z87_1) * bigM
prob += Curt >= smallC + Amari - (1 - z87_1) * bigM
z88_1 = LpVariable("z88_1", cat="Binary")
prob += Ayesha + smallC <= Janette + bigM * z88_1
prob += Ayesha + smallC <= Chase + bigM * z88_1
prob += Ayesha >= smallC + Janette - (1 - z88_1) * bigM
prob += Ayesha >= smallC + Chase - (1 - z88_1) * bigM
z89_1 = LpVariable("z89_1", cat="Binary")
prob += Amari + smallC <= Conner + bigM * z89_1
prob += Amari + smallC <= Neal + bigM * z89_1
prob += Amari >= smallC + Conner - (1 - z89_1) * bigM
prob += Amari >= smallC + Neal - (1 - z89_1) * bigM
z90_1 = LpVariable("z90_1", cat="Binary")
prob += Amari + smallC <= Neal + bigM * z90_1
prob += Amari + smallC <= Janette + bigM * z90_1
prob += Amari >= smallC + Neal - (1 - z90_1) * bigM
prob += Amari >= smallC + Janette - (1 - z90_1) * bigM
z91_1 = LpVariable("z91_1", cat="Binary")
prob += Mckenna + smallC <= Skylar + bigM * z91_1
prob += Mckenna + smallC <= Oisin + bigM * z91_1
prob += Mckenna >= smallC + Skylar - (1 - z91_1) * bigM
prob += Mckenna >= smallC + Oisin - (1 - z91_1) * bigM
z92_1 = LpVariable("z92_1", cat="Binary")
prob += Ayesha + smallC <= Oisin + bigM * z92_1
prob += Ayesha + smallC <= Paris + bigM * z92_1
prob += Ayesha >= smallC + Oisin - (1 - z92_1) * bigM
prob += Ayesha >= smallC + Paris - (1 - z92_1) * bigM
z93_1 = LpVariable("z93_1", cat="Binary")
prob += Paris + smallC <= Ruben + bigM * z93_1
prob += Paris + smallC <= Skylar + bigM * z93_1
prob += Paris >= smallC + Ruben - (1 - z93_1) * bigM
prob += Paris >= smallC + Skylar - (1 - z93_1) * bigM
z94_1 = LpVariable("z94_1", cat="Binary")
prob += Mckenna + smallC <= Lianne + bigM * z94_1
prob += Mckenna + smallC <= Ruben + bigM * z94_1
prob += Mckenna >= smallC + Lianne - (1 - z94_1) * bigM
prob += Mckenna >= smallC + Ruben - (1 - z94_1) * bigM
z95_1 = LpVariable("z95_1", cat="Binary")
prob += Mckenna + smallC <= Joni + bigM * z95_1
prob += Mckenna + smallC <= Pam + bigM * z95_1
prob += Mckenna >= smallC + Joni - (1 - z95_1) * bigM
prob += Mckenna >= smallC + Pam - (1 - z95_1) * bigM
z96_1 = LpVariable("z96_1", cat="Binary")
prob += Oisin + smallC <= Dominick + bigM * z96_1
prob += Oisin + smallC <= Amari + bigM * z96_1
prob += Oisin >= smallC + Dominick - (1 - z96_1) * bigM
prob += Oisin >= smallC + Amari - (1 - z96_1) * bigM
z97_1 = LpVariable("z97_1", cat="Binary")
prob += Daragh + smallC <= Pam + bigM * z97_1
prob += Daragh + smallC <= Gene + bigM * z97_1
prob += Daragh >= smallC + Pam - (1 - z97_1) * bigM
prob += Daragh >= smallC + Gene - (1 - z97_1) * bigM
z98_1 = LpVariable("z98_1", cat="Binary")
prob += Ruben + smallC <= Oisin + bigM * z98_1
prob += Ruben + smallC <= Daragh + bigM * z98_1
prob += Ruben >= smallC + Oisin - (1 - z98_1) * bigM
prob += Ruben >= smallC + Daragh - (1 - z98_1) * bigM
z99_1 = LpVariable("z99_1", cat="Binary")
prob += Amari + smallC <= Chase + bigM * z99_1
prob += Amari + smallC <= Pam + bigM * z99_1
prob += Amari >= smallC + Chase - (1 - z99_1) * bigM
prob += Amari >= smallC + Pam - (1 - z99_1) * bigM
z100_1 = LpVariable("z100_1", cat="Binary")
prob += Joni + smallC <= Paris + bigM * z100_1
prob += Joni + smallC <= Wesley + bigM * z100_1
prob += Joni >= smallC + Paris - (1 - z100_1) * bigM
prob += Joni >= smallC + Wesley - (1 - z100_1) * bigM
z101_1 = LpVariable("z101_1", cat="Binary")
prob += Ayesha + smallC <= Wesley + bigM * z101_1
prob += Ayesha + smallC <= Oisin + bigM * z101_1
prob += Ayesha >= smallC + Wesley - (1 - z101_1) * bigM
prob += Ayesha >= smallC + Oisin - (1 - z101_1) * bigM
z102_1 = LpVariable("z102_1", cat="Binary")
prob += Skylar + smallC <= Lianne + bigM * z102_1
prob += Skylar + smallC <= Wesley + bigM * z102_1
prob += Skylar >= smallC + Lianne - (1 - z102_1) * bigM
prob += Skylar >= smallC + Wesley - (1 - z102_1) * bigM
z103_1 = LpVariable("z103_1", cat="Binary")
prob += Paris + smallC <= Oisin + bigM * z103_1
prob += Paris + smallC <= Daragh + bigM * z103_1
prob += Paris >= smallC + Oisin - (1 - z103_1) * bigM
prob += Paris >= smallC + Daragh - (1 - z103_1) * bigM
z104_1 = LpVariable("z104_1", cat="Binary")
prob += Conner + smallC <= Lianne + bigM * z104_1
prob += Conner + smallC <= Daragh + bigM * z104_1
prob += Conner >= smallC + Lianne - (1 - z104_1) * bigM
prob += Conner >= smallC + Daragh - (1 - z104_1) * bigM
z105_1 = LpVariable("z105_1", cat="Binary")
prob += Neal + smallC <= Mckenna + bigM * z105_1
prob += Neal + smallC <= Janette + bigM * z105_1
prob += Neal >= smallC + Mckenna - (1 - z105_1) * bigM
prob += Neal >= smallC + Janette - (1 - z105_1) * bigM
z106_1 = LpVariable("z106_1", cat="Binary")
prob += Ayesha + smallC <= Neal + bigM * z106_1
prob += Ayesha + smallC <= Amari + bigM * z106_1
prob += Ayesha >= smallC + Neal - (1 - z106_1) * bigM
prob += Ayesha >= smallC + Amari - (1 - z106_1) * bigM
z107_1 = LpVariable("z107_1", cat="Binary")
prob += Skylar + smallC <= Conner + bigM * z107_1
prob += Skylar + smallC <= Mckenna + bigM * z107_1
prob += Skylar >= smallC + Conner - (1 - z107_1) * bigM
prob += Skylar >= smallC + Mckenna - (1 - z107_1) * bigM
z108_1 = LpVariable("z108_1", cat="Binary")
prob += Amari + smallC <= Janette + bigM * z108_1
prob += Amari + smallC <= Neal + bigM * z108_1
prob += Amari >= smallC + Janette - (1 - z108_1) * bigM
prob += Amari >= smallC + Neal - (1 - z108_1) * bigM
z109_1 = LpVariable("z109_1", cat="Binary")
prob += Paris + smallC <= Oisin + bigM * z109_1
prob += Paris + smallC <= Daragh + bigM * z109_1
prob += Paris >= smallC + Oisin - (1 - z109_1) * bigM
prob += Paris >= smallC + Daragh - (1 - z109_1) * bigM
z110_1 = LpVariable("z110_1", cat="Binary")
prob += Janette + smallC <= Daragh + bigM * z110_1
prob += Janette + smallC <= Lianne + bigM * z110_1
prob += Janette >= smallC + Daragh - (1 - z110_1) * bigM
prob += Janette >= smallC + Lianne - (1 - z110_1) * bigM
z111_1 = LpVariable("z111_1", cat="Binary")
prob += Ayesha + smallC <= Amari + bigM * z111_1
prob += Ayesha + smallC <= Curt + bigM * z111_1
prob += Ayesha >= smallC + Amari - (1 - z111_1) * bigM
prob += Ayesha >= smallC + Curt - (1 - z111_1) * bigM
z112_1 = LpVariable("z112_1", cat="Binary")
prob += Skylar + smallC <= Paris + bigM * z112_1
prob += Skylar + smallC <= Daragh + bigM * z112_1
prob += Skylar >= smallC + Paris - (1 - z112_1) * bigM
prob += Skylar >= smallC + Daragh - (1 - z112_1) * bigM
z113_1 = LpVariable("z113_1", cat="Binary")
prob += Amari + smallC <= Lianne + bigM * z113_1
prob += Amari + smallC <= Gene + bigM * z113_1
prob += Amari >= smallC + Lianne - (1 - z113_1) * bigM
prob += Amari >= smallC + Gene - (1 - z113_1) * bigM
z114_1 = LpVariable("z114_1", cat="Binary")
prob += Mckenna + smallC <= Conner + bigM * z114_1
prob += Mckenna + smallC <= Dominick + bigM * z114_1
prob += Mckenna >= smallC + Conner - (1 - z114_1) * bigM
prob += Mckenna >= smallC + Dominick - (1 - z114_1) * bigM
z115_1 = LpVariable("z115_1", cat="Binary")
prob += Amari + smallC <= Skylar + bigM * z115_1
prob += Amari + smallC <= Curt + bigM * z115_1
prob += Amari >= smallC + Skylar - (1 - z115_1) * bigM
prob += Amari >= smallC + Curt - (1 - z115_1) * bigM
z116_1 = LpVariable("z116_1", cat="Binary")
prob += Ayesha + smallC <= Paris + bigM * z116_1
prob += Ayesha + smallC <= Wesley + bigM * z116_1
prob += Ayesha >= smallC + Paris - (1 - z116_1) * bigM
prob += Ayesha >= smallC + Wesley - (1 - z116_1) * bigM
z117_1 = LpVariable("z117_1", cat="Binary")
prob += Oisin + smallC <= Neal + bigM * z117_1
prob += Oisin + smallC <= Wesley + bigM * z117_1
prob += Oisin >= smallC + Neal - (1 - z117_1) * bigM
prob += Oisin >= smallC + Wesley - (1 - z117_1) * bigM
z118_1 = LpVariable("z118_1", cat="Binary")
prob += Mckenna + smallC <= Lianne + bigM * z118_1
prob += Mckenna + smallC <= Skylar + bigM * z118_1
prob += Mckenna >= smallC + Lianne - (1 - z118_1) * bigM
prob += Mckenna >= smallC + Skylar - (1 - z118_1) * bigM
z119_1 = LpVariable("z119_1", cat="Binary")
prob += Janette + smallC <= Mckenna + bigM * z119_1
prob += Janette + smallC <= Ayesha + bigM * z119_1
prob += Janette >= smallC + Mckenna - (1 - z119_1) * bigM
prob += Janette >= smallC + Ayesha - (1 - z119_1) * bigM
z120_1 = LpVariable("z120_1", cat="Binary")
prob += Mckenna + smallC <= Oisin + bigM * z120_1
prob += Mckenna + smallC <= Skylar + bigM * z120_1
prob += Mckenna >= smallC + Oisin - (1 - z120_1) * bigM
prob += Mckenna >= smallC + Skylar - (1 - z120_1) * bigM
z121_1 = LpVariable("z121_1", cat="Binary")
prob += Pam + smallC <= Mckenna + bigM * z121_1
prob += Pam + smallC <= Wesley + bigM * z121_1
prob += Pam >= smallC + Mckenna - (1 - z121_1) * bigM
prob += Pam >= smallC + Wesley - (1 - z121_1) * bigM
z122_1 = LpVariable("z122_1", cat="Binary")
prob += Neal + smallC <= Skylar + bigM * z122_1
prob += Neal + smallC <= Conner + bigM * z122_1
prob += Neal >= smallC + Skylar - (1 - z122_1) * bigM
prob += Neal >= smallC + Conner - (1 - z122_1) * bigM
z123_1 = LpVariable("z123_1", cat="Binary")
prob += Ayesha + smallC <= Carla + bigM * z123_1
prob += Ayesha + smallC <= Chase + bigM * z123_1
prob += Ayesha >= smallC + Carla - (1 - z123_1) * bigM
prob += Ayesha >= smallC + Chase - (1 - z123_1) * bigM
z124_1 = LpVariable("z124_1", cat="Binary")
prob += Pam + smallC <= Ruben + bigM * z124_1
prob += Pam + smallC <= Lianne + bigM * z124_1
prob += Pam >= smallC + Ruben - (1 - z124_1) * bigM
prob += Pam >= smallC + Lianne - (1 - z124_1) * bigM
z125_1 = LpVariable("z125_1", cat="Binary")
prob += Conner + smallC <= Janette + bigM * z125_1
prob += Conner + smallC <= Curt + bigM * z125_1
prob += Conner >= smallC + Janette - (1 - z125_1) * bigM
prob += Conner >= smallC + Curt - (1 - z125_1) * bigM
z126_1 = LpVariable("z126_1", cat="Binary")
prob += Pam + smallC <= Paris + bigM * z126_1
prob += Pam + smallC <= Wesley + bigM * z126_1
prob += Pam >= smallC + Paris - (1 - z126_1) * bigM
prob += Pam >= smallC + Wesley - (1 - z126_1) * bigM
z127_1 = LpVariable("z127_1", cat="Binary")
prob += Pam + smallC <= Oisin + bigM * z127_1
prob += Pam + smallC <= Paris + bigM * z127_1
prob += Pam >= smallC + Oisin - (1 - z127_1) * bigM
prob += Pam >= smallC + Paris - (1 - z127_1) * bigM
z128_1 = LpVariable("z128_1", cat="Binary")
prob += Neal + smallC <= Conner + bigM * z128_1
prob += Neal + smallC <= Curt + bigM * z128_1
prob += Neal >= smallC + Conner - (1 - z128_1) * bigM
prob += Neal >= smallC + Curt - (1 - z128_1) * bigM
z129_1 = LpVariable("z129_1", cat="Binary")
prob += Lianne + smallC <= Oisin + bigM * z129_1
prob += Lianne + smallC <= Ruben + bigM * z129_1
prob += Lianne >= smallC + Oisin - (1 - z129_1) * bigM
prob += Lianne >= smallC + Ruben - (1 - z129_1) * bigM
z130_1 = LpVariable("z130_1", cat="Binary")
prob += Janette + smallC <= Dominick + bigM * z130_1
prob += Janette + smallC <= Daragh + bigM * z130_1
prob += Janette >= smallC + Dominick - (1 - z130_1) * bigM
prob += Janette >= smallC + Daragh - (1 - z130_1) * bigM
z131_1 = LpVariable("z131_1", cat="Binary")
prob += Amari + smallC <= Conner + bigM * z131_1
prob += Amari + smallC <= Neal + bigM * z131_1
prob += Amari >= smallC + Conner - (1 - z131_1) * bigM
prob += Amari >= smallC + Neal - (1 - z131_1) * bigM
z132_1 = LpVariable("z132_1", cat="Binary")
prob += Mckenna + smallC <= Dominick + bigM * z132_1
prob += Mckenna + smallC <= Joni + bigM * z132_1
prob += Mckenna >= smallC + Dominick - (1 - z132_1) * bigM
prob += Mckenna >= smallC + Joni - (1 - z132_1) * bigM
z133_1 = LpVariable("z133_1", cat="Binary")
prob += Neal + smallC <= Dominick + bigM * z133_1
prob += Neal + smallC <= Chase + bigM * z133_1
prob += Neal >= smallC + Dominick - (1 - z133_1) * bigM
prob += Neal >= smallC + Chase - (1 - z133_1) * bigM
z134_1 = LpVariable("z134_1", cat="Binary")
prob += Wesley + smallC <= Daragh + bigM * z134_1
prob += Wesley + smallC <= Oisin + bigM * z134_1
prob += Wesley >= smallC + Daragh - (1 - z134_1) * bigM
prob += Wesley >= smallC + Oisin - (1 - z134_1) * bigM
z135_1 = LpVariable("z135_1", cat="Binary")
prob += Janette + smallC <= Conner + bigM * z135_1
prob += Janette + smallC <= Neal + bigM * z135_1
prob += Janette >= smallC + Conner - (1 - z135_1) * bigM
prob += Janette >= smallC + Neal - (1 - z135_1) * bigM
z136_1 = LpVariable("z136_1", cat="Binary")
prob += Lianne + smallC <= Skylar + bigM * z136_1
prob += Lianne + smallC <= Paris + bigM * z136_1
prob += Lianne >= smallC + Skylar - (1 - z136_1) * bigM
prob += Lianne >= smallC + Paris - (1 - z136_1) * bigM
z137_1 = LpVariable("z137_1", cat="Binary")
prob += Ruben + smallC <= Janette + bigM * z137_1
prob += Ruben + smallC <= Gene + bigM * z137_1
prob += Ruben >= smallC + Janette - (1 - z137_1) * bigM
prob += Ruben >= smallC + Gene - (1 - z137_1) * bigM
z138_1 = LpVariable("z138_1", cat="Binary")
prob += Joni + smallC <= Carla + bigM * z138_1
prob += Joni + smallC <= Amari + bigM * z138_1
prob += Joni >= smallC + Carla - (1 - z138_1) * bigM
prob += Joni >= smallC + Amari - (1 - z138_1) * bigM
z139_1 = LpVariable("z139_1", cat="Binary")
prob += Oisin + smallC <= Dominick + bigM * z139_1
prob += Oisin + smallC <= Skylar + bigM * z139_1
prob += Oisin >= smallC + Dominick - (1 - z139_1) * bigM
prob += Oisin >= smallC + Skylar - (1 - z139_1) * bigM
z140_1 = LpVariable("z140_1", cat="Binary")
prob += Mckenna + smallC <= Dominick + bigM * z140_1
prob += Mckenna + smallC <= Chase + bigM * z140_1
prob += Mckenna >= smallC + Dominick - (1 - z140_1) * bigM
prob += Mckenna >= smallC + Chase - (1 - z140_1) * bigM
z141_1 = LpVariable("z141_1", cat="Binary")
prob += Janette + smallC <= Conner + bigM * z141_1
prob += Janette + smallC <= Neal + bigM * z141_1
prob += Janette >= smallC + Conner - (1 - z141_1) * bigM
prob += Janette >= smallC + Neal - (1 - z141_1) * bigM
z142_1 = LpVariable("z142_1", cat="Binary")
prob += Daragh + smallC <= Wesley + bigM * z142_1
prob += Daragh + smallC <= Neal + bigM * z142_1
prob += Daragh >= smallC + Wesley - (1 - z142_1) * bigM
prob += Daragh >= smallC + Neal - (1 - z142_1) * bigM
z143_1 = LpVariable("z143_1", cat="Binary")
prob += Curt + smallC <= Wesley + bigM * z143_1
prob += Curt + smallC <= Lianne + bigM * z143_1
prob += Curt >= smallC + Wesley - (1 - z143_1) * bigM
prob += Curt >= smallC + Lianne - (1 - z143_1) * bigM
z144_1 = LpVariable("z144_1", cat="Binary")
prob += Amari + smallC <= Janette + bigM * z144_1
prob += Amari + smallC <= Neal + bigM * z144_1
prob += Amari >= smallC + Janette - (1 - z144_1) * bigM
prob += Amari >= smallC + Neal - (1 - z144_1) * bigM
z145_1 = LpVariable("z145_1", cat="Binary")
prob += Oisin + smallC <= Chase + bigM * z145_1
prob += Oisin + smallC <= Conner + bigM * z145_1
prob += Oisin >= smallC + Chase - (1 - z145_1) * bigM
prob += Oisin >= smallC + Conner - (1 - z145_1) * bigM
z146_1 = LpVariable("z146_1", cat="Binary")
prob += Pam + smallC <= Paris + bigM * z146_1
prob += Pam + smallC <= Skylar + bigM * z146_1
prob += Pam >= smallC + Paris - (1 - z146_1) * bigM
prob += Pam >= smallC + Skylar - (1 - z146_1) * bigM
z147_1 = LpVariable("z147_1", cat="Binary")
prob += Janette + smallC <= Joni + bigM * z147_1
prob += Janette + smallC <= Amari + bigM * z147_1
prob += Janette >= smallC + Joni - (1 - z147_1) * bigM
prob += Janette >= smallC + Amari - (1 - z147_1) * bigM
z148_1 = LpVariable("z148_1", cat="Binary")
prob += Ruben + smallC <= Amari + bigM * z148_1
prob += Ruben + smallC <= Ayesha + bigM * z148_1
prob += Ruben >= smallC + Amari - (1 - z148_1) * bigM
prob += Ruben >= smallC + Ayesha - (1 - z148_1) * bigM
z149_1 = LpVariable("z149_1", cat="Binary")
prob += Conner + smallC <= Curt + bigM * z149_1
prob += Conner + smallC <= Chase + bigM * z149_1
prob += Conner >= smallC + Curt - (1 - z149_1) * bigM
prob += Conner >= smallC + Chase - (1 - z149_1) * bigM
z150_1 = LpVariable("z150_1", cat="Binary")
prob += Joni + smallC <= Amari + bigM * z150_1
prob += Joni + smallC <= Curt + bigM * z150_1
prob += Joni >= smallC + Amari - (1 - z150_1) * bigM
prob += Joni >= smallC + Curt - (1 - z150_1) * bigM
z151_1 = LpVariable("z151_1", cat="Binary")
prob += Lianne + smallC <= Pam + bigM * z151_1
prob += Lianne + smallC <= Carla + bigM * z151_1
prob += Lianne >= smallC + Pam - (1 - z151_1) * bigM
prob += Lianne >= smallC + Carla - (1 - z151_1) * bigM
z152_1 = LpVariable("z152_1", cat="Binary")
prob += Paris + smallC <= Oisin + bigM * z152_1
prob += Paris + smallC <= Daragh + bigM * z152_1
prob += Paris >= smallC + Oisin - (1 - z152_1) * bigM
prob += Paris >= smallC + Daragh - (1 - z152_1) * bigM
z153_1 = LpVariable("z153_1", cat="Binary")
prob += Wesley + smallC <= Ruben + bigM * z153_1
prob += Wesley + smallC <= Mckenna + bigM * z153_1
prob += Wesley >= smallC + Ruben - (1 - z153_1) * bigM
prob += Wesley >= smallC + Mckenna - (1 - z153_1) * bigM
z154_1 = LpVariable("z154_1", cat="Binary")
prob += Lianne + smallC <= Carla + bigM * z154_1
prob += Lianne + smallC <= Chase + bigM * z154_1
prob += Lianne >= smallC + Carla - (1 - z154_1) * bigM
prob += Lianne >= smallC + Chase - (1 - z154_1) * bigM
z155_1 = LpVariable("z155_1", cat="Binary")
prob += Curt + smallC <= Conner + bigM * z155_1
prob += Curt + smallC <= Janette + bigM * z155_1
prob += Curt >= smallC + Conner - (1 - z155_1) * bigM
prob += Curt >= smallC + Janette - (1 - z155_1) * bigM
z156_1 = LpVariable("z156_1", cat="Binary")
prob += Pam + smallC <= Carla + bigM * z156_1
prob += Pam + smallC <= Chase + bigM * z156_1
prob += Pam >= smallC + Carla - (1 - z156_1) * bigM
prob += Pam >= smallC + Chase - (1 - z156_1) * bigM
z157_1 = LpVariable("z157_1", cat="Binary")
prob += Conner + smallC <= Daragh + bigM * z157_1
prob += Conner + smallC <= Ayesha + bigM * z157_1
prob += Conner >= smallC + Daragh - (1 - z157_1) * bigM
prob += Conner >= smallC + Ayesha - (1 - z157_1) * bigM
z158_1 = LpVariable("z158_1", cat="Binary")
prob += Pam + smallC <= Lianne + bigM * z158_1
prob += Pam + smallC <= Daragh + bigM * z158_1
prob += Pam >= smallC + Lianne - (1 - z158_1) * bigM
prob += Pam >= smallC + Daragh - (1 - z158_1) * bigM
z159_1 = LpVariable("z159_1", cat="Binary")
prob += Curt + smallC <= Amari + bigM * z159_1
prob += Curt + smallC <= Neal + bigM * z159_1
prob += Curt >= smallC + Amari - (1 - z159_1) * bigM
prob += Curt >= smallC + Neal - (1 - z159_1) * bigM
z160_1 = LpVariable("z160_1", cat="Binary")
prob += Oisin + smallC <= Carla + bigM * z160_1
prob += Oisin + smallC <= Gene + bigM * z160_1
prob += Oisin >= smallC + Carla - (1 - z160_1) * bigM
prob += Oisin >= smallC + Gene - (1 - z160_1) * bigM
z161_1 = LpVariable("z161_1", cat="Binary")
prob += Neal + smallC <= Gene + bigM * z161_1
prob += Neal + smallC <= Lianne + bigM * z161_1
prob += Neal >= smallC + Gene - (1 - z161_1) * bigM
prob += Neal >= smallC + Lianne - (1 - z161_1) * bigM
z162_1 = LpVariable("z162_1", cat="Binary")
prob += Janette + smallC <= Neal + bigM * z162_1
prob += Janette + smallC <= Conner + bigM * z162_1
prob += Janette >= smallC + Neal - (1 - z162_1) * bigM
prob += Janette >= smallC + Conner - (1 - z162_1) * bigM
z163_1 = LpVariable("z163_1", cat="Binary")
prob += Lianne + smallC <= Skylar + bigM * z163_1
prob += Lianne + smallC <= Ruben + bigM * z163_1
prob += Lianne >= smallC + Skylar - (1 - z163_1) * bigM
prob += Lianne >= smallC + Ruben - (1 - z163_1) * bigM
z164_1 = LpVariable("z164_1", cat="Binary")
prob += Curt + smallC <= Oisin + bigM * z164_1
prob += Curt + smallC <= Ayesha + bigM * z164_1
prob += Curt >= smallC + Oisin - (1 - z164_1) * bigM
prob += Curt >= smallC + Ayesha - (1 - z164_1) * bigM
z165_1 = LpVariable("z165_1", cat="Binary")
prob += Janette + smallC <= Skylar + bigM * z165_1
prob += Janette + smallC <= Daragh + bigM * z165_1
prob += Janette >= smallC + Skylar - (1 - z165_1) * bigM
prob += Janette >= smallC + Daragh - (1 - z165_1) * bigM
z166_1 = LpVariable("z166_1", cat="Binary")
prob += Paris + smallC <= Conner + bigM * z166_1
prob += Paris + smallC <= Curt + bigM * z166_1
prob += Paris >= smallC + Conner - (1 - z166_1) * bigM
prob += Paris >= smallC + Curt - (1 - z166_1) * bigM
z167_1 = LpVariable("z167_1", cat="Binary")
prob += Mckenna + smallC <= Paris + bigM * z167_1
prob += Mckenna + smallC <= Daragh + bigM * z167_1
prob += Mckenna >= smallC + Paris - (1 - z167_1) * bigM
prob += Mckenna >= smallC + Daragh - (1 - z167_1) * bigM
z168_1 = LpVariable("z168_1", cat="Binary")
prob += Ruben + smallC <= Daragh + bigM * z168_1
prob += Ruben + smallC <= Oisin + bigM * z168_1
prob += Ruben >= smallC + Daragh - (1 - z168_1) * bigM
prob += Ruben >= smallC + Oisin - (1 - z168_1) * bigM
z169_1 = LpVariable("z169_1", cat="Binary")
prob += Daragh + smallC <= Ayesha + bigM * z169_1
prob += Daragh + smallC <= Paris + bigM * z169_1
prob += Daragh >= smallC + Ayesha - (1 - z169_1) * bigM
prob += Daragh >= smallC + Paris - (1 - z169_1) * bigM
z170_1 = LpVariable("z170_1", cat="Binary")
prob += Skylar + smallC <= Mckenna + bigM * z170_1
prob += Skylar + smallC <= Lianne + bigM * z170_1
prob += Skylar >= smallC + Mckenna - (1 - z170_1) * bigM
prob += Skylar >= smallC + Lianne - (1 - z170_1) * bigM
z171_1 = LpVariable("z171_1", cat="Binary")
prob += Conner + smallC <= Chase + bigM * z171_1
prob += Conner + smallC <= Skylar + bigM * z171_1
prob += Conner >= smallC + Chase - (1 - z171_1) * bigM
prob += Conner >= smallC + Skylar - (1 - z171_1) * bigM
z172_1 = LpVariable("z172_1", cat="Binary")
prob += Ruben + smallC <= Paris + bigM * z172_1
prob += Ruben + smallC <= Oisin + bigM * z172_1
prob += Ruben >= smallC + Paris - (1 - z172_1) * bigM
prob += Ruben >= smallC + Oisin - (1 - z172_1) * bigM
z173_1 = LpVariable("z173_1", cat="Binary")
prob += Pam + smallC <= Daragh + bigM * z173_1
prob += Pam + smallC <= Ruben + bigM * z173_1
prob += Pam >= smallC + Daragh - (1 - z173_1) * bigM
prob += Pam >= smallC + Ruben - (1 - z173_1) * bigM
z174_1 = LpVariable("z174_1", cat="Binary")
prob += Curt + smallC <= Chase + bigM * z174_1
prob += Curt + smallC <= Daragh + bigM * z174_1
prob += Curt >= smallC + Chase - (1 - z174_1) * bigM
prob += Curt >= smallC + Daragh - (1 - z174_1) * bigM
z175_1 = LpVariable("z175_1", cat="Binary")
prob += Wesley + smallC <= Joni + bigM * z175_1
prob += Wesley + smallC <= Pam + bigM * z175_1
prob += Wesley >= smallC + Joni - (1 - z175_1) * bigM
prob += Wesley >= smallC + Pam - (1 - z175_1) * bigM
z176_1 = LpVariable("z176_1", cat="Binary")
prob += Ayesha + smallC <= Chase + bigM * z176_1
prob += Ayesha + smallC <= Curt + bigM * z176_1
prob += Ayesha >= smallC + Chase - (1 - z176_1) * bigM
prob += Ayesha >= smallC + Curt - (1 - z176_1) * bigM
z177_1 = LpVariable("z177_1", cat="Binary")
prob += Conner + smallC <= Carla + bigM * z177_1
prob += Conner + smallC <= Wesley + bigM * z177_1
prob += Conner >= smallC + Carla - (1 - z177_1) * bigM
prob += Conner >= smallC + Wesley - (1 - z177_1) * bigM
z178_1 = LpVariable("z178_1", cat="Binary")
prob += Paris + smallC <= Daragh + bigM * z178_1
prob += Paris + smallC <= Oisin + bigM * z178_1
prob += Paris >= smallC + Daragh - (1 - z178_1) * bigM
prob += Paris >= smallC + Oisin - (1 - z178_1) * bigM
z179_1 = LpVariable("z179_1", cat="Binary")
prob += Ayesha + smallC <= Neal + bigM * z179_1
prob += Ayesha + smallC <= Carla + bigM * z179_1
prob += Ayesha >= smallC + Neal - (1 - z179_1) * bigM
prob += Ayesha >= smallC + Carla - (1 - z179_1) * bigM
z180_1 = LpVariable("z180_1", cat="Binary")
prob += Pam + smallC <= Chase + bigM * z180_1
prob += Pam + smallC <= Ayesha + bigM * z180_1
prob += Pam >= smallC + Chase - (1 - z180_1) * bigM
prob += Pam >= smallC + Ayesha - (1 - z180_1) * bigM
z181_1 = LpVariable("z181_1", cat="Binary")
prob += Mckenna + smallC <= Janette + bigM * z181_1
prob += Mckenna + smallC <= Ayesha + bigM * z181_1
prob += Mckenna >= smallC + Janette - (1 - z181_1) * bigM
prob += Mckenna >= smallC + Ayesha - (1 - z181_1) * bigM
z182_1 = LpVariable("z182_1", cat="Binary")
prob += Oisin + smallC <= Curt + bigM * z182_1
prob += Oisin + smallC <= Wesley + bigM * z182_1
prob += Oisin >= smallC + Curt - (1 - z182_1) * bigM
prob += Oisin >= smallC + Wesley - (1 - z182_1) * bigM
z183_1 = LpVariable("z183_1", cat="Binary")
prob += Conner + smallC <= Janette + bigM * z183_1
prob += Conner + smallC <= Daragh + bigM * z183_1
prob += Conner >= smallC + Janette - (1 - z183_1) * bigM
prob += Conner >= smallC + Daragh - (1 - z183_1) * bigM
z184_1 = LpVariable("z184_1", cat="Binary")
prob += Ayesha + smallC <= Oisin + bigM * z184_1
prob += Ayesha + smallC <= Daragh + bigM * z184_1
prob += Ayesha >= smallC + Oisin - (1 - z184_1) * bigM
prob += Ayesha >= smallC + Daragh - (1 - z184_1) * bigM
z185_1 = LpVariable("z185_1", cat="Binary")
prob += Ruben + smallC <= Paris + bigM * z185_1
prob += Ruben + smallC <= Oisin + bigM * z185_1
prob += Ruben >= smallC + Paris - (1 - z185_1) * bigM
prob += Ruben >= smallC + Oisin - (1 - z185_1) * bigM
z186_1 = LpVariable("z186_1", cat="Binary")
prob += Daragh + smallC <= Carla + bigM * z186_1
prob += Daragh + smallC <= Curt + bigM * z186_1
prob += Daragh >= smallC + Carla - (1 - z186_1) * bigM
prob += Daragh >= smallC + Curt - (1 - z186_1) * bigM
z187_1 = LpVariable("z187_1", cat="Binary")
prob += Lianne + smallC <= Paris + bigM * z187_1
prob += Lianne + smallC <= Skylar + bigM * z187_1
prob += Lianne >= smallC + Paris - (1 - z187_1) * bigM
prob += Lianne >= smallC + Skylar - (1 - z187_1) * bigM
z188_1 = LpVariable("z188_1", cat="Binary")
prob += Joni + smallC <= Ayesha + bigM * z188_1
prob += Joni + smallC <= Chase + bigM * z188_1
prob += Joni >= smallC + Ayesha - (1 - z188_1) * bigM
prob += Joni >= smallC + Chase - (1 - z188_1) * bigM
z189_1 = LpVariable("z189_1", cat="Binary")
prob += Neal + smallC <= Conner + bigM * z189_1
prob += Neal + smallC <= Chase + bigM * z189_1
prob += Neal >= smallC + Conner - (1 - z189_1) * bigM
prob += Neal >= smallC + Chase - (1 - z189_1) * bigM
z190_1 = LpVariable("z190_1", cat="Binary")
prob += Janette + smallC <= Amari + bigM * z190_1
prob += Janette + smallC <= Lianne + bigM * z190_1
prob += Janette >= smallC + Amari - (1 - z190_1) * bigM
prob += Janette >= smallC + Lianne - (1 - z190_1) * bigM
z191_1 = LpVariable("z191_1", cat="Binary")
prob += Neal + smallC <= Janette + bigM * z191_1
prob += Neal + smallC <= Chase + bigM * z191_1
prob += Neal >= smallC + Janette - (1 - z191_1) * bigM
prob += Neal >= smallC + Chase - (1 - z191_1) * bigM
z192_1 = LpVariable("z192_1", cat="Binary")
prob += Daragh + smallC <= Joni + bigM * z192_1
prob += Daragh + smallC <= Carla + bigM * z192_1
prob += Daragh >= smallC + Joni - (1 - z192_1) * bigM
prob += Daragh >= smallC + Carla - (1 - z192_1) * bigM
z193_1 = LpVariable("z193_1", cat="Binary")
prob += Amari + smallC <= Neal + bigM * z193_1
prob += Amari + smallC <= Conner + bigM * z193_1
prob += Amari >= smallC + Neal - (1 - z193_1) * bigM
prob += Amari >= smallC + Conner - (1 - z193_1) * bigM
z194_1 = LpVariable("z194_1", cat="Binary")
prob += Joni + smallC <= Mckenna + bigM * z194_1
prob += Joni + smallC <= Daragh + bigM * z194_1
prob += Joni >= smallC + Mckenna - (1 - z194_1) * bigM
prob += Joni >= smallC + Daragh - (1 - z194_1) * bigM
z195_1 = LpVariable("z195_1", cat="Binary")
prob += Skylar + smallC <= Paris + bigM * z195_1
prob += Skylar + smallC <= Ruben + bigM * z195_1
prob += Skylar >= smallC + Paris - (1 - z195_1) * bigM
prob += Skylar >= smallC + Ruben - (1 - z195_1) * bigM
z196_1 = LpVariable("z196_1", cat="Binary")
prob += Ruben + smallC <= Joni + bigM * z196_1
prob += Ruben + smallC <= Amari + bigM * z196_1
prob += Ruben >= smallC + Joni - (1 - z196_1) * bigM
prob += Ruben >= smallC + Amari - (1 - z196_1) * bigM
z197_1 = LpVariable("z197_1", cat="Binary")
prob += Neal + smallC <= Chase + bigM * z197_1
prob += Neal + smallC <= Oisin + bigM * z197_1
prob += Neal >= smallC + Chase - (1 - z197_1) * bigM
prob += Neal >= smallC + Oisin - (1 - z197_1) * bigM
z198_1 = LpVariable("z198_1", cat="Binary")
prob += Ruben + smallC <= Curt + bigM * z198_1
prob += Ruben + smallC <= Janette + bigM * z198_1
prob += Ruben >= smallC + Curt - (1 - z198_1) * bigM
prob += Ruben >= smallC + Janette - (1 - z198_1) * bigM
z199_1 = LpVariable("z199_1", cat="Binary")
prob += Skylar + smallC <= Oisin + bigM * z199_1
prob += Skylar + smallC <= Ruben + bigM * z199_1
prob += Skylar >= smallC + Oisin - (1 - z199_1) * bigM
prob += Skylar >= smallC + Ruben - (1 - z199_1) * bigM
z200_1 = LpVariable("z200_1", cat="Binary")
prob += Paris + smallC <= Chase + bigM * z200_1
prob += Paris + smallC <= Wesley + bigM * z200_1
prob += Paris >= smallC + Chase - (1 - z200_1) * bigM
prob += Paris >= smallC + Wesley - (1 - z200_1) * bigM
z201_1 = LpVariable("z201_1", cat="Binary")
prob += Paris + smallC <= Daragh + bigM * z201_1
prob += Paris + smallC <= Oisin + bigM * z201_1
prob += Paris >= smallC + Daragh - (1 - z201_1) * bigM
prob += Paris >= smallC + Oisin - (1 - z201_1) * bigM
z202_1 = LpVariable("z202_1", cat="Binary")
prob += Joni + smallC <= Gene + bigM * z202_1
prob += Joni + smallC <= Ayesha + bigM * z202_1
prob += Joni >= smallC + Gene - (1 - z202_1) * bigM
prob += Joni >= smallC + Ayesha - (1 - z202_1) * bigM
z203_1 = LpVariable("z203_1", cat="Binary")
prob += Curt + smallC <= Neal + bigM * z203_1
prob += Curt + smallC <= Janette + bigM * z203_1
prob += Curt >= smallC + Neal - (1 - z203_1) * bigM
prob += Curt >= smallC + Janette - (1 - z203_1) * bigM
z204_1 = LpVariable("z204_1", cat="Binary")
prob += Ayesha + smallC <= Joni + bigM * z204_1
prob += Ayesha + smallC <= Oisin + bigM * z204_1
prob += Ayesha >= smallC + Joni - (1 - z204_1) * bigM
prob += Ayesha >= smallC + Oisin - (1 - z204_1) * bigM
z205_1 = LpVariable("z205_1", cat="Binary")
prob += Oisin + smallC <= Joni + bigM * z205_1
prob += Oisin + smallC <= Ayesha + bigM * z205_1
prob += Oisin >= smallC + Joni - (1 - z205_1) * bigM
prob += Oisin >= smallC + Ayesha - (1 - z205_1) * bigM
z206_1 = LpVariable("z206_1", cat="Binary")
prob += Janette + smallC <= Oisin + bigM * z206_1
prob += Janette + smallC <= Chase + bigM * z206_1
prob += Janette >= smallC + Oisin - (1 - z206_1) * bigM
prob += Janette >= smallC + Chase - (1 - z206_1) * bigM
z207_1 = LpVariable("z207_1", cat="Binary")
prob += Janette + smallC <= Neal + bigM * z207_1
prob += Janette + smallC <= Conner + bigM * z207_1
prob += Janette >= smallC + Neal - (1 - z207_1) * bigM
prob += Janette >= smallC + Conner - (1 - z207_1) * bigM
z208_1 = LpVariable("z208_1", cat="Binary")
prob += Pam + smallC <= Skylar + bigM * z208_1
prob += Pam + smallC <= Daragh + bigM * z208_1
prob += Pam >= smallC + Skylar - (1 - z208_1) * bigM
prob += Pam >= smallC + Daragh - (1 - z208_1) * bigM
z209_1 = LpVariable("z209_1", cat="Binary")
prob += Oisin + smallC <= Skylar + bigM * z209_1
prob += Oisin + smallC <= Paris + bigM * z209_1
prob += Oisin >= smallC + Skylar - (1 - z209_1) * bigM
prob += Oisin >= smallC + Paris - (1 - z209_1) * bigM
z210_1 = LpVariable("z210_1", cat="Binary")
prob += Joni + smallC <= Pam + bigM * z210_1
prob += Joni + smallC <= Daragh + bigM * z210_1
prob += Joni >= smallC + Pam - (1 - z210_1) * bigM
prob += Joni >= smallC + Daragh - (1 - z210_1) * bigM
z211_1 = LpVariable("z211_1", cat="Binary")
prob += Wesley + smallC <= Lianne + bigM * z211_1
prob += Wesley + smallC <= Oisin + bigM * z211_1
prob += Wesley >= smallC + Lianne - (1 - z211_1) * bigM
prob += Wesley >= smallC + Oisin - (1 - z211_1) * bigM
z212_1 = LpVariable("z212_1", cat="Binary")
prob += Paris + smallC <= Oisin + bigM * z212_1
prob += Paris + smallC <= Daragh + bigM * z212_1
prob += Paris >= smallC + Oisin - (1 - z212_1) * bigM
prob += Paris >= smallC + Daragh - (1 - z212_1) * bigM
z213_1 = LpVariable("z213_1", cat="Binary")
prob += Wesley + smallC <= Mckenna + bigM * z213_1
prob += Wesley + smallC <= Lianne + bigM * z213_1
prob += Wesley >= smallC + Mckenna - (1 - z213_1) * bigM
prob += Wesley >= smallC + Lianne - (1 - z213_1) * bigM
z214_1 = LpVariable("z214_1", cat="Binary")
prob += Joni + smallC <= Daragh + bigM * z214_1
prob += Joni + smallC <= Lianne + bigM * z214_1
prob += Joni >= smallC + Daragh - (1 - z214_1) * bigM
prob += Joni >= smallC + Lianne - (1 - z214_1) * bigM
z215_1 = LpVariable("z215_1", cat="Binary")
prob += Neal + smallC <= Mckenna + bigM * z215_1
prob += Neal + smallC <= Ruben + bigM * z215_1
prob += Neal >= smallC + Mckenna - (1 - z215_1) * bigM
prob += Neal >= smallC + Ruben - (1 - z215_1) * bigM
z216_1 = LpVariable("z216_1", cat="Binary")
prob += Pam + smallC <= Carla + bigM * z216_1
prob += Pam + smallC <= Gene + bigM * z216_1
prob += Pam >= smallC + Carla - (1 - z216_1) * bigM
prob += Pam >= smallC + Gene - (1 - z216_1) * bigM
z217_1 = LpVariable("z217_1", cat="Binary")
prob += Neal + smallC <= Dominick + bigM * z217_1
prob += Neal + smallC <= Lianne + bigM * z217_1
prob += Neal >= smallC + Dominick - (1 - z217_1) * bigM
prob += Neal >= smallC + Lianne - (1 - z217_1) * bigM
z218_1 = LpVariable("z218_1", cat="Binary")
prob += Skylar + smallC <= Lianne + bigM * z218_1
prob += Skylar + smallC <= Gene + bigM * z218_1
prob += Skylar >= smallC + Lianne - (1 - z218_1) * bigM
prob += Skylar >= smallC + Gene - (1 - z218_1) * bigM
z219_1 = LpVariable("z219_1", cat="Binary")
prob += Ayesha + smallC <= Paris + bigM * z219_1
prob += Ayesha + smallC <= Daragh + bigM * z219_1
prob += Ayesha >= smallC + Paris - (1 - z219_1) * bigM
prob += Ayesha >= smallC + Daragh - (1 - z219_1) * bigM
z220_1 = LpVariable("z220_1", cat="Binary")
prob += Janette + smallC <= Neal + bigM * z220_1
prob += Janette + smallC <= Conner + bigM * z220_1
prob += Janette >= smallC + Neal - (1 - z220_1) * bigM
prob += Janette >= smallC + Conner - (1 - z220_1) * bigM
z221_1 = LpVariable("z221_1", cat="Binary")
prob += Lianne + smallC <= Daragh + bigM * z221_1
prob += Lianne + smallC <= Skylar + bigM * z221_1
prob += Lianne >= smallC + Daragh - (1 - z221_1) * bigM
prob += Lianne >= smallC + Skylar - (1 - z221_1) * bigM
z222_1 = LpVariable("z222_1", cat="Binary")
prob += Amari + smallC <= Lianne + bigM * z222_1
prob += Amari + smallC <= Joni + bigM * z222_1
prob += Amari >= smallC + Lianne - (1 - z222_1) * bigM
prob += Amari >= smallC + Joni - (1 - z222_1) * bigM
z223_1 = LpVariable("z223_1", cat="Binary")
prob += Pam + smallC <= Ruben + bigM * z223_1
prob += Pam + smallC <= Mckenna + bigM * z223_1
prob += Pam >= smallC + Ruben - (1 - z223_1) * bigM
prob += Pam >= smallC + Mckenna - (1 - z223_1) * bigM
z224_1 = LpVariable("z224_1", cat="Binary")
prob += Lianne + smallC <= Skylar + bigM * z224_1
prob += Lianne + smallC <= Ruben + bigM * z224_1
prob += Lianne >= smallC + Skylar - (1 - z224_1) * bigM
prob += Lianne >= smallC + Ruben - (1 - z224_1) * bigM
z225_1 = LpVariable("z225_1", cat="Binary")
prob += Pam + smallC <= Chase + bigM * z225_1
prob += Pam + smallC <= Janette + bigM * z225_1
prob += Pam >= smallC + Chase - (1 - z225_1) * bigM
prob += Pam >= smallC + Janette - (1 - z225_1) * bigM
z226_1 = LpVariable("z226_1", cat="Binary")
prob += Skylar + smallC <= Curt + bigM * z226_1
prob += Skylar + smallC <= Pam + bigM * z226_1
prob += Skylar >= smallC + Curt - (1 - z226_1) * bigM
prob += Skylar >= smallC + Pam - (1 - z226_1) * bigM
z227_1 = LpVariable("z227_1", cat="Binary")
prob += Pam + smallC <= Ayesha + bigM * z227_1
prob += Pam + smallC <= Curt + bigM * z227_1
prob += Pam >= smallC + Ayesha - (1 - z227_1) * bigM
prob += Pam >= smallC + Curt - (1 - z227_1) * bigM
z228_1 = LpVariable("z228_1", cat="Binary")
prob += Lianne + smallC <= Oisin + bigM * z228_1
prob += Lianne + smallC <= Ruben + bigM * z228_1
prob += Lianne >= smallC + Oisin - (1 - z228_1) * bigM
prob += Lianne >= smallC + Ruben - (1 - z228_1) * bigM
z229_1 = LpVariable("z229_1", cat="Binary")
prob += Oisin + smallC <= Pam + bigM * z229_1
prob += Oisin + smallC <= Dominick + bigM * z229_1
prob += Oisin >= smallC + Pam - (1 - z229_1) * bigM
prob += Oisin >= smallC + Dominick - (1 - z229_1) * bigM
z230_1 = LpVariable("z230_1", cat="Binary")
prob += Skylar + smallC <= Dominick + bigM * z230_1
prob += Skylar + smallC <= Joni + bigM * z230_1
prob += Skylar >= smallC + Dominick - (1 - z230_1) * bigM
prob += Skylar >= smallC + Joni - (1 - z230_1) * bigM
z231_1 = LpVariable("z231_1", cat="Binary")
prob += Paris + smallC <= Dominick + bigM * z231_1
prob += Paris + smallC <= Neal + bigM * z231_1
prob += Paris >= smallC + Dominick - (1 - z231_1) * bigM
prob += Paris >= smallC + Neal - (1 - z231_1) * bigM
z232_1 = LpVariable("z232_1", cat="Binary")
prob += Mckenna + smallC <= Curt + bigM * z232_1
prob += Mckenna + smallC <= Neal + bigM * z232_1
prob += Mckenna >= smallC + Curt - (1 - z232_1) * bigM
prob += Mckenna >= smallC + Neal - (1 - z232_1) * bigM
z233_1 = LpVariable("z233_1", cat="Binary")
prob += Joni + smallC <= Neal + bigM * z233_1
prob += Joni + smallC <= Dominick + bigM * z233_1
prob += Joni >= smallC + Neal - (1 - z233_1) * bigM
prob += Joni >= smallC + Dominick - (1 - z233_1) * bigM
z234_1 = LpVariable("z234_1", cat="Binary")
prob += Skylar + smallC <= Daragh + bigM * z234_1
prob += Skylar + smallC <= Oisin + bigM * z234_1
prob += Skylar >= smallC + Daragh - (1 - z234_1) * bigM
prob += Skylar >= smallC + Oisin - (1 - z234_1) * bigM
z235_1 = LpVariable("z235_1", cat="Binary")
prob += Lianne + smallC <= Ayesha + bigM * z235_1
prob += Lianne + smallC <= Chase + bigM * z235_1
prob += Lianne >= smallC + Ayesha - (1 - z235_1) * bigM
prob += Lianne >= smallC + Chase - (1 - z235_1) * bigM
z236_1 = LpVariable("z236_1", cat="Binary")
prob += Neal + smallC <= Janette + bigM * z236_1
prob += Neal + smallC <= Lianne + bigM * z236_1
prob += Neal >= smallC + Janette - (1 - z236_1) * bigM
prob += Neal >= smallC + Lianne - (1 - z236_1) * bigM
z237_1 = LpVariable("z237_1", cat="Binary")
prob += Amari + smallC <= Mckenna + bigM * z237_1
prob += Amari + smallC <= Dominick + bigM * z237_1
prob += Amari >= smallC + Mckenna - (1 - z237_1) * bigM
prob += Amari >= smallC + Dominick - (1 - z237_1) * bigM
z238_1 = LpVariable("z238_1", cat="Binary")
prob += Wesley + smallC <= Mckenna + bigM * z238_1
prob += Wesley + smallC <= Skylar + bigM * z238_1
prob += Wesley >= smallC + Mckenna - (1 - z238_1) * bigM
prob += Wesley >= smallC + Skylar - (1 - z238_1) * bigM
z239_1 = LpVariable("z239_1", cat="Binary")
prob += Lianne + smallC <= Dominick + bigM * z239_1
prob += Lianne + smallC <= Mckenna + bigM * z239_1
prob += Lianne >= smallC + Dominick - (1 - z239_1) * bigM
prob += Lianne >= smallC + Mckenna - (1 - z239_1) * bigM
z240_1 = LpVariable("z240_1", cat="Binary")
prob += Oisin + smallC <= Ayesha + bigM * z240_1
prob += Oisin + smallC <= Daragh + bigM * z240_1
prob += Oisin >= smallC + Ayesha - (1 - z240_1) * bigM
prob += Oisin >= smallC + Daragh - (1 - z240_1) * bigM
z241_1 = LpVariable("z241_1", cat="Binary")
prob += Ayesha + smallC <= Paris + bigM * z241_1
prob += Ayesha + smallC <= Daragh + bigM * z241_1
prob += Ayesha >= smallC + Paris - (1 - z241_1) * bigM
prob += Ayesha >= smallC + Daragh - (1 - z241_1) * bigM
z242_1 = LpVariable("z242_1", cat="Binary")
prob += Joni + smallC <= Conner + bigM * z242_1
prob += Joni + smallC <= Amari + bigM * z242_1
prob += Joni >= smallC + Conner - (1 - z242_1) * bigM
prob += Joni >= smallC + Amari - (1 - z242_1) * bigM
z243_1 = LpVariable("z243_1", cat="Binary")
prob += Daragh + smallC <= Pam + bigM * z243_1
prob += Daragh + smallC <= Carla + bigM * z243_1
prob += Daragh >= smallC + Pam - (1 - z243_1) * bigM
prob += Daragh >= smallC + Carla - (1 - z243_1) * bigM
z244_1 = LpVariable("z244_1", cat="Binary")
prob += Conner + smallC <= Pam + bigM * z244_1
prob += Conner + smallC <= Daragh + bigM * z244_1
prob += Conner >= smallC + Pam - (1 - z244_1) * bigM
prob += Conner >= smallC + Daragh - (1 - z244_1) * bigM
z245_1 = LpVariable("z245_1", cat="Binary")
prob += Janette + smallC <= Curt + bigM * z245_1
prob += Janette + smallC <= Gene + bigM * z245_1
prob += Janette >= smallC + Curt - (1 - z245_1) * bigM
prob += Janette >= smallC + Gene - (1 - z245_1) * bigM
z246_1 = LpVariable("z246_1", cat="Binary")
prob += Neal + smallC <= Skylar + bigM * z246_1
prob += Neal + smallC <= Chase + bigM * z246_1
prob += Neal >= smallC + Skylar - (1 - z246_1) * bigM
prob += Neal >= smallC + Chase - (1 - z246_1) * bigM
z247_1 = LpVariable("z247_1", cat="Binary")
prob += Wesley + smallC <= Ruben + bigM * z247_1
prob += Wesley + smallC <= Mckenna + bigM * z247_1
prob += Wesley >= smallC + Ruben - (1 - z247_1) * bigM
prob += Wesley >= smallC + Mckenna - (1 - z247_1) * bigM
z248_1 = LpVariable("z248_1", cat="Binary")
prob += Pam + smallC <= Janette + bigM * z248_1
prob += Pam + smallC <= Dominick + bigM * z248_1
prob += Pam >= smallC + Janette - (1 - z248_1) * bigM
prob += Pam >= smallC + Dominick - (1 - z248_1) * bigM
z249_1 = LpVariable("z249_1", cat="Binary")
prob += Paris + smallC <= Mckenna + bigM * z249_1
prob += Paris + smallC <= Skylar + bigM * z249_1
prob += Paris >= smallC + Mckenna - (1 - z249_1) * bigM
prob += Paris >= smallC + Skylar - (1 - z249_1) * bigM
z250_1 = LpVariable("z250_1", cat="Binary")
prob += Paris + smallC <= Skylar + bigM * z250_1
prob += Paris + smallC <= Neal + bigM * z250_1
prob += Paris >= smallC + Skylar - (1 - z250_1) * bigM
prob += Paris >= smallC + Neal - (1 - z250_1) * bigM
z251_1 = LpVariable("z251_1", cat="Binary")
prob += Wesley + smallC <= Curt + bigM * z251_1
prob += Wesley + smallC <= Janette + bigM * z251_1
prob += Wesley >= smallC + Curt - (1 - z251_1) * bigM
prob += Wesley >= smallC + Janette - (1 - z251_1) * bigM
z252_1 = LpVariable("z252_1", cat="Binary")
prob += Skylar + smallC <= Daragh + bigM * z252_1
prob += Skylar + smallC <= Ruben + bigM * z252_1
prob += Skylar >= smallC + Daragh - (1 - z252_1) * bigM
prob += Skylar >= smallC + Ruben - (1 - z252_1) * bigM
z253_1 = LpVariable("z253_1", cat="Binary")
prob += Curt + smallC <= Conner + bigM * z253_1
prob += Curt + smallC <= Neal + bigM * z253_1
prob += Curt >= smallC + Conner - (1 - z253_1) * bigM
prob += Curt >= smallC + Neal - (1 - z253_1) * bigM
z254_1 = LpVariable("z254_1", cat="Binary")
prob += Curt + smallC <= Neal + bigM * z254_1
prob += Curt + smallC <= Amari + bigM * z254_1
prob += Curt >= smallC + Neal - (1 - z254_1) * bigM
prob += Curt >= smallC + Amari - (1 - z254_1) * bigM
z255_1 = LpVariable("z255_1", cat="Binary")
prob += Ruben + smallC <= Lianne + bigM * z255_1
prob += Ruben + smallC <= Skylar + bigM * z255_1
prob += Ruben >= smallC + Lianne - (1 - z255_1) * bigM
prob += Ruben >= smallC + Skylar - (1 - z255_1) * bigM
z256_1 = LpVariable("z256_1", cat="Binary")
prob += Joni + smallC <= Carla + bigM * z256_1
prob += Joni + smallC <= Gene + bigM * z256_1
prob += Joni >= smallC + Carla - (1 - z256_1) * bigM
prob += Joni >= smallC + Gene - (1 - z256_1) * bigM
z257_1 = LpVariable("z257_1", cat="Binary")
prob += Ruben + smallC <= Mckenna + bigM * z257_1
prob += Ruben + smallC <= Janette + bigM * z257_1
prob += Ruben >= smallC + Mckenna - (1 - z257_1) * bigM
prob += Ruben >= smallC + Janette - (1 - z257_1) * bigM
z258_1 = LpVariable("z258_1", cat="Binary")
prob += Ayesha + smallC <= Pam + bigM * z258_1
prob += Ayesha + smallC <= Dominick + bigM * z258_1
prob += Ayesha >= smallC + Pam - (1 - z258_1) * bigM
prob += Ayesha >= smallC + Dominick - (1 - z258_1) * bigM
z259_1 = LpVariable("z259_1", cat="Binary")
prob += Skylar + smallC <= Oisin + bigM * z259_1
prob += Skylar + smallC <= Paris + bigM * z259_1
prob += Skylar >= smallC + Oisin - (1 - z259_1) * bigM
prob += Skylar >= smallC + Paris - (1 - z259_1) * bigM
z260_1 = LpVariable("z260_1", cat="Binary")
prob += Oisin + smallC <= Curt + bigM * z260_1
prob += Oisin + smallC <= Daragh + bigM * z260_1
prob += Oisin >= smallC + Curt - (1 - z260_1) * bigM
prob += Oisin >= smallC + Daragh - (1 - z260_1) * bigM
z261_1 = LpVariable("z261_1", cat="Binary")
prob += Oisin + smallC <= Paris + bigM * z261_1
prob += Oisin + smallC <= Pam + bigM * z261_1
prob += Oisin >= smallC + Paris - (1 - z261_1) * bigM
prob += Oisin >= smallC + Pam - (1 - z261_1) * bigM
z262_1 = LpVariable("z262_1", cat="Binary")
prob += Mckenna + smallC <= Ayesha + bigM * z262_1
prob += Mckenna + smallC <= Amari + bigM * z262_1
prob += Mckenna >= smallC + Ayesha - (1 - z262_1) * bigM
prob += Mckenna >= smallC + Amari - (1 - z262_1) * bigM
z263_1 = LpVariable("z263_1", cat="Binary")
prob += Lianne + smallC <= Daragh + bigM * z263_1
prob += Lianne + smallC <= Paris + bigM * z263_1
prob += Lianne >= smallC + Daragh - (1 - z263_1) * bigM
prob += Lianne >= smallC + Paris - (1 - z263_1) * bigM
z264_1 = LpVariable("z264_1", cat="Binary")
prob += Ayesha + smallC <= Paris + bigM * z264_1
prob += Ayesha + smallC <= Lianne + bigM * z264_1
prob += Ayesha >= smallC + Paris - (1 - z264_1) * bigM
prob += Ayesha >= smallC + Lianne - (1 - z264_1) * bigM
z265_1 = LpVariable("z265_1", cat="Binary")
prob += Neal + smallC <= Curt + bigM * z265_1
prob += Neal + smallC <= Carla + bigM * z265_1
prob += Neal >= smallC + Curt - (1 - z265_1) * bigM
prob += Neal >= smallC + Carla - (1 - z265_1) * bigM
z266_1 = LpVariable("z266_1", cat="Binary")
prob += Mckenna + smallC <= Ruben + bigM * z266_1
prob += Mckenna + smallC <= Skylar + bigM * z266_1
prob += Mckenna >= smallC + Ruben - (1 - z266_1) * bigM
prob += Mckenna >= smallC + Skylar - (1 - z266_1) * bigM
z267_1 = LpVariable("z267_1", cat="Binary")
prob += Daragh + smallC <= Dominick + bigM * z267_1
prob += Daragh + smallC <= Janette + bigM * z267_1
prob += Daragh >= smallC + Dominick - (1 - z267_1) * bigM
prob += Daragh >= smallC + Janette - (1 - z267_1) * bigM
z268_1 = LpVariable("z268_1", cat="Binary")
prob += Wesley + smallC <= Chase + bigM * z268_1
prob += Wesley + smallC <= Dominick + bigM * z268_1
prob += Wesley >= smallC + Chase - (1 - z268_1) * bigM
prob += Wesley >= smallC + Dominick - (1 - z268_1) * bigM
z269_1 = LpVariable("z269_1", cat="Binary")
prob += Neal + smallC <= Daragh + bigM * z269_1
prob += Neal + smallC <= Paris + bigM * z269_1
prob += Neal >= smallC + Daragh - (1 - z269_1) * bigM
prob += Neal >= smallC + Paris - (1 - z269_1) * bigM
z270_1 = LpVariable("z270_1", cat="Binary")
prob += Ayesha + smallC <= Gene + bigM * z270_1
prob += Ayesha + smallC <= Mckenna + bigM * z270_1
prob += Ayesha >= smallC + Gene - (1 - z270_1) * bigM
prob += Ayesha >= smallC + Mckenna - (1 - z270_1) * bigM
z271_1 = LpVariable("z271_1", cat="Binary")
prob += Mckenna + smallC <= Amari + bigM * z271_1
prob += Mckenna + smallC <= Gene + bigM * z271_1
prob += Mckenna >= smallC + Amari - (1 - z271_1) * bigM
prob += Mckenna >= smallC + Gene - (1 - z271_1) * bigM
z272_1 = LpVariable("z272_1", cat="Binary")
prob += Conner + smallC <= Ruben + bigM * z272_1
prob += Conner + smallC <= Chase + bigM * z272_1
prob += Conner >= smallC + Ruben - (1 - z272_1) * bigM
prob += Conner >= smallC + Chase - (1 - z272_1) * bigM
z273_1 = LpVariable("z273_1", cat="Binary")
prob += Conner + smallC <= Skylar + bigM * z273_1
prob += Conner + smallC <= Paris + bigM * z273_1
prob += Conner >= smallC + Skylar - (1 - z273_1) * bigM
prob += Conner >= smallC + Paris - (1 - z273_1) * bigM
z274_1 = LpVariable("z274_1", cat="Binary")
prob += Paris + smallC <= Curt + bigM * z274_1
prob += Paris + smallC <= Carla + bigM * z274_1
prob += Paris >= smallC + Curt - (1 - z274_1) * bigM
prob += Paris >= smallC + Carla - (1 - z274_1) * bigM
z275_1 = LpVariable("z275_1", cat="Binary")
prob += Ayesha + smallC <= Amari + bigM * z275_1
prob += Ayesha + smallC <= Janette + bigM * z275_1
prob += Ayesha >= smallC + Amari - (1 - z275_1) * bigM
prob += Ayesha >= smallC + Janette - (1 - z275_1) * bigM
z276_1 = LpVariable("z276_1", cat="Binary")
prob += Curt + smallC <= Conner + bigM * z276_1
prob += Curt + smallC <= Amari + bigM * z276_1
prob += Curt >= smallC + Conner - (1 - z276_1) * bigM
prob += Curt >= smallC + Amari - (1 - z276_1) * bigM
z277_1 = LpVariable("z277_1", cat="Binary")
prob += Pam + smallC <= Ayesha + bigM * z277_1
prob += Pam + smallC <= Dominick + bigM * z277_1
prob += Pam >= smallC + Ayesha - (1 - z277_1) * bigM
prob += Pam >= smallC + Dominick - (1 - z277_1) * bigM
z278_1 = LpVariable("z278_1", cat="Binary")
prob += Curt + smallC <= Gene + bigM * z278_1
prob += Curt + smallC <= Ayesha + bigM * z278_1
prob += Curt >= smallC + Gene - (1 - z278_1) * bigM
prob += Curt >= smallC + Ayesha - (1 - z278_1) * bigM
z279_1 = LpVariable("z279_1", cat="Binary")
prob += Conner + smallC <= Curt + bigM * z279_1
prob += Conner + smallC <= Wesley + bigM * z279_1
prob += Conner >= smallC + Curt - (1 - z279_1) * bigM
prob += Conner >= smallC + Wesley - (1 - z279_1) * bigM
z280_1 = LpVariable("z280_1", cat="Binary")
prob += Joni + smallC <= Amari + bigM * z280_1
prob += Joni + smallC <= Neal + bigM * z280_1
prob += Joni >= smallC + Amari - (1 - z280_1) * bigM
prob += Joni >= smallC + Neal - (1 - z280_1) * bigM
z281_1 = LpVariable("z281_1", cat="Binary")
prob += Lianne + smallC <= Paris + bigM * z281_1
prob += Lianne + smallC <= Oisin + bigM * z281_1
prob += Lianne >= smallC + Paris - (1 - z281_1) * bigM
prob += Lianne >= smallC + Oisin - (1 - z281_1) * bigM
z282_1 = LpVariable("z282_1", cat="Binary")
prob += Skylar + smallC <= Ruben + bigM * z282_1
prob += Skylar + smallC <= Daragh + bigM * z282_1
prob += Skylar >= smallC + Ruben - (1 - z282_1) * bigM
prob += Skylar >= smallC + Daragh - (1 - z282_1) * bigM
z283_1 = LpVariable("z283_1", cat="Binary")
prob += Amari + smallC <= Conner + bigM * z283_1
prob += Amari + smallC <= Janette + bigM * z283_1
prob += Amari >= smallC + Conner - (1 - z283_1) * bigM
prob += Amari >= smallC + Janette - (1 - z283_1) * bigM
z284_1 = LpVariable("z284_1", cat="Binary")
prob += Pam + smallC <= Conner + bigM * z284_1
prob += Pam + smallC <= Ayesha + bigM * z284_1
prob += Pam >= smallC + Conner - (1 - z284_1) * bigM
prob += Pam >= smallC + Ayesha - (1 - z284_1) * bigM
z285_1 = LpVariable("z285_1", cat="Binary")
prob += Ruben + smallC <= Daragh + bigM * z285_1
prob += Ruben + smallC <= Paris + bigM * z285_1
prob += Ruben >= smallC + Daragh - (1 - z285_1) * bigM
prob += Ruben >= smallC + Paris - (1 - z285_1) * bigM
z286_1 = LpVariable("z286_1", cat="Binary")
prob += Lianne + smallC <= Pam + bigM * z286_1
prob += Lianne + smallC <= Ayesha + bigM * z286_1
prob += Lianne >= smallC + Pam - (1 - z286_1) * bigM
prob += Lianne >= smallC + Ayesha - (1 - z286_1) * bigM
z287_1 = LpVariable("z287_1", cat="Binary")
prob += Skylar + smallC <= Carla + bigM * z287_1
prob += Skylar + smallC <= Conner + bigM * z287_1
prob += Skylar >= smallC + Carla - (1 - z287_1) * bigM
prob += Skylar >= smallC + Conner - (1 - z287_1) * bigM
z288_1 = LpVariable("z288_1", cat="Binary")
prob += Joni + smallC <= Curt + bigM * z288_1
prob += Joni + smallC <= Amari + bigM * z288_1
prob += Joni >= smallC + Curt - (1 - z288_1) * bigM
prob += Joni >= smallC + Amari - (1 - z288_1) * bigM
z289_1 = LpVariable("z289_1", cat="Binary")
prob += Ayesha + smallC <= Paris + bigM * z289_1
prob += Ayesha + smallC <= Joni + bigM * z289_1
prob += Ayesha >= smallC + Paris - (1 - z289_1) * bigM
prob += Ayesha >= smallC + Joni - (1 - z289_1) * bigM
z290_1 = LpVariable("z290_1", cat="Binary")
prob += Paris + smallC <= Daragh + bigM * z290_1
prob += Paris + smallC <= Oisin + bigM * z290_1
prob += Paris >= smallC + Daragh - (1 - z290_1) * bigM
prob += Paris >= smallC + Oisin - (1 - z290_1) * bigM
z291_1 = LpVariable("z291_1", cat="Binary")
prob += Ayesha + smallC <= Mckenna + bigM * z291_1
prob += Ayesha + smallC <= Joni + bigM * z291_1
prob += Ayesha >= smallC + Mckenna - (1 - z291_1) * bigM
prob += Ayesha >= smallC + Joni - (1 - z291_1) * bigM
z292_1 = LpVariable("z292_1", cat="Binary")
prob += Ayesha + smallC <= Amari + bigM * z292_1
prob += Ayesha + smallC <= Carla + bigM * z292_1
prob += Ayesha >= smallC + Amari - (1 - z292_1) * bigM
prob += Ayesha >= smallC + Carla - (1 - z292_1) * bigM
z293_1 = LpVariable("z293_1", cat="Binary")
prob += Skylar + smallC <= Oisin + bigM * z293_1
prob += Skylar + smallC <= Daragh + bigM * z293_1
prob += Skylar >= smallC + Oisin - (1 - z293_1) * bigM
prob += Skylar >= smallC + Daragh - (1 - z293_1) * bigM
z294_1 = LpVariable("z294_1", cat="Binary")
prob += Joni + smallC <= Pam + bigM * z294_1
prob += Joni + smallC <= Mckenna + bigM * z294_1
prob += Joni >= smallC + Pam - (1 - z294_1) * bigM
prob += Joni >= smallC + Mckenna - (1 - z294_1) * bigM
z295_1 = LpVariable("z295_1", cat="Binary")
prob += Wesley + smallC <= Daragh + bigM * z295_1
prob += Wesley + smallC <= Lianne + bigM * z295_1
prob += Wesley >= smallC + Daragh - (1 - z295_1) * bigM
prob += Wesley >= smallC + Lianne - (1 - z295_1) * bigM
z296_1 = LpVariable("z296_1", cat="Binary")
prob += Curt + smallC <= Janette + bigM * z296_1
prob += Curt + smallC <= Conner + bigM * z296_1
prob += Curt >= smallC + Janette - (1 - z296_1) * bigM
prob += Curt >= smallC + Conner - (1 - z296_1) * bigM
z297_1 = LpVariable("z297_1", cat="Binary")
prob += Ayesha + smallC <= Neal + bigM * z297_1
prob += Ayesha + smallC <= Carla + bigM * z297_1
prob += Ayesha >= smallC + Neal - (1 - z297_1) * bigM
prob += Ayesha >= smallC + Carla - (1 - z297_1) * bigM
z298_1 = LpVariable("z298_1", cat="Binary")
prob += Curt + smallC <= Conner + bigM * z298_1
prob += Curt + smallC <= Amari + bigM * z298_1
prob += Curt >= smallC + Conner - (1 - z298_1) * bigM
prob += Curt >= smallC + Amari - (1 - z298_1) * bigM
z299_1 = LpVariable("z299_1", cat="Binary")
prob += Lianne + smallC <= Janette + bigM * z299_1
prob += Lianne + smallC <= Joni + bigM * z299_1
prob += Lianne >= smallC + Janette - (1 - z299_1) * bigM
prob += Lianne >= smallC + Joni - (1 - z299_1) * bigM
z300_1 = LpVariable("z300_1", cat="Binary")
prob += Oisin + smallC <= Chase + bigM * z300_1
prob += Oisin + smallC <= Wesley + bigM * z300_1
prob += Oisin >= smallC + Chase - (1 - z300_1) * bigM
prob += Oisin >= smallC + Wesley - (1 - z300_1) * bigM
z301_1 = LpVariable("z301_1", cat="Binary")
prob += Daragh + smallC <= Mckenna + bigM * z301_1
prob += Daragh + smallC <= Chase + bigM * z301_1
prob += Daragh >= smallC + Mckenna - (1 - z301_1) * bigM
prob += Daragh >= smallC + Chase - (1 - z301_1) * bigM
z302_1 = LpVariable("z302_1", cat="Binary")
prob += Oisin + smallC <= Conner + bigM * z302_1
prob += Oisin + smallC <= Ruben + bigM * z302_1
prob += Oisin >= smallC + Conner - (1 - z302_1) * bigM
prob += Oisin >= smallC + Ruben - (1 - z302_1) * bigM
z303_1 = LpVariable("z303_1", cat="Binary")
prob += Curt + smallC <= Conner + bigM * z303_1
prob += Curt + smallC <= Neal + bigM * z303_1
prob += Curt >= smallC + Conner - (1 - z303_1) * bigM
prob += Curt >= smallC + Neal - (1 - z303_1) * bigM
z304_1 = LpVariable("z304_1", cat="Binary")
prob += Ruben + smallC <= Oisin + bigM * z304_1
prob += Ruben + smallC <= Paris + bigM * z304_1
prob += Ruben >= smallC + Oisin - (1 - z304_1) * bigM
prob += Ruben >= smallC + Paris - (1 - z304_1) * bigM
z305_1 = LpVariable("z305_1", cat="Binary")
prob += Curt + smallC <= Conner + bigM * z305_1
prob += Curt + smallC <= Janette + bigM * z305_1
prob += Curt >= smallC + Conner - (1 - z305_1) * bigM
prob += Curt >= smallC + Janette - (1 - z305_1) * bigM
z306_1 = LpVariable("z306_1", cat="Binary")
prob += Amari + smallC <= Skylar + bigM * z306_1
prob += Amari + smallC <= Carla + bigM * z306_1
prob += Amari >= smallC + Skylar - (1 - z306_1) * bigM
prob += Amari >= smallC + Carla - (1 - z306_1) * bigM
z307_1 = LpVariable("z307_1", cat="Binary")
prob += Paris + smallC <= Daragh + bigM * z307_1
prob += Paris + smallC <= Oisin + bigM * z307_1
prob += Paris >= smallC + Daragh - (1 - z307_1) * bigM
prob += Paris >= smallC + Oisin - (1 - z307_1) * bigM
z308_1 = LpVariable("z308_1", cat="Binary")
prob += Daragh + smallC <= Janette + bigM * z308_1
prob += Daragh + smallC <= Ruben + bigM * z308_1
prob += Daragh >= smallC + Janette - (1 - z308_1) * bigM
prob += Daragh >= smallC + Ruben - (1 - z308_1) * bigM
z309_1 = LpVariable("z309_1", cat="Binary")
prob += Pam + smallC <= Paris + bigM * z309_1
prob += Pam + smallC <= Oisin + bigM * z309_1
prob += Pam >= smallC + Paris - (1 - z309_1) * bigM
prob += Pam >= smallC + Oisin - (1 - z309_1) * bigM
z310_1 = LpVariable("z310_1", cat="Binary")
prob += Daragh + smallC <= Dominick + bigM * z310_1
prob += Daragh + smallC <= Ayesha + bigM * z310_1
prob += Daragh >= smallC + Dominick - (1 - z310_1) * bigM
prob += Daragh >= smallC + Ayesha - (1 - z310_1) * bigM
z311_1 = LpVariable("z311_1", cat="Binary")
prob += Wesley + smallC <= Mckenna + bigM * z311_1
prob += Wesley + smallC <= Oisin + bigM * z311_1
prob += Wesley >= smallC + Mckenna - (1 - z311_1) * bigM
prob += Wesley >= smallC + Oisin - (1 - z311_1) * bigM
z312_1 = LpVariable("z312_1", cat="Binary")
prob += Wesley + smallC <= Amari + bigM * z312_1
prob += Wesley + smallC <= Chase + bigM * z312_1
prob += Wesley >= smallC + Amari - (1 - z312_1) * bigM
prob += Wesley >= smallC + Chase - (1 - z312_1) * bigM
z313_1 = LpVariable("z313_1", cat="Binary")
prob += Wesley + smallC <= Daragh + bigM * z313_1
prob += Wesley + smallC <= Oisin + bigM * z313_1
prob += Wesley >= smallC + Daragh - (1 - z313_1) * bigM
prob += Wesley >= smallC + Oisin - (1 - z313_1) * bigM
z314_1 = LpVariable("z314_1", cat="Binary")
prob += Lianne + smallC <= Neal + bigM * z314_1
prob += Lianne + smallC <= Amari + bigM * z314_1
prob += Lianne >= smallC + Neal - (1 - z314_1) * bigM
prob += Lianne >= smallC + Amari - (1 - z314_1) * bigM
z315_1 = LpVariable("z315_1", cat="Binary")
prob += Pam + smallC <= Ayesha + bigM * z315_1
prob += Pam + smallC <= Conner + bigM * z315_1
prob += Pam >= smallC + Ayesha - (1 - z315_1) * bigM
prob += Pam >= smallC + Conner - (1 - z315_1) * bigM
z316_1 = LpVariable("z316_1", cat="Binary")
prob += Paris + smallC <= Daragh + bigM * z316_1
prob += Paris + smallC <= Oisin + bigM * z316_1
prob += Paris >= smallC + Daragh - (1 - z316_1) * bigM
prob += Paris >= smallC + Oisin - (1 - z316_1) * bigM
z317_1 = LpVariable("z317_1", cat="Binary")
prob += Conner + smallC <= Janette + bigM * z317_1
prob += Conner + smallC <= Carla + bigM * z317_1
prob += Conner >= smallC + Janette - (1 - z317_1) * bigM
prob += Conner >= smallC + Carla - (1 - z317_1) * bigM
z318_1 = LpVariable("z318_1", cat="Binary")
prob += Skylar + smallC <= Daragh + bigM * z318_1
prob += Skylar + smallC <= Ruben + bigM * z318_1
prob += Skylar >= smallC + Daragh - (1 - z318_1) * bigM
prob += Skylar >= smallC + Ruben - (1 - z318_1) * bigM
z319_1 = LpVariable("z319_1", cat="Binary")
prob += Neal + smallC <= Pam + bigM * z319_1
prob += Neal + smallC <= Ruben + bigM * z319_1
prob += Neal >= smallC + Pam - (1 - z319_1) * bigM
prob += Neal >= smallC + Ruben - (1 - z319_1) * bigM
z320_1 = LpVariable("z320_1", cat="Binary")
prob += Curt + smallC <= Dominick + bigM * z320_1
prob += Curt + smallC <= Joni + bigM * z320_1
prob += Curt >= smallC + Dominick - (1 - z320_1) * bigM
prob += Curt >= smallC + Joni - (1 - z320_1) * bigM
z321_1 = LpVariable("z321_1", cat="Binary")
prob += Ayesha + smallC <= Amari + bigM * z321_1
prob += Ayesha + smallC <= Conner + bigM * z321_1
prob += Ayesha >= smallC + Amari - (1 - z321_1) * bigM
prob += Ayesha >= smallC + Conner - (1 - z321_1) * bigM
z322_1 = LpVariable("z322_1", cat="Binary")
prob += Neal + smallC <= Gene + bigM * z322_1
prob += Neal + smallC <= Lianne + bigM * z322_1
prob += Neal >= smallC + Gene - (1 - z322_1) * bigM
prob += Neal >= smallC + Lianne - (1 - z322_1) * bigM
z323_1 = LpVariable("z323_1", cat="Binary")
prob += Mckenna + smallC <= Wesley + bigM * z323_1
prob += Mckenna + smallC <= Neal + bigM * z323_1
prob += Mckenna >= smallC + Wesley - (1 - z323_1) * bigM
prob += Mckenna >= smallC + Neal - (1 - z323_1) * bigM
z324_1 = LpVariable("z324_1", cat="Binary")
prob += Skylar + smallC <= Daragh + bigM * z324_1
prob += Skylar + smallC <= Oisin + bigM * z324_1
prob += Skylar >= smallC + Daragh - (1 - z324_1) * bigM
prob += Skylar >= smallC + Oisin - (1 - z324_1) * bigM
z325_1 = LpVariable("z325_1", cat="Binary")
prob += Conner + smallC <= Chase + bigM * z325_1
prob += Conner + smallC <= Ruben + bigM * z325_1
prob += Conner >= smallC + Chase - (1 - z325_1) * bigM
prob += Conner >= smallC + Ruben - (1 - z325_1) * bigM
z326_1 = LpVariable("z326_1", cat="Binary")
prob += Lianne + smallC <= Oisin + bigM * z326_1
prob += Lianne + smallC <= Paris + bigM * z326_1
prob += Lianne >= smallC + Oisin - (1 - z326_1) * bigM
prob += Lianne >= smallC + Paris - (1 - z326_1) * bigM
z327_1 = LpVariable("z327_1", cat="Binary")
prob += Daragh + smallC <= Joni + bigM * z327_1
prob += Daragh + smallC <= Dominick + bigM * z327_1
prob += Daragh >= smallC + Joni - (1 - z327_1) * bigM
prob += Daragh >= smallC + Dominick - (1 - z327_1) * bigM
z328_1 = LpVariable("z328_1", cat="Binary")
prob += Ayesha + smallC <= Ruben + bigM * z328_1
prob += Ayesha + smallC <= Gene + bigM * z328_1
prob += Ayesha >= smallC + Ruben - (1 - z328_1) * bigM
prob += Ayesha >= smallC + Gene - (1 - z328_1) * bigM
z329_1 = LpVariable("z329_1", cat="Binary")
prob += Wesley + smallC <= Gene + bigM * z329_1
prob += Wesley + smallC <= Chase + bigM * z329_1
prob += Wesley >= smallC + Gene - (1 - z329_1) * bigM
prob += Wesley >= smallC + Chase - (1 - z329_1) * bigM
z330_1 = LpVariable("z330_1", cat="Binary")
prob += Curt + smallC <= Joni + bigM * z330_1
prob += Curt + smallC <= Wesley + bigM * z330_1
prob += Curt >= smallC + Joni - (1 - z330_1) * bigM
prob += Curt >= smallC + Wesley - (1 - z330_1) * bigM
z331_1 = LpVariable("z331_1", cat="Binary")
prob += Skylar + smallC <= Oisin + bigM * z331_1
prob += Skylar + smallC <= Daragh + bigM * z331_1
prob += Skylar >= smallC + Oisin - (1 - z331_1) * bigM
prob += Skylar >= smallC + Daragh - (1 - z331_1) * bigM
z332_1 = LpVariable("z332_1", cat="Binary")
prob += Conner + smallC <= Mckenna + bigM * z332_1
prob += Conner + smallC <= Dominick + bigM * z332_1
prob += Conner >= smallC + Mckenna - (1 - z332_1) * bigM
prob += Conner >= smallC + Dominick - (1 - z332_1) * bigM
z333_1 = LpVariable("z333_1", cat="Binary")
prob += Wesley + smallC <= Pam + bigM * z333_1
prob += Wesley + smallC <= Neal + bigM * z333_1
prob += Wesley >= smallC + Pam - (1 - z333_1) * bigM
prob += Wesley >= smallC + Neal - (1 - z333_1) * bigM
z334_1 = LpVariable("z334_1", cat="Binary")
prob += Mckenna + smallC <= Chase + bigM * z334_1
prob += Mckenna + smallC <= Pam + bigM * z334_1
prob += Mckenna >= smallC + Chase - (1 - z334_1) * bigM
prob += Mckenna >= smallC + Pam - (1 - z334_1) * bigM
z335_1 = LpVariable("z335_1", cat="Binary")
prob += Lianne + smallC <= Mckenna + bigM * z335_1
prob += Lianne + smallC <= Conner + bigM * z335_1
prob += Lianne >= smallC + Mckenna - (1 - z335_1) * bigM
prob += Lianne >= smallC + Conner - (1 - z335_1) * bigM
z336_1 = LpVariable("z336_1", cat="Binary")
prob += Skylar + smallC <= Chase + bigM * z336_1
prob += Skylar + smallC <= Pam + bigM * z336_1
prob += Skylar >= smallC + Chase - (1 - z336_1) * bigM
prob += Skylar >= smallC + Pam - (1 - z336_1) * bigM
z337_1 = LpVariable("z337_1", cat="Binary")
prob += Pam + smallC <= Oisin + bigM * z337_1
prob += Pam + smallC <= Daragh + bigM * z337_1
prob += Pam >= smallC + Oisin - (1 - z337_1) * bigM
prob += Pam >= smallC + Daragh - (1 - z337_1) * bigM
z338_1 = LpVariable("z338_1", cat="Binary")
prob += Ruben + smallC <= Curt + bigM * z338_1
prob += Ruben + smallC <= Chase + bigM * z338_1
prob += Ruben >= smallC + Curt - (1 - z338_1) * bigM
prob += Ruben >= smallC + Chase - (1 - z338_1) * bigM
z339_1 = LpVariable("z339_1", cat="Binary")
prob += Skylar + smallC <= Pam + bigM * z339_1
prob += Skylar + smallC <= Amari + bigM * z339_1
prob += Skylar >= smallC + Pam - (1 - z339_1) * bigM
prob += Skylar >= smallC + Amari - (1 - z339_1) * bigM
z340_1 = LpVariable("z340_1", cat="Binary")
prob += Amari + smallC <= Chase + bigM * z340_1
prob += Amari + smallC <= Skylar + bigM * z340_1
prob += Amari >= smallC + Chase - (1 - z340_1) * bigM
prob += Amari >= smallC + Skylar - (1 - z340_1) * bigM
z341_1 = LpVariable("z341_1", cat="Binary")
prob += Oisin + smallC <= Curt + bigM * z341_1
prob += Oisin + smallC <= Conner + bigM * z341_1
prob += Oisin >= smallC + Curt - (1 - z341_1) * bigM
prob += Oisin >= smallC + Conner - (1 - z341_1) * bigM
z342_1 = LpVariable("z342_1", cat="Binary")
prob += Mckenna + smallC <= Amari + bigM * z342_1
prob += Mckenna + smallC <= Janette + bigM * z342_1
prob += Mckenna >= smallC + Amari - (1 - z342_1) * bigM
prob += Mckenna >= smallC + Janette - (1 - z342_1) * bigM
z343_1 = LpVariable("z343_1", cat="Binary")
prob += Daragh + smallC <= Pam + bigM * z343_1
prob += Daragh + smallC <= Conner + bigM * z343_1
prob += Daragh >= smallC + Pam - (1 - z343_1) * bigM
prob += Daragh >= smallC + Conner - (1 - z343_1) * bigM
z344_1 = LpVariable("z344_1", cat="Binary")
prob += Daragh + smallC <= Wesley + bigM * z344_1
prob += Daragh + smallC <= Ayesha + bigM * z344_1
prob += Daragh >= smallC + Wesley - (1 - z344_1) * bigM
prob += Daragh >= smallC + Ayesha - (1 - z344_1) * bigM
z345_1 = LpVariable("z345_1", cat="Binary")
prob += Mckenna + smallC <= Chase + bigM * z345_1
prob += Mckenna + smallC <= Dominick + bigM * z345_1
prob += Mckenna >= smallC + Chase - (1 - z345_1) * bigM
prob += Mckenna >= smallC + Dominick - (1 - z345_1) * bigM
z346_1 = LpVariable("z346_1", cat="Binary")
prob += Mckenna + smallC <= Amari + bigM * z346_1
prob += Mckenna + smallC <= Conner + bigM * z346_1
prob += Mckenna >= smallC + Amari - (1 - z346_1) * bigM
prob += Mckenna >= smallC + Conner - (1 - z346_1) * bigM
z347_1 = LpVariable("z347_1", cat="Binary")
prob += Janette + smallC <= Amari + bigM * z347_1
prob += Janette + smallC <= Ayesha + bigM * z347_1
prob += Janette >= smallC + Amari - (1 - z347_1) * bigM
prob += Janette >= smallC + Ayesha - (1 - z347_1) * bigM
z348_1 = LpVariable("z348_1", cat="Binary")
prob += Lianne + smallC <= Amari + bigM * z348_1
prob += Lianne + smallC <= Mckenna + bigM * z348_1
prob += Lianne >= smallC + Amari - (1 - z348_1) * bigM
prob += Lianne >= smallC + Mckenna - (1 - z348_1) * bigM
z349_1 = LpVariable("z349_1", cat="Binary")
prob += Amari + smallC <= Conner + bigM * z349_1
prob += Amari + smallC <= Janette + bigM * z349_1
prob += Amari >= smallC + Conner - (1 - z349_1) * bigM
prob += Amari >= smallC + Janette - (1 - z349_1) * bigM
z350_1 = LpVariable("z350_1", cat="Binary")
prob += Conner + smallC <= Gene + bigM * z350_1
prob += Conner + smallC <= Daragh + bigM * z350_1
prob += Conner >= smallC + Gene - (1 - z350_1) * bigM
prob += Conner >= smallC + Daragh - (1 - z350_1) * bigM
z351_1 = LpVariable("z351_1", cat="Binary")
prob += Paris + smallC <= Daragh + bigM * z351_1
prob += Paris + smallC <= Oisin + bigM * z351_1
prob += Paris >= smallC + Daragh - (1 - z351_1) * bigM
prob += Paris >= smallC + Oisin - (1 - z351_1) * bigM
z352_1 = LpVariable("z352_1", cat="Binary")
prob += Pam + smallC <= Chase + bigM * z352_1
prob += Pam + smallC <= Neal + bigM * z352_1
prob += Pam >= smallC + Chase - (1 - z352_1) * bigM
prob += Pam >= smallC + Neal - (1 - z352_1) * bigM
z353_1 = LpVariable("z353_1", cat="Binary")
prob += Ruben + smallC <= Paris + bigM * z353_1
prob += Ruben + smallC <= Daragh + bigM * z353_1
prob += Ruben >= smallC + Paris - (1 - z353_1) * bigM
prob += Ruben >= smallC + Daragh - (1 - z353_1) * bigM
z354_1 = LpVariable("z354_1", cat="Binary")
prob += Daragh + smallC <= Paris + bigM * z354_1
prob += Daragh + smallC <= Conner + bigM * z354_1
prob += Daragh >= smallC + Paris - (1 - z354_1) * bigM
prob += Daragh >= smallC + Conner - (1 - z354_1) * bigM
z355_1 = LpVariable("z355_1", cat="Binary")
prob += Joni + smallC <= Janette + bigM * z355_1
prob += Joni + smallC <= Curt + bigM * z355_1
prob += Joni >= smallC + Janette - (1 - z355_1) * bigM
prob += Joni >= smallC + Curt - (1 - z355_1) * bigM
z356_1 = LpVariable("z356_1", cat="Binary")
prob += Mckenna + smallC <= Ruben + bigM * z356_1
prob += Mckenna + smallC <= Daragh + bigM * z356_1
prob += Mckenna >= smallC + Ruben - (1 - z356_1) * bigM
prob += Mckenna >= smallC + Daragh - (1 - z356_1) * bigM
z357_1 = LpVariable("z357_1", cat="Binary")
prob += Skylar + smallC <= Wesley + bigM * z357_1
prob += Skylar + smallC <= Mckenna + bigM * z357_1
prob += Skylar >= smallC + Wesley - (1 - z357_1) * bigM
prob += Skylar >= smallC + Mckenna - (1 - z357_1) * bigM
z358_1 = LpVariable("z358_1", cat="Binary")
prob += Joni + smallC <= Paris + bigM * z358_1
prob += Joni + smallC <= Ruben + bigM * z358_1
prob += Joni >= smallC + Paris - (1 - z358_1) * bigM
prob += Joni >= smallC + Ruben - (1 - z358_1) * bigM
z359_1 = LpVariable("z359_1", cat="Binary")
prob += Oisin + smallC <= Paris + bigM * z359_1
prob += Oisin + smallC <= Dominick + bigM * z359_1
prob += Oisin >= smallC + Paris - (1 - z359_1) * bigM
prob += Oisin >= smallC + Dominick - (1 - z359_1) * bigM
z360_1 = LpVariable("z360_1", cat="Binary")
prob += Oisin + smallC <= Neal + bigM * z360_1
prob += Oisin + smallC <= Wesley + bigM * z360_1
prob += Oisin >= smallC + Neal - (1 - z360_1) * bigM
prob += Oisin >= smallC + Wesley - (1 - z360_1) * bigM
z361_1 = LpVariable("z361_1", cat="Binary")
prob += Ruben + smallC <= Ayesha + bigM * z361_1
prob += Ruben + smallC <= Janette + bigM * z361_1
prob += Ruben >= smallC + Ayesha - (1 - z361_1) * bigM
prob += Ruben >= smallC + Janette - (1 - z361_1) * bigM
z362_1 = LpVariable("z362_1", cat="Binary")
prob += Oisin + smallC <= Paris + bigM * z362_1
prob += Oisin + smallC <= Lianne + bigM * z362_1
prob += Oisin >= smallC + Paris - (1 - z362_1) * bigM
prob += Oisin >= smallC + Lianne - (1 - z362_1) * bigM
z363_1 = LpVariable("z363_1", cat="Binary")
prob += Ruben + smallC <= Mckenna + bigM * z363_1
prob += Ruben + smallC <= Janette + bigM * z363_1
prob += Ruben >= smallC + Mckenna - (1 - z363_1) * bigM
prob += Ruben >= smallC + Janette - (1 - z363_1) * bigM
z364_1 = LpVariable("z364_1", cat="Binary")
prob += Oisin + smallC <= Wesley + bigM * z364_1
prob += Oisin + smallC <= Skylar + bigM * z364_1
prob += Oisin >= smallC + Wesley - (1 - z364_1) * bigM
prob += Oisin >= smallC + Skylar - (1 - z364_1) * bigM
z365_1 = LpVariable("z365_1", cat="Binary")
prob += Curt + smallC <= Ayesha + bigM * z365_1
prob += Curt + smallC <= Paris + bigM * z365_1
prob += Curt >= smallC + Ayesha - (1 - z365_1) * bigM
prob += Curt >= smallC + Paris - (1 - z365_1) * bigM
z366_1 = LpVariable("z366_1", cat="Binary")
prob += Neal + smallC <= Daragh + bigM * z366_1
prob += Neal + smallC <= Carla + bigM * z366_1
prob += Neal >= smallC + Daragh - (1 - z366_1) * bigM
prob += Neal >= smallC + Carla - (1 - z366_1) * bigM
z367_1 = LpVariable("z367_1", cat="Binary")
prob += Wesley + smallC <= Neal + bigM * z367_1
prob += Wesley + smallC <= Curt + bigM * z367_1
prob += Wesley >= smallC + Neal - (1 - z367_1) * bigM
prob += Wesley >= smallC + Curt - (1 - z367_1) * bigM
z368_1 = LpVariable("z368_1", cat="Binary")
prob += Ayesha + smallC <= Carla + bigM * z368_1
prob += Ayesha + smallC <= Chase + bigM * z368_1
prob += Ayesha >= smallC + Carla - (1 - z368_1) * bigM
prob += Ayesha >= smallC + Chase - (1 - z368_1) * bigM
z369_1 = LpVariable("z369_1", cat="Binary")
prob += Oisin + smallC <= Dominick + bigM * z369_1
prob += Oisin + smallC <= Chase + bigM * z369_1
prob += Oisin >= smallC + Dominick - (1 - z369_1) * bigM
prob += Oisin >= smallC + Chase - (1 - z369_1) * bigM
z370_1 = LpVariable("z370_1", cat="Binary")
prob += Joni + smallC <= Chase + bigM * z370_1
prob += Joni + smallC <= Gene + bigM * z370_1
prob += Joni >= smallC + Chase - (1 - z370_1) * bigM
prob += Joni >= smallC + Gene - (1 - z370_1) * bigM
z371_1 = LpVariable("z371_1", cat="Binary")
prob += Pam + smallC <= Ruben + bigM * z371_1
prob += Pam + smallC <= Oisin + bigM * z371_1
prob += Pam >= smallC + Ruben - (1 - z371_1) * bigM
prob += Pam >= smallC + Oisin - (1 - z371_1) * bigM
z372_1 = LpVariable("z372_1", cat="Binary")
prob += Daragh + smallC <= Ayesha + bigM * z372_1
prob += Daragh + smallC <= Pam + bigM * z372_1
prob += Daragh >= smallC + Ayesha - (1 - z372_1) * bigM
prob += Daragh >= smallC + Pam - (1 - z372_1) * bigM
z373_1 = LpVariable("z373_1", cat="Binary")
prob += Ruben + smallC <= Daragh + bigM * z373_1
prob += Ruben + smallC <= Paris + bigM * z373_1
prob += Ruben >= smallC + Daragh - (1 - z373_1) * bigM
prob += Ruben >= smallC + Paris - (1 - z373_1) * bigM
z374_1 = LpVariable("z374_1", cat="Binary")
prob += Joni + smallC <= Dominick + bigM * z374_1
prob += Joni + smallC <= Amari + bigM * z374_1
prob += Joni >= smallC + Dominick - (1 - z374_1) * bigM
prob += Joni >= smallC + Amari - (1 - z374_1) * bigM
z375_1 = LpVariable("z375_1", cat="Binary")
prob += Paris + smallC <= Oisin + bigM * z375_1
prob += Paris + smallC <= Daragh + bigM * z375_1
prob += Paris >= smallC + Oisin - (1 - z375_1) * bigM
prob += Paris >= smallC + Daragh - (1 - z375_1) * bigM
z376_1 = LpVariable("z376_1", cat="Binary")
prob += Conner + smallC <= Dominick + bigM * z376_1
prob += Conner + smallC <= Paris + bigM * z376_1
prob += Conner >= smallC + Dominick - (1 - z376_1) * bigM
prob += Conner >= smallC + Paris - (1 - z376_1) * bigM
z377_1 = LpVariable("z377_1", cat="Binary")
prob += Lianne + smallC <= Gene + bigM * z377_1
prob += Lianne + smallC <= Conner + bigM * z377_1
prob += Lianne >= smallC + Gene - (1 - z377_1) * bigM
prob += Lianne >= smallC + Conner - (1 - z377_1) * bigM
z378_1 = LpVariable("z378_1", cat="Binary")
prob += Daragh + smallC <= Carla + bigM * z378_1
prob += Daragh + smallC <= Skylar + bigM * z378_1
prob += Daragh >= smallC + Carla - (1 - z378_1) * bigM
prob += Daragh >= smallC + Skylar - (1 - z378_1) * bigM
z379_1 = LpVariable("z379_1", cat="Binary")
prob += Lianne + smallC <= Pam + bigM * z379_1
prob += Lianne + smallC <= Janette + bigM * z379_1
prob += Lianne >= smallC + Pam - (1 - z379_1) * bigM
prob += Lianne >= smallC + Janette - (1 - z379_1) * bigM
z380_1 = LpVariable("z380_1", cat="Binary")
prob += Lianne + smallC <= Joni + bigM * z380_1
prob += Lianne + smallC <= Gene + bigM * z380_1
prob += Lianne >= smallC + Joni - (1 - z380_1) * bigM
prob += Lianne >= smallC + Gene - (1 - z380_1) * bigM
z381_1 = LpVariable("z381_1", cat="Binary")
prob += Conner + smallC <= Lianne + bigM * z381_1
prob += Conner + smallC <= Ruben + bigM * z381_1
prob += Conner >= smallC + Lianne - (1 - z381_1) * bigM
prob += Conner >= smallC + Ruben - (1 - z381_1) * bigM
z382_1 = LpVariable("z382_1", cat="Binary")
prob += Mckenna + smallC <= Lianne + bigM * z382_1
prob += Mckenna + smallC <= Skylar + bigM * z382_1
prob += Mckenna >= smallC + Lianne - (1 - z382_1) * bigM
prob += Mckenna >= smallC + Skylar - (1 - z382_1) * bigM
z383_1 = LpVariable("z383_1", cat="Binary")
prob += Oisin + smallC <= Conner + bigM * z383_1
prob += Oisin + smallC <= Ruben + bigM * z383_1
prob += Oisin >= smallC + Conner - (1 - z383_1) * bigM
prob += Oisin >= smallC + Ruben - (1 - z383_1) * bigM
z384_1 = LpVariable("z384_1", cat="Binary")
prob += Paris + smallC <= Oisin + bigM * z384_1
prob += Paris + smallC <= Daragh + bigM * z384_1
prob += Paris >= smallC + Oisin - (1 - z384_1) * bigM
prob += Paris >= smallC + Daragh - (1 - z384_1) * bigM
z385_1 = LpVariable("z385_1", cat="Binary")
prob += Wesley + smallC <= Mckenna + bigM * z385_1
prob += Wesley + smallC <= Skylar + bigM * z385_1
prob += Wesley >= smallC + Mckenna - (1 - z385_1) * bigM
prob += Wesley >= smallC + Skylar - (1 - z385_1) * bigM
z386_1 = LpVariable("z386_1", cat="Binary")
prob += Pam + smallC <= Skylar + bigM * z386_1
prob += Pam + smallC <= Ruben + bigM * z386_1
prob += Pam >= smallC + Skylar - (1 - z386_1) * bigM
prob += Pam >= smallC + Ruben - (1 - z386_1) * bigM
z387_1 = LpVariable("z387_1", cat="Binary")
prob += Wesley + smallC <= Skylar + bigM * z387_1
prob += Wesley + smallC <= Mckenna + bigM * z387_1
prob += Wesley >= smallC + Skylar - (1 - z387_1) * bigM
prob += Wesley >= smallC + Mckenna - (1 - z387_1) * bigM
z388_1 = LpVariable("z388_1", cat="Binary")
prob += Wesley + smallC <= Lianne + bigM * z388_1
prob += Wesley + smallC <= Skylar + bigM * z388_1
prob += Wesley >= smallC + Lianne - (1 - z388_1) * bigM
prob += Wesley >= smallC + Skylar - (1 - z388_1) * bigM
z389_1 = LpVariable("z389_1", cat="Binary")
prob += Janette + smallC <= Ruben + bigM * z389_1
prob += Janette + smallC <= Pam + bigM * z389_1
prob += Janette >= smallC + Ruben - (1 - z389_1) * bigM
prob += Janette >= smallC + Pam - (1 - z389_1) * bigM
z390_1 = LpVariable("z390_1", cat="Binary")
prob += Janette + smallC <= Daragh + bigM * z390_1
prob += Janette + smallC <= Chase + bigM * z390_1
prob += Janette >= smallC + Daragh - (1 - z390_1) * bigM
prob += Janette >= smallC + Chase - (1 - z390_1) * bigM
z391_1 = LpVariable("z391_1", cat="Binary")
prob += Paris + smallC <= Oisin + bigM * z391_1
prob += Paris + smallC <= Daragh + bigM * z391_1
prob += Paris >= smallC + Oisin - (1 - z391_1) * bigM
prob += Paris >= smallC + Daragh - (1 - z391_1) * bigM
z392_1 = LpVariable("z392_1", cat="Binary")
prob += Skylar + smallC <= Ruben + bigM * z392_1
prob += Skylar + smallC <= Daragh + bigM * z392_1
prob += Skylar >= smallC + Ruben - (1 - z392_1) * bigM
prob += Skylar >= smallC + Daragh - (1 - z392_1) * bigM
z393_1 = LpVariable("z393_1", cat="Binary")
prob += Lianne + smallC <= Carla + bigM * z393_1
prob += Lianne + smallC <= Mckenna + bigM * z393_1
prob += Lianne >= smallC + Carla - (1 - z393_1) * bigM
prob += Lianne >= smallC + Mckenna - (1 - z393_1) * bigM
z394_1 = LpVariable("z394_1", cat="Binary")
prob += Pam + smallC <= Wesley + bigM * z394_1
prob += Pam + smallC <= Lianne + bigM * z394_1
prob += Pam >= smallC + Wesley - (1 - z394_1) * bigM
prob += Pam >= smallC + Lianne - (1 - z394_1) * bigM
z395_1 = LpVariable("z395_1", cat="Binary")
prob += Ruben + smallC <= Paris + bigM * z395_1
prob += Ruben + smallC <= Daragh + bigM * z395_1
prob += Ruben >= smallC + Paris - (1 - z395_1) * bigM
prob += Ruben >= smallC + Daragh - (1 - z395_1) * bigM
z396_1 = LpVariable("z396_1", cat="Binary")
prob += Daragh + smallC <= Neal + bigM * z396_1
prob += Daragh + smallC <= Gene + bigM * z396_1
prob += Daragh >= smallC + Neal - (1 - z396_1) * bigM
prob += Daragh >= smallC + Gene - (1 - z396_1) * bigM
z397_1 = LpVariable("z397_1", cat="Binary")
prob += Mckenna + smallC <= Chase + bigM * z397_1
prob += Mckenna + smallC <= Joni + bigM * z397_1
prob += Mckenna >= smallC + Chase - (1 - z397_1) * bigM
prob += Mckenna >= smallC + Joni - (1 - z397_1) * bigM
z398_1 = LpVariable("z398_1", cat="Binary")
prob += Neal + smallC <= Carla + bigM * z398_1
prob += Neal + smallC <= Gene + bigM * z398_1
prob += Neal >= smallC + Carla - (1 - z398_1) * bigM
prob += Neal >= smallC + Gene - (1 - z398_1) * bigM
z399_1 = LpVariable("z399_1", cat="Binary")
prob += Oisin + smallC <= Janette + bigM * z399_1
prob += Oisin + smallC <= Ruben + bigM * z399_1
prob += Oisin >= smallC + Janette - (1 - z399_1) * bigM
prob += Oisin >= smallC + Ruben - (1 - z399_1) * bigM
z400_1 = LpVariable("z400_1", cat="Binary")
prob += Skylar + smallC <= Paris + bigM * z400_1
prob += Skylar + smallC <= Daragh + bigM * z400_1
prob += Skylar >= smallC + Paris - (1 - z400_1) * bigM
prob += Skylar >= smallC + Daragh - (1 - z400_1) * bigM
z401_1 = LpVariable("z401_1", cat="Binary")
prob += Wesley + smallC <= Neal + bigM * z401_1
prob += Wesley + smallC <= Gene + bigM * z401_1
prob += Wesley >= smallC + Neal - (1 - z401_1) * bigM
prob += Wesley >= smallC + Gene - (1 - z401_1) * bigM
z402_1 = LpVariable("z402_1", cat="Binary")
prob += Ayesha + smallC <= Lianne + bigM * z402_1
prob += Ayesha + smallC <= Ruben + bigM * z402_1
prob += Ayesha >= smallC + Lianne - (1 - z402_1) * bigM
prob += Ayesha >= smallC + Ruben - (1 - z402_1) * bigM
z403_1 = LpVariable("z403_1", cat="Binary")
prob += Ayesha + smallC <= Curt + bigM * z403_1
prob += Ayesha + smallC <= Chase + bigM * z403_1
prob += Ayesha >= smallC + Curt - (1 - z403_1) * bigM
prob += Ayesha >= smallC + Chase - (1 - z403_1) * bigM
z404_1 = LpVariable("z404_1", cat="Binary")
prob += Janette + smallC <= Conner + bigM * z404_1
prob += Janette + smallC <= Neal + bigM * z404_1
prob += Janette >= smallC + Conner - (1 - z404_1) * bigM
prob += Janette >= smallC + Neal - (1 - z404_1) * bigM
z405_1 = LpVariable("z405_1", cat="Binary")
prob += Neal + smallC <= Ayesha + bigM * z405_1
prob += Neal + smallC <= Oisin + bigM * z405_1
prob += Neal >= smallC + Ayesha - (1 - z405_1) * bigM
prob += Neal >= smallC + Oisin - (1 - z405_1) * bigM
z406_1 = LpVariable("z406_1", cat="Binary")
prob += Oisin + smallC <= Skylar + bigM * z406_1
prob += Oisin + smallC <= Chase + bigM * z406_1
prob += Oisin >= smallC + Skylar - (1 - z406_1) * bigM
prob += Oisin >= smallC + Chase - (1 - z406_1) * bigM
z407_1 = LpVariable("z407_1", cat="Binary")
prob += Oisin + smallC <= Gene + bigM * z407_1
prob += Oisin + smallC <= Chase + bigM * z407_1
prob += Oisin >= smallC + Gene - (1 - z407_1) * bigM
prob += Oisin >= smallC + Chase - (1 - z407_1) * bigM
z408_1 = LpVariable("z408_1", cat="Binary")
prob += Ruben + smallC <= Daragh + bigM * z408_1
prob += Ruben + smallC <= Oisin + bigM * z408_1
prob += Ruben >= smallC + Daragh - (1 - z408_1) * bigM
prob += Ruben >= smallC + Oisin - (1 - z408_1) * bigM
z409_1 = LpVariable("z409_1", cat="Binary")
prob += Conner + smallC <= Ayesha + bigM * z409_1
prob += Conner + smallC <= Dominick + bigM * z409_1
prob += Conner >= smallC + Ayesha - (1 - z409_1) * bigM
prob += Conner >= smallC + Dominick - (1 - z409_1) * bigM
z410_1 = LpVariable("z410_1", cat="Binary")
prob += Daragh + smallC <= Gene + bigM * z410_1
prob += Daragh + smallC <= Mckenna + bigM * z410_1
prob += Daragh >= smallC + Gene - (1 - z410_1) * bigM
prob += Daragh >= smallC + Mckenna - (1 - z410_1) * bigM
z411_1 = LpVariable("z411_1", cat="Binary")
prob += Daragh + smallC <= Mckenna + bigM * z411_1
prob += Daragh + smallC <= Dominick + bigM * z411_1
prob += Daragh >= smallC + Mckenna - (1 - z411_1) * bigM
prob += Daragh >= smallC + Dominick - (1 - z411_1) * bigM
z412_1 = LpVariable("z412_1", cat="Binary")
prob += Oisin + smallC <= Skylar + bigM * z412_1
prob += Oisin + smallC <= Gene + bigM * z412_1
prob += Oisin >= smallC + Skylar - (1 - z412_1) * bigM
prob += Oisin >= smallC + Gene - (1 - z412_1) * bigM
z413_1 = LpVariable("z413_1", cat="Binary")
prob += Neal + smallC <= Daragh + bigM * z413_1
prob += Neal + smallC <= Paris + bigM * z413_1
prob += Neal >= smallC + Daragh - (1 - z413_1) * bigM
prob += Neal >= smallC + Paris - (1 - z413_1) * bigM
z414_1 = LpVariable("z414_1", cat="Binary")
prob += Daragh + smallC <= Dominick + bigM * z414_1
prob += Daragh + smallC <= Chase + bigM * z414_1
prob += Daragh >= smallC + Dominick - (1 - z414_1) * bigM
prob += Daragh >= smallC + Chase - (1 - z414_1) * bigM
z415_1 = LpVariable("z415_1", cat="Binary")
prob += Conner + smallC <= Curt + bigM * z415_1
prob += Conner + smallC <= Ayesha + bigM * z415_1
prob += Conner >= smallC + Curt - (1 - z415_1) * bigM
prob += Conner >= smallC + Ayesha - (1 - z415_1) * bigM
z416_1 = LpVariable("z416_1", cat="Binary")
prob += Curt + smallC <= Gene + bigM * z416_1
prob += Curt + smallC <= Pam + bigM * z416_1
prob += Curt >= smallC + Gene - (1 - z416_1) * bigM
prob += Curt >= smallC + Pam - (1 - z416_1) * bigM
z417_1 = LpVariable("z417_1", cat="Binary")
prob += Wesley + smallC <= Chase + bigM * z417_1
prob += Wesley + smallC <= Conner + bigM * z417_1
prob += Wesley >= smallC + Chase - (1 - z417_1) * bigM
prob += Wesley >= smallC + Conner - (1 - z417_1) * bigM
z418_1 = LpVariable("z418_1", cat="Binary")
prob += Amari + smallC <= Mckenna + bigM * z418_1
prob += Amari + smallC <= Joni + bigM * z418_1
prob += Amari >= smallC + Mckenna - (1 - z418_1) * bigM
prob += Amari >= smallC + Joni - (1 - z418_1) * bigM
z419_1 = LpVariable("z419_1", cat="Binary")
prob += Pam + smallC <= Oisin + bigM * z419_1
prob += Pam + smallC <= Paris + bigM * z419_1
prob += Pam >= smallC + Oisin - (1 - z419_1) * bigM
prob += Pam >= smallC + Paris - (1 - z419_1) * bigM
z420_1 = LpVariable("z420_1", cat="Binary")
prob += Neal + smallC <= Curt + bigM * z420_1
prob += Neal + smallC <= Amari + bigM * z420_1
prob += Neal >= smallC + Curt - (1 - z420_1) * bigM
prob += Neal >= smallC + Amari - (1 - z420_1) * bigM
z421_1 = LpVariable("z421_1", cat="Binary")
prob += Mckenna + smallC <= Daragh + bigM * z421_1
prob += Mckenna + smallC <= Ruben + bigM * z421_1
prob += Mckenna >= smallC + Daragh - (1 - z421_1) * bigM
prob += Mckenna >= smallC + Ruben - (1 - z421_1) * bigM
z422_1 = LpVariable("z422_1", cat="Binary")
prob += Pam + smallC <= Gene + bigM * z422_1
prob += Pam + smallC <= Neal + bigM * z422_1
prob += Pam >= smallC + Gene - (1 - z422_1) * bigM
prob += Pam >= smallC + Neal - (1 - z422_1) * bigM
z423_1 = LpVariable("z423_1", cat="Binary")
prob += Paris + smallC <= Mckenna + bigM * z423_1
prob += Paris + smallC <= Joni + bigM * z423_1
prob += Paris >= smallC + Mckenna - (1 - z423_1) * bigM
prob += Paris >= smallC + Joni - (1 - z423_1) * bigM
z424_1 = LpVariable("z424_1", cat="Binary")
prob += Joni + smallC <= Janette + bigM * z424_1
prob += Joni + smallC <= Carla + bigM * z424_1
prob += Joni >= smallC + Janette - (1 - z424_1) * bigM
prob += Joni >= smallC + Carla - (1 - z424_1) * bigM
z425_1 = LpVariable("z425_1", cat="Binary")
prob += Conner + smallC <= Wesley + bigM * z425_1
prob += Conner + smallC <= Oisin + bigM * z425_1
prob += Conner >= smallC + Wesley - (1 - z425_1) * bigM
prob += Conner >= smallC + Oisin - (1 - z425_1) * bigM
z426_1 = LpVariable("z426_1", cat="Binary")
prob += Conner + smallC <= Joni + bigM * z426_1
prob += Conner + smallC <= Daragh + bigM * z426_1
prob += Conner >= smallC + Joni - (1 - z426_1) * bigM
prob += Conner >= smallC + Daragh - (1 - z426_1) * bigM
z427_1 = LpVariable("z427_1", cat="Binary")
prob += Amari + smallC <= Conner + bigM * z427_1
prob += Amari + smallC <= Janette + bigM * z427_1
prob += Amari >= smallC + Conner - (1 - z427_1) * bigM
prob += Amari >= smallC + Janette - (1 - z427_1) * bigM
z428_1 = LpVariable("z428_1", cat="Binary")
prob += Paris + smallC <= Daragh + bigM * z428_1
prob += Paris + smallC <= Oisin + bigM * z428_1
prob += Paris >= smallC + Daragh - (1 - z428_1) * bigM
prob += Paris >= smallC + Oisin - (1 - z428_1) * bigM
z429_1 = LpVariable("z429_1", cat="Binary")
prob += Paris + smallC <= Oisin + bigM * z429_1
prob += Paris + smallC <= Daragh + bigM * z429_1
prob += Paris >= smallC + Oisin - (1 - z429_1) * bigM
prob += Paris >= smallC + Daragh - (1 - z429_1) * bigM
z430_1 = LpVariable("z430_1", cat="Binary")
prob += Ruben + smallC <= Carla + bigM * z430_1
prob += Ruben + smallC <= Neal + bigM * z430_1
prob += Ruben >= smallC + Carla - (1 - z430_1) * bigM
prob += Ruben >= smallC + Neal - (1 - z430_1) * bigM
z431_1 = LpVariable("z431_1", cat="Binary")
prob += Oisin + smallC <= Curt + bigM * z431_1
prob += Oisin + smallC <= Conner + bigM * z431_1
prob += Oisin >= smallC + Curt - (1 - z431_1) * bigM
prob += Oisin >= smallC + Conner - (1 - z431_1) * bigM
z432_1 = LpVariable("z432_1", cat="Binary")
prob += Daragh + smallC <= Joni + bigM * z432_1
prob += Daragh + smallC <= Skylar + bigM * z432_1
prob += Daragh >= smallC + Joni - (1 - z432_1) * bigM
prob += Daragh >= smallC + Skylar - (1 - z432_1) * bigM
z433_1 = LpVariable("z433_1", cat="Binary")
prob += Curt + smallC <= Amari + bigM * z433_1
prob += Curt + smallC <= Conner + bigM * z433_1
prob += Curt >= smallC + Amari - (1 - z433_1) * bigM
prob += Curt >= smallC + Conner - (1 - z433_1) * bigM
z434_1 = LpVariable("z434_1", cat="Binary")
prob += Daragh + smallC <= Wesley + bigM * z434_1
prob += Daragh + smallC <= Conner + bigM * z434_1
prob += Daragh >= smallC + Wesley - (1 - z434_1) * bigM
prob += Daragh >= smallC + Conner - (1 - z434_1) * bigM
z435_1 = LpVariable("z435_1", cat="Binary")
prob += Conner + smallC <= Pam + bigM * z435_1
prob += Conner + smallC <= Amari + bigM * z435_1
prob += Conner >= smallC + Pam - (1 - z435_1) * bigM
prob += Conner >= smallC + Amari - (1 - z435_1) * bigM
z436_1 = LpVariable("z436_1", cat="Binary")
prob += Daragh + smallC <= Carla + bigM * z436_1
prob += Daragh + smallC <= Chase + bigM * z436_1
prob += Daragh >= smallC + Carla - (1 - z436_1) * bigM
prob += Daragh >= smallC + Chase - (1 - z436_1) * bigM
z437_1 = LpVariable("z437_1", cat="Binary")
prob += Paris + smallC <= Carla + bigM * z437_1
prob += Paris + smallC <= Lianne + bigM * z437_1
prob += Paris >= smallC + Carla - (1 - z437_1) * bigM
prob += Paris >= smallC + Lianne - (1 - z437_1) * bigM
z438_1 = LpVariable("z438_1", cat="Binary")
prob += Amari + smallC <= Neal + bigM * z438_1
prob += Amari + smallC <= Conner + bigM * z438_1
prob += Amari >= smallC + Neal - (1 - z438_1) * bigM
prob += Amari >= smallC + Conner - (1 - z438_1) * bigM
z439_1 = LpVariable("z439_1", cat="Binary")
prob += Oisin + smallC <= Carla + bigM * z439_1
prob += Oisin + smallC <= Joni + bigM * z439_1
prob += Oisin >= smallC + Carla - (1 - z439_1) * bigM
prob += Oisin >= smallC + Joni - (1 - z439_1) * bigM
z440_1 = LpVariable("z440_1", cat="Binary")
prob += Neal + smallC <= Amari + bigM * z440_1
prob += Neal + smallC <= Lianne + bigM * z440_1
prob += Neal >= smallC + Amari - (1 - z440_1) * bigM
prob += Neal >= smallC + Lianne - (1 - z440_1) * bigM
z441_1 = LpVariable("z441_1", cat="Binary")
prob += Skylar + smallC <= Daragh + bigM * z441_1
prob += Skylar + smallC <= Oisin + bigM * z441_1
prob += Skylar >= smallC + Daragh - (1 - z441_1) * bigM
prob += Skylar >= smallC + Oisin - (1 - z441_1) * bigM
z442_1 = LpVariable("z442_1", cat="Binary")
prob += Ayesha + smallC <= Skylar + bigM * z442_1
prob += Ayesha + smallC <= Paris + bigM * z442_1
prob += Ayesha >= smallC + Skylar - (1 - z442_1) * bigM
prob += Ayesha >= smallC + Paris - (1 - z442_1) * bigM
z443_1 = LpVariable("z443_1", cat="Binary")
prob += Paris + smallC <= Daragh + bigM * z443_1
prob += Paris + smallC <= Oisin + bigM * z443_1
prob += Paris >= smallC + Daragh - (1 - z443_1) * bigM
prob += Paris >= smallC + Oisin - (1 - z443_1) * bigM
z444_1 = LpVariable("z444_1", cat="Binary")
prob += Ayesha + smallC <= Conner + bigM * z444_1
prob += Ayesha + smallC <= Amari + bigM * z444_1
prob += Ayesha >= smallC + Conner - (1 - z444_1) * bigM
prob += Ayesha >= smallC + Amari - (1 - z444_1) * bigM
z445_1 = LpVariable("z445_1", cat="Binary")
prob += Mckenna + smallC <= Oisin + bigM * z445_1
prob += Mckenna + smallC <= Lianne + bigM * z445_1
prob += Mckenna >= smallC + Oisin - (1 - z445_1) * bigM
prob += Mckenna >= smallC + Lianne - (1 - z445_1) * bigM
z446_1 = LpVariable("z446_1", cat="Binary")
prob += Lianne + smallC <= Oisin + bigM * z446_1
prob += Lianne + smallC <= Paris + bigM * z446_1
prob += Lianne >= smallC + Oisin - (1 - z446_1) * bigM
prob += Lianne >= smallC + Paris - (1 - z446_1) * bigM
z447_1 = LpVariable("z447_1", cat="Binary")
prob += Lianne + smallC <= Paris + bigM * z447_1
prob += Lianne + smallC <= Ruben + bigM * z447_1
prob += Lianne >= smallC + Paris - (1 - z447_1) * bigM
prob += Lianne >= smallC + Ruben - (1 - z447_1) * bigM
z448_1 = LpVariable("z448_1", cat="Binary")
prob += Curt + smallC <= Oisin + bigM * z448_1
prob += Curt + smallC <= Pam + bigM * z448_1
prob += Curt >= smallC + Oisin - (1 - z448_1) * bigM
prob += Curt >= smallC + Pam - (1 - z448_1) * bigM
z449_1 = LpVariable("z449_1", cat="Binary")
prob += Curt + smallC <= Janette + bigM * z449_1
prob += Curt + smallC <= Neal + bigM * z449_1
prob += Curt >= smallC + Janette - (1 - z449_1) * bigM
prob += Curt >= smallC + Neal - (1 - z449_1) * bigM
z450_1 = LpVariable("z450_1", cat="Binary")
prob += Skylar + smallC <= Neal + bigM * z450_1
prob += Skylar + smallC <= Joni + bigM * z450_1
prob += Skylar >= smallC + Neal - (1 - z450_1) * bigM
prob += Skylar >= smallC + Joni - (1 - z450_1) * bigM
z451_1 = LpVariable("z451_1", cat="Binary")
prob += Conner + smallC <= Curt + bigM * z451_1
prob += Conner + smallC <= Chase + bigM * z451_1
prob += Conner >= smallC + Curt - (1 - z451_1) * bigM
prob += Conner >= smallC + Chase - (1 - z451_1) * bigM
z452_1 = LpVariable("z452_1", cat="Binary")
prob += Curt + smallC <= Conner + bigM * z452_1
prob += Curt + smallC <= Janette + bigM * z452_1
prob += Curt >= smallC + Conner - (1 - z452_1) * bigM
prob += Curt >= smallC + Janette - (1 - z452_1) * bigM
z453_1 = LpVariable("z453_1", cat="Binary")
prob += Skylar + smallC <= Dominick + bigM * z453_1
prob += Skylar + smallC <= Ayesha + bigM * z453_1
prob += Skylar >= smallC + Dominick - (1 - z453_1) * bigM
prob += Skylar >= smallC + Ayesha - (1 - z453_1) * bigM
z454_1 = LpVariable("z454_1", cat="Binary")
prob += Wesley + smallC <= Skylar + bigM * z454_1
prob += Wesley + smallC <= Mckenna + bigM * z454_1
prob += Wesley >= smallC + Skylar - (1 - z454_1) * bigM
prob += Wesley >= smallC + Mckenna - (1 - z454_1) * bigM
z455_1 = LpVariable("z455_1", cat="Binary")
prob += Paris + smallC <= Oisin + bigM * z455_1
prob += Paris + smallC <= Daragh + bigM * z455_1
prob += Paris >= smallC + Oisin - (1 - z455_1) * bigM
prob += Paris >= smallC + Daragh - (1 - z455_1) * bigM
z456_1 = LpVariable("z456_1", cat="Binary")
prob += Amari + smallC <= Skylar + bigM * z456_1
prob += Amari + smallC <= Ayesha + bigM * z456_1
prob += Amari >= smallC + Skylar - (1 - z456_1) * bigM
prob += Amari >= smallC + Ayesha - (1 - z456_1) * bigM
z457_1 = LpVariable("z457_1", cat="Binary")
prob += Wesley + smallC <= Neal + bigM * z457_1
prob += Wesley + smallC <= Janette + bigM * z457_1
prob += Wesley >= smallC + Neal - (1 - z457_1) * bigM
prob += Wesley >= smallC + Janette - (1 - z457_1) * bigM
z458_1 = LpVariable("z458_1", cat="Binary")
prob += Daragh + smallC <= Joni + bigM * z458_1
prob += Daragh + smallC <= Amari + bigM * z458_1
prob += Daragh >= smallC + Joni - (1 - z458_1) * bigM
prob += Daragh >= smallC + Amari - (1 - z458_1) * bigM
z459_1 = LpVariable("z459_1", cat="Binary")
prob += Ruben + smallC <= Oisin + bigM * z459_1
prob += Ruben + smallC <= Paris + bigM * z459_1
prob += Ruben >= smallC + Oisin - (1 - z459_1) * bigM
prob += Ruben >= smallC + Paris - (1 - z459_1) * bigM
z460_1 = LpVariable("z460_1", cat="Binary")
prob += Joni + smallC <= Chase + bigM * z460_1
prob += Joni + smallC <= Carla + bigM * z460_1
prob += Joni >= smallC + Chase - (1 - z460_1) * bigM
prob += Joni >= smallC + Carla - (1 - z460_1) * bigM
z461_1 = LpVariable("z461_1", cat="Binary")
prob += Joni + smallC <= Dominick + bigM * z461_1
prob += Joni + smallC <= Amari + bigM * z461_1
prob += Joni >= smallC + Dominick - (1 - z461_1) * bigM
prob += Joni >= smallC + Amari - (1 - z461_1) * bigM
z462_1 = LpVariable("z462_1", cat="Binary")
prob += Ruben + smallC <= Amari + bigM * z462_1
prob += Ruben + smallC <= Carla + bigM * z462_1
prob += Ruben >= smallC + Amari - (1 - z462_1) * bigM
prob += Ruben >= smallC + Carla - (1 - z462_1) * bigM
z463_1 = LpVariable("z463_1", cat="Binary")
prob += Paris + smallC <= Ruben + bigM * z463_1
prob += Paris + smallC <= Ayesha + bigM * z463_1
prob += Paris >= smallC + Ruben - (1 - z463_1) * bigM
prob += Paris >= smallC + Ayesha - (1 - z463_1) * bigM
z464_1 = LpVariable("z464_1", cat="Binary")
prob += Conner + smallC <= Dominick + bigM * z464_1
prob += Conner + smallC <= Curt + bigM * z464_1
prob += Conner >= smallC + Dominick - (1 - z464_1) * bigM
prob += Conner >= smallC + Curt - (1 - z464_1) * bigM
z465_1 = LpVariable("z465_1", cat="Binary")
prob += Ruben + smallC <= Skylar + bigM * z465_1
prob += Ruben + smallC <= Wesley + bigM * z465_1
prob += Ruben >= smallC + Skylar - (1 - z465_1) * bigM
prob += Ruben >= smallC + Wesley - (1 - z465_1) * bigM
z466_1 = LpVariable("z466_1", cat="Binary")
prob += Oisin + smallC <= Daragh + bigM * z466_1
prob += Oisin + smallC <= Lianne + bigM * z466_1
prob += Oisin >= smallC + Daragh - (1 - z466_1) * bigM
prob += Oisin >= smallC + Lianne - (1 - z466_1) * bigM
z467_1 = LpVariable("z467_1", cat="Binary")
prob += Curt + smallC <= Mckenna + bigM * z467_1
prob += Curt + smallC <= Daragh + bigM * z467_1
prob += Curt >= smallC + Mckenna - (1 - z467_1) * bigM
prob += Curt >= smallC + Daragh - (1 - z467_1) * bigM
z468_1 = LpVariable("z468_1", cat="Binary")
prob += Paris + smallC <= Daragh + bigM * z468_1
prob += Paris + smallC <= Oisin + bigM * z468_1
prob += Paris >= smallC + Daragh - (1 - z468_1) * bigM
prob += Paris >= smallC + Oisin - (1 - z468_1) * bigM
z469_1 = LpVariable("z469_1", cat="Binary")
prob += Curt + smallC <= Amari + bigM * z469_1
prob += Curt + smallC <= Janette + bigM * z469_1
prob += Curt >= smallC + Amari - (1 - z469_1) * bigM
prob += Curt >= smallC + Janette - (1 - z469_1) * bigM
z470_1 = LpVariable("z470_1", cat="Binary")
prob += Ayesha + smallC <= Paris + bigM * z470_1
prob += Ayesha + smallC <= Dominick + bigM * z470_1
prob += Ayesha >= smallC + Paris - (1 - z470_1) * bigM
prob += Ayesha >= smallC + Dominick - (1 - z470_1) * bigM
z471_1 = LpVariable("z471_1", cat="Binary")
prob += Amari + smallC <= Chase + bigM * z471_1
prob += Amari + smallC <= Curt + bigM * z471_1
prob += Amari >= smallC + Chase - (1 - z471_1) * bigM
prob += Amari >= smallC + Curt - (1 - z471_1) * bigM
z472_1 = LpVariable("z472_1", cat="Binary")
prob += Janette + smallC <= Conner + bigM * z472_1
prob += Janette + smallC <= Neal + bigM * z472_1
prob += Janette >= smallC + Conner - (1 - z472_1) * bigM
prob += Janette >= smallC + Neal - (1 - z472_1) * bigM
z473_1 = LpVariable("z473_1", cat="Binary")
prob += Janette + smallC <= Curt + bigM * z473_1
prob += Janette + smallC <= Lianne + bigM * z473_1
prob += Janette >= smallC + Curt - (1 - z473_1) * bigM
prob += Janette >= smallC + Lianne - (1 - z473_1) * bigM
z474_1 = LpVariable("z474_1", cat="Binary")
prob += Neal + smallC <= Pam + bigM * z474_1
prob += Neal + smallC <= Janette + bigM * z474_1
prob += Neal >= smallC + Pam - (1 - z474_1) * bigM
prob += Neal >= smallC + Janette - (1 - z474_1) * bigM
z475_1 = LpVariable("z475_1", cat="Binary")
prob += Amari + smallC <= Janette + bigM * z475_1
prob += Amari + smallC <= Neal + bigM * z475_1
prob += Amari >= smallC + Janette - (1 - z475_1) * bigM
prob += Amari >= smallC + Neal - (1 - z475_1) * bigM
z476_1 = LpVariable("z476_1", cat="Binary")
prob += Mckenna + smallC <= Ayesha + bigM * z476_1
prob += Mckenna + smallC <= Carla + bigM * z476_1
prob += Mckenna >= smallC + Ayesha - (1 - z476_1) * bigM
prob += Mckenna >= smallC + Carla - (1 - z476_1) * bigM
z477_1 = LpVariable("z477_1", cat="Binary")
prob += Ayesha + smallC <= Mckenna + bigM * z477_1
prob += Ayesha + smallC <= Gene + bigM * z477_1
prob += Ayesha >= smallC + Mckenna - (1 - z477_1) * bigM
prob += Ayesha >= smallC + Gene - (1 - z477_1) * bigM
z478_1 = LpVariable("z478_1", cat="Binary")
prob += Pam + smallC <= Joni + bigM * z478_1
prob += Pam + smallC <= Chase + bigM * z478_1
prob += Pam >= smallC + Joni - (1 - z478_1) * bigM
prob += Pam >= smallC + Chase - (1 - z478_1) * bigM
z479_1 = LpVariable("z479_1", cat="Binary")
prob += Paris + smallC <= Ruben + bigM * z479_1
prob += Paris + smallC <= Conner + bigM * z479_1
prob += Paris >= smallC + Ruben - (1 - z479_1) * bigM
prob += Paris >= smallC + Conner - (1 - z479_1) * bigM
z480_1 = LpVariable("z480_1", cat="Binary")
prob += Ruben + smallC <= Neal + bigM * z480_1
prob += Ruben + smallC <= Gene + bigM * z480_1
prob += Ruben >= smallC + Neal - (1 - z480_1) * bigM
prob += Ruben >= smallC + Gene - (1 - z480_1) * bigM
z481_1 = LpVariable("z481_1", cat="Binary")
prob += Janette + smallC <= Conner + bigM * z481_1
prob += Janette + smallC <= Neal + bigM * z481_1
prob += Janette >= smallC + Conner - (1 - z481_1) * bigM
prob += Janette >= smallC + Neal - (1 - z481_1) * bigM
z482_1 = LpVariable("z482_1", cat="Binary")
prob += Mckenna + smallC <= Paris + bigM * z482_1
prob += Mckenna + smallC <= Skylar + bigM * z482_1
prob += Mckenna >= smallC + Paris - (1 - z482_1) * bigM
prob += Mckenna >= smallC + Skylar - (1 - z482_1) * bigM
z483_1 = LpVariable("z483_1", cat="Binary")
prob += Lianne + smallC <= Daragh + bigM * z483_1
prob += Lianne + smallC <= Skylar + bigM * z483_1
prob += Lianne >= smallC + Daragh - (1 - z483_1) * bigM
prob += Lianne >= smallC + Skylar - (1 - z483_1) * bigM
z484_1 = LpVariable("z484_1", cat="Binary")
prob += Joni + smallC <= Neal + bigM * z484_1
prob += Joni + smallC <= Ayesha + bigM * z484_1
prob += Joni >= smallC + Neal - (1 - z484_1) * bigM
prob += Joni >= smallC + Ayesha - (1 - z484_1) * bigM
z485_1 = LpVariable("z485_1", cat="Binary")
prob += Mckenna + smallC <= Neal + bigM * z485_1
prob += Mckenna + smallC <= Dominick + bigM * z485_1
prob += Mckenna >= smallC + Neal - (1 - z485_1) * bigM
prob += Mckenna >= smallC + Dominick - (1 - z485_1) * bigM
z486_1 = LpVariable("z486_1", cat="Binary")
prob += Skylar + smallC <= Oisin + bigM * z486_1
prob += Skylar + smallC <= Paris + bigM * z486_1
prob += Skylar >= smallC + Oisin - (1 - z486_1) * bigM
prob += Skylar >= smallC + Paris - (1 - z486_1) * bigM
z487_1 = LpVariable("z487_1", cat="Binary")
prob += Conner + smallC <= Mckenna + bigM * z487_1
prob += Conner + smallC <= Ruben + bigM * z487_1
prob += Conner >= smallC + Mckenna - (1 - z487_1) * bigM
prob += Conner >= smallC + Ruben - (1 - z487_1) * bigM
z488_1 = LpVariable("z488_1", cat="Binary")
prob += Oisin + smallC <= Wesley + bigM * z488_1
prob += Oisin + smallC <= Paris + bigM * z488_1
prob += Oisin >= smallC + Wesley - (1 - z488_1) * bigM
prob += Oisin >= smallC + Paris - (1 - z488_1) * bigM
z489_1 = LpVariable("z489_1", cat="Binary")
prob += Curt + smallC <= Janette + bigM * z489_1
prob += Curt + smallC <= Conner + bigM * z489_1
prob += Curt >= smallC + Janette - (1 - z489_1) * bigM
prob += Curt >= smallC + Conner - (1 - z489_1) * bigM
z490_1 = LpVariable("z490_1", cat="Binary")
prob += Amari + smallC <= Neal + bigM * z490_1
prob += Amari + smallC <= Janette + bigM * z490_1
prob += Amari >= smallC + Neal - (1 - z490_1) * bigM
prob += Amari >= smallC + Janette - (1 - z490_1) * bigM
z491_1 = LpVariable("z491_1", cat="Binary")
prob += Daragh + smallC <= Gene + bigM * z491_1
prob += Daragh + smallC <= Mckenna + bigM * z491_1
prob += Daragh >= smallC + Gene - (1 - z491_1) * bigM
prob += Daragh >= smallC + Mckenna - (1 - z491_1) * bigM
z492_1 = LpVariable("z492_1", cat="Binary")
prob += Daragh + smallC <= Ruben + bigM * z492_1
prob += Daragh + smallC <= Skylar + bigM * z492_1
prob += Daragh >= smallC + Ruben - (1 - z492_1) * bigM
prob += Daragh >= smallC + Skylar - (1 - z492_1) * bigM
z493_1 = LpVariable("z493_1", cat="Binary")
prob += Joni + smallC <= Ruben + bigM * z493_1
prob += Joni + smallC <= Lianne + bigM * z493_1
prob += Joni >= smallC + Ruben - (1 - z493_1) * bigM
prob += Joni >= smallC + Lianne - (1 - z493_1) * bigM
z494_1 = LpVariable("z494_1", cat="Binary")
prob += Conner + smallC <= Janette + bigM * z494_1
prob += Conner + smallC <= Gene + bigM * z494_1
prob += Conner >= smallC + Janette - (1 - z494_1) * bigM
prob += Conner >= smallC + Gene - (1 - z494_1) * bigM
z495_1 = LpVariable("z495_1", cat="Binary")
prob += Wesley + smallC <= Amari + bigM * z495_1
prob += Wesley + smallC <= Conner + bigM * z495_1
prob += Wesley >= smallC + Amari - (1 - z495_1) * bigM
prob += Wesley >= smallC + Conner - (1 - z495_1) * bigM
z496_1 = LpVariable("z496_1", cat="Binary")
prob += Joni + smallC <= Gene + bigM * z496_1
prob += Joni + smallC <= Curt + bigM * z496_1
prob += Joni >= smallC + Gene - (1 - z496_1) * bigM
prob += Joni >= smallC + Curt - (1 - z496_1) * bigM
z497_1 = LpVariable("z497_1", cat="Binary")
prob += Paris + smallC <= Conner + bigM * z497_1
prob += Paris + smallC <= Lianne + bigM * z497_1
prob += Paris >= smallC + Conner - (1 - z497_1) * bigM
prob += Paris >= smallC + Lianne - (1 - z497_1) * bigM
z498_1 = LpVariable("z498_1", cat="Binary")
prob += Ayesha + smallC <= Neal + bigM * z498_1
prob += Ayesha + smallC <= Conner + bigM * z498_1
prob += Ayesha >= smallC + Neal - (1 - z498_1) * bigM
prob += Ayesha >= smallC + Conner - (1 - z498_1) * bigM
z499_1 = LpVariable("z499_1", cat="Binary")
prob += Daragh + smallC <= Neal + bigM * z499_1
prob += Daragh + smallC <= Amari + bigM * z499_1
prob += Daragh >= smallC + Neal - (1 - z499_1) * bigM
prob += Daragh >= smallC + Amari - (1 - z499_1) * bigM

GLPK().solve(prob)
ages = {}
for v in prob.variables():
	if v.name in wizzies:
		print(v.name, "=", v.varValue)
		ages[v.name] = v.varValue
sorted_ages = sorted(ages.items(), key = lambda x: x[1])
relative_mapping = {}
for i in range(len(sorted_ages)):
	relative_mapping[sorted_ages[i][0]] = i
