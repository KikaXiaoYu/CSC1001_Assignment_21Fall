def isPrime(number):
    t=1
    for i in range(2,number):
        if number%i==0:
            t=0
            break
    if t==1:
        return True
    else:
        return False

def reverseNumber(number):
    number=str(number)
    reverseNumber=str()
    for i in range(len(number)-1,-1,-1):
        reverseNumber+=(number[i])
    return int(reverseNumber)

def saveEmirp():
    n=0
    number=10
    Emirps=list()
    while n<100:
        if isPrime(number) and isPrime(reverseNumber(number)) and number!=reverseNumber(number):
            Emirps.append(number)
            n+=1
        number+=1
    return Emirps

def printEmirp(Emirps):
    for i in range(0,100):
        print ("%5i"%Emirps[i],end="")
        if (i+1)%10==0:
            print("")

def emirps_100():
    printEmirp(saveEmirp())
   
if __name__ == '__main__':
    emirps_100()