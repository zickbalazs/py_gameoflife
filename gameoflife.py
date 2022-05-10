import time
from colorama import Fore, Back, Style
from random import randint
from os import system
from checkers import *
def _g():
    return randint(0,1) 
def Row():
    row = []
    for item in range(20):
        row.append(randint(0,1))
    return row
def DisplayTable():
    for row in table:
        line = ""
        for col in row:
            if col==1:
                line+=Fore.RED+Back.RED+"-"
            else:
                line+=Fore.BLACK+Back.BLACK+"-"
        print(line)
    print(Style.RESET_ALL)
table = [
    Row(),
    Row(),
    Row(),
    Row(),
    Row(),
    Row(),
    Row(),
    Row(),
    Row(),
    Row(),
    Row(),
    Row()
]
def NextGen():
    for i in range(0, len(table)):
        for g in range(0, len(table[i])):
            balhatar = False
            jobbhatar = False
            fenthatar = False
            alulhatar = False
            if i==0:
                fenthatar = True
            elif i==len(table)-1:
                alulhatar = True
            if g==0:
                balhatar = True
            elif g==len(table[i])-1:
                jobbhatar = True
            if balhatar:
                if fenthatar:
                    BFCount()
                elif alulhatar:
                    BACount()
                else:
                    BCount()
            elif jobbhatar:
                if fenthatar:
                    JFCount()
                elif alulhatar:
                    JACount()
                else:
                    JCount()
            else:
                if fenthatar:
                    FCount()
                elif alulhatar:
                    ACount()
                else: 
                    Count()


system('cls')
NextGen()
DisplayTable()