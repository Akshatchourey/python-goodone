import matplotlib.pyplot as plt

# with open('25,000 prime no.txt', 'r') as file:
#     data = file.read()
#     primes = [int(num) for num in data.split()]

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149]
plt.plot(primes, linestyle='dashed', marker='o', markerfacecolor='red', markersize=5)
plt.title('Line Graph of N Prime Numbers')
plt.xlabel('Index')
plt.ylabel('Prime Number')
plt.grid(True)
# plt.savefig('prime_numbers.png', dpi=600)
plt.show()

a = input("Enter to exit:")
