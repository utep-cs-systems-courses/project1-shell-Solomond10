#! /usr/bin/env python3

import os, sys, re

parentPid = os.getpid()

PS1 =  os.environ.get('$PS1')

while True:

       #args = ["random", "shell.py"]
       
       #print(PS1)

       if( PS1 == None):
              a = input("$ ")
        #      sys.ps1 = "$ "

       #a = input("$ ")
              
       if( PS1 == "exit"):
              sys.exit(1);

       processValue = os.fork()


       if processValue < 0:
              os.write(1,"The fork has failed")
              sys.exit(1)

       elif processValue == 0: #Child
              os.write(1,("\nThis is the child").encode())
              os.write(1,("\nChild's PID: %d" %os.getpid()).encode())
              os.write(1, ("\nChild is being terminated\n").encode())
              #print("PS1 is empty")
              args = [a,"shell.py"]
              
              for dir in re.split(":", os.environ['PATH']):

                     prDir = "%s/%s" % (dir, args[0])

                     try:
                            os.execve(prDir, args ,os.environ)

                     except FileNotFoundError:
                            pass
                     
              os.write(2, ("Child:    Could not execute %s\n" % args[0]).encode())
              sys.exit(1)


       else: #Parent
              os.write(1,("\nThis the parent").encode())
              os.write(1,("\nParent's PID: %d" %parentPid).encode())

       #PS1 = None
       
       #sys.exit(1)
#              else:
 #                    os.write(1,("Parent: Child %d has been terminated with the exit code %d",os.getPid()))
#print(" THE END ")
