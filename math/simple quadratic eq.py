# ax^2 + bx + c = 0
import math

def quadratic(a, b, c):
    d = b*b - 4*a*c
    r = math.fabs(math.sqrt(d))
    if d == 0:
        print("both the roots are ", (-b)/2*a)
        print("both the roots are ", (-b)/2*a)
    elif d > 0:
        print("both the roots are ", (-b+r)/2*a)
        print("both the roots are ", (-b-r)/2*a)
    else:
        print("both the roots are ", -b+r/2*a, 'i')
        print("both the roots are ", -b-r/2*a, 'i')


if __name__ == "__main__":
    a = int(input("enter the no a:"))
    b = int(input("enter the no b:"))
    c = int(input("enter the no c:"))
    if a == 0:
        print("roots is not posible.")
    else:
        quadratic(a, b, c)
input("Enter roi exit;")
