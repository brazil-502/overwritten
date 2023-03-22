#overwritter
#developer: brazil_502
#version: 1.0

import os
import time

print("""\
           ___                               _ _   _                     
          /___\__   _____ _ ____      ___ __(_) |_| |_ ___ _ __          
 _____   //  //\ \ / / _ \ '__\ \ /\ / / '__| | __| __/ _ \ '_ \   _____ 
|_____| / \_//  \ V /  __/ |   \ V  V /| |  | | |_| ||  __/ | | | |_____|
        \___/    \_/ \___|_|    \_/\_/ |_|  |_|\__|\__\___|_| |_|        """)

print("developer(s): brazil_502")

path = input("the file name:- ")

if os.path.exists(path):
    print("that file exists!")
    time.sleep(0.1)
    print("reading file.")
    time.sleep(0.1)
    print("reading file..")
    time.sleep(0.1)
    print("reading file...")
    time.sleep(0.1)
    print("reading file..")
    time.sleep(0.1)
    print("reading file.")
    time.sleep(0.1)
    print("reading file..")
    time.sleep(0.1)
    print("reading file...")
    time.sleep(0.1)
    print("- FILE CONTENTS -")
elif os.path.isdir(path):
           print("that is a directory!")
              
else:
    print("that file does not exist")

try:
    with open(path) as file:
        print(file.read())
        print("- - - - - -")
except FileNotFoundError:
    print(" ")

if os.path.exists(path):
    with open(path, 'w') as file:
        file.write(input("enter the override:- "))
        print("overwriting.")
        time.sleep(0.1)
        print("overwriting..")
        time.sleep(0.1)
        print("overwriting...")
        time.sleep(0.1)
        print("overwriting..")
        time.sleep(0.1)
        print("overwriting.")
        time.sleep(0.1)
        print("overwriting..")
        time.sleep(0.1)
        print("overwriting...")
        time.sleep(0.1)
        print("Done!")


