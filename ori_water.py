#!/usr/bin/python3
# -*- coding: UTF-8 -*-
### 计算MD中单个水分子的朝向。written by Hao Cao ###
import numpy as np
import linecache


O_num = input('请输入O原子序号: ')
H1_num = input('请输入H1原子序号: ')
H2_num = input('请输入H2原子序号: ')
file1 = open('5ps-10ps.xyz', 'r')
output = open('ori_water.txt', 'w')
linenum_1 = int(O_num) + 2  # O原子所在行数
linenum_2 = int(H1_num) + 2  # 第一个H原子所在行数
linenum_3 = int(H2_num) + 2 # 第二个H原子所在行数
total_atom = int(linecache.getline('5ps-10ps.xyz', 1))  # 总原子数

def f(x, y, z):
    xyz_O = linecache.getline('5ps-10ps.xyz', x).strip('\n').split()  # 读取目标行
    xyz_O.pop(0)  # 去掉元素项
    f_O = []
    for i in xyz_O:  # 转化成列表
        f_O.append(float(i))
    xyz_H1 = linecache.getline('5ps-10ps.xyz', y).strip('\n').split()
    xyz_H1.pop(0)
    f_H1 = []
    for i in xyz_H1:
        f_H1.append(float(i))
    xyz_H2 = linecache.getline('5ps-10ps.xyz', z).strip('\n').split()
    xyz_H2.pop(0)
    f_H2 = []
    for i in xyz_H2:
        f_H2.append(float(i))
    a1 = np.array(f_O)
    a2 = np.array(f_H1)
    a3 = np.array(f_H2)
    bond1 = a1 - a2
    bond2 = a1 - a3
    bond_dis = bond1 + bond2     # 角平分线向量12
    z_xl = np.array([0, 0, 1])  # z方向法向量
    cos = bond_dis.dot(z_xl) / (np.sqrt(bond_dis.dot(bond_dis)) * np.sqrt((z_xl.dot(z_xl))))
    angle = np.arccos(cos) * 180 / np.pi
    output.write(str(angle) + '\n')


while linecache.getline('5ps-10ps.xyz', linenum_1) != '':
    f(linenum_1, linenum_2, linenum_3)
    linenum_1 = linenum_1 + total_atom + 2
    linenum_2 = linenum_2 + total_atom + 2
    linenum_3 = linenum_3 + total_atom + 2

output.close()

# 计算平均夹角
sum_angle = 0
times = 0
with open('ori_water.txt') as file2:
    for line in file2.readlines():
        lines = line.strip('\n').split()
        num = float(lines[0])
        sum_angle = num + sum_angle
        times = times + 1

print('平均夹角为： ' + str(sum_angle/times))