t=0

while t==0:
    try:
        a=eval(input("Enter the final account value:"))
    except:
        a=-1
    if a>0:
        t+=1
    else:
        print("Please enter a positive number!")

while t==1:
     try:
        b=eval(input("Enter the annual interest rate:"))
     except:
        b=-1
     if b>0:
        t+=1
     else:
        print("Please enter a positive number!")

while t==2:
     try:
        c=eval(input("Enter the number of years:"))
     except:
        c=-1
     if c>0:
        t+=1
     else:
        print("Please enter a positive number!")

d=a/(1+b*0.01)**c
print ("The initial value is:",d)
