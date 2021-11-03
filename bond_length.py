#!/usr/bin/python3
# -*- coding: UTF-8 -*-
### Written by Hao Cao ###
import linecache
import numpy as np

ele_1 = input('请输入原子序号1：')  # 输入需要计算的原子序号
ele_2 = input('请输入原子序号2：')
file1 = open('test-pos-1.xyz', 'r')
output = open('bond-length.txt', 'w')
linenum_1 = int(ele_1) + 2  # 第一个原子所在行数
linenum_2 = int(ele_2) + 2  # 第二个原子所在行数
total_atom = int(linecache.getline('test-pos-1.xyz', 1))  # 总原子数

def f(x, y):
    xyz_1 = linecache.getline('test-pos-1.xyz', x).strip('\n').split()  # 读取目标行
    xyz_1.pop(0)  # 去掉每行元素项
    f_1 = []
    for i in xyz_1:
        f_1.append(float(i))
    xyz_2 = linecache.getline('test-pos-1.xyz', y).strip('\n').split()
    xyz_2.pop(0)
    f_2 = []
    for i in xyz_2:
        f_2.append(float(i))
    a1 = np.array(f_1)
    a2 = np.array(f_2)
    bond = a1 - a2
    bond_length = np.sqrt((bond * bond).sum())  # 计算键长
    output.write(str(bond_length) + '\n')


while linecache.getline('test-pos-1.xyz', linenum_1) != '':
    f(linenum_1, linenum_2)
    linenum_1 = linenum_1 + total_atom + 2
    linenum_2 = linenum_2 + total_atom + 2

output.close()

# 计算平均键长
sum_bond_length = 0
linenum = 0
with open('bond-length.txt') as file2:
    for line in file2.readlines():
        lines = line.strip('\n').split()
        num = float(lines[0])
        sum_bond_length = num + sum_bond_length
        linenum = linenum + 1

print('平均键长为： ' + str(sum_bond_length/linenum))
