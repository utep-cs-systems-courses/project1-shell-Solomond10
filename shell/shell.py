#! /usr/bin/env python3

import os, sys, re

parentPid = os.getpid()



def getCommand():

       prompt = "$ "
       
       if "PS1" in os.environ:
              prompt = os.environ["PS1"]

       userCommand = input(prompt)

       return userCommand


while True:

       userCommand = getCommand()

       if userCommand == "exit":
              break
       
       processValue = os.fork()

       if processValue < 0:
              os.write(1,"The fork has failed")
              sys.exit(1)

       elif processValue == 0: 
              os.write(1,("\nThis is the child").encode())
              os.write(1,("\nChild's PID: %d" %os.getpid()).encode())
              os.write(1, ("\nChild is being terminated\n").encode())

              #args = [userCommand,"shell.py"]
              #a2 = "/bin/sh/" #originally
              #userCommand = "/bin/"+userCommand 
              #print(userCommand)
              
              f = "shell.py"
              args = [userCommand, f]

              os.close(1)                 # redirect child's stdout
              os.open("outputFile.txt", os.O_CREAT | os.O_WRONLY);
              os.set_inheritable(1, True)
              
              for dir in re.split(":", os.environ['PATH']):

                     prDir = "%s/%s" % (dir, args[0])

                     try:
                            os.execve(prDir, args ,os.environ)

                     except FileNotFoundError:
                            pass
                     
              os.write(2, ("\nChild: %d Could not execute \n" %os.getpid()).encode())
              os.write(1, ("Command: %s was not found\n" %userCommand).encode())
              sys.exit(1)


       else: #Parent
              os.write(1,("\nThis is the parent. My pid is %d\n"%parentPid).encode())
              childPid = os.wait()
              os.write(1, ("From Parent: Child %d was terminated with exit code %d\n" %childPid).encode())
