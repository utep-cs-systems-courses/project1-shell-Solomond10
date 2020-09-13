#! /usr/bin/env python3

import os, sys, re

prompt = "$ "

while True:

    userCommand = input(prompt)
    
    if(userCommand == "exit"):
        break;

    #os.fork()
    
    #os.execve(userCommand)
    
print(" THE END ")
