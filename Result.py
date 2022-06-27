y=int(input("enter the Maximum Marks."))
x=str(input("enter the name of the student"))
a=int(input(f"the marks obyained in maths out of {y} :"))
b=int(input(f"the marks obyained in chemastry out of {y} :"))
c=int(input(f"the marks obyained in english out of {y} :"))
d=int(input(f"the marks obyained in physic out of {y} :"))
e=int(input(f"the marks obyained in computer python out of {y} :"))

h=a+b+c+d+e
o=(h*100)/(y*5)

if(o>=37):
    print(x,"is pass","\nhe obtained ",o,"%")
    if(o<70):
        print("he scored D gread.")
    elif(o<80):
        print("he scored C gread.")
    elif(o<90):
        print("he scored B gread.")
    else:
        print("he scored A gread.")
else:
    print("fale")

print("Thx")
input("enter to exit") 






















