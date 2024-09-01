def getDigit(number):
    if 0<=number<10:
        return number
    else:
        realnumber=int()
        number=str(number)
        for i in number:
            realnumber+=int(i)
        return realnumber

def sumOfDoubleEvenPlace(number):
    number=str(number)
    sum=int()
    for i in range(len(number)-2,-1,-2):
        sum+=getDigit(int(number[i])*2)
    return sum

def sumOfOddPlace(number):
    number=str(number)
    sum=int()
    for i in range(len(number)-1,-1,-2):
        sum+=int(number[i])
    return sum

def isValid(number):
    if (sumOfDoubleEvenPlace(number)+sumOfOddPlace(number))%10==0 and 13<=len(str(number))<=16 and str(number)[0] in ["4","5","37","6"]:
        return True
    else:
        return False

if __name__ == '__main__':
    ans1 = isValid(4388576018402626)
    ans2 = isValid(4388576018410707)