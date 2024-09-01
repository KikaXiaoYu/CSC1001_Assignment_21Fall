def createLockers(lockers):
    for i in range(0,100):
        lockers.append(0)

def studentGoThrough(student,lockers):
    for i in range(student,101,student):
        if lockers[i-1]:
            lockers[i-1]=0
        else:
            lockers[i-1]=1

def togetherGoThrough(lockers):
    for student in range(1,101):
        studentGoThrough(student,lockers)

def findOpenLokcers(lokcers):
    open_lockers=[]
    for i in range(0,100):
        if lokcers[i]:
            open_lockers.append(i+1)
    return open_lockers

def locker_puzzle():
    lockers = []
    for i in range(100):
        lockers.append(False)
    open_lockers=[]
    togetherGoThrough(lockers)
    open_lockers = findOpenLokcers(lockers)
    return open_lockers

if __name__ == '__main__':
    open_lockers = locker_puzzle()
    print(open_lockers)