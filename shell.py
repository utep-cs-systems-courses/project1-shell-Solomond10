#! /usr/bin/env python3

import os, sys, re

parentPid = os.getpid()
prompt = "$ "

while True:

    userCommand = input(prompt)
    
    if(userCommand == "exit"):
        break;

    processValue = os.fork()

    if processValue < 0:
        os.write(1,"The fork has failed")
        sys.exit(1)

    elif processValue == 0:
        os.write(1,("\nThis is the child").encode())
        os.write(1,("\nChild's PID: %d" %os.getpid()).encode())
        time.sleep(1)
        os.write(1, ("\nChild is being terminated").encode())
        path = "~/OS/Lab2?project1-shell-Solomond10"
        os.execve(path,userCommand,os.environ)
    else:
        os.write(1,("\nThis the parent").encode())
        os.write(1,("\nParent's PID: %d" %parentPid).encode())

   # if child > 0:
    #    print()
    #else: child == 0:
    
    #os.execve(userCommand)
    
print(" THE END ")
