#! /usr/bin/env python3

import os, sys

while 1:

    parentPid = os.getpid()
    processValue = os.fork()

    if processValue == 0:
        print("This is the child")
        print("Child's PID: ", os.getpid())
        sys.exit(1)
    else:
        print("This the parent")
        print("Parent's PID: ", parentPid)

    print("Enter Y to keep going else the program will stop")
    a = input()
    a = a.lower()
    
    if a == 'y':
        continue
    else:
        break;
