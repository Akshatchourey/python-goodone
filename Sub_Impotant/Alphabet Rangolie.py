allAlphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
n = int(input("enter the no:- "))
length = 4 * n - 3
d = int((length - 1) / 2)

for l in range(1, 2 * n):
    i = l
    if n < l:
        i = 2*n-l

    final = ""
    final += "-" * d

    for b in range(n - 1, n - i, -1):
        final += allAlphabets[b] + "-"

    for a in range(n - i, n):
        final += allAlphabets[a]
        if a != n - 1:
            final += "-"

    final += "-" * d
    if l < n:
        d -= 2
    else:
        d += 2
    print(final)

input("enter to exit. thx.")
