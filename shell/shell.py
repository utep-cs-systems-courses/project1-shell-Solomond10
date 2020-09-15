#! /usr/bin/env python3

import os, sys, re

#parentPid = os.getpid()
#export PS1
#= "$ "

while True:

       args = ["random", "shell.py"]
       PS1 =  os.environ.get('PS1')

       if(PS1 == None):
              PS1 = input("$ ")
       else:
             # print("PS1 is not empty")

              userCommand = input()
              
              if(userCommand == "exit"):

                     sys.exit(1);

              processValue = os.fork()

              if processValue < 0:
                     os.write(1,"The fork has failed")
                     sys.exit(1)

              elif processValue == 0:
                     os.write(1,("\nThis is the child").encode())
                     os.write(1,("\nChild's PID: %d" %os.getpid()).encode())
                     os.write(1, ("\nChild is being terminated").encode())
                                   #print("PS1 is empty")
                     for dir in re.split(":", os.environ['PATH']):


                            prDir = "%s/%s" % (dir, args[0])

                            #print(prDir)
                            try:
                                   os.execve(prDir, args ,os.environ)

                            except FileNotFoundError:
                                   pass

              else:
                     os.write(1,("\nThis the parent").encode())
                     os.write(1,("\nParent's PID: %d" %parentPid).encode())
   
#print(" THE END ")
