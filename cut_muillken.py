#!/usr/bin/python3
# -*- coding: UTF-8 -*-
file = open('charge', 'w')
with open('CHARGE.mulliken', 'r') as tra:
    for line in tra.readlines()[1:835263]:
        file.write(line)
file.close()