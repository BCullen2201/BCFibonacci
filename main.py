from os import system

def main():
    def createFibSeq():
        num01 = 0
        num02 = 1

        for i in range(0, 501):
            result = num01 + num02
            num01 = num02
            num02 = result
            print(result)

    system("clear")
    createFibSeq()

if __name__ == "__main__":
    main()