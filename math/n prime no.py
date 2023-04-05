# 25,000Th prime no = 287117.00

"""
seq=[]
asq=[1]
x=1
a=int(input("Input the no of prime numder."))
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
  




num = int(input("input the no."))
c = 287118 #to continew from 21,000
c = 2
while num != 0:
    for i in range(2, c):
        if c % i == 0:
            break
    else:
        print(c, end=" ")
        num -= 1
    c += 1


y=0
while(y==0):
     s=int(input("Enter the no you want to reechack."))
     for x in range(1,s+1):
         if(s%x==0):
             print(x)
     y=bool(input("do you want to reechack if not press enter."))

print("thx")
print("Have a nice day.")
input("press enter to exit.")
