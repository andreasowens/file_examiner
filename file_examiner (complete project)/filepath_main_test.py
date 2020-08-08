# andres owens 58449528 and berkeley nguyen 50314922. ics 32.
# project 1

import os

def directory_check():
    '''will check if input is valid file directory. if so, continue
    into said directory. if not, display error message and allow user
    to re-enter valid directory. continues until valid directory is
    inputted.'''
    directory = ''
    while directory_check != ():
        directory = input()
        if os.path.isdir(directory):
            break
        else:
            print("ERROR")
directory_check()



def characteristics_check():
    '''has 3 levels of checking. if input is N, checks if rest of input
    is filename, if input is E, takes rest of input and checks for all
    files with same extension, if input is S, takes rest of input and
    checks for files of larger size (in bytes)'''
    while characteristics_check != ():
        searchtype = input()
        if searchtype[0] == "N":
            os.path.exists(searchtype[2:-1])
            print("1")
        elif searchtype[0] == "E":
            print("2")
        elif searchtype[0] == "S":
            print("3")
        else:
            print("ERROR")
characteristics_check()

#action = input()
