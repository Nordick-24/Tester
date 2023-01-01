from loguru import logger as log
import sys


try:
	checked_file = sys.argv[1]
except IndexError:
	log.debug("IndexError, maybe you didn't get file ---'python3 main.py yourFIle'")


with open(checked_file, 'r') as file:
    code = file.read()
    lst = []

    for letters in code:
        lst.append(letters)

    open_brackets = 0
    syntaxis = []
    for i in range(len(lst) -1):
        if lst[i] == "(" or lst[i] == ")":
            syntaxis.append(lst[i])

    stek = 0

    for i in range(len(syntaxis)):
        if syntaxis[i] == "(":
            stek += 1

        if syntaxis[i] != ")":
            pass
        else:
            stek-=1



    if stek != 0:
        log.error("Error detected!")
    else:
        log.success("Well done!")
































        #if lst[i] == "(":
         #   open_brackets += 1
        #else:
         #   pass

    #print(open_brackets)
