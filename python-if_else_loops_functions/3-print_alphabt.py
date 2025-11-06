#!/usr/bin/python3


for ascii in range(97, 123):
    res = chr(ascii)
    if ascii == (113,101):
        continue
    print("{}".format(res), end="")
