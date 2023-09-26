# 25,000Th prime no = 287117.00
# 50,000Th prime no = 611953.00 by (Willans)
import math

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

# Type 2

num = int(input("input the no."))
# c = 287118 #to continue from 25,000
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

y = 'y'
while y == 'y':
    s = int(input("Enter No:- "))
    for x in range(1,s+1):
        if s%x == 0:
            print(x)
    y = input("Do you want to recheck, Enter 'y'/'n':- ")

print("\nthx")
print("Have a nice day.")
input("press enter to exit.")
