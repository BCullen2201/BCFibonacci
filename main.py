from os import system

def createFibSeq():
    num01 = 0
    num02 = 1

    x = input("How many numbers do you want to see?: ")

    for i in range(0, int(x)):
        result = num01 + num02
        num01 = num02
        num02 = result
        print(result)

def main():
    system("clear")
    createFibSeq()

if __name__ == "__main__":
    main()
