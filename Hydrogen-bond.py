#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import linecache
import numpy as np


lattice_a = np.array([10.8232,0,0])
lattice_b = np.array([0,9.3732,0])
total_atom = int(linecache.getline('5ps-10ps.xyz', 1))
file = open('5ps-10ps.xyz', 'r')
output = open('hydrogen-bond.txt', 'w')
OH_output = open('O-H distance.txt','w')
def surf(x, y):
    total_z = 0
    with open('5ps-10ps.xyz', 'r') as file:
        for line in file.readlines()[x+48:y]:
            lines = line.strip('\n').split()
            if lines[0] == 'Ru':
                z_coor = float(lines[3])
                total_z = z_coor + total_z
    global z_surface
    z_surface = total_z / 16



def data(x,y):
    global O_atom_total
    global H_atom_total
    O_atom_total = []
    H_atom_total = []
    with open('5ps-10ps.xyz', 'r') as file:
        for line in file.readlines()[x:y]:
            lines = line.strip('\n').split()
            if lines[0] == "O":
                lines.pop(0)
                O_atom = list(map(float,lines))
                O_atom_total.append(np.array(O_atom))
            elif lines[0] == 'H':
                lines.pop(0)
                H_atom = list(map(float,lines))
                H_atom_total.append(np.array(H_atom))
        #print(H_atom_total)

def cal(x,y):
    global N_1, N_2, N_3, N_4, N_5, N_6, N_7, N_8, N_9, N_10, N_11, N_12, N_13, N_14, N_15, N_16, N_17, N_18, N_19, N_20
    global N_21, N_22, N_23, N_24, N_25, N_26, N_27, N_28, N_29, N_30
    N_1 = N_2 = N_3 = N_4 = N_5 = N_6 = N_7 = N_8 = N_9 = N_10 = N_11 = N_12 = N_13 = N_14 = N_15 = N_16 = N_17 = N_18 = N_19 = N_20 = 0
    N_21 = N_22 = N_23 = N_24 = N_25 = N_26 = N_27 = N_28 = N_29 = N_30 = 0
    for i_O in x:
        for i_H in y:
              d_OH = i_O-i_H
              d_bond = np.sqrt((d_OH * d_OH).sum())
              OH_output.write(str(d_bond)+'\n')
              if 1.2 < d_bond < 2:
                O_location = i_O[2] - z_surface
                if O_location < 0.5:
                    N_1 = N_1 + 1
                elif O_location < 1:
                    N_2 = N_2 + 1
                elif O_location < 1.5:
                    N_3 = N_3 + 1
                elif O_location < 2:
                    N_4 = N_4 + 1
                elif O_location < 2.5:
                    N_5 = N_5 + 1
                elif O_location < 3:
                    N_6 = N_6 + 1
                elif O_location < 3.5:
                    N_7 = N_7 + 1
                elif O_location < 4:
                    N_8 = N_8 + 1
                elif O_location < 4.5:
                    N_9 = N_9 + 1
                elif O_location < 5:
                    N_10 = N_10 + 1
                elif O_location < 5.5:
                    N_11 = N_11 + 1
                elif O_location < 6:
                    N_12 = N_12 + 1
                elif O_location < 6.5:
                    N_13 = N_13 + 1
                elif O_location < 7:
                    N_14 = N_14 + 1
                elif O_location < 7.5:
                    N_15 = N_15 + 1
                elif O_location < 8:
                    N_16 = N_16 + 1
                elif O_location < 8.5:
                    N_17 = N_17 + 1
                elif O_location < 9:
                    N_18 = N_18 + 1
                elif O_location < 9.5:
                    N_19 = N_19 + 1
                elif O_location < 10:
                    N_20 = N_20 + 1
                elif O_location < 10.5:
                    N_21 = N_21 + 1
                elif O_location < 11:
                    N_22 = N_22 + 1
                elif O_location < 11.5:
                    N_23 = N_23 + 1
                elif O_location < 12:
                    N_24 = N_24 + 1
                elif O_location < 12.5:
                    N_25 = N_25 + 1
                elif O_location < 13:
                    N_26 = N_26 + 1
                elif O_location < 13.5:
                    N_27 = N_27 + 1
                elif O_location < 14:
                    N_28 = N_28 + 1
                elif O_location < 14.5:
                    N_29 = N_29 + 1
                elif O_location < 15:
                    N_30 = N_30 + 1




