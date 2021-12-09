# 1
n = int(input("Введите количество симолов: "))
r = ""
while n > 0:
    r += "*"
    n -= 1
    print(r)
# 2
n = int(input("Введите количество симолов: "))
while n > 0:
    print("*"*n)
    n -= 1

# 3
a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
while a <= b:
    if a %2 != 0:
        print(a, end=" ")
    a += 1

# 4
n = int(input("Введите число: "))
a = n
b = 0
while n > 0:
    i = n % 10
    b = b * 10 + i
    n = n//10
if (a == b):
    print("Число полиндром")
else:
    print("Число не полиндром")