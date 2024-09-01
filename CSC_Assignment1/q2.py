a=int(input("Enter an integer:"))
if a<0:
    a=-a
w=10
n=0
while a>=w:
    n+=1
    w*=10
for b in range(n,-1,-1):
    c=a//10**b
    print (c)
    a=a-c*10**b
    
