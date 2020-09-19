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

       cmdLine = userCommand.split()
       
       if "exit" == cmdLine[0]:
              break

       if "cd" == cmdLine[0]:
              directory = "/"+cmdLine[1]
              path = os.getcwd()
              os.chdir(path+directory)
              print("Old path: ",path)
              print("New path: ",os.getcwd())
              continue
                     
       if len(cmdLine) is 1:
              cmd = cmdLine
       else:
              cmd = cmdLine[0]
       
       processValue = os.fork()

       if processValue < 0:
              os.write(1,"The fork has failed")
              sys.exit(1)

       elif processValue == 0: 
              os.write(1,("\nThis is the child").encode())
              os.write(1,("\nChild's PID: %d" %os.getpid()).encode())
              os.write(1, ("\nChild is being terminated\n\n").encode())

              if len(cmdLine) != 1:
                     #Checks to see if string is a file
                     try:
                            fileName = cmdLine[len(cmdLine)-1]
                            with open(fileName) as inputFile:
                                   if '' in inputFile.read():
                                          #print(inputFile)
                                          args = [cmd, fileName]

                     except FileNotFoundError:
                            print("File wasn't found")
              else:
                     args = cmd
   
              if '>' in cmdLine:

                     os.close(1)                 # redirect child's output
                     os.open(cmdLine[2], os.O_CREAT | os.O_WRONLY);
                     os.set_inheritable(1, True)

              elif '<' in cmdLine: #redirect's child input

                     fName = cmdLine[1]
                     with open(fName) as irFile:
                            line = (irFile.read()).strip()
                            c = line.split()
                            args = [ c[0], c[1] ]

              for dir in re.split(":", os.environ['PATH']):

                     prDir = "%s/%s" % (dir, args[0])

                     try:
                            os.execve(prDir, args ,os.environ)

                     except:
                            pass
                     
              os.write(2, ("\nChild: %d Could not execute \n" %os.getpid()).encode())
              os.write(1, ("Command: %s was not found\n" %userCommand).encode())
              sys.exit(1)

       #Parent
       else:
              os.write(1,("\nThis is the parent. My pid is %d\n"%parentPid).encode())
              childPid = os.wait()
              os.write(1, ("\nFrom Parent: Child %d was terminated with exit code %d\n" %childPid).encode())