def lattice_change_plus(x,y):
    x_end = []
    for i in x:
        i = i + y
        x_end.append(i)
    x = x_end

def lattice_change_minor(x,y):
    for i in x:
        i = i - y

D_1 = D_2 = D_3 = D_4 = D_5 = D_6 = D_7 = D_8 = D_9 = D_10 = 0
D_11 = D_12 = D_13 = D_14 = D_15 = D_16 = D_17 = D_18 = D_19 = D_20 = 0
D_21 = D_22 = D_23 = D_24 = D_25 = D_26 = D_27 = D_28 = D_29 = D_30 = 0
line_init = 3
line_end = 3 + total_atom
linenum = 0
while linecache.getline('5ps-10ps.xyz', line_init) != '':
    data(line_init,line_end)
#    print(O_atom_total)
    surf(line_init,line_end)
    cal(O_atom_total,H_atom_total)
    D_1 = N_1 + D_1
    D_2 = N_2 + D_2
    D_3 = N_3 + D_3
    D_4 = N_4 + D_4
    D_5 = N_5 + D_5
    D_6 = N_6 + D_6
    D_7 = N_7 + D_7
    D_8 = N_8 + D_8
    D_9 = N_9 + D_9
    D_10 = N_10 + D_10
    D_11 = N_11 + D_11
    D_12 = N_12 + D_12
    D_13 = N_13 + D_13
    D_14 = N_14 + D_14
    D_15 = N_15 + D_15
    D_16 = N_16 + D_16
    D_17 = N_17 + D_17
    D_18 = N_18 + D_18
    D_19 = N_19 + D_19
    D_20 = N_20 + D_20
    D_21 = N_21 + D_21
    D_22 = N_22 + D_22
    D_23 = N_23 + D_23
    D_24 = N_24 + D_24
    D_25 = N_25 + D_25
    D_26 = N_26 + D_26
    D_27 = N_27 + D_27
    D_28 = N_28 + D_28
    D_29 = N_29 + D_29
    D_30 = N_30 + D_30
    O_atom_ap = []
    for i in O_atom_total:
        i = i + lattice_a
        O_atom_ap.append(i)
    O_atom_total = O_atom_ap
#    lattice_change_plus(O_atom_total,lattice_a)
#    print(O_atom_total)
    cal(O_atom_total, H_atom_total)
    D_1 = N_1 + D_1
    D_2 = N_2 + D_2
    D_3 = N_3 + D_3
    D_4 = N_4 + D_4
    D_5 = N_5 + D_5
    D_6 = N_6 + D_6
    D_7 = N_7 + D_7
    D_8 = N_8 + D_8
    D_9 = N_9 + D_9
    D_10 = N_10 + D_10
    D_11 = N_11 + D_11
    D_12 = N_12 + D_12
    D_13 = N_13 + D_13
    D_14 = N_14 + D_14
    D_15 = N_15 + D_15
    D_16 = N_16 + D_16
    D_17 = N_17 + D_17
    D_18 = N_18 + D_18
    D_19 = N_19 + D_19
    D_20 = N_20 + D_20
    D_21 = N_21 + D_21
    D_22 = N_22 + D_22
    D_23 = N_23 + D_23
    D_24 = N_24 + D_24
    D_25 = N_25 + D_25
    D_26 = N_26 + D_26
    D_27 = N_27 + D_27
    D_28 = N_28 + D_28
    D_29 = N_29 + D_29
    D_30 = N_30 + D_30
    O_atom_ap = []
    for i in O_atom_total:
        i = i - 2*lattice_a
        O_atom_ap.append(i)
    O_atom_total = O_atom_ap
