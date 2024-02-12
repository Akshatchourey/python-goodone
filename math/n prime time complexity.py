import matplotlib.pyplot as plt
from math import sqrt

''' 
To check prime no approx 6cr you need to loop 
6cr no ---> traditional method
or 7745 ---> sqrt() method
or 985 ---> my method

45B you need 45B or 2L or 17984
'''
# plt.subplot(1,2,1)
a = 4
x = []
y = []
with open('2Lakh10Th prime no.txt', 'r') as file:
    data = file.read()
    primes = [int(num) for num in data.split()]
    for i in range(100):
        p = primes[i]
        while p > sqrt(a):
            a += 1
        x.append(a)
        y.append(i+1)

plt.plot([sqrt(n) for n in range(a)], markersize=5)
plt.plot(x, y, markersize=5)

plt.title("Different Time Complexity")
plt.grid(True)
plt.show()
