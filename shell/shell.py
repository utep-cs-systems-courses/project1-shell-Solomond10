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
              #sys.exit(1);
              break
       
       processValue = os.fork()

       cl = userCommand.split() 

       if len(cl) == 2:

              cmd = cl[0]
              p = cl[1]

              #print (cmd)
              #print (p)
       
              if cmd == "cd":
                     os.chdir(p)

       print(os.getcwd())

       if processValue < 0:
              os.write(1,"The fork has failed")
              sys.exit(1)

       elif processValue == 0: 
       #       os.write(1,("\nThis is the child").encode())
       #       os.write(1,("\nChild's PID: %d" %os.getpid()).encode())
       #       os.write(1, ("\nChild is being terminated\n").encode())

              #args = [userCommand,"shell.py"]
              #a2 = "/bin/sh/" #originally
              a2 = "shell.py"
              #userCommand = "/bin/"+userCommand 
              #print(userCommand)
              args = [userCommand, a2]
              
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

'''def getCommand():

       prompt = "$ "
       
       if "PS1" in os.environ:
              prompt = os.environ["PS1"]

       userCommand = input(prompt)

       return userCommand

#       if userCommand == "exit":
 #             sys.exit(1);
'''
