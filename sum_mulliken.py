#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import linecache

linenum_1 = 1
linenum_2 = 95
times = 0
sum_C_charge = 0
sum_N_charge = 0


def cal_charge(x, y):
    global sum_C_charge
    global sum_N_charge
    with open('mulliken', 'r') as file:
        for line in file.readlines()[x:y]:
            lines = line.strip('\n').split()
            print(lines)
            if lines[1] == 'C':
                C_charge = float(lines[5])
                sum_C_charge = C_charge + sum_C_charge
            elif lines[1] == 'N':
                N_charge = float(lines[5])
                sum_N_charge = N_charge + sum_N_charge


while linecache.getline('mulliken', linenum_1) != '':
    cal_charge(linenum_1, linenum_2)
    linenum_1 = linenum_1 + 529
    linenum_2 = linenum_2 + 529
    times = times + 1
    print(times)

C_net_charge = sum_C_charge / times
N_net_charge = sum_N_charge / times
out = open('sum_net_charge.txt', 'w')
out.write('C:  ' + str(C_net_charge) + '\n')
out.write('N:  ' + str(N_net_charge) + '\n')
out.close()
