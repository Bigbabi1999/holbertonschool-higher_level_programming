#!/usr/bin/python3
#include<stdio.h>
def uppercase(str):
    for ch in str:
        if ord(ch) >= 65 and ord(ch) <= 90:
            print("{}".format(ch), end="")
            print()
