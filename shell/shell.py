#! /usr/bin/env python3

import os, sys, re

parentPid = os.getpid()

PS1 = os.environ.get('PS1')

while True:

       if PS1 == None:
              os.environ['PS1'] = "$ "
              userCommand = input(os.environ.get('PS1'))
           
       if userCommand == "exit":
              sys.exit(1);

       processValue = os.fork()


       if processValue < 0:
              os.write(1,"The fork has failed")
              sys.exit(1)

       elif processValue == 0: #Child
              os.write(1,("\nThis is the child").encode())
              os.write(1,("\nChild's PID: %d" %os.getpid()).encode())
              os.write(1, ("\nChild is being terminated\n").encode())

              args = [userCommand,"shell.py"]
              
              for dir in re.split(":", os.environ['PATH']):

                     prDir = "%s/%s" % (dir, args[0])

                     try:
                            os.execve(prDir, args ,os.environ)

                     except FileNotFoundError:
                            pass
                     
              os.write(2, ("Child: %d Could not execute \n" %os.getpid()).encode())
              os.write(1, ("Command: %s was not found\n" % a).encode())
              sys.exit(1)


       else: #Parent
              os.write(1,("\nThis the parent").encode())
              os.write(1,("\nParent's PID: %d" %parentPid).encode())
