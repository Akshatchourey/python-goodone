#Program to fnd area of circle.
z=input("press 1 to acess Area of circle\n2 for S.I.\n3 for C.I.")

if(z==1):
    pi=3.14
    r=float(input("the radious ="))
    area=pi*r*r
    print("area of circle=",area)


elif(z==2):
    #Program to print the simple intrest.
    P=float(input("\n\nthe principle tou taken"))
    I=float(input("rate of intrest"))
    T=5
    Simple_intrest=P*I*T/100
    Amount=P+Simple_intrest
    print("the simple intrest is",Simple_intrest)
    print("the amount to summit is",Amount)

else:
    #Program to print the commpoand intrest.
    p=float(input("enter the value of PRINCIPAL."))
    r=float(input("enter the value of intrest RATE."))
    n=int(input("enter the duration of TIME."))
    c=(r/100)+1
    u=(c**n)-1
    ci=u*p

    print("the totle amount is =",ci)

input("press enter to exit")
