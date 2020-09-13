#! /usr/bin/env python3

import os, sys, time

while 1:

    parentPid = os.getpid()
    processValue = os.fork()

    os.write(1, ("Forking is being done").encode())

    
    if processValue < 0:
        os.write(1,"The fork has failed")
        sys.exit(1)
        
    elif processValue == 0:
        os.write(1,("\nThis is the child").encode())
        os.write(1,("\nChild's PID: %d" %os.getpid()).encode())
        time.sleep(1)
        os.write(1, ("\nChild is being terminated").encode())
        
    

    else:
        os.write(1,("\nThis the parent").encode())
        os.write(1,("\nParent's PID: %d" %parentPid).encode())

    print("\nEnter Y to keep going else the program will stop")
    a = input()
    a = a.lower()
    
    if a == 'y':
        continue
    else:
        break;

sys.exit(1)
