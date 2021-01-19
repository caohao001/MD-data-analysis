#!/usr/bin/python3
# -*- coding: UTF-8 -*-
###################### 统计每帧H键数目 ##########################
import linecache
import numpy as np

atom_num = int(linecache.getline('5ps-10ps.xyz', 1))
O1 = int(input('O原子序号1：  '))
O2 = int(input('O原子序号2：  '))
output = open('H-bond.txt', 'w')
line_num_1 = 1
line_num_2 = line_num_1 + atom_num + 1


def cal_H_bond(x, y):
    H_bond_num = 0
    with open('5ps-10ps.xyz', 'r') as file:
        for lineO in file.readlines()[x:y]:
            lines = lineO.strip('\n').split()
            O1_num = O1 + x + 1
            O2_num = O2 + x + 1
            O1_xyz = linecache.getline('5ps-10ps.xyz', O1_num).strip('\n').split()
            O1_xyz.pop(0)
            O1_list = []
            for i in O1_xyz:
                O1_list.append(float(i))
            O1_np = np.array(O1_list)
            O2_xyz = linecache.getline('5ps-10ps.xyz', O2_num).strip('\n').split()
            O2_xyz.pop(0)
            O2_list = []
            for i in O2_xyz:
                O2_list.append(float(i))
            O2_np = np.array(O2_list)
            if lines[0] == 'H':
                lines.pop(0)
                H_xyz = lines
                H_list = []
                for i in H_xyz:
                    H_list.append(float(i))
                H_np = np.array(H_list)
                bond1 = H_np - O1_np
                bond2 = H_np - O2_np
                H_bond1 = np.sqrt((bond1 * bond1).sum())
                H_bond2 = np.sqrt((bond2 * bond2).sum())
                if H_bond1 < 2.2 or H_bond2 < 2.2:               #####  氢键键长判断
                    with open('5ps-10ps.xyz', 'r') as file_O:
                        for line in file_O.readlines()[x:y]:
                            lines_O = line.strip('\n').split()
                            if lines_O[0] == 'O':
                                lines_O.pop(0)
                                O_xyz = lines_O
                                O_list = []
                                for i in O_xyz:
                                    O_list.append(float(i))
                                O_np = np.array(O_list)
                                OH_bond = H_np - O_np
                                OH_bond_length = np.sqrt((OH_bond * OH_bond).sum())
                                if OH_bond_length < 1.2:
                                    O_O_bond1 = O1_np - O_np
                                    O_O_bond2 = O2_np - O_np
                                    if np.sqrt((O_O_bond1 * O_O_bond1).sum()) < np.sqrt((O_O_bond2 * O_O_bond2).sum()):
                                        bian_1 = O_O_bond1
                                        bian_2 = OH_bond
                                        L1 = np.sqrt(bian_1.dot(bian_1))
                                        L2 = np.sqrt(bian_2.dot(bian_2))
                                        cos_angle = bian_1.dot(bian_2) / (L1 * L2)
                                        angle = np.arccos(cos_angle) * 360 / 2 / np.pi
                                        if angle < 20:                     ##### 氢键键角判断
                                            H_bond_num = H_bond_num + 1
                                    elif np.sqrt((O_O_bond1 * O_O_bond1).sum()) > np.sqrt((O_O_bond2 * O_O_bond2).sum()):
                                        bian_1 = O_O_bond2
                                        bian_2 = OH_bond
                                        L1 = np.sqrt(bian_1.dot(bian_1))
                                        L2 = np.sqrt(bian_2.dot(bian_2))
                                        cos_angle = bian_1.dot(bian_2) / (L1 * L2)
                                        angle = np.arccos(cos_angle) * 360 / 2 / np.pi
                                        if angle < 20:
                                            H_bond_num = H_bond_num + 1
        output.write(str(H_bond_num) + '\n')


while linecache.getline('5ps-10ps.xyz', line_num_1) != '':
    cal_H_bond(line_num_1, line_num_2)
    line_num_1 = line_num_1 + atom_num + 2
    line_num_2 = line_num_2 + atom_num + 2
output.close()


linenum = 0
sum_H_bond = 0
with open('H-bond.txt') as file2:
    for line in file2.readlines():
        lines = line.strip('\n').split()
        num = float(lines[0])
        sum_H_bond = sum_H_bond + num
        linenum = linenum + 1
print('平均氢键数目为： ' + str(sum_H_bond / linenum))
