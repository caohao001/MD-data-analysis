#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import linecache

mulliken = open('CHARGE.mulliken', 'r')
ele_num = int(input('原子编号： '))
linenum = ele_num + 406322
sum_charge = 0
times = 0
output = open('Na_charge.txt', 'w')

def f(x):
    global sum_charge
    target = linecache.getline('CHARGE.mulliken', x).strip('\n').split()
    charge = float(target[5])
    output.write(str(charge) + '\n')
    sum_charge = charge + sum_charge


while linecache.getline('CHARGE.mulliken', linenum) != '':
    f(linenum)
    linenum = linenum + 527
    times = times + 1

net_charge = sum_charge / times
file = open('net_charge.txt', 'w')
file.write(str(net_charge))
file.close()
