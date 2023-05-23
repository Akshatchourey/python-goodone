# old chess problen
# n = 64 not posible so dont even try.
# ans comes out to be approximately 6.27710174 × 10^570 ---> 2 ** 2 ** 64 ----> 2 ** 18446744073709600000

n = 11
ans = 2
for i in range(n):
    ans += ans ** 2
print(ans)

a = input("Enter to exit")
