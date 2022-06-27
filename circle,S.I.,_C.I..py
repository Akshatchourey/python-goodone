'''#Program to fnd area of circle.
pi=3.14
r=float(input("the radious ="))
area=pi*r*r
print("area of circle=",area)



#Program to print the simple intrest.
P=float(input("\n\nthe principle tou taken"))
I=float(input("rate of intrest"))
T=5
Simple_intrest=P*I*T/100
Amount=P+Simple_intrest
print("the simple intrest is",Simple_intrest)
print("the amount to summit is",Amount)'''


#Program to print the commpoand intrest.
a=float(input("enter the value of investment."))
r=float(input("enter the value of intrest rate."))
t=int(input("enter the duration of tine."))
n=int(input("no of times intrest is compounded per unit time."))
p=a*(1+r/n)**(n*t)
print("the totle amount is =",p)

