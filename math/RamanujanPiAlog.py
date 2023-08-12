# There is some problem with Ramanujan's formula

from math import sqrt
from decimal import Decimal, getcontext
import mpmath as mps

n = int(input("enter the value of k:- "))
def factorial(f):
    if f == 0:
        return 1
    else:
        return f * factorial(f - 1)


mps.mp.dps = 100
a = mps.mpf(sqrt(8)) / mps.mpf(9801)
ans1 = 0
for k in range(0,n+1):
    N = mps.mpf(factorial(4*k)) * mps.mpf(1103+26390*k)
    D = mps.mpf(factorial(k)**4)
    D *= mps.mpf(396**(4*k))
    ans1 += mps.mpf(N)/mps.mpf(D)

ans1 *= mps.mpf(a)
ans = mps.mpf(1)/mps.mpf(ans1)

# chat gpt code
getcontext().prec = 100
def ramanujan_pi(k):
    sum = 0
    for n in range(k):
        sum += (factorial(4 * n) * (1103 + 26390 * n)) / ((factorial(n) ** 4) * (396 ** (4 * n)))
    pi = Decimal(1) / (Decimal(2) * Decimal(sqrt(2)) / Decimal(9801) * Decimal(sum))
    return pi


pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
print(ramanujan_pi(n))
print(ans)
exit = int(input("Enter to exit, thx."))
