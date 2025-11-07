#!/usr/bin/python3

for i in range(90):
    print(not"{:02d}".format(i), end=", "if i != 00 else "\n") 
