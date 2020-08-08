# andres owens 58449528 and berkeley nguyen 50314922. ics 32.
# project 1

import os
import shutil
from pathlib import Path

#----------line 1----------
def directory_check():
    '''will check if input is valid file directory. if so, continue
    into said directory. if not, display error message and allow user
    to re-enter valid directory. continues until valid directory is
    inputted.'''
    while directory_check != ():
        p = Path(input())
        if p.exists():
            return p
            break
        else:
            print("ERROR")
            
#----------line 2----------
def characteristics(p, a):
    '''takes in files and takes into account appropriate characteristic or
    action'''
    if searchtype[0] == 'N':
        if searchtype[2:] == p.name:
            actions(p, a)
            
    elif searchtype[0] == 'E':
        if searchtype[2:] == p.suffix or searchtype[2:] == p.suffix[1:]:
            actions(p, a)
            
    elif searchtype[0] == 'S':
        if int(searchtype[2:]) < p.stat().st_size:
            actions(p, a)

    else:
        print('ERROR')


#----------line 3----------
def actions(p, action):
    '''function takes in path and executes specific actions'''
    if action == 'P':
        print(str(p))
    elif action == 'F':
        print(str(p))
        file = open(str(p), 'r')
        print(file.readline())
        file.close()
    elif action == 'D':
        print(str(p))
        shutil.copy2(str(p), str(p) + ".dup")
    elif action == 'T':
        print(str(p))
        os.utime(str(p), None)
 

def actiontype():
    action = input()
    while action != 'P' and action != 'F' and action != 'D' and action != 'T':
        print('ERROR')
        action = input()
    return action


#----------Recursion FUNC----------
def dir_or_file(p, a):
    '''function goes through path by path and checks entire directory
    to check for subdirectories and files'''
    for p in p.iterdir():
        if p.is_dir():
            dir_or_file(p, a)
        else:
            characteristics(p, a)



############################
#######Function Calls#######
p = directory_check()

searchtype = input()
while searchtype[0] != 'N' and searchtype[0] != 'E' and searchtype[0] != 'S':
    print('ERROR')
    searchtype = input()
    
a = actiontype()

dir_or_file(p, a)













