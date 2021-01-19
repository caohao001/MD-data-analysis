#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import linecache

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
a31 = "15-15.5 A :  "
a32 = "15.5-16 A :  "
a33 = "16-16.5 A :  "
a34 = "16.5-17 A :  "
a35 = "17-17.5 A :  "
a36 = "17.5-18 A :  "
a37 = "18-18.5 A :  "
a38 = "18.5-19 A :  "
a39 = "19-19.5 A :  "
a40 = "19.5-20 A :  "
output = open('water-density.txt', 'w')


def surf(x, y):
    total_z = 0
    with open('2ps-3ps.xyz', 'r') as file:
        for line in file.readlines()[x:y]:
            lines = line.strip('\n').split()
            if lines[0] == 'C' or lines[0] == 'N' or lines[0] == 'Fe':
                z_coor = float(lines[3])
                total_z = z_coor + total_z
    global z_surface
    z_surface = total_z / 95


def coor(x, y):
    global z_surface
    global N_1, N_2, N_3, N_4, N_5, N_6, N_7, N_8, N_9, N_10
    global N_11, N_12, N_13, N_14, N_15, N_16, N_17, N_18, N_19, N_20
    global N_21, N_22, N_23, N_24, N_25, N_26, N_27, N_28, N_29, N_30
    global N_31, N_32, N_33, N_34, N_35, N_36, N_37, N_38, N_39, N_40
    N_1 = N_2 = N_3 = N_4 = N_5 = N_6 = N_7 = N_8 = N_9 = N_10 = 0
    N_11 = N_12 = N_13 = N_14 = N_15 = N_16 = N_17 = N_18 = N_19 = N_20 = 0
    N_21 = N_22 = N_23 = N_24 = N_25 = N_26 = N_27 = N_28 = N_29 = N_30 = 0
    N_31 = N_32 = N_33 = N_34 = N_35 = N_36 = N_37 = N_38 = N_39 = N_40 = 0
    with open('2ps-3ps.xyz', 'r') as file:
        for line in file.readlines()[x:y]:
            lines = line.strip('\n').split()
            if lines[0] == 'O':
                O_location = float(lines[3]) - z_surface
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
                elif O_location < 15.5:
                    N_31 = N_31 + 1
                elif O_location < 16:
                    N_32 = N_32 + 1
                elif O_location < 16.5:
                    N_33 = N_33 + 1
                elif O_location < 17:
                    N_34 = N_34 + 1
                elif O_location < 17.5:
                    N_35 = N_35 + 1
                elif O_location < 18:
                    N_36 = N_36 + 1
                elif O_location < 18.5:
                    N_37 = N_37 + 1
                elif O_location < 19:
                    N_38 = N_38 + 1
                elif O_location < 19.5:
                    N_39 = N_39 + 1
                elif O_location < 20:
                    N_40 = N_40 + 1


total_atom = int(linecache.getline('2ps-3ps.xyz', 1))
a = 3
b = 3 + total_atom
linenum = 0
D_1 = D_2 = D_3 = D_4 = D_5 = D_6 = D_7 = D_8 = D_9 = D_10 = 0
D_11 = D_12 = D_13 = D_14 = D_15 = D_16 = D_17 = D_18 = D_19 = D_20 = 0
D_21 = D_22 = D_23 = D_24 = D_25 = D_26 = D_27 = D_28 = D_29 = D_30 = 0
D_31 = D_32 = D_33 = D_34 = D_35 = D_36 = D_37 = D_38 = D_39 = D_40 = 0
while linecache.getline('2ps-3ps.xyz', a) != '':
    surf(a, b)
    coor(a, b)
    a = a + total_atom + 2
    b = b + total_atom + 2
    linenum = linenum + 1
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
    D_31 = N_31 + D_31
    D_32 = N_32 + D_32
    D_33 = N_33 + D_33
    D_34 = N_34 + D_34
    D_35 = N_35 + D_35
    D_36 = N_36 + D_36
    D_37 = N_37 + D_37
    D_38 = N_38 + D_38
    D_39 = N_39 + D_39
    D_40 = N_40 + D_40

output.write(a1 + str(D_1 / (4.2 * linenum)) + '\n')
output.write(a2 + str(D_2 / (4.2 * linenum)) + '\n')
output.write(a3 + str(D_3 / (4.2 * linenum)) + '\n')
output.write(a4 + str(D_4 / (4.2 * linenum)) + '\n')
output.write(a5 + str(D_5 / (4.2 * linenum)) + '\n')
output.write(a6 + str(D_6 / (4.2 * linenum)) + '\n')
output.write(a7 + str(D_7 / (4.2 * linenum)) + '\n')
output.write(a8 + str(D_8 / (4.2 * linenum)) + '\n')
output.write(a9 + str(D_9 / (4.2 * linenum)) + '\n')
output.write(a10 + str(D_10 / (4.2 * linenum)) + '\n')
output.write(a11 + str(D_11 / (4.2 * linenum)) + '\n')
output.write(a12 + str(D_12 / (4.2 * linenum)) + '\n')
output.write(a13 + str(D_13 / (4.2 * linenum)) + '\n')
output.write(a14 + str(D_14 / (4.2 * linenum)) + '\n')
output.write(a15 + str(D_15 / (4.2 * linenum)) + '\n')
output.write(a16 + str(D_16 / (4.2 * linenum)) + '\n')
output.write(a17 + str(D_17 / (4.2 * linenum)) + '\n')
output.write(a18 + str(D_18 / (4.2 * linenum)) + '\n')
output.write(a19 + str(D_19 / (4.2 * linenum)) + '\n')
output.write(a20 + str(D_20 / (4.2 * linenum)) + '\n')
output.write(a21 + str(D_21 / (4.2 * linenum)) + '\n')
output.write(a22 + str(D_22 / (4.2 * linenum)) + '\n')
output.write(a23 + str(D_23 / (4.2 * linenum)) + '\n')
output.write(a24 + str(D_24 / (4.2 * linenum)) + '\n')
output.write(a25 + str(D_25 / (4.2 * linenum)) + '\n')
output.write(a26 + str(D_26 / (4.2 * linenum)) + '\n')
output.write(a27 + str(D_27 / (4.2 * linenum)) + '\n')
output.write(a28 + str(D_28 / (4.2 * linenum)) + '\n')
output.write(a29 + str(D_29 / (4.2 * linenum)) + '\n')
output.write(a30 + str(D_30 / (4.2 * linenum)) + '\n')
output.write(a31 + str(D_31 / (4.2 * linenum)) + '\n')
output.write(a32 + str(D_32 / (4.2 * linenum)) + '\n')
output.write(a33 + str(D_33 / (4.2 * linenum)) + '\n')
output.write(a34 + str(D_34 / (4.2 * linenum)) + '\n')
output.write(a35 + str(D_35 / (4.2 * linenum)) + '\n')
output.write(a36 + str(D_36 / (4.2 * linenum)) + '\n')
output.write(a37 + str(D_37 / (4.2 * linenum)) + '\n')
output.write(a38 + str(D_38 / (4.2 * linenum)) + '\n')
output.write(a39 + str(D_39 / (4.2 * linenum)) + '\n')
output.write(a40 + str(D_40 / (4.2 * linenum)) + '\n')
output.close()