#    lattice_change_minor(O_atom_total,2*lattice_a)
#    print(O_atom_total)
    cal(O_atom_total, H_atom_total)
    D_1 = N_1 + D_1
    D_2 = N_2 + D_2
    D_3 = N_3 + D_3
    D_4 = N_4 + D_4
    D_5 = N_5 + D_5
    D_6 = N_6 + D_6
    D_7 = N_7 + D_7
    D_8 = N_8 + D_8
    D_9 = N_9 + D_9
    D_10 = N_10 + D_10
    D_11 = N_11 + D_11
    D_12 = N_12 + D_12
    D_13 = N_13 + D_13
    D_14 = N_14 + D_14
    D_15 = N_15 + D_15
    D_16 = N_16 + D_16
    D_17 = N_17 + D_17
    D_18 = N_18 + D_18
    D_19 = N_19 + D_19
    D_20 = N_20 + D_20
    D_21 = N_21 + D_21
    D_22 = N_22 + D_22
    D_23 = N_23 + D_23
    D_24 = N_24 + D_24
    D_25 = N_25 + D_25
    D_26 = N_26 + D_26
    D_27 = N_27 + D_27
    D_28 = N_28 + D_28
    D_29 = N_29 + D_29
    D_30 = N_30 + D_30
    O_atom_ap = []
    for i in O_atom_total:
        i = i + lattice_a
        O_atom_ap.append(i)
    O_atom_total = O_atom_ap
#    lattice_change_plus(O_atom_total, lattice_a)
#    lattice_change_plus(O_atom_total, lattice_b)
    O_atom_ap = []
    for i in O_atom_total:
        i = i + lattice_b
        O_atom_ap.append(i)
    O_atom_total = O_atom_ap
    cal(O_atom_total, H_atom_total)
    D_1 = N_1 + D_1
    D_2 = N_2 + D_2
    D_3 = N_3 + D_3
    D_4 = N_4 + D_4
    D_5 = N_5 + D_5
    D_6 = N_6 + D_6
    D_7 = N_7 + D_7
    D_8 = N_8 + D_8
    D_9 = N_9 + D_9
    D_10 = N_10 + D_10
    D_11 = N_11 + D_11
    D_12 = N_12 + D_12
    D_13 = N_13 + D_13
    D_14 = N_14 + D_14
    D_15 = N_15 + D_15
    D_16 = N_16 + D_16
    D_17 = N_17 + D_17
    D_18 = N_18 + D_18
    D_19 = N_19 + D_19
    D_20 = N_20 + D_20
    D_21 = N_21 + D_21
    D_22 = N_22 + D_22
    D_23 = N_23 + D_23
    D_24 = N_24 + D_24
    D_25 = N_25 + D_25
    D_26 = N_26 + D_26
    D_27 = N_27 + D_27
    D_28 = N_28 + D_28
    D_29 = N_29 + D_29
    D_30 = N_30 + D_30
    O_atom_ap = []
    for i in O_atom_total:
        i = i - 2*lattice_b
        O_atom_ap.append(i)
    O_atom_total = O_atom_ap
#    lattice_change_minor(O_atom_total, 2*lattice_b)
    cal(O_atom_total, H_atom_total)
    D_1 = N_1 + D_1
    D_2 = N_2 + D_2
    D_3 = N_3 + D_3
    D_4 = N_4 + D_4
    D_5 = N_5 + D_5
    D_6 = N_6 + D_6
    D_7 = N_7 + D_7
    D_8 = N_8 + D_8
    D_9 = N_9 + D_9
    D_10 = N_10 + D_10
    D_11 = N_11 + D_11
    D_12 = N_12 + D_12
    D_13 = N_13 + D_13
    D_14 = N_14 + D_14
    D_15 = N_15 + D_15
    D_16 = N_16 + D_16
    D_17 = N_17 + D_17
    D_18 = N_18 + D_18
    D_19 = N_19 + D_19
    D_20 = N_20 + D_20
    D_21 = N_21 + D_21
    D_22 = N_22 + D_22
    D_23 = N_23 + D_23
    D_24 = N_24 + D_24
    D_25 = N_25 + D_25
    D_26 = N_26 + D_26
    D_27 = N_27 + D_27
    D_28 = N_28 + D_28
    D_29 = N_29 + D_29
    D_30 = N_30 + D_30
    line_init = line_init + total_atom + 2
    line_end = line_end + total_atom + 2
    linenum = linenum + 1

