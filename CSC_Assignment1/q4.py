N=-1
while N<=0:
    try:
        N=int(input("PLease enter a positive integer:"))
    except:
        N=-1
    if N<=0:
        print("Invalid input!")

print ("%-8s"%"m","%-8s"%"m+1","%-8s"%"m**(m+1)")
for m in range(1,N+1):
    print ("%-8d"%m,"%-8d"%(m+1),"%-8d"%m**(m+1))