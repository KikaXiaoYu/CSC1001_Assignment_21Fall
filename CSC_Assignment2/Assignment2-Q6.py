import random


def printTotal(list_total):
    for n in range(0, 8):
        for i in range(0, 8):
            print("|", list_total[n][i], sep="", end="")
        print("|")


def createListLine():
    list_line = list()
    for i in range(0, 8):
        list_line.append(" ")
    return list_line


def createListTotal(list_total):
    for i in range(0, 8):
        list_total.append(createListLine())


def letRandom():
    list_number = list()
    while len(list_number) < 8:
        add = random.randint(1, 8)
        if list_number.count(add) == 0:
            list_number.append(add)
    return list_number


def placeRandom(list_total, list_number):
    for i in range(0, 8):
        list_total[i][list_number[i]-1] = "Q"


def isValid(list_number):
    for i in range(0, 8):
        for j in range(0, 8):
            if j != i:
                a = list_number[i]+i+1
                b = list_number[j]+j+1
                c = list_number[i]-i-1
                d = list_number[j]-j-1
                if a != b and c != d:
                    result = 1
                else:
                    return False
    return result


def eight_queens():
    while True:
        list_number = letRandom()
        if isValid(list_number):
            list_total = list()
            createListTotal(list_total)
            placeRandom(list_total, list_number)
            printTotal(list_total)
            break


if __name__ == "__main__":
    eight_queens()