a1 = "0-0.5 A :     "
a2 = "0.5-1 A :     "
a3 = "1-1.5 A :     "
a4 = "1.5-2 A :     "
a5 = "2-2.5 A :     "
a6 = "2.5-3 A :     "
a7 = "3-3.5 A :     "
a8 = "3.5-4 A :     "
a9 = "4-4.5 A :     "
a10 = "4.5-5 A :    "
a11 = "5-5.5 A :    "
a12 = "5.5-6 A :    "
a13 = "6-6.5 A :    "
a14 = "6.5-7 A :    "
a15 = "7-7.5 A :    "
a16 = "7.5-8 A :    "
a17 = "8-8.5 A :    "
a18 = "8.5-9 A :    "
a19 = "9-9.5 A :    "
a20 = "9.5-10 A :   "
a21 = "10-10.5 A :  "
a22 = "10.5-11 A :  "
a23 = "11-11.5 A :  "
a24 = "11.5-12 A :  "
a25 = "12-12.5 A :  "
a26 = "12.5-13 A :  "
a27 = "13-13.5 A :  "
a28 = "13.5-14 A :  "
a29 = "14-14.5 A :  "
a30 = "14.5-15 A :  "
output.write(a1 + str(D_1 / (linenum)) + '\n')
output.write(a2 + str(D_2 / (linenum)) + '\n')
output.write(a3 + str(D_3 / (linenum)) + '\n')
output.write(a4 + str(D_4 / (linenum)) + '\n')
output.write(a5 + str(D_5 / (linenum)) + '\n')
output.write(a6 + str(D_6 / (linenum)) + '\n')
output.write(a7 + str(D_7 / (linenum)) + '\n')
output.write(a8 + str(D_8 / (linenum)) + '\n')
output.write(a9 + str(D_9 / (linenum)) + '\n')
output.write(a10 + str(D_10 / (linenum)) + '\n')
output.write(a11 + str(D_11 / (linenum)) + '\n')
output.write(a12 + str(D_12 / (linenum)) + '\n')
output.write(a13 + str(D_13 / (linenum)) + '\n')
output.write(a14 + str(D_14 / (linenum)) + '\n')
output.write(a15 + str(D_15 / (linenum)) + '\n')
output.write(a16 + str(D_16 / (linenum)) + '\n')
output.write(a17 + str(D_17 / (linenum)) + '\n')
output.write(a18 + str(D_18 / (linenum)) + '\n')
output.write(a19 + str(D_19 / (linenum)) + '\n')
output.write(a20 + str(D_20 / (linenum)) + '\n')
output.write(a21 + str(D_21 / (linenum)) + '\n')
output.write(a22 + str(D_22 / (linenum)) + '\n')
output.write(a23 + str(D_23 / (linenum)) + '\n')
output.write(a24 + str(D_24 / (linenum)) + '\n')
output.write(a25 + str(D_25 / (linenum)) + '\n')
output.write(a26 + str(D_26 / (linenum)) + '\n')
output.write(a27 + str(D_27 / (linenum)) + '\n')
output.write(a28 + str(D_28 / (linenum)) + '\n')
output.write(a29 + str(D_29 / (linenum)) + '\n')
output.write(a30 + str(D_30 / (linenum)) + '\n')
