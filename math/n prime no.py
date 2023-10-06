# last prime no 2L10Th up till found 28,98,527

import math
num = int(input("input the no."))

# Type 1
"""
seq=[]
asq=[1]
x=1
a=int(input("Input the no of prime number."))
while(len(asq)<=a):
     x+=1
     for i in range (2,x+1):
          if(x%i==0):
             seq.append(x)
             if(x==i):
                  if(len(seq)==1):
                       asq.append(x)
                  seq=[]
     if(len(asq)==a):
          break       
             
print(asq)
print(len(asq))
print("thx")
"""

# Type 2 squre root
"""
c = 2
while num != 0:
    for i in range(2, int(math.sqrt(c))):
        if c % i == 0:
            break
    else:
        print(c, end=" ")
        num -= 1
    c += 1
print("\n")
"""

# Type 3 Willans prime detecting formula.
"""
n = int(input("Enter n:- "))
j = 2
A = 1
# file1 = open("50,000 prime no(Willans).txt","a")# Append mode
while n > 0:
    A *= j-1
    if (A+1)%j == 0:
        print(j, end=" ")
        # file1.write(f"{j} ")
        n -= 1
    j += 1
# file1.close()
"""

# Type 4 my type of formula
file0 = open("2Lakh10Th prime no.txt", "a+")
file0.seek(0)
arr = file0.readline().split()
primes = [int(no) for no in arr]
a = primes[len(primes)-1]+1
file0.seek(0, 2)
while num != 0:
    checker = 0
    for u in primes:
        if u > math.sqrt(a):
            break
        if a % u == 0:
            checker += 1
            break
    if checker == 0:
        print(a, end=" ")
        file0.write(f"{a} ")
        primes.append(a)
        num -= 1
    a += 1
file0.close()

# Type check1(for single no)
"""
y = 'y'
while y == 'y':
    s = int(input("Enter No:- "))
    for x in range(1, s + 1):
        if s % x == 0:
            print(x)
    y = input("Do you want to recheck, Enter 'y'/'n':- ")
"""

# Typ check2(for two files) Take's-Time to run
"""
file0 = open("2Lakh10Th prime no.txt", "r").readline().split()
primes = [int(no) for no in file0]
print(len(primes))
for no in primes:
    for n in range(2, int(math.sqrt(no))):
        if no%n == 0:
            print(no)
            break
"""

print("\nthx")
print("Have a nice day.")
input("press enter to exit.")
