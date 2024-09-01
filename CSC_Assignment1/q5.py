N=-1
while N<=0:
    try:
        N=int(input("PLease enter a positive integer:"))
    except:
        N=-1
    if N<=0:
        print("Invalid input!")
print("The prime numbers smaller than %d include:"%(N))
m=2
n=0
while m<N:
    t=0
    for a in range(2,m):
        if m%a==0:
            t+=1
            break
    if t==0:
        print (m,end="\t")
        n+=1
        if n==8:
            n=0
            print()
    m=m+1
            
