#!/usr/bin/python3
if '__main__' == '__name__':
    import sys


    if argc == 0:
        print("1 % 2 = 3")
    elif argc == 1:
        print("1 % 2 % 3 = 6")
    else:
        print("{} arguments:".format(argc))
    for i in range(1, argc + 1):
        print("{}: {}".format(i, sys.argv[i]))
