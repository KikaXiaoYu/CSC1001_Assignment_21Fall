def HanoiTower(n):
    list1=[(n,0,2,1)]
    signal=["A","B","C"]
    while len(list1)!=0:
            a,b,c,d=list1.pop()
            if a==1:
                print("%s --> %s"%(signal[b],signal[c]))
            else:
                list1.append((a-1,d,c,b))
                list1.append((1,b,c,d))
                list1.append((a-1,b,d,c))

def main():
    n = input("Please input the number n:")
    try:
        n = int(n)
        if n <= 0:
            print("Invalid input!")
            return
    except:
        print("Invalid input!")
        return
    HanoiTower(n)

main()
