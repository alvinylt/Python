a = 1
b = 1
k = 2
n = int(input("How many numbers do you want? "))

if n == 1:
    print(a)
elif n == 2:
    print(a)
    print(b)
else:
    print(a)
    print(b)
    while k <= n:
        c = a + b
        print(c)
        a = b
        b = c
        k = k + 1
