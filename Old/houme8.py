# 1
print("Вычеслите площадь фигур \nВыбор фигуры: \n1- прямоугольник  \n2- треугольник \n3- круг ")
a = int(input("Ведите номер фигуры: "))
if a == 1:
    f = int(input("Ведите длину a: "))
    k = int(input("Ведите ширину b: "))
    print("Площадь прямоугольника: ", (f * k))
if a == 2:
    b = int(input("Ведите основание: "))
    c = int(input("Ведите высоту: "))
    print("Площадь треугольника: ", (b * c) / 2)
if a == 3:
    w = int(input("Ведите радиус: "))
    print("Площадь круга: ", round(pi * (w ** 2), 2))

# 2
import random as r

mas = [r.randint(2, 21) for i in range(11)]
print(mas)
a = []
b = []
for i in mas:
    if i != 1:
        for j in range(2, i):
            if (i % j) == 0:
                a.append(i)
                break
        else:
            b.append(i)
print(a)
print(b)
print("Мin: ", min(b))
print("Max: ", max(a))
#
# # 3  мы же разбирали на уроке...
def a(n, even=True):
    s = 0
    while n > 0:
        b = n % 10
        if even and b % 2 == 0:
            s += b
        elif not even and b % 2 != 0:
            s += b
        n //= 10
    return s


print("Сумма четных элементов")
print(a(9874023))
print(a(38271))
print(a(123456789))
print("Сумма нечетных элементов")
print(a(9874023, even=False))
print(a(38271, even=False))
print(a(123456789, even=False))
