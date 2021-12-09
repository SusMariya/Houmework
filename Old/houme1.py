# 1
n = int(input("Введите количество симолов: "))
m = input("Введите тип симола: ")
r = int(input("Введите ориентацию линии (0 - горизонтальная, 1-  вертикальная): "))
if r == 1:
    while n > 0:
        print(m)
        n -= 1
else:
    while n > 0:
        print(m, end ="")
        n -= 1

# 2
print("Выбирете операцию:"
      "\n1 - r  - применяет унарный минус к операнду"
      "\n2 - + - сложение"
      "\n3 - - - вычитание"
      "\n4 - / - деление"
      "\n5 - * - умножение"
      "\n6 - % - деление по модулю ("
      "\n7 - < - минимальное из двух чисел"
      "\n8 - > - максимальное из двух чисел")
next = "x"
while next == 'x' or '[':
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    c = int(input("Выбирете операцию: "))
    if c == 1:
        print(a * -1, " и ", b * -1)
    elif c == 2:
        print(a + b)
    elif c == 3:
        print(a - b)
    elif c == 4:
        if b != 0:
            print(a / b)
        else:
            print("На ноль делить нельзя")
    elif c == 5:
        print(a * b)
    elif c == 6:
        print(a % b)
    elif c == 7:
        if a < b:
            print(a)
        else:
            print(b)
    elif c == 8:
        if a > b:
            print(a)
        else:
            print(b)
    else:
        print("Ошибка")
    next = input("Введите 'х' чтобы продолжить")

# 3

x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))
z = float(input("Введите второе число: "))
if x > y and x > z:
    print("Максимальное число: ", x)
elif y > x and y > z:
    print("Максимальное число: ", y)
else:
    print("Максимальное число: ", z)

# 4
ch = int(input("Введите количество чисел последовательности: "))
v = float(input("Введите число: "))
min_v = v
max_v = v
c = 1
sum_v = v
while c < ch:
    v = float(input("Введите число: "))
    sum_v += v
    if v < min_v:
        min_v = v
    if v > max_v:
        max_v = v
    c += 1
print("Количество чисел: ", c)
print("Среднее арифметическое  чисел: ", sum_v/c)
print("Минимальное число: ", min_v)
print("Максимальное число: ", max_v)