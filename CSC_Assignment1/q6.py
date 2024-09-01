tri=-1
while tri==-1:
    try:
         tri=input("Enter a trigonometric function (sin, cos, tan):")
    except:
        tri=-1
    if tri!="sin" and tri!="cos" and tri!="tan":
      print("Invalid input!")
      tri=-1

p=-1
while p==-1:
    try:
        a=eval(input("Enter lower bound a:"))
        p=1
    except:
        p=-1
        print("Invalid input!")

p=-1
while p==-1:
    try:
        b=eval(input("Enter higher bound b:"))
        if b>a:
            p=1
        else:
            p=-1
            print("Invalid input!")
    except:
        p=-1
        print("Invalid input!")

n=-1
while n<=0:
    try:
        n=int(input("Enter the number of sub-intervals n:"))
    except:
        n=-1
    if n<=0:
        print("Invalid input!")

from math import sin
from math import cos
from math import tan
sum=0
if tri=="sin":
    for i in range(1,n+1):
        sum+=(b-a)/n*sin(a+(b-a)/n*(i-1/2))
if tri=="cos":
    for i in range(1,n+1):
        sum+=(b-a)/n*cos(a+(b-a)/n*(i-1/2))
if tri=="tan":
    for i in range(1,n+1):
        sum+=(b-a)/n*tan(a+(b-a)/n*(i-1/2))
print(sum)