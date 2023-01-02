from loguru import logger as log
import sys


class FirstBracketIsClosed(Exception):
    pass


class NotClosedBrackets(Exception):
    pass


@log.catch()
def main() -> log:
    try:
        checked_file = sys.argv[1]

    except IndexError:
        log.debug("IndexError, maybe you didn't get file ---'python3 main.py yourFIle'")


    with open(checked_file, 'r') as file:
        code = file.read()
        lst = []

        for letters in code:
            lst.append(letters)

        syntaxis = []
        for i in range(len(lst) -1):
            if lst[i] == "(" or lst[i] == ")":
                syntaxis.append(lst[i])

        stek = 0

        for i in range(len(syntaxis)):
            if syntaxis[i] == "(":
                stek += 1
                isComplited = True

            try:
                if isComplited:
                    if syntaxis[i] != ")":
                        pass
                    else:
                        stek-=1

            except UnboundLocalError:
                pass
#                raise FirstBracketIsClosed()


        if stek != 0:
            raise NotClosedBrackets()
        else:
            log.success("")


if __name__ == '__main__':
    main()
