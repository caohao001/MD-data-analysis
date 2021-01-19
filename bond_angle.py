#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import numpy as np
import linecache

# 计算每一帧的键长
file1 = open('5ps-15ps.xyz', 'r')
output = open('bond-angle.txt', 'w')
output.write('angle           Cos(angle)')
center_atom = input('键角中心原子序号： ')
side_atom_1 = input('键角两边原子序号1： ')
side_atom_2 = input('键角两边原子序号2： ')
linenum_ca = int(center_atom) + 2
linenum_s1 = int(side_atom_1) + 2
linenum_s2 = int(side_atom_2) + 2
total_atom = int(linecache.getline('5ps-15ps.xyz', 1))


def f(x, y, z):
    xyz_ca = linecache.getline('5ps-15ps.xyz', x).strip('\n').split()  # 中心原子坐标
    xyz_ca.pop(0)
    f_ca = []
    for i in xyz_ca:
        f_ca.append(float(i))
    xyz_1 = linecache.getline('5ps-15ps.xyz', y).strip('\n').split()   #角度两边原子坐标
    xyz_1.pop(0)
    f_1 = []
    for i in xyz_1:
        f_1.append(float(i))
    xyz_2 = linecache.getline('5ps-15ps.xyz', z).strip('\n').split()
    xyz_2.pop(0)
    f_2 = []
    for i in xyz_2:
        f_2.append(float(i))
    np_ca = np.array(f_ca)
    np_1 = np.array(f_1)
    np_2 = np.array(f_2)
    bian_1 = np_1 - np_ca
    bian_2 = np_2 - np_ca
    L1 = np.sqrt(bian_1.dot(bian_1))
    L2 = np.sqrt(bian_2.dot(bian_2))
    cos_angle = bian_1.dot(bian_2) / (L1 * L2)
    angle = np.arccos(cos_angle) * 360/2/np.pi
    output.write(str(angle) + '       ' + str(cos_angle) + '\n')


while linecache.getline('5ps-15ps.xyz', linenum_ca) != '':
    f(linenum_ca, linenum_s1, linenum_s2)
    linenum_ca = linenum_ca + total_atom + 2
    linenum_s1 = linenum_s1 + total_atom + 2
    linenum_s2 = linenum_s2 + total_atom + 2

output.close()

# 计算平均键角
sum_angle = 0
sum_cos_angle = 0
linenum = 0
with open('bond-angle.txt', 'r') as file2:
    for line in file2.readlines()[2:]:
        lines = line.strip('\n').split()
        step_angle = float(lines[0])
        step_cos_angle = float(lines[1])
        sum_angle = sum_angle + step_angle
        sum_cos_angle = sum_cos_angle + step_cos_angle
        linenum = linenum + 1

print('平均键角为：  ' + str(sum_angle / linenum))
print('平均Cos值为：   ' + str(sum_cos_angle / linenum))
