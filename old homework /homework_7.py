import datetime 
import os
import time

#def clearscreen():
   # os.system('cls' if os.name == 'nt' else 'clear; date; cal')
def clearscreen():
    clear=lambda:os.system("cls")
    clear()

def translate(text): 
    text=str(text)
    letters=[]
    for letter in text:
        letters.append(NUMBERS[letter])
    #print(letters)
    for elem in letters:
        print(elem, sep="")

NUMBERS={
"1":u"""
  ■
■ ■
  ■
  ■
■ ■ ■""",
"2":u"""
■ ■ ■
    ■
■ ■ ■
■
■ ■ ■ """,
"3":u"""
■ ■ ■
    ■
■ ■ ■
    ■
■ ■ ■""",
"4":u"""
■   ■
■   ■
■ ■ ■
    ■
    ■""",
"5":u"""
■ ■ ■
■
■ ■ ■
    ■
■ ■ ■""",
"6":u"""
■ ■ ■
■
■ ■ ■
■   ■
■ ■ ■""",
"7":u"""
■ ■ ■
    ■
    ■
    ■
    ■""",
"8":u"""
■ ■ ■
■   ■
■ ■ ■
■   ■
■ ■ ■""",
"9":u"""
■ ■ ■
■   ■
■ ■ ■
    ■
■ ■ ■""",
"0":u"""
■ ■ ■
■   ■
■   ■
■   ■
■ ■ ■""",
":":u"""

  ■    

  ■
  """}

while True:
    time.sleep(1)
   # clearscreen()
    translate(str((datetime.datetime.now()).strftime("%H:%M:%S")))

