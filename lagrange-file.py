#!/usr/bin/python3
# -*- coding: UTF-8 -*-
file = open('5ps-15ps.txt', 'w')
aver_f = open('average-force.txt', 'w')
force = 0
times = 0
with open('test-1.LagrangeMultLog', 'r') as lag:
    for line in lag.readlines()[10000:30000]:
        lines = line.strip('\n').split()
        if 'Shake' in lines:
            file.write(lines[3]+'\n')
            force = force + float(lines[3])
            times = times + 1
average_force = (force * 51.439) / times
aver_f.write(str(average_force) + ' eV/A')
print(str(average_force) + ' eV/A')
file.close()
aver_f.close()
