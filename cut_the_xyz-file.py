#!/usr/bin/python3
# -*- coding: UTF-8 -*-

file = open('5ps-10ps.txt', 'w')
with open('test-pos-1.xyz', 'r') as tra:
    for line in tra.readlines()[524001:1048524]:
        file.write(line)
file.close()
