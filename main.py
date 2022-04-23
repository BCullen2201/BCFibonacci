from os import system

def createFibSeq():
    num01 = 0
    num02 = 1

    for i in range(0, 501):
        result = num01 + num02
        num01 = num02
        num02 = result
        print(result)

def main(): # main function, gets called at start
    createFibSeq()

while True: # infinite loop, keeps window open
    system("clear")
    createFibSeq()
    input()