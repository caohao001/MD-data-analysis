#!/usr/bin/python3
# -*- coding: UTF-8 -*-
############## 原子距离表面Z坐标的距离 ###########################
import linecache
output = open('z-coordinate', 'w')
total_num = int(linecache.getline('test-pos-1.xyz', 1))
ion = int(input('请输入原子序号：   '))
num_init = 1
num_end = num_init + total_num + 1
total_z = 0
times = 0
def surf_z(x, y):
    total_Cz = 0
    with open('test-pos-1.xyz', 'r') as file:
        for line in file.readlines()[x:y]:
            lines = line.strip('\n').split()
            if lines[0] == 'C' or lines[0] == 'N' or lines[0] == 'Fe':
                z_coor = float(lines[3])
                total_Cz = z_coor + total_Cz
    global z_surface
    z_surface = total_Cz / 95

def atom_z(x,y):
    line = linecache.getline('test-pos-1.xyz', x + ion + 1)
    lines = line.strip('\n').split()
    print(lines)
    global z_coordinate
    z_coordinate = float(lines[3])



while linecache.getline('test-pos-1.xyz', num_init) != '':
    surf_z(num_init, num_end)
    atom_z(num_init, num_end)
    z_surf_atom = z_coordinate - z_surface
    total_z = z_surf_atom + total_z
    times = times + 1
    num_init = num_init + total_num + 2
    num_end = num_end + total_num + 2
    output.write(str(z_surf_atom) + '\n')
aver_init = str(total_z / times)
print('平均坐标为： ' + aver_init)

