#print sum,division,product,diffrence,modof two numbers

def allOperator():
    sum=a+b
    print("the sum =", sum)
    substract=a-b
    print("the diffrence =",substract)
    division=a/b
    print("the division =",division)
    modulus=a%b
    print("the mode =",modulus)
    floordivision=a//b
    print("the floordivision =", floordivision)
    exponent=a**b
    print("the exponent =",exponent)
    solution=sum+substract+division+floordivision+exponent+modulus
    print("the solution = ",solution)
    print("The solution is the choureys golden solution")

    # print("data type of solution is",type(soluti))




#more easier way.

a=int(input("Enter the value of a = N/R/complax no."))
b=int(input("Enter the value of b = N/R/complax no."))
ope=(input("enter the operator.+,-,*,/,%,**,//,>,<,.>=,<="))
if(ope=="+"):
    print("addtion is=",a+b)
elif(ope=="-"):
    print("substraction is=",a-b)
elif(ope=="*"):
    print("product is=",a*b)
elif(ope=="/"):
    print("division is=",a/b)
elif(ope=="%"): 
    print("remander is=",a%b)
elif(ope=="//"):
    print("The flot division is=",a//b)
elif(ope==">"):
    print("a is grater then b=",a>b)
elif(ope=="<"):
    print("a is less then b=",a<b)
elif(ope==">="):
    print("a is grater or equal to b=",a>=b)
elif(ope=="<="):
    print("a is less or equal to b=",a<=b)    
else:
    print("pawer is=",a**b)

d = input("you want an atomatic result of all the posible value of A and B enter y :")

if(d == "y"):
    print("Your ans sir.")
    allOperator(
)


a = input("Press enter to exit.")  





    
