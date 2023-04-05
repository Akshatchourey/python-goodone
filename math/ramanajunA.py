k = int(input("enter the value of k."))
a = c = 1
for i in range(1, k+1):
    a *= i
for i in range(1, 4*k+1):
    c *= i
b = 4*k
ans = 9801*a*396**b
ans1 = 2.828*c*((26390*k)+1103)
ans2 = ans/ans1
print(ans2)
