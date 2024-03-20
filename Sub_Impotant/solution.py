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

a = int(input("Enter the no1 = N,R,Complex no."))
b = int(input("Enter the no2 = N,R,Complex no."))
ope = input("enter the operator.\n +,-,*,/,%,//,**\n ==,!=,>,<,>=,<=\n &,|,^,~")

# Arithmatic operator
if ope == '+': print("Addition is = ", a + b)
elif ope == '-': print("Subtraction is = ", a - b)
elif ope == '*': print("product is = ", a*b)
elif ope == '/': print("division is = ", a / b)
elif ope == '%': print("Remainder is = ", a % b)
elif ope == '//': print("The flot division is = ", a // b)
elif ope == '**': print("Power is = ", a ** b)

# Relational operators
elif ope == '==': print("a equals to b ", a == b)
elif ope == '!=': print("a not equals to b ", a != b)
elif ope == '>': print("a is grater then b ", a > b)
elif ope == '<': print("a is less then b ", a < b)
elif ope == '>=': print("a is grater or equal to b ", a >= b)
elif ope == '<=': print("a is less or equal to b ", a <= b)

# Bitwise operators
elif ope == '&': print("Bitwise AND between a and b = ", a & b)
elif ope == '|': print("Bitwise OR between a and b = ", a | b)
elif ope == '^': print("Bitwise XOR between a and b = ", a ^ b)
elif ope == '~': print("Bitwise NOT between a = ", ~a)
else: print("Error occurred.")

# Logical operators
print("logical and ", True and True)
print("logical or ", False or True)
print("logical not ", not False)

# Assignment operators
assignPl = 5
assignPl += 1
assignPl -= 1
assignPl *= 14
assignPl /= 1
assignPl %= 7
print(assignPl)

# Increment/decrement operators
print("pre-increment", ++assignPl)
print("pre-decrement", --assignPl)


d = input("you want an atomatic result of all the posible value of A and B enter y :")

if (d == "y"):
    print("Your ans sir.")
    allOperator()


input("Press enter to exit.")  
